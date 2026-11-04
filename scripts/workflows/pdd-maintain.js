export const meta = {
  name: 'pdd-maintain',
  description: 'Research only the fast-section lines scripts could not re-confirm, refute every patch, return settled patches. READ-ONLY.',
  whenToUse: 'After `python3 scripts/maintain.py plan`; pass its plan.json entries as args.items. Footer, stamp and ledger are done by `maintain.py apply`.',
  phases: [
    { title: 'Research', detail: 'one agent per cluster that still has worklist lines' },
    { title: 'Refute', detail: 'one refuter per cluster; script pre-check first' },
  ],
}

// args: { root: repo checkout, dir: plan output dir, date: 'YYYY-MM-DD', items: plan.json entries }
const M = 'opus'
const pb = cc => `${args.root}/skills/property-deep-dive/countries/${cc}/playbook.md`

const BASE = `You maintain one country playbook of the property-deep-dive skill (repo ${args.root}). Today is ${args.date}.
READ-ONLY: never modify repo files or git state; return exact patches only. The anti-hallucination contract in CLAUDE.md applies in full: every figure is sourced (fetched now; primary sources first, lower tiers labelled), computed (inputs inline) or estimated (est. + calibration sentence); never guess.
Your reasoning and your tool output are what this run pays for, so spend little of both. Reason in short notes, about 100 words per line at most, nothing between tool calls. Work in batches: one Bash call fetches every source you need into ${args.root}/_local/maint-cache/ and prints only the grep hits, never more than 60 lines; search with max_results 3; read a long page with tavily_extract and a query, never whole. A worklist line may carry hints: the best passages on pages this run already read, with their URLs. Check those before fetching anything. Give up on a source after three routes (other language version, statistics API or PDF, official gazette, archived copy) and label the figure instead.
Patch rules: old = exact substring of the current file, unique (grep -c); keep table pipe counts; keep curated caveats; reader-facing prose only. Never describe how a page was fetched (status codes, bot walls, tool names): CI rejects it; write "could not be read for verification on <date> — check it directly". Data two or more years old carries "— rates/figures may have changed since". Every "computed" chain must hold (CI re-computes it).`

const PATCH = { type: 'object', properties: {
  file: { type: 'string' }, section: { type: 'string' }, old: { type: 'string' }, new: { type: 'string' },
  kind: { type: 'string', enum: ['fact-changed', 'asof-confirmed', 'relabelled', 'deprecated'] },
  note: { type: 'string' },
  evidence: { type: 'array', items: { type: 'object', properties: { url: { type: 'string' }, tier: { type: 'string' }, fact: { type: 'string' }, quote: { type: 'string' } }, required: ['url', 'fact', 'quote'] } },
}, required: ['file', 'section', 'old', 'new', 'kind'] }
const RESEARCH = { type: 'object', properties: {
  items: { type: 'array', items: PATCH },
  sections: { type: 'array', items: { type: 'object', properties: {
    section: { type: 'string' }, closed: { type: 'boolean' }, note: { type: 'string' },
    remaining: { type: 'array', items: { type: 'string' } },
  }, required: ['section', 'closed', 'note'] } },
  shared_requests: { type: 'array', items: { type: 'object', properties: { file: { type: 'string' }, request: { type: 'string' }, evidence: { type: 'string' } }, required: ['file', 'request'] } },
  confirmed_lines: { type: 'array', items: { type: 'object', properties: { line: { type: 'string' }, urls: { type: 'array', items: { type: 'string' } } }, required: ['line', 'urls'] } },
}, required: ['items', 'sections'] }
const VERDICT = { type: 'object', properties: {
  items: { type: 'array', items: { type: 'object', properties: {
    index: { type: 'integer' }, ok: { type: 'boolean' }, severity: { type: 'string', enum: ['none', 'minor', 'major', 'fatal'] },
    reason: { type: 'string' }, corrected_new: { type: 'string' },
  }, required: ['index', 'ok', 'severity', 'reason'] } },
  section_flags: { type: 'array', items: { type: 'object', properties: { section: { type: 'string' }, closed_ok: { type: 'boolean' }, reason: { type: 'string' } }, required: ['section', 'closed_ok'] } },
  confirmed_rejected: { type: 'array', items: { type: 'integer' } },
  flags_cleared: { type: 'array', items: { type: 'integer' } },
}, required: ['items', 'section_flags', 'confirmed_rejected', 'flags_cleared'] }

