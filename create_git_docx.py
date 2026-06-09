"""Word document version of the Git / Web Developer Tools (FWDN 232) summary.
Mirrors create_git_summary.py: blue terms, red/orange keywords, exam tips/traps,
reference tables, then 15 practice MCQs and an answer key."""
from _keywords_git import KEYWORDS_RED, KEYWORDS_ORANGE
from docx import Document
from docx.shared import RGBColor, Pt, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from datetime import date

BLUE  = RGBColor(0x00, 0x70, 0xC0)
RED   = RGBColor(0xC0, 0x00, 0x00)
GREEN = RGBColor(0x37, 0x86, 0x10)
NAVY  = RGBColor(0x1F, 0x39, 0x64)
TEAL  = RGBColor(0x17, 0x6B, 0x7F)
ORANGE= RGBColor(0xC0, 0x55, 0x00)
GREY  = RGBColor(0x70, 0x70, 0x70)


def shd(para, fill):
    pPr = para._p.get_or_add_pPr()
    e = OxmlElement('w:shd')
    e.set(qn('w:val'), 'clear'); e.set(qn('w:color'), 'auto'); e.set(qn('w:fill'), fill)
    pPr.append(e)


def colorize(run, word):
    tok = word.lower().strip(".,;:()“”\"'")
    if tok in KEYWORDS_RED:
        run.font.color.rgb = RED; run.font.bold = True
    elif tok in KEYWORDS_ORANGE:
        run.font.color.rgb = ORANGE; run.font.bold = True


def ch(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text); r.font.size = Pt(13); r.font.bold = True; r.font.color.rgb = NAVY
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bot = OxmlElement('w:bottom')
    bot.set(qn('w:val'), 'single'); bot.set(qn('w:sz'), '6')
    bot.set(qn('w:space'), '1'); bot.set(qn('w:color'), '1F3964')
    pBdr.append(bot); pPr.append(pBdr)


def sec(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(text); r.font.size = Pt(10.5); r.font.bold = True; r.font.color.rgb = TEAL


def trm(doc, name, defn):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1.5); p.paragraph_format.space_after = Pt(1.5)
    p.paragraph_format.left_indent = Inches(0.12)
    r = p.add_run(name + ": "); r.font.color.rgb = BLUE; r.font.bold = True; r.font.size = Pt(9.5)
    for w in defn.split():
        run = p.add_run(w + " "); run.font.size = Pt(9.5); colorize(run, w)


def codef(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.22); p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1); shd(p, 'F2F2F2')
    r = p.add_run(text); r.font.name = 'Consolas'; r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(0x26, 0x34, 0x3F)


def tipf(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.12); p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2); shd(p, 'E2EFDA')
    r = p.add_run("Exam Tip: "); r.font.bold = True; r.font.color.rgb = GREEN; r.font.size = Pt(8.5)
    for w in text.split():
        run = p.add_run(w + " "); run.font.size = Pt(8.5); colorize(run, w)


def trapf(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.12); p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2); shd(p, 'FCE4D6')
    r = p.add_run("Exam Trap: "); r.font.bold = True; r.font.color.rgb = RED; r.font.size = Pt(8.5)
    for w in text.split():
        run = p.add_run(w + " "); run.font.size = Pt(8.5); colorize(run, w)


