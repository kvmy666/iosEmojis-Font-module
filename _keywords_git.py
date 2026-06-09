"""
Git-domain keyword sets, shared by create_git_summary.py and create_git_docx.py.
Two tiers, same scheme as the security summaries:
  RED    = critical / destructive / imperative words
  ORANGE = core Git actions and objects
A token in a definition is colored if its lowercased, punctuation-stripped form
is in one of these sets.
"""

KEYWORDS_RED = {
    # imperative / absolute
    "always", "never", "must", "cannot", "only", "not", "no",
    "don't", "do", "avoid", "important", "critical", "note", "warning",
    # destructive / loss
    "delete", "deletes", "deleted", "deleting",
    "overwrite", "overwrites", "overwriting", "overwritten",
    "force", "forces", "forced", "forcing",
    "discard", "discards", "discarded", "discarding",
    "lose", "loses", "losing", "lost",
    "remove", "removes", "removed", "removing",
    "corrupt", "corrupts", "corrupted", "corruption",
    "conflict", "conflicts", "conflicting",
    "detached", "dangerous", "careful", "permanently", "permanent",
    "untracked", "orphaned", "rewrite", "rewrites", "rewriting", "rewritten",
    "abandon", "abort", "aborts", "rejected", "fatal", "error", "errors", "bug", "bugs",
    "reset", "revert", "reverts", "reverting", "rebase", "amend",
    "hard", "faulty", "mistake", "mistakes",
}

KEYWORDS_ORANGE = {
    # snapshots / commits
    "commit", "commits", "committed", "committing",
    "snapshot", "snapshots", "checkpoint", "checkpoints",
    "hash", "history", "log",
    # branches
    "branch", "branches", "branching",
    "merge", "merges", "merged", "merging",
    "checkout", "fast-forward", "no-fast-forward",
    # remotes / sync
    "push", "pushes", "pushed", "pushing",
    "pull", "pulls", "pulled", "pulling",
    "fetch", "fetches", "fetched", "fetching",
    "clone", "clones", "cloned", "cloning",
    "remote", "remotes", "origin", "upstream",
    "repository", "repositories", "repo", "fork", "forked",
    "synchronize", "synchronized", "sync", "synced",
    # staging / tracking
    "stage", "staged", "staging", "staging area", "index",
    "track", "tracks", "tracked", "tracking",
    "initialize", "initialized", "initialization", "init",
    # objects / refs
    "head", "ref", "refs", "reflog", "tag", "tags", "tagging",
    "stash", "stashes", "stashed", "stashing",
    "cherry-pick", "rebasing", "squash", "squashing",
    "distributed", "centralized", "working", "directory",
    # collaboration / devops
    "pull request", "hook", "hooks", "workflow", "workflows",
    "blame", "bisect", "fsck", "shortlog",
}