const research = it => agent(`${BASE}
Playbook: ${pb(it.code)}. Worklist: ${args.dir}/${it.code}.json → clusters["${it.cluster}"].lines (${it.lines} lines in ${it.sections.join(', ')}).
Every other fast-section line was re-confirmed today by scripts/evidence-ledger.py against the page that proved it last time: do not re-check those.
For each worklist line (status NO_EVIDENCE = no recorded source; NOT_CONFIRMED = the recorded page no longer shows the figures together; confirmed_values / missing_values = only the missing ones need work):
a. Confirmed against a primary source, unchanged → kind asof-confirmed (refresh its "(<year> data, source X)" tag). Changed → kind fact-changed.
b. No primary source publishes it → kind relabelled: "est." with inputs and a calibration sentence, its real tier and date, or "data not publicly available — verify at <authority URL>".
c. A primary source exists but cannot be read → keep the figure and tag, add the may-have-changed suffix if due, point to it ("verify at <URL>").
For a and c give evidence[] with the exact deep URL that shows the figure, and in quote up to 25 words copied exactly from that page around the figure, in the page's language: never a paraphrase, a script checks it. Scripts also check that every new figure of a patch stands on its evidence pages, and hold the patch if it does not, so list every page a figure came from. An expired field on a line means a date it looks forward to has passed: update what happened.
A worklist line you confirmed without changing it gets no patch: list it in confirmed_lines (the exact current line text + every deep URL its figures rest on). The refuter checks it, then the ledger stores a fingerprint of those pages, so the next run skips the line while they stay unchanged.
Report sections[] for ${it.sections.join(', ')}: closed=true only if every worklist line there is now confirmed or labelled. Each section's note is printed in the playbook: one or two sentences for a reader on what was confirmed or changed, naming sources, with no word about this run (worklist, patch, ledger, refuter).
Touch only these sections, with one exception: a line anywhere else in this playbook (Country profile, quirks, other sections, the Status Confidence paragraph) that restates a figure you changed or now contradicts your patch gets its own patch, with section set to where it sits. Never the Status stamp, Per-section table or Update history (maintain.py writes them). Changes to shared files go in shared_requests with evidence.`,
  { label: `research:${it.code}:${it.cluster}`, phase: 'Research', schema: RESEARCH, model: M })

const refute = (it, res) => agent(`${BASE}
You are the adversarial refuter for the "${it.cluster}" patches on ${pb(it.code)} (worklist ${args.dir}/${it.code}.json). Default to ok=false when in doubt.
First write PROPOSED.items to a temp JSON file and run: python3 ${args.root}/scripts/maintain.py precheck <file>. MACHINE_CONFIRMED means the patch's figures stand together on its evidence page: check only meaning (scope, date, legal status, label honesty) from the evidence and re-fetch only if that check needs the page. REFETCH means re-fetch and confirm the page shows exactly what the new text says. FLAGGED means a script could not trace a figure, and names it: "near miss" gives the number the page has instead, so a digit was probably miscopied; treat every flagged figure as wrong until you read it on the page yourself, and fix it in corrected_new. List in flags_cleared the index of each flagged patch whose final figures you did read, and say where in reason: a flagged patch not listed there is held back.
Relabelled patches fail most often (half needed a fix in past runs): check that no est. hides a figure a primary source publishes, inputs and a calibration sentence are present, nothing curated was deleted.
Also check old is exact and unique, tables keep their pipe counts, the prose rules above. corrected_new, when you give one, is a full replacement for the patch's new; never change old.
Then check confirmed_lines: the next run trusts them without an agent while their pages stay unchanged. Read each on its URLs (pages already saved under ${args.root}/_local/maint-cache/ need no new fetch) and put the index of any line its pages do not fully support in confirmed_rejected.
Then judge each section's closed claim in section_flags as the section would read after the patches.
PROPOSED:
${JSON.stringify(res, null, 1)}`, { label: `refute:${it.code}:${it.cluster}`, phase: 'Refute', schema: VERDICT, model: M })

const settle = (it, res, v) => {
  const verdicts = new Map((v ? v.items : []).map(i => [i.index, i]))
  const flags = new Map((v ? v.section_flags : []).map(f => [f.section, f]))
  return {
    cluster: it.cluster,
    items: res.items.map((p, i) => {
      const b = verdicts.get(i)
      if (!v) return { ...p, status: 'DROP', refuter: 'no refuter verdict' }
      const cleared = v.flags_cleared.includes(i)
      if (b && b.corrected_new) return { ...p, new: b.corrected_new, status: 'APPLY_CORRECTED', refuter: b.reason, flag_cleared: cleared }
      if (b && !b.ok && ['major', 'fatal'].includes(b.severity)) return { ...p, status: 'DROP', refuter: b.reason }
      return { ...p, status: 'APPLY', flag_cleared: cleared }
    }),
    sections: res.sections.map(s => ({ ...s, closed: !!(s.closed && v && (flags.get(s.section) || { closed_ok: true }).closed_ok) })),
    shared_requests: res.shared_requests || [],
    confirmed_lines: v ? (res.confirmed_lines || []).filter((_, i) => !v.confirmed_rejected.includes(i)) : [],
  }
}

const settled = await pipeline(args.items, it => research(it), (res, it) => refute(it, res).then(v => settle(it, res, v)))
const byCode = {}
settled.forEach((c, i) => { if (c) (byCode[args.items[i].code] = byCode[args.items[i].code] || []).push(c) })
const dropped = args.items.filter((_, i) => !settled[i]).map(it => `${it.code}:${it.cluster}`)
if (dropped.length) log(`no result for ${dropped.join(', ')}: those sections stay open`)
return { date: args.date, playbooks: Object.entries(byCode).map(([code, clusters]) => ({ code, clusters })) }
