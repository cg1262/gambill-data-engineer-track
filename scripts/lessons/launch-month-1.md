# Launch, Month 1: Weekly Lesson Scripts (Weeks 1 to 4)

Four talking-head lesson videos, one per week, for Chris to record to camera. Each one opens the week on the Phase 1 page: it sets up the concepts the learner reads on their own, briefs the lab, states what a pass looks like, and plants the hot-seat question for the live review.

Target: about 5 minutes each (650 to 800 words). Voice: direct, warm, second person, no hype. Same rhythm as the welcome videos: short sentences, one idea at a time, the lab is the point.

Structure every script follows:

1. Cold open (the failure this week prevents)
2. Why this matters on a real team
3. The ideas (the concept lessons, in the order the page lists them)
4. The lab briefing
5. What a pass looks like
6. The hot seat (the question you will ask live)
7. Close

Source of truth for every claim: `site/phase-1.html`, weeks 1 to 4. If the page changes, change the script.

---

## Week 1: Dev environment, the command line, and Git
**Module:** M00 · **Closes:** G6 · **Hours on the page:** ~4h lessons + ~3h lab
**Target:** ~5.5 minutes (~750 words)

Somewhere on a shared drive right now there is a folder called final_analysis_v3_ACTUAL. It has a notebook in it. Nobody knows which version produced the number that went to the board. Nobody can answer "who changed this and why." That folder is how a company loses a week of work and ships a number it can't reproduce.

Week one is where you make sure that folder is never yours.

Welcome to Launch. No data this week. I know, you came here for data. But every pipeline, every model, every dashboard you build in the next fifty weeks gets committed into the repo you stand up right now. Reproducibility and traceability start here, not later. Get this right and the rest of the course has a home.

Here is what you are learning in the lessons this week.

First, the terminal. Paths, files, pipes. You will live in a shell for the rest of your career, so you learn to move around one without thinking about it.

Second, the Git model. Three places your work can be: the working tree, the stage, and history. Most Git confusion comes from not knowing which of those three you are looking at. Once you can picture it, the commands stop being magic.

Third, branches, remotes, and the pull request. On a real team you never work on main. You branch, you commit small, you push, you open a PR, somebody reviews it, it merges. That loop is the job. We practice it before there is any data to argue about.

Fourth, environments. A virtual environment and a pinned requirements file. The reason is simple: your code has to run on a machine that is not yours.

Fifth, repo hygiene. A README that tells a stranger how to run it. A .gitignore that keeps secrets, the venv, and raw data out of history. The structure a teammate expects.

Now the lab. You are standing up the course repository the way a real data team would.

You create the skeleton: src, data raw, data processed, notes, a README, a .gitignore, a requirements file. You init Git. You create a venv, install exactly one package, and freeze it. Then you check that the venv folder does not show up in git status. If it does, your ignore file is wrong and you fix it now, not in week thirty.

You finish the starter script, check_env.py. It prints the Python version and proves the pinned package imports. That script is your evidence the environment rebuilds from the requirements file alone.

First commit on main: just the baseline. Ignore file, README skeleton, requirements. One commit. Then you branch, feature slash env-setup, and you build the rest in at least three small commits. Add the script. Fill in the README. Add a decisions note. Each commit message says what changed and why, in the imperative. "Add env check script so a fresh clone can verify setup." Not "stuff."

Push it. Open the pull request. Write the description as a checklist a reviewer could tick off. Then review your own diff like you are the teammate. No secrets. No venv. No two-hundred-megabyte CSV. Leave a comment on your own PR. Merge it. Delete the branch.

Last step, and this is the one people skip. Fresh clone. Rebuild the venv from scratch. Install from requirements. Run the script. It has to pass with zero manual fixes. Write down in notes/decisions.md what you kept out of Git and why, and whether you squashed or merge-committed and why.

What does a pass look like?

