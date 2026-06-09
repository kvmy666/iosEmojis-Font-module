"""
Git / Web Developer Tools (FWDN 232) – Study Summary
8 Chapters (1,2,3,5,6,7,8,9) | 12–15 pages target
Same format as previous summaries (blue terms, red/orange keywords, exam tips/traps),
followed by 15 practice MCQs and an answer key.
"""
import re
from _keywords_git import KEYWORDS_RED, KEYWORDS_ORANGE
from datetime import date


def colorize(text):
    parts = re.split(r'(\s+)', text)
    out = []
    for p in parts:
        tok = p.lower().strip(".,;:()“”\"'")
        if tok in KEYWORDS_RED:
            out.append(f'<span class="kw-red">{p}</span>')
        elif tok in KEYWORDS_ORANGE:
            out.append(f'<span class="kw-orange">{p}</span>')
        else:
            out.append(p)
    return "".join(out)


def term(name, definition):
    return (f'<p class="term"><span class="term-name">{name}:</span> '
            f'{colorize(definition)}</p>')


def code(line):
    return f'<pre class="code">{line}</pre>'


def tip(text):
    return f'<div class="tip"><strong>Exam Tip:</strong> {colorize(text)}</div>'


def trap(text):
    return f'<div class="trap"><strong>Exam Trap:</strong> {colorize(text)}</div>'


def bullet(text):
    return f'<li>{colorize(text)}</li>'


def chapter(title):
    return f'<h2>{title}</h2>'


def section(title):
    return f'<h3>{title}</h3>'


def mcq(n, stem, options):
    letters = "ABCD"
    opts = "".join(
        f'<div class="mcq-opt"><span class="mcq-letter">{letters[i]}.</span> {o}</div>'
        for i, o in enumerate(options)
    )
    return (f'<div class="mcq"><p class="mcq-q">Q{n}. {stem}</p>{opts}</div>')


CSS = """
@page {
    size: A4;
    margin: 16mm 18mm 16mm 18mm;
    @bottom-right { content: counter(page); font-size:9pt; color:#888; }
}
.cover {
    page-break-after: always;
    text-align: center;
    padding: 44pt 28pt;
    border: 2pt solid #1F3964;
    border-radius: 8pt;
    background: linear-gradient(150deg,#EBF3FB,#F8FBFF);
    min-height: 230mm;
    box-sizing: border-box;
}
body { font-family: Calibri, Arial, sans-serif; font-size:9.5pt; color:#222; line-height:1.45; }
h1   { color:#1F3964; font-size:24pt; margin:0 0 6pt; }
.subtitle { color:#17738F; font-size:13pt; margin:4pt 0; }
.course   { font-size:11pt; font-weight:bold; margin:6pt 0; }
.date-line{ color:#888; font-size:10pt; }
h2 {
    color:#1F3964; font-size:12.5pt; font-weight:bold;
    border-bottom:2pt solid #1F3964;
    padding-bottom:2pt; margin:0; margin-bottom:4pt;
    page-break-before: always;
}
h3 { color:#17738F; font-size:10pt; font-weight:bold; margin-top:8pt; margin-bottom:2pt; }
p.term { margin:2.5pt 0 2.5pt 10pt; font-size:9.5pt; }
span.term-name { color:#0070C0; font-weight:bold; }
span.kw-red    { color:#C00000; font-weight:bold; }
span.kw-orange { color:#C05500; font-weight:bold; }
pre.code {
    font-family:'Courier New',monospace; font-size:8pt;
    background:#F2F2F2; color:#26343F;
    margin:2pt 0 2pt 18pt; padding:3pt 6pt;
    border-radius:3pt; white-space:pre-wrap; word-break:break-all;
}
ul { margin:2pt 0 2pt 24pt; padding:0; }
li { margin:1pt 0; font-size:9.5pt; }
.tip  { background:#E2EFDA; border-left:3pt solid #378610; padding:3pt 7pt; margin:3pt 0 3pt 8pt; font-size:8.5pt; }
.tip strong { color:#378610; }
.trap { background:#FCE4D6; border-left:3pt solid #C00000; padding:3pt 7pt; margin:3pt 0 3pt 8pt; font-size:8.5pt; }
.trap strong { color:#C00000; }
.ref-table { width:100%; border-collapse:collapse; font-size:8.5pt; margin:4pt 0 4pt 8pt; }
.ref-table th { background:#1F3964; color:white; padding:3pt 6pt; text-align:left; }
.ref-table td { border:1pt solid #BFBFBF; padding:2pt 6pt; }
.ref-table tr:nth-child(even) td { background:#F2F2F2; }
code { font-family:'Courier New',monospace; background:#F2F2F2; padding:0 2pt; border-radius:2pt; }
.mcq { margin:5pt 0 5pt 4pt; page-break-inside: avoid; }
.mcq-q { font-weight:bold; margin:0 0 2pt; font-size:9.5pt; }
.mcq-opt { margin:0.5pt 0 0.5pt 14pt; font-size:9pt; }
.mcq-letter { font-weight:bold; color:#1F3964; }
.ans-table { width:100%; border-collapse:collapse; font-size:9pt; margin:4pt 0; }
.ans-table th { background:#378610; color:white; padding:3pt 6pt; text-align:left; }
.ans-table td { border:1pt solid #BFBFBF; padding:3pt 6pt; vertical-align:top; }
.ans-table tr:nth-child(even) td { background:#F2F2F2; }
.ans-letter { font-weight:bold; color:#C00000; }
.intro-note { font-size:8.5pt; color:#555; font-style:italic; margin:2pt 0 6pt 4pt; }
"""

