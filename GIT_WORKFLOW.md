# Git Workflow & Team Collaboration Guide

**Last Updated:** January 27, 2026  
**Purpose:** Guide team collaboration on the Liaison Program project using Git and GitHub

---

## Overview

This project uses Git for version control and GitHub for hosting. Team members work on features in parallel using branches and pull requests.

---

## 🚀 Getting Started

### Initial Setup (One Time)

```bash
# Clone the repository
git clone https://github.com/[owner]/mc451-liaison-program.git
cd mc451-liaison-program

# Configure Git with your info
git config user.name "Your Name"
git config user.email "your.email@university.edu"

# Verify
git config --list | grep user
```

### Before Each Work Session

```bash
# Make sure you're on the right branch
git branch

# Update your local repo with latest changes from team
git fetch origin
git status
```

---

## 🌳 Branch Strategy

We use a simple branching model:

### Main Branch (`main`)
- **What:** Live, production-ready code
- **Who commits here:** Only reviewed and tested code
- **Rule:** Direct commits forbidden - use pull requests only
- **Deploy:** Automatic (GitHub Pages deploys when changes merge to main)

### Feature Branches
- **What:** Working branches for features or fixes
- **Naming:** `feature/description` or `fix/description`
- **Life:** Created from `main`, merged back when done
- **Examples:**
  - `feature/phase-2-content`
  - `fix/navbar-mobile`
  - `feature/customize-colors`
  - `fix/broken-links`

### Workflow Diagram

```
┌─────────────────────────────────────────────────┐
│ main branch (production, always deployable)     │
│ ✅ Code reviewed, tested, ready for students   │
└────────────────────┬────────────────────────────┘
                     │ Pull request (code review)
                     │ ↓
┌────────────────────┴────────────────────────────┐
│ feature/phase-2-content (your work)             │
│ 🔨 In progress, getting feedback               │
└─────────────────────────────────────────────────┘
```

---

## 💼 Typical Workflow

### 1. Start a New Feature

```bash
# Switch to main and get latest code
git checkout main
git pull origin main

# Create a new branch for your feature
git branch feature/phase-2-content
git checkout feature/phase-2-content

# Or, more concisely:
git checkout -b feature/phase-2-content
```

### 2. Make Your Changes

```bash
# Edit files in VS Code or your editor
# Example: Edit modules/02_discovery/index.qmd
#         Add Phase 2 content

# Check what you changed
git status
git diff modules/02_discovery/index.qmd
```

### 3. Test Your Changes

```bash
# Rebuild the website to test
quarto render

# Open _site/index.html in browser to preview
# Check: Do links work? Does content look right? Mobile OK?

# No errors? Great! Ready to commit.
```

### 4. Commit Your Changes

```bash
# Stage files (tell Git you want to save these changes)
git add modules/02_discovery/index.qmd

# Or stage everything that changed:
git add .

# Check what you staged
git status

# Save changes with a descriptive message
git commit -m "Add Phase 2 Discovery content: research questions and data planning"
```

**Good commit messages:**
- Describe WHAT you changed
- Describe WHY you changed it
- Use present tense: "Add" not "Added"
- Examples:
  - ✅ "Add Phase 2 content with research question activities"
  - ✅ "Fix navbar mobile dropdown issues"
  - ✅ "Update instructor contact info in syllabus"
  - ❌ "Updated stuff"
  - ❌ "Fix things"

### 5. Push to GitHub

```bash
# Send your branch to GitHub
git push origin feature/phase-2-content

# First time pushing a branch? Git will suggest:
# git push --set-upstream origin feature/phase-2-content
# Just copy and paste that command
```

### 6. Create a Pull Request

This is how your code gets reviewed before merging to main.