A fresh clone runs three commands and prints the Python version, the package version, and an "environment OK" line. The log on main shows a merged PR with at least three atomic commits. Nothing in the history, and I mean the whole history, contains the venv, a .env file, or raw data. The README covers setup, run, and layout. The decisions note exists and says something real.

Here is the hot seat for the live review this week. Have your repo open.

"Show me your git log. Pick one commit and tell me what changed and why. Then show me the line in your .gitignore that kept the venv out of history, and tell me what would have happened to the repo if that line was missing."

If you can answer that out loud, you understand week one. If you stumble, good, that is what the live review is for.

Go build the repo. Week two we put data in it.

**[on-screen / b-roll]** Lower-third: "Week 1 · M00 · Dev environment, CLI and Git." Cutaway A: the three-box Git model (working tree, stage, history) with a file moving through. Cutaway B: a terminal running the three commands from a fresh clone and printing "environment OK." Callout at the hot seat: the question text, right third.

---

## Week 2: The DE mental model and the data lifecycle
**Module:** M01 · **Closes:** G1, G9, G10 · **Hours on the page:** ~4h lessons + ~5h lab
**Target:** ~4.5 minutes (~660 words)

Ask most people what a data engineer makes and they say "pipelines." Wrong answer. A pipeline is plumbing. What you make is a data product: a table somebody depends on, with a known grain, a named owner, and a promise about how fresh and how clean it is.

This week you learn to see data that way. Still no heavy code. This is a thinking week, and it is the one that separates people who can defend their work from people who just ran a job.

Why it matters. When a stakeholder asks "can I trust this number," the answer lives in things like grain, freshness, and ownership. If you can't name them, you can't defend the number. Every later week in this course, the modeling, the incremental loads, the quality tests, is built on the vocabulary you pick up here.

The ideas.

One. What a data product is. Grain, owner, consumers, contract. The trap is calling the pipeline the product. The pipeline is how it gets made. The product is the thing on the other end that someone uses.

Two. The lifecycle. Source system, ingest, store, transform, serve, consume. You trace a real dataset through every one of those hops and say where the data physically lives at each step. We touch bronze, silver, gold as an intuition only. No tooling yet.

Three. Operational versus analytical systems. The app that takes a 311 call and the warehouse that reports on 311 calls are different systems with different copies of the data, and there are good reasons for that. You learn what changes shape between them.

Four. The anatomy of a data contract. Schema and types. Grain. Freshness, or an SLA. Nullability. Business semantics. A named owner. A contract is not a list of column names. It is a set of promises.

Five. Reading a source's docs to find the true grain of a row before you trust it. The data dictionary tells you what the publisher thinks one row means. Fifty sample rows tell you what it actually means. Sometimes those disagree.

The lab. You take NYC 311 Service Requests on the Socrata open data portal. You look at the live schema through the API preview and the published data dictionary. You pull around fifty sample rows with curl or a browser. No Python. That is week three.

Then you produce three artifacts in Markdown and commit them through a PR into last week's repo.

First, a lifecycle diagram. From the city's 311 intake system, to the open data portal, to your ingest, to storage, to a transformed table, to at least two named consumers. Every hop labeled. No mystery boxes.

Second, a one-page data contract. Schema with types and nullability. Freshness. Business meaning. An owner.

Third, the grain in one sentence, plus two consumers and the distinct question each one answers. The grain sentence is the hard part. "One row per service request" sounds right until you find a request that appears twice because it was reassigned. Look at the rows.

Add a three-sentence why note: why you chose that grain, and exactly who breaks if the grain is wrong.

A pass. The diagram names every hop. The contract has grain, typed schema with nullability, freshness, and an owner with a name. The grain is one defensible sentence that matches the actual rows. Two consumers with genuinely different needs. Merged through a PR.

The hot seat.

"State the grain of your dataset in one sentence. Now tell me exactly who breaks, and how, if that grain is wrong or silently changes."

