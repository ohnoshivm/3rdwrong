---
title: "Link watch skill + save Oryzo frames"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Link watch skill + save Oryzo frames

- Sent: 10-30 19:40 IST
- Provider: opencode
- Model: opencode/deepseek-v4.1-flash-free
- Options: {"variant": "low"}
- Mode: async · Role: implementation

## Brief (verbatim)

````text
Objective: two small file operations in the repo at <project>. Do nothing else.

1. Make the "watch" skill available at project level:
   mkdir -p <project>/.claude/skills
   ln -s ~/.agents/skills/watch <project>/.claude/skills/watch
   (If the link already exists and points to that target, leave it. Do not copy the skill's files, a symlink only.)
   Verify: test -f <project>/.claude/skills/watch/SKILL.md

2. Save reference frames. Create <project>/research/oryzo/video-frames/ and copy these files from <temporary-session>/watchframes/ under the new names shown (source -> destination name):
   f_001.jpg -> 00.00s-hero-rest.jpg
   f_002.jpg -> 00.33s-hero-blur-out.jpg
   f_003.jpg -> 00.67s-isnt-just-a-coaster-line-highlight.jpg
   f_004.jpg -> 01.00s-coaster-rotate-a.jpg
   f_005.jpg -> 01.33s-coaster-rotate-b.jpg
   f_006.jpg -> 01.67s-powered-by-ai-char-blur-in.jpg
   f_009.jpg -> 02.67s-hand-hover-edge-glow.jpg
   f_010.jpg -> 03.00s-hand-holds-coaster.jpg
   f_011.jpg -> 03.33s-caption-line-mask-out.jpg
   f_014.jpg -> 04.33s-coaster-rotate-reverse.jpg
   f_026.jpg -> 08.67s-heading-first-char-blur-in.jpg
   f_032.jpg -> 10.33s-hero-side-tab-returns.jpg

Constraints: do not modify, delete, or commit any other file; do not run git commit. Do not touch <temporary-session>/watchframes itself.

Acceptance: symlink resolves to SKILL.md; 12 jpg files exist in research/oryzo/video-frames with the exact names above.

Output: a completion report with status, the output of `ls -la <project>/.claude/skills` and `ls <project>/research/oryzo/video-frames | wc -l`, and any blockers.
````
