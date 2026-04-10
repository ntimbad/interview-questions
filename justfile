# Justfile for interview-questions repo

# Push changes to remote
push MESSAGE:
    git add .
    git commit -m "{{MESSAGE}}\n\nCo-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
    git push

# Quick push with default message
qpush:
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
