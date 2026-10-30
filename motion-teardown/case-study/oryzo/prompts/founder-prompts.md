---
title: "The founder's key messages"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# The founder's key messages

Every message below was typed or dictated by our founder during the session on 30–31 October 2026 (times IST). They are **lightly edited**: spelling and punctuation corrected, profanity removed, filler trimmed, and nothing added. Ellipses mark cuts. The director's replies are summarised in square brackets.

## 19:34 · The opening request (lightly edited)

> I want you to use the /watch skill, which is in the system. You have to find it, add it to this project, and use the skill to watch this video. It's a website I admire a lot; the motion and the hero section are extremely good. Have a look at the whole screen recording and go through everything, and after that I will give you the actual website. What you have to do is go to the website, use the reverse-engineer skill and reverse engineer the entire website. But before that, I want you to watch this video and come up with a plan for how we can reverse engineer it and get the exact same quality of motion, scroll animations and interactive elements into our websites.

[The first attempt had hit the Claude five-hour usage limit; this was resumed with "continue". The director answered with `MOTION-PLAN.md`: ten effects, E1–E10, each with a hypothesis and what to measure.]

## 19:50 · How was it made? (lightly edited)

> All right, now that you have watched the whole video, tell me how this motion was made. We have to recreate this, so give me some ideas on how we can recreate it, and then I will give you the reverse-engineering task.

## 19:58 · Tools and prompting (lightly edited)

> So now that we have to build this thing, what are the tools, what's the tech stack we have to use, and how can we prompt Claude to build something like this?

## 20:05 · The reverse-engineering prompt and the scope (lightly edited)

> All right, I want you to give me a reverse-engineering prompt. I'm going to use the reverse-engineering skill with a DeepSeek model, specifically DeepSeek V4.1 Flash 1017, and reverse engineer the website. I don't want you to reverse engineer the whole website, only the particular part which is recorded in the video, like the main hero section and just one or two scrolls. That's it, don't do too much. Then come back, give me the whole report, and then rebuild the exact thing. Not inspired by it: build the exact thing as it is right now. So give me the reverse-engineering prompt and I will run it with the skill.

[The director wrote brief 02. The founder pasted it back to be sent; Markdown had turned `__THREE_DEVTOOLS__` into bold, which the director fixed before sending.]

## 20:25–20:26 · After the DNS failure (lightly edited)

> Use Claude.

[The founder interrupted this message a moment later and sent:]

> Continue with DeepSeek.

## 21:18 · Progress check

> How long?

[Estimated another one to two hours.]

## 21:22 · The first "speed up" (lightly edited)

> Speed up the process, dude.

[The single agent was stopped and the work split across agents A, B and C, briefs 05–07.]

## 23:06 · Teach me (lightly edited)

> Now combine the REA and watch insights and then teach me how we can build something like this.

## 23:34 · The rebuild (lightly edited)

> All right, guide me through the images and anything you need from me. For images, use GPT to generate them, and rebuild the exact version but in a red and white colour theme.

[The director asked four multiple-choice questions in one prompt. Answers: crimson and white; new GPT-generated props; a free substitute font; keep the ORYZO copy. Then `BUILD-SPEC.md` and briefs 08–10.]

## 00:29 · The second "speed up" (lightly edited)

> I need you to speed up the process.

## 00:32 · On the red glow (lightly edited)

> No, it works, I'm fine with it… and speed up the process.

[Replying to the director's note that the rebuild's red edge glow was much stronger than the original's thin rim. The glow was kept as it was.]

## 01:20 · Show me

> Show it to me in localhost.

## 01:28 · Approval (lightly edited)

> You nailed it, bro… you did it, proud of you. Now give me the zip file of it so I can share it with my bro.

## 01:33 · The request for this guide (lightly edited)

> Now create a very, very thorough system and guide for it, so I can learn this from: one, a developer's perspective; two, the perspective of an AI genius who uses AI to code and build the whole thing, basically a vibe coder; and three, a smart system for AI to learn and replicate. And if possible, add a case study on how you and we did it. I want the whole process: from screen recording the site, to me prompting you, to you doing the work, to reverse engineering, to image generation, to the 3D elements, to you actually creating that hand and everything… We are going to publish this on Substack, Medium, Twitter and maybe other platforms too… We also had a lot of flaws, so I want you to think it through and make it even better. Don't go straight into building the system and the guide. Think first, then give me suggestions for what else we can add.

## 01:41 · Decisions for the guide (lightly edited excerpt)

> The side-by-side scroll video is a really good one; I have already recorded both versions, so we can use them… You can add the failures too, but don't make them too prominent… Prompts are very, very important: how you guided the reverse-engineering part, how you guided the sub-agents, how the video part guided everything. Also give an honourable mention to the watch skill and the reverse-engineer-anything skill… The level ladder for learners is definitely an important part. The bring-your-own-site worksheet is also a really good one… We need a really proper, very well-written long-form article… I would prefer one mega guide rather than a series.

[One request in this message, to publish Lusion's captured shaders and code dumps, was not adopted. The approved editorial brief keeps the techniques in our own words and does not reproduce Lusion's code.]