body = []

# ── COVER ───────────────────────────────────────────────────────
body.append(f"""
<div class="cover">
  <h1>Git &amp; Version Control</h1>
  <p class="subtitle">Study Summary &ndash; Chapters 1&ndash;9</p>
  <br>
  <p class="course">FWDN 232: Web Developer Tools &nbsp;|&nbsp; Full Stack Web Developer</p>
  <p style="font-size:9pt;color:#444;margin-top:8pt;">
    Textbook: <em>Jump Start Git</em>, 2nd Edition (2020) &mdash; Shaumik Daityari
  </p>
  <br>
  <p style="font-size:9pt;color:#444;line-height:1.8;">
    Ch1: Introduction to Version Control &bull; Ch2: Getting Started with Git<br>
    Ch3: Branching in Git &bull; Ch5: Git Workflows<br>
    Ch6: Correcting Errors &bull; Ch7: Unlocking Git&rsquo;s Full Potential<br>
    Ch8: Integrate Git in Your Development Cycle &bull; Ch9: Git GUI Tools<br>
    <span style="font-size:8pt;color:#888;">(Chapter 4 not included in source material)</span>
  </p>
  <br><br>
  <p style="font-size:8.5pt;color:#555;">Includes 15 practice MCQs with answer key</p>
  <p class="date-line">Prepared: {date.today().strftime('%B %Y')}</p>
</div>
""")

# ════════════════════════════════════════════════════════════════
# CHAPTER 1 – INTRODUCTION TO VERSION CONTROL
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 1: Introduction to Git &amp; Version Control"))
body.append(section("Key Definitions"))

body.append(term("Version Control (VCS)",
    "A system that records changes to a file or group of files over time, so you can review "
    "or revert to specific versions later. Think of it as taking snapshots / checkpoints of your work."))

body.append(term("Backup vs Version Control",
    "Version control removes the need for duplicate-named backup files, but it does NOT replace a "
    "real backup solution (e.g. external drive or cloud) that protects against disk failure."))

body.append(term("Centralized VCS",
    "A single copy of the project is hosted on a central server that everyone connects to; "
    "uses a 'first come, first served' principle. Examples: CVS, Subversion (SVN)."))

body.append(term("Distributed VCS",
    "Every developer has a full copy of the entire project, including its complete history. "
    "Developers work and commit offline, then synchronize changes later. Examples: Git, Mercurial, Bazaar."))

body.append(term("Git",
    "A distributed version control system created by Linus Torvalds (Junio Hamano is the primary "
    "maintainer). Designed to be distributed, reliable, fast, and safe from corruption."))

body.append(term("Git vs GitHub",
    "Git is the version control system itself. GitHub is a cloud-based hosting service that stores "
    "Git repositories and adds a web interface. They are NOT the same thing."))

body.append(term("Conflict",
    "Occurs when multiple people change the same file in clashing ways. The VCS highlights the conflict "
    "and lets you resolve it, so no data is lost."))