**Method 1: GitHub website**
1. Go to [github.com/[owner]/mc451-liaison-program](https://github.com)
2. You'll see a banner: "feature/phase-2-content had recent pushes"
3. Click "Compare & pull request"
4. Write a title and description
5. Click "Create pull request"

**Method 2: GitHub CLI (if installed)**
```bash
# From your feature branch
gh pr create --base main --title "Add Phase 2 content" --body "Adds discovery activities and resources"
```

### 7. Review & Feedback

A team member (or Copilot bot) will:
- Review your changes
- Leave comments if changes needed
- Approve when ready

**Making requested changes?**

```bash
# Make edits to fix feedback
# Example: Editor asks to add more details to Phase 2 overview

# Stage and commit your changes (same as step 4)
git add modules/02_discovery/index.qmd
git commit -m "Add more detail to Phase 2 overview based on review feedback"

# Push again (same branch)
git push origin feature/phase-2-content

# The pull request automatically updates! No need to create a new one.
```

### 8. Merge & Deploy

When approval is granted:

1. Click "Merge pull request" on GitHub
2. Delete the feature branch (optional, but recommended)
3. GitHub Actions automatically:
   - Rebuilds the site (`quarto render`)
   - Deploys to GitHub Pages
   - Site updates in 1-2 minutes

**Verify deployment:**
```bash
# Switch back to main
git checkout main
git pull origin main

# You now have the new code locally
# Your browser will show the new content in 1-2 minutes
```

---

## 🔄 Common Scenarios

### Scenario 1: You Started Before Someone Else Finished

```bash
# You're on feature/phase-2-content
# Teammate just merged feature/phase-3-content to main
# Now you have a conflict

# Get the latest main branch
git fetch origin

# Update your feature branch with main's changes
git rebase origin/main

# OR, if you prefer merge:
git merge origin/main

# If there are conflicts, resolve them:
# 1. VS Code will show conflicts in editor
# 2. You choose which version to keep
# 3. Stage and commit:
git add .
git commit -m "Resolve merge conflict with main"

# Push again
git push origin feature/phase-2-content
```

### Scenario 2: You Made a Mistake and Want to Undo

**Option 1: Undo last commit (not pushed)**
```bash
git reset --soft HEAD~1
# Changes are undone but files stay modified
# You can edit them again and re-commit
```

**Option 2: Undo a file back to last commit**
```bash
git checkout modules/02_discovery/index.qmd
# That file reverts to last committed version
# Unsaved changes are lost!
```

**Option 3: View changes before committing**
```bash
git diff modules/02_discovery/index.qmd
# Shows what changed (red - removed, green - added)
# Press q to exit
```

### Scenario 3: You Forgot to Save Before Committing

```bash
# You ran `git commit` but didn't stage changes first
# Use:
git add .
git commit -m "Stage forgotten changes"
```

### Scenario 4: Your Branch is Behind Main by 10 Commits

```bash
# Your feature branch is old, main has lots of new changes
# Update your branch:
git fetch origin
git rebase origin/main
# Now your branch has main's latest changes

# Push (with force flag, since history changed):
git push origin feature/phase-2-content --force-with-lease
# --force-with-lease is safer than --force
```

### Scenario 5: You Want to Delete Your Branch

```bash
# Local deletion
git branch -d feature/phase-2-content

# Remote deletion
git push origin --delete feature/phase-2-content
```

---

## 👥 Team Coordination

### Daily Standup Example

```
Developer 1 (Content):
"Yesterday: Finished Phase 2 content
Today: Working on Phase 3 activities
Blocker: Need example research datasets"

Developer 2 (Frontend):
"Yesterday: Fixed mobile navbar
Today: Updating colors and branding
Blocker: None"

Developer 3 (DevOps):
"Yesterday: Set up GitHub Actions
Today: Testing deployment
Blocker: Need write access to settings"
```

### Before Starting Major Work

```bash
# What are others working on?
git branch -r
# Shows: origin/feature/phase-2, origin/feature/fix-links, etc.

# Who has uncommitted changes?
git status

# What's the latest on main?
git log origin/main --oneline -5
```

---

## 🔐 Protecting Main Branch

To prevent accidents, main branch should have protections:

**GitHub Settings → Branches → Add Rule (for main)**
- ✅ Require pull request reviews before merging
- ✅ Dismiss stale pull request approvals
- ✅ Require status checks to pass before merging
- ✅ Require branches to be up to date before merging

This ensures:
- Code is reviewed before going live
- Tests pass before deployment
- No accidental deletions

---

## 📊 Viewing History

### See recent commits

```bash
# Last 5 commits on current branch
git log --oneline -5

# Last 5 commits on main
git log origin/main --oneline -5

# Commits by a person
git log --author="Jane Doe" --oneline

# Commits on a date
git log --since="2 weeks ago" --oneline
```

### See who changed what

```bash
# Show line-by-line who changed what
git blame modules/02_discovery/index.qmd
```

### Compare two branches

```bash
# What's different between your branch and main?
git diff main feature/phase-2-content

# How many commits ahead are you?
git log main..feature/phase-2-content --oneline
```

---

## 🚨 Emergency Recovery

### Oops, I Deleted Something!

```bash
# Git reflog shows everything you've done (30 days history)
git reflog

# Find the commit before deletion
# Reset to that point:
git reset --hard abc123
```

### Oops, I Committed Sensitive Data!

```bash
# Remove file from all history (BEFORE pushing to GitHub)
git rm --cached sensitive-file.txt
git commit -m "Remove sensitive file"

# If already pushed, contact team immediately
# Sensitive data must be rotated (new passwords, API keys)
```

### Oops, I Pushed the Wrong Branch!

```bash
# If branch is not merged yet:
git push origin --delete wrong-branch

# If it's merged:
# Create a "revert" commit that undoes the merge
git revert -m 1 abc123
git push origin main
```

---

## 🛠️ Useful Git Aliases

Make Git commands shorter:

```bash
# Add to ~/.gitconfig
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    unstage = reset HEAD
    last = log -1 HEAD
    visual = log --oneline --all --graph
```

Then you can use:
```bash
git st          # Instead of git status
git co -b name  # Instead of git checkout -b name
git visual      # See full branch diagram
```

---

## 📚 Resources

### Git Documentation
- [GitHub's Git Guides](https://github.com/git-guides)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [Pro Git Book](https://git-scm.com/book) (free, online)

### GitHub Specific
- [GitHub Docs](https://docs.github.com/)
- [GitHub Guides](https://guides.github.com/)
- [GitHub Skills](https://skills.github.com/) - Interactive tutorials

### Troubleshooting
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Recovery commands
- [Git Tips](https://git-tips.github.io/)

---

## ✅ Checklist for New Team Members

- [ ] Git is installed (`git --version`)
- [ ] Git is configured with your name and email
- [ ] You have access to GitHub repository
- [ ] You can clone the repo locally
- [ ] You can create a feature branch
- [ ] You can run `quarto render` successfully
- [ ] You can make a commit and push a branch
- [ ] You can create a pull request on GitHub
- [ ] You've read this guide and understood the workflow

---

## 💡 Best Practices

### Do ✅
- Write descriptive commit messages
- Create a new branch for each feature
- Test locally before pushing
- Review code before merging
- Pull latest main before starting new work
- Delete merged branches to keep repo clean

### Don't ❌
- Commit directly to main
- Write vague messages ("Update stuff")
- Push large, untested changes
- Ignore merge conflicts
- Work on main while others work on features
- Keep dead branches around

---

## 🎓 Learning Path

1. **Beginner:** Complete scenarios 1-5 in "Typical Workflow"
2. **Intermediate:** Learn branches, merges, rebasing
3. **Advanced:** Squashing commits, cherry-picking, bisecting

Start with the basics and grow your Git skills over time!

---

*Last updated: January 27, 2026*
