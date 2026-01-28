# Documentation Index & Quick Reference

**Last Updated:** January 27, 2026  
**Purpose:** Find the right documentation for your needs

---

## 🚀 New to the Project? Start Here

1. **5-minute overview:** [PROJECT_HANDOFF_SUMMARY.md](PROJECT_HANDOFF_SUMMARY.md)
2. **15-minute deep dive:** [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md)
3. **What to work on:** [ROADMAP.md](ROADMAP.md)
4. **Set up locally:** [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) → "Development Setup"

---

## 📚 Documentation by Role

### 👨‍💻 Software Developer

**Essential Reading:**
- [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) - Technical setup, workflows, common tasks
- [GIT_WORKFLOW.md](GIT_WORKFLOW.md) - How to collaborate with team
- [ARCHITECTURE.md](ARCHITECTURE.md) - Why things are built this way

**Task-Specific Guides:**
- Working on UI/frontend? → [ROADMAP.md](ROADMAP.md) Phase 2 section
- Writing content? → [CONTENT_PLAN.md](CONTENT_PLAN.md)
- Setting up deployment? → [DEPLOYMENT.md](DEPLOYMENT.md)
- Testing code? → [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md)

**Reference Docs:**
- [_quarto.yml](_quarto.yml) - Website configuration
- [build_vault.py](build_vault.py) - Vault generation script (with comments)
- [custom-styling.scss](custom-styling.scss) - Styling and theming

### ✍️ Content Developer/Writer

**Essential Reading:**
- [CONTENT_PLAN.md](CONTENT_PLAN.md) - What content is needed, where, when
- [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) - How to work with QMD files
- [modules/01_orientation/index.qmd](modules/01_orientation/index.qmd) - Example phase structure

**Guidelines:**
- [ROADMAP.md](ROADMAP.md) → "Content Guidelines" section
- [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) → "Customize Module Content"

**Current Work:**
- Phase 2 Discovery: [modules/02_discovery/index.qmd](modules/02_discovery/index.qmd)
- Phase 3 Dictionary: [modules/03_dictionary/index.qmd](modules/03_dictionary/index.qmd)
- Phase 4 Execution: [modules/04_execution/index.qmd](modules/04_execution/index.qmd)
- Phase 5 Delivery: [modules/05_delivery/index.qmd](modules/05_delivery/index.qmd)

### 🎨 UX/Design Developer

**Essential Reading:**
- [ROADMAP.md](ROADMAP.md) → "Phase 2: IMPORTANT" section
- [ARCHITECTURE.md](ARCHITECTURE.md) → "Why Bootstrap?" section
- [custom-styling.scss](custom-styling.scss) - Styling system

**Design Resources:**
- [UX_IMPROVEMENT_PLAN.md](UX_IMPROVEMENT_PLAN.md) - Original design research
- [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) → "Visual & Layout Testing"

**Reference Sites:**
- SIM Lab: https://sim-lab-siue.github.io/
- HCI Lab CMU: https://www.hcilab.cmu.edu/
- Media Lab MIT: https://www.media.mit.edu/

### 🚢 DevOps/Deployment Engineer

**Essential Reading:**
- [DEPLOYMENT.md](DEPLOYMENT.md) - How to deploy the site
- [GIT_WORKFLOW.md](GIT_WORKFLOW.md) - Merging and CI/CD
- [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) → "Pre-Deployment Testing"

**Configuration Files:**
- [_quarto.yml](_quarto.yml) - Quarto site config
- `.github/workflows/` - GitHub Actions configuration (if exists)

**Key Commands:**
```bash
quarto render           # Build the site locally
quarto preview          # Preview locally with live reload
git push origin main    # Deploy (if using GitHub Pages)
```

### 📊 Project Manager / Scrum Master

**Essential Reading:**
- [PROJECT_HANDOFF_SUMMARY.md](PROJECT_HANDOFF_SUMMARY.md) - Executive summary
- [ROADMAP.md](ROADMAP.md) - Priorities, effort, timeline
- [CONTENT_PLAN.md](CONTENT_PLAN.md) - Content completion tracking

**Planning Documents:**
- Sprint planning templates in [ROADMAP.md](ROADMAP.md)
- [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md) - Pre-launch items
- [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) - QA tracking

**For Status Reports:**
- [CONTENT_PLAN.md](CONTENT_PLAN.md) → "Content Status Summary" table
- [ROADMAP.md](ROADMAP.md) → "Phase 1: CRITICAL" section

### 👨‍🏫 Instructor / Course Owner (Non-Technical)

**Essential Reading:**
- [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) - How to personalize your course
- [START_HERE.md](START_HERE.md) - Student onboarding guide

**Quick References:**
- [QUICK_START.md](QUICK_START.md) - Visual guide for students
- [setup.qmd](setup.qmd) - What students read for setup

**For Help:**
- Contact your developer or development team
- Don't need to read technical docs

### 👨‍🎓 Student