body.append(tip("Git was built by Linus Torvalds (the Linux creator) because BitKeeper, though good, was a commercial product unsuitable for an open-source project like Linux."))
body.append(tip("Distributed VCS lets you work offline and sync directly with peers, bypassing the central server entirely."))
body.append(trap("Do NOT confuse VCS (version control system, the general category) with CVS (Concurrent Versions System, just one specific tool)."))
body.append(trap("Version control is NOT a backup solution. 'Backup' here means avoiding duplicate files — you still need real off-site backups against disk failure."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 2 – GETTING STARTED WITH GIT
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 2: Getting Started with Git"))
body.append(section("Key Definitions"))

body.append(term("Repository",
    "The parent directory containing your project — all files and directories tracked by Git. "
    "Created by running git init, which adds a hidden .git directory."))

body.append(term("The Three Basic Operations",
    "Git performs three core operations on your project: track (tell Git to watch a file), "
    "stage (mark changes to record), and commit (save a snapshot)."))

body.append(term("Tracked vs Untracked",
    "A tracked file is one Git monitors for changes. New files are untracked by default and are "
    "ignored until you explicitly run git add to track them."))

body.append(term("Staging",
    "Tagging certain (or all) changes that you want to record in the next commit. "
    "git add moves changes into the staging area."))

body.append(term("Commit",
    "A snapshot that records the current state of your code since the last commit. Each commit has a "
    "unique commit hash, the author details, a message, and the list of changes. You can revert to any commit."))

body.append(term("Commit Hash",
    "A unique identifying signature generated automatically for each commit (40 characters). "
    "Usually the first 5–6 characters are enough to identify it; 3 characters is too ambiguous."))

body.append(term("git diff",
    "Shows the changes in tracked files since the last commit. Lines added are shown with + (green), "
    "lines removed with - (red)."))

body.append(term("Remote",
    "A copy of your repository stored elsewhere (a server, the cloud, or a peer's machine). "
    "origin is the conventional name for the default remote."))

body.append(term(".gitignore",
    "A file in the repository root that lists files, directories, or extensions Git should never track "
    "(e.g. *.exe, .DS_Store, node_modules). Patterns use wildcards like *.exe."))

body.append(section("Essential Commands"))
body.append(code('git config --global user.name "Name"    # set identity for all repos'))
body.append(code('git init                                 # initialize a repository'))
body.append(code('git add .          # stage all  |  git add file   # stage one file'))
body.append(code('git commit -m "message"                  # create a commit'))
body.append(code('git status   |   git log   |   git show <hash>'))
body.append(code('git remote add origin <url>   &&   git push -u origin master'))

body.append(tip("The package-manager mantra: it installs an OLDER but MORE RELIABLE version of Git. Memorize that trade-off."))
body.append(tip("'Why git add again?' — like packing a parcel: git add = put item in the box, git commit = seal & label it, git push = send it. You re-add because you choose WHICH changed files to commit."))
body.append(trap("git add does NOT create a commit — it only stages. Changes are not saved to history until git commit runs."))
body.append(trap("The -u flag in 'git push -u origin master' LINKS your branch to the remote for future reference; it does not 'upload urgently'."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 3 – BRANCHING IN GIT
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 3: Branching in Git"))
body.append(section("Key Definitions"))

body.append(term("Branch",
    "An independent path of development — effectively a new copy of the project you can experiment on "
    "without affecting the original (master) branch. A branch is a named sequence of commits."))

body.append(term("master Branch",
    "The default branch you start in. The name 'master' implies no superiority — it is just a convention "
    "for the main line of development."))

body.append(term("HEAD",
    "A pointer to the latest commit of the current active branch — i.e. the tip of the branch. "
    "HEAD and the tip of the active branch point to the same commit."))

body.append(term("Cloning",
    "The process of creating a local copy of a repository from a different source. After cloning you can "
    "also see remote branches with git branch -a."))

body.append(term("Checkout",
    "Switches the active branch. git checkout <name> moves to an existing branch; "
    "git checkout -b <name> creates and switches in one step."))

body.append(term("Merge",
    "Combines the changes of one branch into another. You must first checkout the destination branch, "
    "then run git merge <source>."))

body.append(term("Fast-Forward Merge",
    "When the target branch has no new commits of its own, Git simply moves the branch pointer forward. "
    "Only the pathway changes and HEAD is updated — no merge commit is created (this is the default)."))

body.append(term("No-Fast-Forward Merge (--no-ff)",
    "Forces Git to create a new merge commit on the base branch even when fast-forward is possible. "
    "Generally recommended for merges into master to logically record the feature."))

body.append(term("Merge Conflict",
    "Happens when the same file is modified in non-common commits in both branches. Git raises a conflict "
    "so you do not lose data and asks you to resolve it manually."))

body.append(section("Branch Commands"))
body.append(code('git branch              # list  |  git branch -a   # include remotes'))
body.append(code('git branch test         # create   |   git checkout test   # switch'))
body.append(code('git checkout -b feature  # create + switch in one command'))
body.append(code('git branch -m newname    # rename current branch'))
body.append(code('git branch -d name   # safe delete   |   git branch -D name   # force delete'))
body.append(code('git checkout master  &&  git merge feature'))

body.append(tip("-d (safe) only deletes a branch already merged/synced; -D (capital) FORCE-deletes even unmerged commits with no warning."))
body.append(tip("Use --no-ff when merging into master so the history clearly shows where a feature was integrated."))
body.append(trap("A fast-forward merge does NOT create a merge commit — it just moves the pointer. Only --no-ff creates a dedicated merge commit."))
body.append(trap("git branch <name> creates a branch but does NOT switch to it — you remain on the current branch until you checkout."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 5 – GIT WORKFLOWS
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 5: Git Workflows"))
body.append(section("Key Definitions"))

body.append(term("Git Workflow",
    "A set of guidelines a team follows to manage a project — covering the architecture, how "
    "contributions are made, and how others' work is merged in."))

body.append(term("Centralized Workflow",
    "The simplest workflow: a single branch (usually master) is used for all operations, treated as the "
    "main copy. Also called the 'trunk' workflow (SVN's master is called trunk). No branching is used."))

body.append(term("Feature-Branch Workflow",
    "Each new feature is developed in its own separate branch, then merged or rebased into master after a "
    "code review. A developer must never directly commit to the local master branch."))

body.append(term("Gitflow Workflow",
    "An extension of the feature-branch workflow with defined branch roles. Two core branches: develop "
    "(latest development) and master (last stable release), plus feature, release, and hotfix branches."))

body.append(term("Hotfix Branch",
    "In Gitflow, a branch created from master to fix a critical bug immediately. Once fixed it is merged "
    "back into BOTH master and develop."))

body.append(term("Forking Workflow",
    "A cloud implementation of the feature-branch workflow. Each developer has a personal server-side copy "
    "(a fork); changes are pushed to the fork and merged via a pull request after review."))

body.append(term("Fork",
    "A developer's personal copy of the central repository in the cloud. origin points to the fork; "
    "upstream points to the central (main) repository."))

body.append(section("Choosing a Workflow"))
body.append("""<table class="ref-table">
<tr><th>Workflow</th><th>Best For</th><th>Branching?</th></tr>
<tr><td>Centralized</td><td>Beginners, solo / personal projects, SVN converts</td><td>No</td></tr>
<tr><td>Feature-branch</td><td>Growing teams, open source (enables code review)</td><td>Yes</td></tr>
<tr><td>Gitflow</td><td>Mature projects, mixed-skill teams, multiple released versions</td><td>Yes (roles)</td></tr>
<tr><td>Forking</td><td>Any cloud-hosted / open-source project</td><td>Yes (+ fork)</td></tr>
</table>""")

body.append(tip("Open-source projects must use at least a feature-branch workflow so code reviews happen before contributor merges."))
body.append(tip("In Gitflow, developers treat the develop branch as a 'pseudo master' and are essentially never directly involved with the real master."))
body.append(trap("The centralized workflow does NOT use branching — giving everyone master access means one bad commit can corrupt the whole repository."))
body.append(trap("In Gitflow a hotfix merges into BOTH master AND develop — forgetting develop means the bug reappears in the next release."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 6 – CORRECTING ERRORS WHILE WORKING WITH GIT
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 6: Correcting Errors While Working with Git"))
body.append(section("Key Definitions"))

body.append(term("Undo git add (untrack)",
    "git rm --cached <file> untracks a file but leaves it on disk. Use it to undo accidentally tracking "
    "a new file before it is committed."))

body.append(term("git reset --soft",
    "Undoes a commit but KEEPS its changes staged for review. HEAD~1 means go back one commit from the "
    "current HEAD."))

body.append(term("git reset --mixed (default)",
    "Undoes the commit AND unstages the changes (files keep their edits but are not staged). "
    "This is the default reset mode."))

body.append(term("git reset --hard",
    "Undoes the commit and discards all changes — takes you to a state even before the files were edited. "
    "Avoid it unless you are absolutely sure; it permanently destroys work."))

body.append(term("reset vs revert",
    "reset rewrites history by moving HEAD backward. revert creates a NEW commit that reverses the changes "
    "of a faulty commit — history is preserved. revert is safe for shared/pushed commits."))

body.append(term("git commit --amend",
    "Changes the message (or content) of the LAST commit. Note the commit hash changes too, effectively "
    "rewriting history."))

body.append(term("Undo a Push (force push)",
    "To remove a pushed commit you reset locally then force the update with git push -f. A normal push is "
    "rejected because the remote HEAD is ahead of your local branch."))

body.append(term("git blame",
    "Shows, for each line of a file, the commit hash, author, and date that last changed it. "
    "Used when you KNOW which file contains the bug."))

body.append(term("git bisect",
    "Performs a binary search through commits to find the one that introduced a bug. You mark a known "
    "'good' commit and a 'bad' commit; Git narrows down in logarithmic steps. Used when you DON'T know the source."))

body.append(section("Reset Modes — Quick Reference"))
body.append("""<table class="ref-table">
<tr><th>Option</th><th>Commit</th><th>Changes Staged?</th><th>Changes Kept?</th></tr>
<tr><td>--soft</td><td>Undone</td><td>Yes (staged)</td><td>Yes</td></tr>
<tr><td>--mixed (default)</td><td>Undone</td><td>No (unstaged)</td><td>Yes</td></tr>
<tr><td>--hard</td><td>Undone</td><td>No</td><td>No (discarded)</td></tr>
</table>""")
body.append(code('git rm --cached file   |   git reset --soft HEAD~1   |   git revert <hash>'))
body.append(code('git commit --amend -m "new message"   |   git push -f origin master'))
body.append(code('git blame file   |   git bisect start <bad> <good>   |   git bisect reset'))

body.append(tip("git bisect can find a bad commit among thousands in just a few steps because it uses BINARY SEARCH (logarithmic). You can automate it: git bisect run <test command>."))
body.append(tip("Use revert (not reset) to undo a commit that has already been PUSHED — it adds a new reversing commit instead of rewriting shared history."))
body.append(trap("--hard PERMANENTLY discards your changes. The book explicitly warns to avoid it unless you are absolutely certain."))
body.append(trap("reset CHANGES history; revert PRESERVES it. Do not use reset on commits others have already pulled."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 7 – UNLOCKING GIT'S FULL POTENTIAL
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 7: Unlocking Git&rsquo;s Full Potential"))
body.append(section("Key Definitions"))

body.append(term("git log --oneline",
    "Compresses each commit to a single line (short hash + message), fitting many more commits on screen. "
    "Combine with --all, --decorate, and --graph to visualize all branches."))

body.append(term("git shortlog",
    "Groups commits by author, showing each contributor and their commit messages. Postfix -n to sort "
    "by number of commits instead of by name."))

body.append(term("Filtering log",
    "git log -n 2 shows the last 2 commits; --after/--before (or --since/--until) filter by date; "
    "--author='Name' filters by author; --grep searches commit messages."))

body.append(term("Tag",
    "A label attached to a specific milestone commit, typically a version number. Two types: lightweight "
    "(name + commit only) and annotated (name + tagger info + message)."))

body.append(term("Annotated vs Lightweight Tag",
    "Annotated tags store the tagger, date, and a message — preferred in organizations. Lightweight tags "
    "are just a name pointing to a commit — handy for personal projects."))

body.append(term("Ref &amp; reflog",
    "A ref (reference) is a pointer to a commit (HEAD, ORIG_HEAD, MERGE_HEAD are refs). The reflog is a "
    "'log of refs' recording every action locally — it can recover lost commits. It is NOT synced to the server."))

body.append(term("git fsck",
    "File system check — finds commits that are not part of any branch (lost commits), which git log "
    "cannot show. Recover one with git merge <hash>."))

body.append(term("Rebase",
    "Rewrites a branch's history by moving it onto a new base commit, producing a LINEAR history without "
    "the loops a merge creates. Preferred for keeping a clean central history."))

body.append(term("Squash",
    "Combining multiple commits into one, done via interactive rebase (git rebase -i HEAD~2). There is no "
    "stand-alone 'git squash' command."))

body.append(term("Stash",
    "Saves uncommitted changes and reverts the working directory to the last commit, so you can switch "
    "context. Reapply later with git stash apply (optionally stash@{n})."))

body.append(term("git add -p",
    "Stages only PART of a file's changes by splitting them into 'hunks'. Options include y (stage), "
    "n (skip), s (split), e (edit). Lets one file's edits go into separate commits."))

body.append(term("Cherry-Pick",
    "Picks a single commit from another branch and applies it to your current branch — when a full merge "
    "or rebase would be too much. git cherry-pick <hash>."))

body.append(section("Power Commands"))
body.append(code('git log --oneline --graph --all --decorate'))
body.append(code('git log --author="Name"   |   git log --grep="test"   |   git log -n 2'))
body.append(code('git tag -a v1.0 -m "msg"   |   git push origin --tags'))
body.append(code('git rebase master   |   git rebase -i HEAD~2   |   git pull --rebase origin master'))
body.append(code('git stash   |   git stash apply stash@{1}   |   git cherry-pick <hash>   |   git reflog'))

body.append(tip("rebase = LINEAR history (no loops); merge = preserves the true branch topology with a merge commit. Prefer rebase to keep a central repo tidy."))
body.append(tip("reflog and fsck are your recovery tools: a 'lost' commit from a hard reset or deleted branch is usually still recoverable."))
body.append(trap("There is NO 'git squash' command — squashing is done through interactive rebase (git rebase -i)."))
body.append(trap("Tags are NOT pushed automatically with git push — you must run git push origin --tags (or push a specific tag)."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 8 – INTEGRATE GIT IN YOUR DEVELOPMENT CYCLE
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 8: Integrate Git in Your Development Cycle"))
body.append(section("Key Definitions"))

body.append(term("DevOps",
    "A cross between Development, Operations, and QA that automates the software development cycle to lower "
    "time to market. Arose to remove the friction between separate dev/test/deploy/maintenance teams."))

body.append(term("Continuous Integration (CI)",
    "The second step of the DevOps cycle: testing all code on every push and merging into the main codebase "
    "if all tests pass. Ensures new changes do not break existing functionality."))

body.append(term("Git Hook",
    "A custom script that executes automatically when a predefined Git event occurs. Lets you trigger "
    "actions at key points in the development life cycle. Stored in the .git/hooks directory."))

body.append(term("Client-side vs Server-side Hooks",
    "Client-side hooks react to local actions (pre-commit, commit-msg, post-commit). Server-side hooks "
    "react to network actions like a push (pre-receive, update, post-receive)."))

body.append(term("pre-commit Hook",
    "The most important hook — runs before a commit message is entered, commonly used to run unit tests "
    "so broken code is never committed."))

body.append(term("Travis CI",
    "A popular hosted CI tool for GitHub repositories (free for open source). On every push it clones the "
    "repo to a cloud VM, installs requirements, and runs predefined unit tests."))

body.append(term(".travis.yml",
    "The configuration file (in the repo root) that tells Travis CI the language, versions, install "
    "commands, and test commands. Each version listed creates a separate build."))

body.append(section("Common Git Hooks"))
body.append("""<table class="ref-table">
<tr><th>Hook</th><th>Triggered</th><th>Side</th></tr>
<tr><td>pre-commit</td><td>Before the commit message is entered</td><td>Client</td></tr>
<tr><td>commit-msg</td><td>With the commit message</td><td>Client</td></tr>
<tr><td>post-commit</td><td>After a commit completes</td><td>Client</td></tr>
<tr><td>pre-push</td><td>Before changes are sent to a remote</td><td>Client</td></tr>
<tr><td>pre-receive / post-receive</td><td>Before / after a push from a client</td><td>Server</td></tr>
</table>""")

body.append(tip("Hooks live in .git/hooks as .sample files. To activate one, remove the .sample extension and make sure the file is executable."))
body.append(tip("Travis CI only tests repositories hosted on GitHub; for other hosts you work around it with submodules."))
body.append(trap("Git hook sample files are Bash scripts (#!/bin/sh), but you CAN change the first line to use another language — they are not limited to Bash."))
body.append(trap("Continuous integration is the SECOND step of DevOps, not the first. Continuous development comes first."))

# ════════════════════════════════════════════════════════════════
# CHAPTER 9 – GIT GUI TOOLS
# ════════════════════════════════════════════════════════════════
body.append(chapter("Chapter 9: Git GUI Tools"))
body.append(section("Key Definitions"))

body.append(term("GUI Tool",
    "A graphical client used instead of the terminal. Easier for beginners, but tools differ in UI and "
    "terminology, lack some terminal power, and run more slowly than commands."))

body.append(term("GitHub Desktop",
    "GitHub's own unified GUI client (Windows + macOS, since 2015). Simplifies the workflow by hiding the "
    "term 'staging' — you just select files and commit. Focused on bridging local repos with the GitHub website."))

body.append(term("Sourcetree",
    "Atlassian's GUI client (Windows + macOS). Works with both Git and Mercurial, offers more features and "
    "control, and its options closely match the terminal commands."))

body.append(term("Submodule",
    "A Git repository nested within a parent repository. Listed in the left menu of Sourcetree alongside "
    "branches, tags, remotes, and stashes."))

body.append(term("Editor Integrations",
    "Git can also be used through text editors: Atom (built-in Git/GitHub), Sublime Text (Git package), "
    "and Visual Studio's version control tools."))

body.append(section("GUI Tool Comparison"))
body.append("""<table class="ref-table">
<tr><th></th><th>GitHub Desktop</th><th>Sourcetree</th></tr>
<tr><td>Developer</td><td>GitHub</td><td>Atlassian</td></tr>
<tr><td>Platforms</td><td>Windows, macOS</td><td>Windows, macOS</td></tr>
<tr><td>VCS support</td><td>Git</td><td>Git + Mercurial</td></tr>
<tr><td>Audience</td><td>Beginners (simplified terms)</td><td>Power users (matches terminal)</td></tr>
</table>""")

body.append(tip("Neither GitHub Desktop nor Sourcetree supports Linux. Cross-platform GUIs include SmartGit, Fork, and GitKraken (Windows/macOS/Linux)."))
body.append(tip("On a remote server (often a headless VM) only command-line Git works — which is why knowing terminal commands matters even if you use a GUI."))
body.append(trap("GitHub Desktop deliberately hides the word 'staging' to simplify things — do not assume the underlying staging step disappeared."))
body.append(trap("GUI tools are NOT cross-platform and run slower than the terminal; no single GUI behaves identically across Windows, macOS, and Linux."))

# ════════════════════════════════════════════════════════════════
# PRACTICE QUESTIONS
# ════════════════════════════════════════════════════════════════
body.append('<h2 style="border-color:#378610;color:#1F6B00;">Practice Questions &mdash; Top 15 MCQ</h2>')
body.append('<p class="intro-note">Choose the single best answer. Options are deliberately close — read carefully. Answer key follows on the next page.</p>')

body.append(mcq(1,
    "A developer needs to keep working offline for a week, committing changes without any server connection, then sync later. Which property of Git makes this possible?",
    ["It is a centralized version control system",
     "It is a distributed VCS where each clone holds the full history",
     "It uses a first-come, first-served locking model",
     "It stores all commits only on the origin remote"]))

body.append(mcq(2,
    "You created a new file but have NOT committed it, and you realize Git should not be tracking it yet. Which command removes it from tracking while keeping the file on disk?",
    ["git rm mistake_file",
     "git reset --hard",
     "git rm --cached mistake_file",
     "git checkout -- mistake_file"]))

body.append(mcq(3,
    "Which statement about a fast-forward merge is correct?",
    ["It always creates a new merge commit",
     "It only moves the branch pointer forward and updates HEAD, with no merge commit",
     "It is triggered by the --no-ff flag",
     "It is the only way to merge when both branches have new commits"]))

body.append(mcq(4,
    "A commit has already been pushed to a shared remote and others have pulled it. You must undo its effect safely. What is the recommended approach?",
    ["git reset --hard then git push -f",
     "git commit --amend",
     "git revert <hash> to add a new reversing commit",
     "git rm --cached on the affected files"]))

body.append(mcq(5,
    "Which reset mode undoes a commit but leaves the changes STAGED, ready to be re-committed?",
    ["git reset --hard HEAD~1",
     "git reset --mixed HEAD~1",
     "git reset --soft HEAD~1",
     "git revert HEAD~1"]))

body.append(mcq(6,
    "You have no idea which of the last 500 commits introduced a bug, but you know a commit from last month was fine. Which tool finds the culprit most efficiently?",
    ["git blame, because it shows line authorship",
     "git bisect, because it does a binary search through commits",
     "git log --oneline, scanning each commit by hand",
     "git reflog, because it lists every local action"]))

body.append(mcq(7,
    "In the Gitflow workflow, where is a hotfix branch created from, and where must it be merged back?",
    ["Created from develop; merged into master only",
     "Created from master; merged into BOTH master and develop",
     "Created from a feature branch; merged into develop only",
     "Created from a release branch; merged into master only"]))

body.append(mcq(8,
    "What is the practical difference between an annotated tag and a lightweight tag?",
    ["Lightweight tags store the tagger name, date, and message",
     "Annotated tags can only be created on the master branch",
     "Annotated tags store tagger info and a message; lightweight tags are just a name pointing to a commit",
     "There is no difference; the names are interchangeable"]))

body.append(mcq(9,
    "You ran git push but it was REJECTED because the remote HEAD is ahead of your local branch after a reset. What must you do to overwrite the remote (assuming you are sure)?",
    ["Run git pull --rebase first, always",
     "Force the push with git push -f",
     "Run git commit --amend and push again",
     "Delete the remote and re-add it"]))

body.append(mcq(10,
    "Which statement about git stash is TRUE?",
    ["Stashed changes are automatically pushed to the remote",
     "A stash saves uncommitted changes and reverts the working directory to the last commit",
     "git stash permanently deletes your uncommitted changes",
     "Stashes are stored on origin and shared with the team"]))

body.append(mcq(11,
    "A teammate wants only ONE specific commit from another branch — not the whole branch. Which command applies just that commit to the current branch?",
    ["git merge <branch>",
     "git rebase <branch>",
     "git cherry-pick <hash>",
     "git checkout <hash>"]))

body.append(mcq(12,
    "Which choice correctly distinguishes Git from GitHub?",
    ["Git is a website; GitHub is a command-line tool",
     "Git is a distributed VCS; GitHub is a cloud service that hosts Git repositories",
     "They are two names for the same product",
     "Git only works online; GitHub works offline"]))

body.append(mcq(13,
    "You want to combine your last three messy commits into a single clean commit before opening a pull request. What do you use?",
    ["The stand-alone git squash command",
     "git merge --squash on master",
     "Interactive rebase: git rebase -i HEAD~3",
     "git reset --soft only"]))

body.append(mcq(14,
    "Which Git hook is most commonly used to run unit tests so that broken code is never recorded, and on which side does it run?",
    ["post-receive, server-side",
     "pre-commit, client-side",
     "pre-receive, server-side",
     "commit-msg, client-side"]))

body.append(mcq(15,
    "Why does the book recommend learning terminal Git even if you prefer a GUI like GitHub Desktop or Sourcetree?",
    ["GUI tools support every operating system identically",
     "GUI tools are always faster than the terminal",
     "On a headless remote server only command-line Git works, and GUIs aren't cross-platform",
     "Terminal commands cannot cause data loss, unlike GUIs"]))

# ════════════════════════════════════════════════════════════════
# ANSWER KEY
# ════════════════════════════════════════════════════════════════
body.append('<h2 style="border-color:#378610;color:#1F6B00;">Answer Key</h2>')
body.append('<p class="intro-note">Correct answers with a one-line justification.</p>')

answers = [
    ("1", "B", "Every clone in a distributed VCS holds the full history, so you can commit offline and sync later."),
    ("2", "C", "git rm --cached untracks the file but leaves it in the file system; plain git rm would also delete it."),
    ("3", "B", "Fast-forward simply advances the pointer/HEAD with no merge commit; --no-ff is what forces a merge commit."),
    ("4", "C", "revert adds a new reversing commit and preserves shared history; reset --hard/-f rewrites history others already have."),
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
rows = "".join(
    f'<tr><td><strong>Q{q}</strong></td><td class="ans-letter">{a}</td><td>{why}</td></tr>'
    for q, a, why in answers
)
body.append(f"""<table class="ans-table">
<tr><th>#</th><th>Answer</th><th>Justification</th></tr>
{rows}
</table>""")

# ── BUILD HTML ──────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>{CSS}</style>
</head>
<body>
{''.join(body)}
</body>
</html>"""

with open("git_summary.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved: git_summary.html")

from weasyprint import HTML as WHTML
WHTML(string=html).write_pdf("git_summary.pdf")
print("Saved: git_summary.pdf")