The misconception I will be hunting for in the live review: treating the contract as a column list. If your contract has no owner and no freshness promise, you wrote documentation, not a contract.

This document becomes the opening artifact of your Phase 1 portfolio. Every model, every incremental load, every test you write later traces back to it. Take it seriously.

**[on-screen / b-roll]** Lower-third: "Week 2 · M01 · The DE mental model." Cutaway A: the six-hop lifecycle as a left-to-right chain, 311 intake at the left, two consumers at the right. Cutaway B: a 311 row with the grain sentence typed over it, then a second row with the same request ID appearing. Callout: "Grain. Owner. Consumers. Contract."

---

## Week 3: Python I, control flow and functions
**Module:** M02 · **Closes:** G1, G6 · **Hours on the page:** ~4h lessons + ~5h lab
**Target:** ~4.5 minutes (~660 words)

Here is a mistake I see in interviews from people with years of notebooks behind them. They write a function that prints a value, and they believe that function has given the value back. It has not. The caller got nothing. Return and print are different things, and if you don't feel that difference in your hands, every script you write will be a little bit broken.

This week is Python from the ground up, and we go slow on purpose. Procedural code only. Variables, control flow, functions, a script you run from the command line. Data structures, file handling, and error handling are next week. Don't skip ahead.

Why it matters. Data engineering is reading records and deciding what to do with each one. That is control flow. And breaking that work into small named pieces you can test and explain is the difference between a script and engineering. Gap six, the dev workflow gap, starts closing right here.

The ideas.

Types and variables. Int, float, string, boolean, None. Truthiness: which values Python treats as false. Coercion: when the language converts a type for you and when you have to ask. You learn to predict what a line does before you run it.

Control flow. If, elif, else. For and while. Break and continue. Guarding against a bad row so the loop keeps going.

Functions. Def. Positional and default parameters. Return versus print. Local versus global scope. The rule of thumb: one function, one job, an explicit return.

Structuring a script. A main entry point. Reading an argument from sys.argv. Clean top-to-bottom flow a stranger can follow.

And just enough data in: reading a CSV with the standard library csv module. Nothing fancy. Pandas is weeks away.

The lab. You build quakestats.py. It pulls the USGS all-day earthquake feed, a live CSV with a time, a magnitude, and a place for every quake in the last twenty-four hours. No auth. Real data, and it changes every time you run it.

The script takes a magnitude threshold as a command-line argument. It loops over every row. And it uses at least three single-purpose functions.

One parses a row's magnitude, and handles a blank magnitude without crashing. The feed has blanks. Count on it.

One classifies a quake into a bucket: minor under two, light two to four, moderate four to six, strong six and up. That is your if, elif, else.

One summarizes. Count per bucket, total, max and average magnitude above the threshold.

Print a formatted report. Run it twice with two different thresholds and save both outputs so I can see the flow react to the argument.

Commit it on a feature branch, atomic commits, merge by PR. Week one habits, every week. Add a three-sentence why note: why you split the logic into functions, how you chose the buckets, and what you did with missing magnitudes.

A pass. The script runs from the command line with a threshold and reacts to it. The bucket counts match a hand-checked sample. Each function does one thing and returns its result, it does not print it. Blank magnitudes are skipped without a crash. Merged by PR, and the repo still clones and runs from the week one requirements file.

The hot seat.

"Pick one of your functions. Walk me through exactly what it takes in and what it returns. Tell me where that value goes next. Justify why that logic is not just inlined in your main loop. Then show me what happens when a row's magnitude is blank."

The misconceptions I will be listening for: return versus print, and single equals versus double equals. If you can trace any line of your own script aloud and say what it does and why, you are done with week three.

This is the first real Python artifact in your portfolio. An argument-driven script that ingests a live public feed and emits a clean summary. Later phases refactor it into tested, importable modules. It starts here.

