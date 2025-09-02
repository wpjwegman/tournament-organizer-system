# GitHub Workflow - Workspace Cleanliness Instructions

## Overview

These instructions ensure workspace cleanliness and proper GitHub workflow practices for the Tournament Organizer project.

## Workspace Cleanliness Rules

### 1. Branch Management

- **Never work directly on `master`** - Always create feature branches
- **Delete merged branches** after successful PR completion
- **Keep branches focused** - One feature/issue per branch
- **Use descriptive branch names** following the convention: `feature/issue-number-brief-description`

### 2. Commit Practices

- **Write clear commit messages** using conventional commit format
- **Commit frequently** with logical, atomic changes
- **No commits with broken code** - ensure all tests pass
- **Sign commits** when required by project policy

### 3. File Organization

- **No temporary files** in the repository (use .gitignore)
- **No personal configuration** files (IDE settings, etc.)
- **No compiled artifacts** unless specifically required
- **No large binary files** without Git LFS

### 4. Before Creating Pull Requests

#### Pre-PR Checklist

1. **Sync with master**:

   ```bash
   git checkout master
   git pull origin master
   git checkout your-feature-branch
   git rebase master
   ```

2. **Run all tests and linters**:

   ```bash
   # For documentation
   cd documents
   uvx pre-commit run --all-files

   # For backend (when implemented)
   cd backend
   # Run backend tests

   # For frontend (when implemented)  
   cd frontend
   # Run frontend tests
   ```

3. **Clean workspace**:

   ```bash
   git status  # Should show clean working tree
   git log --oneline master..HEAD  # Review your commits
   ```

### 5. Professional Local Workflow: Containerized Validation

To ensure your local results match CI (GitHub Actions uses Ubuntu), run all hooks and tools inside a Linux container with your code mounted:

```powershell
# Build the container (if not already built)
podman build -f documents/Containerfile -t docs-quality:latest documents

# Run the container interactively, mounting your project
podman run --rm -it -v ${PWD}:/workspace -w /workspace/documents docs-quality:latest pwsh

# Inside the container:
. .venv/Scripts/Activate.ps1  # Activate Python environment if needed
uv run pre-commit run --all-files
uv run python scripts/validation/check_nav_orphans.py
uv run python scripts/linting/domain_linter.py --check-only
uv run python scripts/linting/repository_linter.py --all-domains --report
markdownlint-cli2 "docs/**/*.md"
```

**Workflow:**
- Run all validation inside the container.
- Fix issues locally, re-run validation in the container.
- Commit only when all checks pass.

### 6. Pull Request Standards

- **Link to GitHub issue** in PR description
- **Clear PR title** describing the change
- **Comprehensive description** of what was changed and why
- **Request appropriate reviewers**
- **Ensure CI/CD passes** before requesting review

### 6. Post-Merge Cleanup

After successful PR merge:

1. **Switch to master**:

   ```bash
   git checkout master
   git pull origin master
   ```

2. **Delete feature branch**:

   ```bash
   git branch -d feature-branch-name
   git push origin --delete feature-branch-name
   ```

3. **Verify clean state**:

   ```bash
   git status
   git branch -a
   ```

## Code Review Guidelines

### For Reviewers

- **Check against project standards**
- **Verify tests are included** for new functionality
- **Ensure documentation is updated** when needed
- **Test locally** if changes are complex
- **Provide constructive feedback**

### For Authors

- **Respond to all review comments**
- **Make requested changes promptly**
- **Re-request review** after making changes
- **Don't force-push** after review has started (use new commits)

## Pull Request Review Process

### Handling PR Comments and Reviews

After creating a PR, follow this process to address review feedback:

#### 1. Check for Review Comments

```bash

# View PR with comments

gh pr view [PR_NUMBER] --comments

# Check review status

gh pr status
```markdown

#### 2. Address Review Comments

For each review comment:

- **Read carefully** and understand the requested change
- **Make specific fixes** addressing the exact concern
- **Test changes** locally before committing
- **Commit with descriptive messages** referencing the review

#### 3. Update Pull Request

```bash

# Make changes to address comments

git add [modified files]
git commit -m "fix: address review comment - [specific issue fixed]"

# Push updates (don't force push during review)

git push origin [branch-name]
```markdown

#### 4. Respond to Comments

- **Reply to each comment** explaining how it was addressed
- **Mark conversations as resolved** when changes are complete
- **Request re-review** when all comments are addressed:

```bash

# Request re-review from specific reviewers

gh pr edit [PR_NUMBER] --add-reviewer [username]
```markdown

#### 5. Follow-up Actions

- **Monitor CI/CD checks** after each update
- **Ensure all tests pass** before requesting final review
- **Update PR description** if scope or approach changed significantly

## Emergency Procedures

### Accidental Commit to Master

1. **Don't panic** - we can fix this
2. **Create branch** from the commit:

   ```bash
   git branch emergency-fix HEAD
   git reset --hard HEAD~1
   git push --force-with-lease origin master
   ```

3. **Create proper PR** from the emergency branch

### Large File Accidentally Committed

1. **Remove from history** using git filter-branch or BFG
2. **Update .gitignore** to prevent recurrence
3. **Force push** (coordinate with team first)

## Automation

### Pre-commit Hooks

The project uses pre-commit hooks to enforce standards:

- **Markdown linting** for documentation
- **YAML validation** for configuration files
- **File size limits** to prevent large commits
- **Trailing whitespace removal**

### GitHub Actions

- **Automatic testing** on all PRs
- **Documentation deployment** on master updates
- **Security scanning** for dependencies
- **Code quality checks**

## Project-Specific Notes

### Domain-Driven Development Order

1. **Documents first** - All business domains and models must be documented
2. **Backend implementation** - Following documented domain models
3. **Frontend implementation** - Consuming backend APIs
4. **Integration testing** - End-to-end validation

### Branch Naming Convention

- `docs/issue-123-tournament-domain` - Documentation updates
- `backend/issue-124-user-registration` - Backend features
- `frontend/issue-125-tournament-ui` - Frontend features
- `hotfix/issue-126-critical-bug` - Critical fixes

## Tools and Commands

### Useful Git Commands

```bash

# Clean up local branches

git remote prune origin
git branch --merged | grep -v master | xargs -n 1 git branch -d

# Check what would be pushed

git log origin/master..HEAD --oneline

# Interactive rebase to clean up commits

git rebase -i HEAD~3
```markdown

### Status Checks

```bash

# Overall project status

git status
git branch -a
git remote -v

# Check for uncommitted changes

git diff --name-only
git diff --cached --name-only
```markdown

---

**Remember**: A clean workspace leads to a clean mind and clean code. Follow these practices consistently for a professional development experience.