def blt(doc, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.left_indent = Inches(0.3); p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    for w in text.split():
        run = p.add_run(w + " "); run.font.size = Pt(9.5); colorize(run, w)


def tbl(doc, headers, rows):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = 'Table Grid'
    t.allow_autofit = True
    hdr = t.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ""
        run = hdr[i].paragraphs[0].add_run(h)
        run.font.bold = True; run.font.size = Pt(8.5); run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shd(hdr[i].paragraphs[0], '1F3964')
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            run = cells[i].paragraphs[0].add_run(val)
            run.font.size = Pt(8.5)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def mcqf(doc, n, stem, options):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(f"Q{n}. {stem}"); r.font.bold = True; r.font.size = Pt(9.5)
    for i, o in enumerate(options):
        letter = "ABCD"[i]
        op = doc.add_paragraph()
        op.paragraph_format.left_indent = Inches(0.3)
        op.paragraph_format.space_before = Pt(0); op.paragraph_format.space_after = Pt(0)
        lr = op.add_run(f"{letter}. "); lr.font.bold = True; lr.font.color.rgb = NAVY; lr.font.size = Pt(9)
        tr = op.add_run(o); tr.font.size = Pt(9)


doc = Document()
for s in doc.sections:
    s.top_margin = Cm(1.6); s.bottom_margin = Cm(1.6); s.left_margin = Cm(1.9); s.right_margin = Cm(1.9)
doc.styles['Normal'].font.name = 'Calibri'; doc.styles['Normal'].font.size = Pt(9.5)

# ── COVER ───────────────────────────────────────────────────────
doc.add_paragraph(); doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Git & Version Control"); r.font.size = Pt(24); r.font.bold = True; r.font.color.rgb = NAVY
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Study Summary — Chapters 1–9"); r.font.size = Pt(14); r.font.color.rgb = TEAL
doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("FWDN 232: Web Developer Tools  |  Full Stack Web Developer"); r.font.size = Pt(11); r.font.bold = True
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Textbook: Jump Start Git, 2nd Edition (2020) — Shaumik Daityari"); r.font.size = Pt(9); r.font.color.rgb = GREY
doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Includes 15 practice MCQs with answer key"); r.font.size = Pt(9); r.font.italic = True
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(f"Prepared: {date.today().strftime('%B %Y')}"); r.font.size = Pt(10); r.font.color.rgb = GREY
doc.add_page_break()

# ── CHAPTER 1 ───────────────────────────────────────────────────
ch(doc, "Chapter 1: Introduction to Git & Version Control")
sec(doc, "Key Definitions")
trm(doc, "Version Control (VCS)", "A system that records changes to a file or group of files over time, so you can review or revert to specific versions later. Think of it as snapshots / checkpoints of your work.")
trm(doc, "Backup vs Version Control", "Version control removes the need for duplicate-named backup files, but it does NOT replace a real backup solution (external drive or cloud) against disk failure.")
trm(doc, "Centralized VCS", "A single copy of the project is hosted on a central server everyone connects to; uses a first-come, first-served principle. Examples: CVS, Subversion (SVN).")
trm(doc, "Distributed VCS", "Every developer has a full copy of the entire project including its complete history. They work and commit offline, then synchronize later. Examples: Git, Mercurial, Bazaar.")
trm(doc, "Git", "A distributed version control system created by Linus Torvalds (Junio Hamano is the primary maintainer). Designed to be distributed, reliable, fast, and safe from corruption.")
trm(doc, "Git vs GitHub", "Git is the version control system itself. GitHub is a cloud-based hosting service that stores Git repositories and adds a web interface. They are NOT the same thing.")
trm(doc, "Conflict", "Occurs when multiple people change the same file in clashing ways. The VCS highlights the conflict and lets you resolve it so no data is lost.")
tipf(doc, "Git was built by Linus Torvalds because BitKeeper, though good, was a commercial product unsuitable for an open-source project like Linux.")
tipf(doc, "Distributed VCS lets you work offline and sync directly with peers, bypassing the central server entirely.")
trapf(doc, "Do NOT confuse VCS (the general category) with CVS (Concurrent Versions System, just one specific tool).")
trapf(doc, "Version control is NOT a backup solution. You still need real off-site backups against disk failure.")

# ── CHAPTER 2 ───────────────────────────────────────────────────
ch(doc, "Chapter 2: Getting Started with Git")
sec(doc, "Key Definitions")
trm(doc, "Repository", "The parent directory containing your project — all files and directories tracked by Git. Created by running git init, which adds a hidden .git directory.")
trm(doc, "The Three Basic Operations", "Git performs three core operations: track (watch a file), stage (mark changes to record), and commit (save a snapshot).")
trm(doc, "Tracked vs Untracked", "A tracked file is one Git monitors for changes. New files are untracked by default and ignored until you run git add to track them.")
trm(doc, "Staging", "Tagging certain (or all) changes that you want to record in the next commit. git add moves changes into the staging area.")
trm(doc, "Commit", "A snapshot recording the state of your code since the last commit. Each has a unique commit hash, author details, a message, and the list of changes. You can revert to any commit.")
trm(doc, "Commit Hash", "A unique identifying signature generated automatically for each commit (40 characters). Usually the first 5–6 characters are enough; 3 is too ambiguous.")
trm(doc, "git diff", "Shows the changes in tracked files since the last commit. Added lines show + (green), removed lines show - (red).")
trm(doc, "Remote", "A copy of your repository stored elsewhere (server, cloud, or peer's machine). origin is the conventional name for the default remote.")
trm(doc, ".gitignore", "A file in the repository root listing files, directories, or extensions Git should never track (e.g. *.exe, .DS_Store, node_modules).")
sec(doc, "Essential Commands")
codef(doc, 'git config --global user.name "Name"     # set identity for all repos')
codef(doc, 'git init                                  # initialize a repository')
codef(doc, 'git add .          # stage all   |   git add file   # stage one')
codef(doc, 'git commit -m "message"                   # create a commit')
codef(doc, 'git remote add origin <url>   &&   git push -u origin master')
tipf(doc, "The package-manager mantra: it installs an OLDER but MORE RELIABLE version of Git. Memorize that trade-off.")
tipf(doc, "'Why git add again?' — like packing a parcel: git add = put item in the box, git commit = seal & label, git push = send. You re-add to choose WHICH files to commit.")
trapf(doc, "git add does NOT create a commit — it only stages. Changes are not saved until git commit runs.")
trapf(doc, "The -u flag in git push -u origin master LINKS your branch to the remote; it does not mean upload urgently.")

# ── CHAPTER 3 ───────────────────────────────────────────────────
ch(doc, "Chapter 3: Branching in Git")
sec(doc, "Key Definitions")
trm(doc, "Branch", "An independent path of development — effectively a new copy of the project you can experiment on without affecting master. A branch is a named sequence of commits.")
trm(doc, "master Branch", "The default branch you start in. The name implies no superiority — it is just a convention for the main line of development.")
trm(doc, "HEAD", "A pointer to the latest commit of the current active branch — the tip of the branch. HEAD and the tip of the active branch point to the same commit.")
trm(doc, "Cloning", "The process of creating a local copy of a repository from a different source. After cloning you can also see remote branches with git branch -a.")
trm(doc, "Checkout", "Switches the active branch. git checkout <name> moves to an existing branch; git checkout -b <name> creates and switches in one step.")
trm(doc, "Merge", "Combines the changes of one branch into another. Checkout the destination branch first, then run git merge <source>.")
trm(doc, "Fast-Forward Merge", "When the target branch has no new commits of its own, Git just moves the pointer forward. Only the pathway changes and HEAD updates — no merge commit (the default).")
trm(doc, "No-Fast-Forward Merge (--no-ff)", "Forces a new merge commit even when fast-forward is possible. Recommended for merges into master to logically record the feature.")
trm(doc, "Merge Conflict", "Happens when the same file is modified in non-common commits in both branches. Git raises a conflict so you do not lose data and asks you to resolve it.")
sec(doc, "Branch Commands")
codef(doc, 'git branch          # list   |   git branch -a   # include remotes')
codef(doc, 'git checkout -b feature      # create + switch in one command')
codef(doc, 'git branch -d name   # safe delete  |  git branch -D name   # force delete')
codef(doc, 'git checkout master   &&   git merge --no-ff feature')
tipf(doc, "-d (safe) only deletes a branch already merged/synced; -D force-deletes even unmerged commits with no warning.")
tipf(doc, "Use --no-ff when merging into master so the history clearly shows where a feature was integrated.")
trapf(doc, "A fast-forward merge does NOT create a merge commit — it just moves the pointer. Only --no-ff creates one.")
trapf(doc, "git branch <name> creates a branch but does NOT switch to it — you stay on the current branch until you checkout.")

# ── CHAPTER 5 ───────────────────────────────────────────────────
ch(doc, "Chapter 5: Git Workflows")
sec(doc, "Key Definitions")
trm(doc, "Git Workflow", "A set of guidelines a team follows to manage a project — covering architecture, how contributions are made, and how others' work is merged in.")
trm(doc, "Centralized Workflow", "The simplest workflow: a single branch (usually master) for all operations, treated as the main copy. Also called the trunk workflow. No branching is used.")
trm(doc, "Feature-Branch Workflow", "Each feature is developed in its own branch, then merged or rebased into master after a code review. A developer must never directly commit to the local master.")
trm(doc, "Gitflow Workflow", "An extension of feature-branch with defined branch roles. Two core branches: develop (latest dev) and master (last stable release), plus feature, release, hotfix branches.")
trm(doc, "Hotfix Branch", "In Gitflow, a branch created from master to fix a critical bug immediately. Once fixed it merges back into BOTH master and develop.")
trm(doc, "Forking Workflow", "A cloud implementation of feature-branch. Each developer has a personal server-side copy (a fork); changes are pushed to the fork and merged via a pull request.")
trm(doc, "Fork", "A developer's personal copy of the central repository in the cloud. origin points to the fork; upstream points to the central repository.")
sec(doc, "Choosing a Workflow")
tbl(doc, ["Workflow", "Best For", "Branching?"], [
    ["Centralized", "Beginners, solo projects, SVN converts", "No"],
    ["Feature-branch", "Growing teams, open source (code review)", "Yes"],
    ["Gitflow", "Mature projects, mixed teams, multiple versions", "Yes (roles)"],
    ["Forking", "Any cloud-hosted / open-source project", "Yes (+ fork)"],
])
tipf(doc, "Open-source projects must use at least a feature-branch workflow so code reviews happen before contributor merges.")
trapf(doc, "The centralized workflow does NOT use branching — giving everyone master access means one bad commit can corrupt the whole repository.")
trapf(doc, "In Gitflow a hotfix merges into BOTH master AND develop — forgetting develop means the bug reappears next release.")

# ── CHAPTER 6 ───────────────────────────────────────────────────
ch(doc, "Chapter 6: Correcting Errors While Working with Git")
sec(doc, "Key Definitions")
trm(doc, "Undo git add (untrack)", "git rm --cached <file> untracks a file but leaves it on disk. Use it to undo accidentally tracking a new file before it is committed.")
trm(doc, "git reset --soft", "Undoes a commit but KEEPS its changes staged for review. HEAD~1 means go back one commit from the current HEAD.")
trm(doc, "git reset --mixed (default)", "Undoes the commit AND unstages the changes (files keep their edits but are not staged). This is the default reset mode.")
trm(doc, "git reset --hard", "Undoes the commit and discards all changes — a state even before the files were edited. Avoid it unless absolutely sure; it permanently destroys work.")
trm(doc, "reset vs revert", "reset rewrites history by moving HEAD backward. revert creates a NEW commit that reverses a faulty commit — history is preserved. revert is safe for pushed commits.")
trm(doc, "git commit --amend", "Changes the message (or content) of the LAST commit. The hash changes too, effectively rewriting history.")
trm(doc, "Undo a Push (force push)", "Reset locally then force the update with git push -f. A normal push is rejected because the remote HEAD is ahead of your local branch.")
trm(doc, "git blame", "Shows, for each line of a file, the commit hash, author, and date that last changed it. Used when you KNOW which file contains the bug.")
trm(doc, "git bisect", "Performs a binary search through commits to find the one that introduced a bug. Mark a good and a bad commit; narrows in logarithmic steps. Used when you DON'T know the source.")
sec(doc, "Reset Modes — Quick Reference")
tbl(doc, ["Option", "Commit", "Staged?", "Changes Kept?"], [
    ["--soft", "Undone", "Yes (staged)", "Yes"],
    ["--mixed (default)", "Undone", "No (unstaged)", "Yes"],
    ["--hard", "Undone", "No", "No (discarded)"],
])
codef(doc, 'git rm --cached file   |   git reset --soft HEAD~1   |   git revert <hash>')
codef(doc, 'git commit --amend -m "new message"   |   git push -f origin master')
tipf(doc, "git bisect finds a bad commit among thousands in a few steps via BINARY SEARCH. Automate it: git bisect run <test command>.")
tipf(doc, "Use revert (not reset) to undo a commit already PUSHED — it adds a new reversing commit instead of rewriting shared history.")
trapf(doc, "--hard PERMANENTLY discards your changes. The book explicitly warns to avoid it unless you are absolutely certain.")
trapf(doc, "reset CHANGES history; revert PRESERVES it. Do not use reset on commits others have already pulled.")

# ── CHAPTER 7 ───────────────────────────────────────────────────
ch(doc, "Chapter 7: Unlocking Git's Full Potential")
sec(doc, "Key Definitions")
trm(doc, "git log --oneline", "Compresses each commit to a single line (short hash + message). Combine with --all, --decorate, and --graph to visualize all branches.")
trm(doc, "git shortlog", "Groups commits by author, showing each contributor and their messages. Postfix -n to sort by number of commits.")
trm(doc, "Filtering log", "git log -n 2 shows the last 2 commits; --after/--before (or --since/--until) filter by date; --author filters by author; --grep searches messages.")
trm(doc, "Tag", "A label attached to a milestone commit, typically a version number. Two types: lightweight and annotated.")
trm(doc, "Annotated vs Lightweight Tag", "Annotated tags store the tagger, date, and a message — preferred in organizations. Lightweight tags are just a name on a commit — handy for personal projects.")
trm(doc, "Ref & reflog", "A ref is a pointer to a commit (HEAD, ORIG_HEAD, MERGE_HEAD are refs). The reflog is a log of refs recording every local action — it can recover lost commits. NOT synced to the server.")
trm(doc, "git fsck", "File system check — finds commits not part of any branch (lost commits) that git log cannot show. Recover one with git merge <hash>.")
trm(doc, "Rebase", "Rewrites a branch's history by moving it onto a new base commit, producing a LINEAR history without the loops a merge creates. Preferred for a clean central history.")
trm(doc, "Squash", "Combining multiple commits into one, done via interactive rebase (git rebase -i HEAD~2). There is no stand-alone git squash command.")
trm(doc, "Stash", "Saves uncommitted changes and reverts the working directory to the last commit, so you can switch context. Reapply later with git stash apply.")
trm(doc, "git add -p", "Stages only PART of a file's changes by splitting them into hunks. Options: y (stage), n (skip), s (split), e (edit). Lets one file's edits go into separate commits.")
trm(doc, "Cherry-Pick", "Picks a single commit from another branch and applies it to your current branch — when a full merge or rebase would be too much. git cherry-pick <hash>.")
sec(doc, "Power Commands")
codef(doc, 'git log --oneline --graph --all --decorate')
codef(doc, 'git tag -a v1.0 -m "msg"   |   git push origin --tags')
codef(doc, 'git rebase master   |   git rebase -i HEAD~2   |   git cherry-pick <hash>')
codef(doc, 'git stash   |   git stash apply stash@{1}   |   git reflog')
tipf(doc, "rebase = LINEAR history (no loops); merge = preserves the true branch topology with a merge commit. Prefer rebase to keep a central repo tidy.")
tipf(doc, "reflog and fsck are your recovery tools: a lost commit from a hard reset or deleted branch is usually still recoverable.")
trapf(doc, "There is NO git squash command — squashing is done through interactive rebase (git rebase -i).")
trapf(doc, "Tags are NOT pushed automatically with git push — you must run git push origin --tags.")

# ── CHAPTER 8 ───────────────────────────────────────────────────
ch(doc, "Chapter 8: Integrate Git in Your Development Cycle")
sec(doc, "Key Definitions")
trm(doc, "DevOps", "A cross between Development, Operations, and QA that automates the software development cycle to lower time to market. Arose to remove friction between separate teams.")
trm(doc, "Continuous Integration (CI)", "The second step of the DevOps cycle: testing all code on every push and merging into the main codebase if all tests pass. Ensures new changes do not break functionality.")
trm(doc, "Git Hook", "A custom script that executes automatically when a predefined Git event occurs. Lets you trigger actions at key points in the life cycle. Stored in the .git/hooks directory.")
trm(doc, "Client-side vs Server-side Hooks", "Client-side hooks react to local actions (pre-commit, commit-msg, post-commit). Server-side hooks react to network actions like a push (pre-receive, update, post-receive).")
trm(doc, "pre-commit Hook", "The most important hook — runs before a commit message is entered, commonly used to run unit tests so broken code is never committed.")
trm(doc, "Travis CI", "A popular hosted CI tool for GitHub repositories (free for open source). On every push it clones the repo to a cloud VM, installs requirements, and runs unit tests.")
trm(doc, ".travis.yml", "The configuration file (in the repo root) telling Travis CI the language, versions, install commands, and test commands. Each version listed creates a separate build.")
sec(doc, "Common Git Hooks")
tbl(doc, ["Hook", "Triggered", "Side"], [
    ["pre-commit", "Before the commit message is entered", "Client"],
    ["commit-msg", "With the commit message", "Client"],
    ["post-commit", "After a commit completes", "Client"],
    ["pre-push", "Before changes are sent to a remote", "Client"],
    ["pre/post-receive", "Before / after a push from a client", "Server"],
])
tipf(doc, "Hooks live in .git/hooks as .sample files. To activate one, remove the .sample extension and make sure the file is executable.")
trapf(doc, "Git hook samples are Bash scripts (#!/bin/sh), but you CAN change the first line to use another language — they are not limited to Bash.")
trapf(doc, "Continuous integration is the SECOND step of DevOps, not the first. Continuous development comes first.")

# ── CHAPTER 9 ───────────────────────────────────────────────────
ch(doc, "Chapter 9: Git GUI Tools")
sec(doc, "Key Definitions")
trm(doc, "GUI Tool", "A graphical client used instead of the terminal. Easier for beginners, but tools differ in UI and terminology, lack some terminal power, and run more slowly.")
trm(doc, "GitHub Desktop", "GitHub's own unified GUI client (Windows + macOS, since 2015). Hides the term staging — you just select files and commit. Focused on bridging local repos with the GitHub website.")
trm(doc, "Sourcetree", "Atlassian's GUI client (Windows + macOS). Works with both Git and Mercurial, offers more features and control, and its options closely match the terminal commands.")
trm(doc, "Submodule", "A Git repository nested within a parent repository. Listed in Sourcetree's left menu alongside branches, tags, remotes, and stashes.")
trm(doc, "Editor Integrations", "Git can also be used through text editors: Atom (built-in Git/GitHub), Sublime Text (Git package), and Visual Studio's version control tools.")
sec(doc, "GUI Tool Comparison")
tbl(doc, ["", "GitHub Desktop", "Sourcetree"], [
    ["Developer", "GitHub", "Atlassian"],
    ["VCS support", "Git", "Git + Mercurial"],
    ["Audience", "Beginners (simplified)", "Power users (matches CLI)"],
])
tipf(doc, "Neither GitHub Desktop nor Sourcetree supports Linux. Cross-platform GUIs include SmartGit, Fork, and GitKraken.")
trapf(doc, "GitHub Desktop deliberately hides the word staging to simplify things — the underlying staging step does not disappear.")
trapf(doc, "GUI tools are NOT cross-platform and run slower than the terminal; no single GUI behaves identically across all operating systems.")

# ── PRACTICE QUESTIONS ──────────────────────────────────────────
doc.add_page_break()
p = doc.add_paragraph()
r = p.add_run("Practice Questions — Top 15 MCQ"); r.font.size = Pt(13); r.font.bold = True; r.font.color.rgb = GREEN
pPr = p._p.get_or_add_pPr(); pBdr = OxmlElement('w:pBdr'); bot = OxmlElement('w:bottom')
bot.set(qn('w:val'), 'single'); bot.set(qn('w:sz'), '6'); bot.set(qn('w:space'), '1'); bot.set(qn('w:color'), '378610')
pBdr.append(bot); pPr.append(pBdr)
p = doc.add_paragraph()
r = p.add_run("Choose the single best answer. Options are deliberately close — read carefully. Answer key follows."); r.font.size = Pt(8.5); r.font.italic = True; r.font.color.rgb = GREY

MCQS = [
    ("A developer needs to keep working offline for a week, committing changes without any server connection, then sync later. Which property of Git makes this possible?",
     ["It is a centralized version control system",
      "It is a distributed VCS where each clone holds the full history",
      "It uses a first-come, first-served locking model",
      "It stores all commits only on the origin remote"]),
    ("You created a new file but have NOT committed it, and you realize Git should not be tracking it yet. Which command removes it from tracking while keeping the file on disk?",
     ["git rm mistake_file",
      "git reset --hard",
      "git rm --cached mistake_file",
      "git checkout -- mistake_file"]),
    ("Which statement about a fast-forward merge is correct?",
     ["It always creates a new merge commit",
      "It only moves the branch pointer forward and updates HEAD, with no merge commit",
      "It is triggered by the --no-ff flag",
      "It is the only way to merge when both branches have new commits"]),
    ("A commit has already been pushed to a shared remote and others have pulled it. You must undo its effect safely. What is the recommended approach?",
     ["git reset --hard then git push -f",
      "git commit --amend",
      "git revert <hash> to add a new reversing commit",
      "git rm --cached on the affected files"]),
    ("Which reset mode undoes a commit but leaves the changes STAGED, ready to be re-committed?",
     ["git reset --hard HEAD~1",
      "git reset --mixed HEAD~1",
      "git reset --soft HEAD~1",
      "git revert HEAD~1"]),
    ("You have no idea which of the last 500 commits introduced a bug, but you know a commit from last month was fine. Which tool finds the culprit most efficiently?",
     ["git blame, because it shows line authorship",
      "git bisect, because it does a binary search through commits",
      "git log --oneline, scanning each commit by hand",
      "git reflog, because it lists every local action"]),
    ("In the Gitflow workflow, where is a hotfix branch created from, and where must it be merged back?",
     ["Created from develop; merged into master only",
      "Created from master; merged into BOTH master and develop",
      "Created from a feature branch; merged into develop only",
      "Created from a release branch; merged into master only"]),
    ("What is the practical difference between an annotated tag and a lightweight tag?",
     ["Lightweight tags store the tagger name, date, and message",
      "Annotated tags can only be created on the master branch",
      "Annotated tags store tagger info and a message; lightweight tags are just a name pointing to a commit",
      "There is no difference; the names are interchangeable"]),
    ("You ran git push but it was REJECTED because the remote HEAD is ahead of your local branch after a reset. What must you do to overwrite the remote (assuming you are sure)?",
     ["Run git pull --rebase first, always",
      "Force the push with git push -f",
      "Run git commit --amend and push again",
      "Delete the remote and re-add it"]),
    ("Which statement about git stash is TRUE?",
     ["Stashed changes are automatically pushed to the remote",
      "A stash saves uncommitted changes and reverts the working directory to the last commit",
      "git stash permanently deletes your uncommitted changes",
      "Stashes are stored on origin and shared with the team"]),
    ("A teammate wants only ONE specific commit from another branch — not the whole branch. Which command applies just that commit to the current branch?",
     ["git merge <branch>",
      "git rebase <branch>",
      "git cherry-pick <hash>",
      "git checkout <hash>"]),
    ("Which choice correctly distinguishes Git from GitHub?",
     ["Git is a website; GitHub is a command-line tool",
      "Git is a distributed VCS; GitHub is a cloud service that hosts Git repositories",
      "They are two names for the same product",
      "Git only works online; GitHub works offline"]),
    ("You want to combine your last three messy commits into a single clean commit before opening a pull request. What do you use?",
     ["The stand-alone git squash command",
      "git merge --squash on master",
      "Interactive rebase: git rebase -i HEAD~3",
      "git reset --soft only"]),
    ("Which Git hook is most commonly used to run unit tests so broken code is never recorded, and on which side does it run?",
     ["post-receive, server-side",
      "pre-commit, client-side",
      "pre-receive, server-side",
      "commit-msg, client-side"]),
    ("Why does the book recommend learning terminal Git even if you prefer a GUI like GitHub Desktop or Sourcetree?",
     ["GUI tools support every operating system identically",
      "GUI tools are always faster than the terminal",
      "On a headless remote server only command-line Git works, and GUIs aren't cross-platform",
      "Terminal commands cannot cause data loss, unlike GUIs"]),
]
for i, (stem, opts) in enumerate(MCQS, 1):
    mcqf(doc, i, stem, opts)

# ── ANSWER KEY ──────────────────────────────────────────────────
doc.add_page_break()
p = doc.add_paragraph()
r = p.add_run("Answer Key"); r.font.size = Pt(13); r.font.bold = True; r.font.color.rgb = GREEN
pPr = p._p.get_or_add_pPr(); pBdr = OxmlElement('w:pBdr'); bot = OxmlElement('w:bottom')
bot.set(qn('w:val'), 'single'); bot.set(qn('w:sz'), '6'); bot.set(qn('w:space'), '1'); bot.set(qn('w:color'), '378610')
pBdr.append(bot); pPr.append(pBdr)

ANSWERS = [
    ("1", "B", "Every clone in a distributed VCS holds the full history, so you can commit offline and sync later."),
    ("2", "C", "git rm --cached untracks the file but leaves it on disk; plain git rm would also delete it."),
    ("3", "B", "Fast-forward simply advances the pointer/HEAD with no merge commit; --no-ff forces a merge commit."),
    ("4", "C", "revert adds a new reversing commit and preserves shared history; reset --hard/-f rewrites history others have."),
    ("5", "C", "--soft undoes the commit but keeps changes staged; --mixed unstages them; --hard discards them."),
    ("6", "B", "git bisect performs a binary search (logarithmic steps); blame is for when you already know the file."),
    ("7", "B", "A hotfix is cut from master and merged back into BOTH master and develop so the fix isn't lost next release."),
    ("8", "C", "Annotated tags carry tagger info + message (preferred in orgs); lightweight tags are just a name on a commit."),
    ("9", "B", "After a local reset the remote is ahead, so a normal push is rejected; -f forces the overwrite."),
    ("10", "B", "stash saves uncommitted work and restores the last-commit state; it is local and reversible, not pushed."),
    ("11", "C", "cherry-pick applies a single chosen commit; merge/rebase would bring the whole branch."),
    ("12", "B", "Git is the VCS itself; GitHub is a cloud hosting service built around Git."),
    ("13", "C", "Squashing is done via interactive rebase (git rebase -i); there is no stand-alone git squash command."),
    ("14", "B", "pre-commit runs client-side before the message is entered — the usual place to run unit tests."),
    ("15", "C", "Headless remote servers only have the CLI, and GUI tools are not cross-platform / behave differently per OS."),
]
t = doc.add_table(rows=1, cols=3)
t.style = 'Table Grid'
hdr = t.rows[0].cells
for i, h in enumerate(["#", "Answer", "Justification"]):
    hdr[i].text = ""
    run = hdr[i].paragraphs[0].add_run(h)
    run.font.bold = True; run.font.size = Pt(9); run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    shd(hdr[i].paragraphs[0], '378610')
for q, a, why in ANSWERS:
    cells = t.add_row().cells
    cells[0].text = ""; r0 = cells[0].paragraphs[0].add_run(f"Q{q}"); r0.font.bold = True; r0.font.size = Pt(9)
    cells[1].text = ""; r1 = cells[1].paragraphs[0].add_run(a); r1.font.bold = True; r1.font.color.rgb = RED; r1.font.size = Pt(9)
    cells[2].text = ""; r2 = cells[2].paragraphs[0].add_run(why); r2.font.size = Pt(9)

doc.save("git_summary.docx")
print("Saved: git_summary.docx")