**[on-screen / b-roll]** Lower-third: "Week 3 · M02 · Python I." Cutaway A: side by side, a function that prints versus a function that returns, with the caller's variable showing None on the left. Cutaway B: the terminal running quakestats.py 2.5 then quakestats.py 4.0, the bucket counts changing. Callout: "One function. One job. Explicit return."

---

## Week 4: Python II, data structures and files
**Module:** M02 · **Closes:** G1, G6, G4 · **Hours on the page:** ~4h lessons + ~6h lab
**Target:** ~5 minutes (~670 words)

A bare except. Four letters, a colon, and pass. I have found that line in production code at companies you have heard of. It swallows every error silently, and the run reports success while half the records fell on the floor. Handled and ignored are not the same thing. This week you learn the difference, in code.

Week four builds on last week's script. Same earthquake feed, now the GeoJSON version, nested and messier. You bring in the four core collections, real file handling, and targeted error handling. By the end you have the pattern this whole course leans on: read, validate, cast, dedupe, aggregate, and reject with a reason.

Why it matters. Gap four is data quality. The quarantine pattern you build this week is the seed of every bronze ingestion and every data quality lab later in the course. The reason one bad row never gets to crash a nightly load, and never gets to vanish silently either, is this week.

The ideas.

The four collections and when to reach for each. List versus tuple, which is mostly about mutability and intent. Set, for membership and dedupe, constant-time lookup. Dict, for keyed aggregation. You choose by mutability, ordering, and how expensive membership is. You justify the choice.

Iteration patterns. For loops, enumerate, zip, and list, dict, and set comprehensions for reshaping records.

File I/O with context managers. The csv module, DictReader and DictWriter. The json module, load, loads, dump, dumps. The with statement, so files close even when something goes wrong.

Error handling. Try, except, else, finally. Catching a specific exception, never a bare one. Two styles: ask permission first, or try it and handle the failure. And the big one: logging a reject versus silently swallowing it.

Type conversion and missing data. None versus an empty string. Safe casting. Deciding, field by field, whether a missing value means reject the record or fill a default.

The lab. Save the USGS all-month GeoJSON feed locally. Iterate the nested features. For each event: validate it, clean it, cast time, magnitude, and coordinates. Dedupe by event ID using a set. When magnitude, place, or time is missing, do not crash and do not drop. Route the record to a rejects file with a reason.

Aggregate count and max magnitude per region into a dict. Write a clean flat CSV and a JSON run summary.

Then break it on purpose. Inject a handful of malformed records: a null magnitude, a truncated JSON object, a missing ID. Run it again. It has to finish, and every bad record has to show up in the quarantine log with a reason.

Merge by PR, as always. Three-sentence why note: why a set for dedupe and a dict for aggregation, and why malformed records get quarantined instead of dropped or allowed to crash the run.

A pass. The script runs to completion on both the raw feed and the seeded one. Every rejected record is in the quarantine log with a reason. The output CSV has no duplicate event IDs. And the counts reconcile: clean plus rejected equals total read. That last line is the one I check first. If your numbers don't add up, something vanished, and you can't tell me where.

The hot seat.

"Walk me through what happens to a single malformed record end to end. Which exception fires, where you catch it, and why you chose to quarantine it instead of dropping it or letting the run crash. Then defend using a set for dedupe over just checking a list."

What I am listening for: the specific exception by name, and the word "reason" when you describe the rejects file. If your answer is "I wrapped it in a try," we are going to talk.

This week produces the first reusable ingestion module in your portfolio. Next week you refactor it into an installable package. And a few phases from now, when you build a bronze layer that quarantines bad CMS pricing rows, you will recognize it. Same pattern, bigger data.

**[on-screen / b-roll]** Lower-third: "Week 4 · M02 · Python II." Cutaway A: the bare except with pass, red, then the targeted except that writes a reject row with a reason, green. Cutaway B: the reconciliation line, clean + rejected = total, with the three numbers adding up. Callout: "Handled is not ignored."
