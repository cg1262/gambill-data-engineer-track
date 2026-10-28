# Week 1: Make your setup reproducible

Module M00 · [Course lesson](../../../site/phase-1.html#w1)

## Script

Your script works. Then somebody clones the repository and gets an import error. You send them three extra commands in a message. A week later, somebody else needs the same three commands. That is a setup problem you can fix before the project gets complicated.

Start with a terminal inside your project. Run `pwd` to check where you are, then `git status` to see what Git knows about this directory. Relative paths start from your current directory. If a command cannot find a file, check that location before changing the code.

Create a virtual environment with `python -m venv .venv`. On macOS or Linux, activate it with `source .venv/bin/activate`. On Windows PowerShell, use the activation script under `.venv/Scripts`. Now `python -m pip` points at the installer for that interpreter. Install your one dependency, then capture the versions in `requirements.txt`. This gives the next person something specific to install.

Before staging anything, add the environment directory, local secrets, and raw data to `.gitignore`. An ignore rule keeps an untracked file out of future staging. It does not remove something you already committed. Think of it as the guest list at the door; it cannot erase yesterday's attendance record.

Now watch the three Git states. Edit a file: that changes your working tree. Run `git add`: that selects its current contents for your next commit. Run `git commit`: that records the staged snapshot locally. A push transfers commits to a remote. Check `git diff` and `git diff --staged` so you know exactly which snapshot you are recording.

For the lab, keep your baseline small. Make a feature branch, add the environment check, README, and decision note in separate meaningful commits, and review the pull request before merging. Follow the course's three-commit exercise without stretching one change into artificial commits.

Then do the part that proves the README works: use a fresh clone, create and activate a new environment, install from the requirements file, and run the check. Do not rely on the environment you already repaired by hand.

Your evidence is a successful clean setup and a reviewable history. Before you move on, explain which files belong in Git, which stay local, and where somebody would find the exact commands to reproduce your result.

## Screen example — not spoken

Run inside the learner's new course repository, after creating `.gitignore`:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install requests
python -m pip freeze > requirements.txt
git status --short
git diff --staged
```

Show that `.venv/` is absent from status. On a separate fresh clone, activate a new venv before `python -m pip install -r requirements.txt` and `python src/check_env.py`.