**Essential Reading:**
- [START_HERE.md](START_HERE.md) - Complete getting started guide
- [QUICK_START.md](QUICK_START.md) - Visual reference
- Course website (go to instructor's deployed URL)

**What You'll Use:**
- [setup.qmd](setup.qmd) - Installation and configuration guide
- Liaison_Vault.zip - Your digital workspace
- Course modules (accessed through website)

---

## 📖 Documentation by Type

### Technical Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) | How to set up, develop, deploy | Developers |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Why tech choices were made | Developers, Tech Leads |
| [GIT_WORKFLOW.md](GIT_WORKFLOW.md) | How to use Git and collaborate | Developers |

### Project Planning

| Document | Purpose | Audience |
|----------|---------|----------|
| [PROJECT_HANDOFF_SUMMARY.md](PROJECT_HANDOFF_SUMMARY.md) | Executive summary of project status | Everyone |
| [ROADMAP.md](ROADMAP.md) | Priorities and planned work | Developers, Managers |
| [CONTENT_PLAN.md](CONTENT_PLAN.md) | What content is needed | Content writers, Managers |
| [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md) | Pre-launch tasks | Managers, QA |

### Process Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) | How to test the website | QA, Developers |
| [DEPLOYMENT.md](DEPLOYMENT.md) | How to deploy the site | DevOps, Developers |
| [GITHUB_SETUP.md](GITHUB_SETUP.md) | GitHub repository setup | DevOps, Tech Lead |
| [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) | How to personalize the site | Instructors, Developers |

### User Guides

| Document | Purpose | Audience |
|----------|---------|----------|
| [START_HERE.md](START_HERE.md) | Getting started overview | Students |
| [QUICK_START.md](QUICK_START.md) | Visual quick reference | Students |
| [setup.qmd](setup.qmd) | Setup instructions (live on website) | Students |
| [README.md](README.md) | Project overview | Everyone |

### UX & Design

| Document | Purpose | Audience |
|----------|---------|----------|
| [UX_IMPROVEMENT_PLAN.md](UX_IMPROVEMENT_PLAN.md) | Original UX research and recommendations | Designers, Product |

---

## 🔍 Find Information By Topic

### **Getting Set Up**
- New developer setup: [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) → "Development Setup"
- GitHub repo setup: [GITHUB_SETUP.md](GITHUB_SETUP.md)
- Local preview: [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) → "Development Workflow"
- Student setup: [setup.qmd](setup.qmd) or [START_HERE.md](START_HERE.md)

### **How to Contribute**
- Working with Git: [GIT_WORKFLOW.md](GIT_WORKFLOW.md)
- Code review process: [GIT_WORKFLOW.md](GIT_WORKFLOW.md) → "Pull Requests"
- Making changes to content: [CONTENT_PLAN.md](CONTENT_PLAN.md) → "Development Workflow"
- Testing changes: [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md)

### **Project Status**
- What's complete: [PROJECT_HANDOFF_SUMMARY.md](PROJECT_HANDOFF_SUMMARY.md) → "What Has Been Built"
- What needs work: [ROADMAP.md](ROADMAP.md) → "Roadmap Priorities"
- Content completion: [CONTENT_PLAN.md](CONTENT_PLAN.md) → "Content Status Summary"
- Launch readiness: [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md)

### **Technical Details**
- Architecture & design: [ARCHITECTURE.md](ARCHITECTURE.md)
- Technology stack: [ARCHITECTURE.md](ARCHITECTURE.md) → "Technology Stack"
- Why each technology: [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) → "Architecture & Technology Stack"
- Configuration: [_quarto.yml](_quarto.yml) with comments
- Styling: [custom-styling.scss](custom-styling.scss) with comments

### **Content & Curriculum**
- What's needed: [CONTENT_PLAN.md](CONTENT_PLAN.md)
- Learning objectives: [CONTENT_PLAN.md](CONTENT_PLAN.md) → Each phase section
- Activity structure: [CONTENT_PLAN.md](CONTENT_PLAN.md) → "Activity Structure"
- Example content: [modules/01_orientation/index.qmd](modules/01_orientation/index.qmd)

### **Deployment & Operations**
- Where to deploy: [DEPLOYMENT.md](DEPLOYMENT.md) → "Deployment Options"
- How to deploy: [DEPLOYMENT.md](DEPLOYMENT.md) → Each option
- Before deploying: [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) → "Pre-Deployment Testing"
- Troubleshooting: [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) → "Common Tasks"

### **Teaching & Course**
- Customizing for your course: [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md)
- What students see: [START_HERE.md](START_HERE.md)
- Course structure: [CONTENT_PLAN.md](CONTENT_PLAN.md) → "The Five-Phase Model"
- Learning objectives: See each phase module file

### **Improvement & Future**
- UX improvements: [ROADMAP.md](ROADMAP.md) → "Phase 2: IMPORTANT"
- Design improvements: [ROADMAP.md](ROADMAP.md) → "Design Inspiration"
- New features: [ROADMAP.md](ROADMAP.md) → "Phase 3: NICE-TO-HAVE"
- Design spec: [UX_IMPROVEMENT_PLAN.md](UX_IMPROVEMENT_PLAN.md)

### **Troubleshooting**
- Git issues: [GIT_WORKFLOW.md](GIT_WORKFLOW.md) → "Emergency Recovery"
- Build problems: [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) → "Common Tasks"
- Deployment issues: [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) → "Troubleshooting"
- Customization help: [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) → "Troubleshooting Customization"

---

## 📋 Quick Checklists

### Pre-Development Checklist
- [ ] Installed Quarto 1.3+
- [ ] Installed Python 3.8+
- [ ] Have Git configured
- [ ] Can clone the repo
- [ ] Can run `quarto render`
- [ ] Read [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md)

### Pre-Commit Checklist
- [ ] Made changes locally
- [ ] Ran `quarto render` (no errors)
- [ ] Tested changes in browser
- [ ] Wrote clear commit message
- [ ] Followed [GIT_WORKFLOW.md](GIT_WORKFLOW.md)

### Pre-Deployment Checklist
- [ ] All tests pass
- [ ] Code reviewed and approved
- [ ] [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) complete
- [ ] Documentation updated
- [ ] No sensitive data in repo
- [ ] Ready to merge to main

### Pre-Launch Checklist
- [ ] All content complete
- [ ] All links tested
- [ ] Mobile responsive verified
- [ ] Accessibility audit passed
- [ ] Performance optimized
- [ ] [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md) complete

---

## 🔗 External Resources

### Official Docs
- **Quarto:** https://quarto.org/docs
- **Bootstrap:** https://getbootstrap.com/docs
- **Git:** https://git-scm.com/doc
- **GitHub:** https://docs.github.com/
- **Obsidian:** https://help.obsidian.md/

### Learning Resources
- **Quarto Websites:** https://quarto.org/docs/websites
- **Markdown Guide:** https://www.markdownguide.org/
- **SCSS:** https://sass-lang.com/guide
- **Git Tutorials:** https://git-scm.com/book (free book)
- **GitHub Skills:** https://skills.github.com/ (interactive)

### Design Inspiration
- **SIM Lab:** https://sim-lab-siue.github.io/
- **Color Picker:** https://color.adobe.com/
- **Coolors:** https://coolors.co/
- **Font Pairs:** https://www.fontpair.co/

---

## 💬 Getting Help

### I Have a Question About...

**Git/GitHub issues:**
1. Check [GIT_WORKFLOW.md](GIT_WORKFLOW.md) → "Common Scenarios"
2. Search GitHub issues
3. Ask team on Slack/Discord

**Quarto/Technical setup:**
1. Check [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md)
2. Search Quarto docs: https://quarto.org/docs
3. Pair program with team member

**Content/Course design:**
1. Check [CONTENT_PLAN.md](CONTENT_PLAN.md)
2. Review example in Phase 1: [modules/01_orientation/](modules/01_orientation/)
3. Ask content team member

**Deployment/DevOps:**
1. Check [DEPLOYMENT.md](DEPLOYMENT.md)
2. Check [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md)
3. Ask DevOps team member

**Customization/Instructor questions:**
1. Check [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md)
2. Contact your developer
3. Create GitHub issue

---

## 📞 Team Communication

### For Questions/Issues:
- **Slack/Discord** - Quick questions, discussion
- **GitHub Issues** - Bug reports, feature requests, technical tracking
- **Pull Requests** - Code review, feedback
- **Email** - Formal communication, decisions

### Documentation Maintenance:
- Docs live in the GitHub repo
- Changes follow same Git workflow
- Keep docs up-to-date with code
- Link within docs for easy navigation

---

## ✅ Documentation Completeness

As of January 27, 2026:

| Document | Completeness | Last Updated |
|----------|-------------|--------------|
| [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) | 100% | Jan 27, 2026 |
| [ARCHITECTURE.md](ARCHITECTURE.md) | 100% | Jan 27, 2026 |
| [ROADMAP.md](ROADMAP.md) | 100% | Jan 27, 2026 |
| [CONTENT_PLAN.md](CONTENT_PLAN.md) | 100% | Jan 27, 2026 |
| [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) | 100% | Jan 27, 2026 |
| [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) | 100% | Jan 27, 2026 |
| [GIT_WORKFLOW.md](GIT_WORKFLOW.md) | 100% | Jan 27, 2026 |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Original, needs update | Jan 2026 |
| [GITHUB_SETUP.md](GITHUB_SETUP.md) | Original, needs update | Jan 2026 |
| [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md) | Original, adequate | Jan 2026 |
| [START_HERE.md](START_HERE.md) | Original, adequate | Jan 2026 |
| [QUICK_START.md](QUICK_START.md) | Original, adequate | Jan 2026 |
| [README.md](README.md) | Updated, 100% | Jan 27, 2026 |

---

*Last updated: January 27, 2026*
