# Justfile for interview-questions repo

# Push changes to remote (requires gh auth)
push MESSAGE:
    @gh auth status || (echo "❌ Not authenticated. Run: gh auth login" && exit 1)
    git add .
    git commit -m "{{MESSAGE}}\n\nCo-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
    git push

# Quick push with default message
qpush:
    @gh auth status || (echo "❌ Not authenticated. Run: gh auth login" && exit 1)
    git add .
    git commit -m "Update interview questions\n\nCo-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
    git push

# Show git status
status:
    git status

# Show recent commits
log:
    git log --oneline -10

# Show diff of unstaged changes
diff:
    git diff

# Show diff of staged changes
diffstaged:
    git diff --cached

# GitHub CLI commands

# View repo in browser
browse:
    gh browse

# View repo info
repo:
    gh repo view

# List recent issues
issues:
    gh issue list --limit 10

# List recent pull requests
prs:
    gh pr list --limit 10

# Create a new issue
issue TITLE:
    gh issue create --title "{{TITLE}}"

# Check GitHub authentication status
auth:
    gh auth status
