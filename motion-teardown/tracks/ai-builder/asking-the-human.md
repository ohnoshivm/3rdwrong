---
title: "Asking the human: only the decisions that are theirs"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Asking the human: only the decisions that are theirs

Every question you put to the person you work for costs them attention and stalls the work until they answer. Ask few, ask well, and ask once. In the oryzo.ai (by [Lusion](https://oryzo.ai)) rebuild we asked four questions in a single prompt, at 23:36 on 30 October, and the build spec was written within minutes of the answers.

## What is a real decision

Ask when **the answer changes what gets built, and nobody but the human can give it.** That means taste, brand, money, legal exposure, and trade-offs between things they care about.

Do not ask when:

- **There is a conventional default.** Pick it, say so in a line, and move on.
- **You can verify it.** Look in the code, the file or the network log.
- **The answer is in the brief or the spec already.**
- **It is a process choice that is yours.** Which agent, which file layout, which test.
- **It only matters to you.** "Is this okay?" asks for reassurance, not information.

## The four questions we asked

One multiple-choice prompt, four questions, each with a recommended option first. The human's choices are marked.

| Question | Options | Their answer |
| --- | --- | --- |
| For the red and white Oryzo rebuild, which colour layout should I use? | **Crimson + white (Recommended)** · White-dominant · Red-dominant | Crimson + white |
| Each prop image on the original desk is three studio renders under different light angles plus a depth map, which lets the props be relit live. How should we make the red and white versions? | **GPT-generated, new art (Recommended)** · Recolour the originals | GPT-generated, new art |
| The original font, Halyard Display, is licensed through Adobe Fonts and won't load outside oryzo.ai. What should the rebuild use? | **Free substitute (Recommended)** · My Adobe Fonts kit | Free substitute |
| Should the copy stay as Oryzo, or use your own brand? | **Keep ORYZO copy** · My own brand | Keep ORYZO copy |

Why these four, and not forty:

- **Colour** and **copy** are taste and brand: no one else can choose them.
- **How to make the props** carries a trade-off. Recolouring the originals would copy Lusion's art. New art costs generation time but keeps the rebuild ours.
- **The font** is a licence. The measurement stage had flagged it; the answer was the human's to give.
- Everything else (stack, file layout, effort levels, test method) was ours to decide, and we did.

## How to ask

1. **Batch them.** One prompt with all the open decisions beats four separate interruptions.
2. **Make it multiple-choice**, with two to four options that cover the realistic choices. The human can always type their own answer.
3. **Put your recommendation first**, labelled "(Recommended)", with a reason in the option text. A good recommendation saves them thinking; a bad one tells you the question was really yours to answer.
4. **Give just enough context to answer in the question itself.** The person may read only the dialog. Our prop question carried the reason (three light angles plus a depth map) so it could be answered without reading anything else.
5. **Say what will happen next.** "Answer these and I'll write the build plan."
6. **Do not ask again.** Record the answers in the spec, verbatim, with a time.

## The same pattern in a message

When the question is bigger than a dialog, use a numbered list with recommendations. This is how we put the publishing decisions to the founder (shortened):

```text
## Decisions I need from you
1. Original demo: rebuild with our own brand and 3D for publishing (recommended), or publish the method with only screenshots of the study?
2. Lusion: contact them before publishing? (Recommended.)
3. Format: one mega-guide, or the series split above?

Answer these and I'll lay out the build plan.
```

## What to do while you wait

If a decision blocks only part of the work, keep the rest moving. In our build the decisions came after the report, and the spec was written the minute they landed. Do not wait on a decision that a placeholder can cover: GL ran on flat placeholders until the generated images existed.

## Quality check for a question

- [ ] Would the answer change what gets built?
- [ ] Could I have found it out myself? If yes, do that.
- [ ] Does each option lead to a distinct result?
- [ ] Is my recommended option first, with a reason?
- [ ] Can the person answer without opening anything else?
- [ ] Have I batched everything I need to ask?

Related: [directing agents](directing-agents.md), [stage 5 of the playbook](../../playbook/05-spec.md), where the answers become the spec.
