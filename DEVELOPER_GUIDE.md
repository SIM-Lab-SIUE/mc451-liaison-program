# Developer Guide: MC451 Liaison Program

**Last Updated:** January 27, 2026  
**Audience:** Developers taking over the Liaison Program project  
**Purpose:** Complete technical and contextual handoff documentation

---

## 🎯 Project Overview

### What Is This Project?

The MC451 Liaison Program Website is a **complete student learning platform** for a university research methods course. The project consists of:

1. **A professional Quarto website** - Student-facing educational content platform
2. **A pre-configured Obsidian vault** - Digital workspace for student research organization
3. **Course modules** - Five phases of research methodology instruction
4. **Administrative documentation** - Deployment, setup, and improvement guides

### Who This Is For

- **Students**: Learning research methods and communication liaison skills
- **Instructors**: Teaching the MC451 course
- **University**: Hosting a modern, professional research program

### Business Context

This is a **startup acquisition scenario**. A single developer built this MVP, and now a small development team is taking over to:
- Improve UX/navigation
- Add missing content to Phase modules
- Maintain and enhance the platform
- Prepare for scale and future iterations

---

## 🏗️ Architecture & Technology Stack

### Core Technologies

| Technology | Purpose | Version | Why Chosen |
|---|---|---|---|
| **Quarto** | Website generation & rendering | 1.3+ | Professional static sites, built on R Markdown ecosystem, excellent documentation |
| **Obsidian** | Student digital workspace | Latest | Non-linear note-taking, built-in backlinks, free tier, large community |
| **Bootstrap** | UI Framework | 5.x | Responsive design, extensive components, works seamlessly with Quarto |
| **SCSS** | Custom styling | 3.x | Variables, mixins, nesting for organized CSS |
| **Python** | Vault generation automation | 3.8+ | Cross-platform, simple file manipulation for setup |
| **Git** | Version control | 2.x | Standard for team collaboration |

### How They Work Together

```
Code (QMD files) 
    ↓
Quarto Render Process
    ↓
Static HTML (in _site/ folder)
    ↓
Deploy to GitHub Pages / Netlify / Server
    ↓
Students access live website

Separately:
Python Script (build_vault.py)
    ↓
Creates Liaison_Vault structure + templates
    ↓
Zips into Liaison_Vault.zip
    ↓
Placed in resources/ for download
    ↓
Students extract and configure in Obsidian
```

### Key Design Patterns

**Modular Content Structure** - Each module is a folder with `index.qmd` and optional chapters
**Template-Based** - Reusable Obsidian templates for students (Weekly Journal, Data Dictionary)
**Static Site Generation** - No backend needed; secure, fast, and easy to deploy
**Client-Side Search** - Built-in Quarto search indexes HTML on student's browser

---

## 📁 Project Structure Deep Dive

### Core Website Files

```
_quarto.yml
├─ Website configuration
├─ Navigation structure
├─ Sidebar organization
└─ Output directory settings

index.qmd
├─ Home page (hero section + 3 main cards)
├─ Student entry points
└─ Links to Setup, Phases, Resources

setup.qmd
├─ Step-by-step installation guide
├─ Obsidian configuration instructions
├─ Troubleshooting tips
└─ First-time student onboarding

syllabus.qmd
├─ Course information (instructor info, meeting times, grading)
├─ Learning objectives
└─ Course policies

about.qmd
├─ Instructor biography
├─ Contact information
└─ Lab/program information
```

### Module Content Structure

```
modules/
├─ 01_orientation/        [✅ CONTENT EXISTS]
│  ├─ index.qmd          (Phase overview, learning objectives, activities)
│  ├─ chapter_01.qmd     (Supporting content chapter)
│  └─ README.md          (Development notes)
│
├─ 02_discovery/          [⚠️ STUB - Needs content]
│  ├─ index.qmd          (Framework exists, content needed)
│  └─ README.md          (Development notes)
│
├─ 03_dictionary/         [⚠️ EMPTY]
│  └─ index.qmd          (Header only, full content needed)
│
├─ 04_execution/          [⚠️ EMPTY]
│  └─ index.qmd          (Header only, full content needed)
│
└─ 05_delivery/           [⚠️ EMPTY]
   └─ index.qmd          (Header only, full content needed)
```

### Student Resources

```
Liaison_Vault/
├─ 00_Inbox/            (Quick note capture)
├─ 01_Journal/          (Weekly student reflections)
├─ 02_Literature/       (Research note organization)
├─ 03_Project/          (Active work)
│  ├─ 01_Prospectus/    (Project proposal)
│  ├─ 02_Codebook/      (Data definitions)
│  ├─ 03_Data/          (Dataset storage)
│  └─ 04_Drafts/        (Work in progress)
├─ 04_Resources/        (Attachments, media)
├─ 99_Templates/        (Reusable templates)
│  ├─ Weekly_Journal_Template.md
│  └─ Data_Dictionary_Template.md
└─ 00_START_HERE.md     (Vault orientation file)

Liaison_Vault.zip       (Distributed to students)
```

### Build & Deployment

```
_site/                  [AUTO-GENERATED]
├─ HTML files (rendered from .qmd)
├─ site_libs/           (CSS, JS, search index)
└─ Ready to deploy to GitHub Pages, Netlify, or server

docs/                   [LEGACY - Can be removed]
└─ Earlier build output (kept for reference)
```

---

## 🛠️ Development Setup

### Prerequisites

- Python 3.8+
- Quarto 1.3+ ([quarto.org/docs/get-started](https://quarto.org/docs/get-started))
- Git
- Text editor (VS Code recommended)
- GitHub account (for deployment)

### Initial Setup

```bash
# Clone the repository
git clone <repo-url>
cd mc451-liaison-program

# Install Quarto (if needed)
# Follow instructions at https://quarto.org/docs/get-started/

# Verify installation
quarto --version
python --version
```

### Development Workflow

```bash
# 1. Edit content (.qmd files) in your editor
#    Changes auto-save

# 2. Render locally to test
quarto render

# 3. Check output in _site/ folder
#    Open any HTML file in browser to preview

# 4. Test responsive design
#    Browser DevTools → Toggle device toolbar (mobile view)

# 5. Commit and push when satisfied
git add .
git commit -m "Add Phase 2 content: Discovery activities"
git push origin main

# 6. GitHub Pages deploys automatically (if configured)
#    Check Actions tab for build status
```

---

## 📚 File Format Guide

### Quarto Markdown Files (.qmd)

Quarto files are Markdown + R/Python code + YAML metadata. For this project, we mainly use Markdown.

**Structure of a .qmd file:**

```yaml
---
title: "Your Page Title"
---

# Main heading

Content here with **bold** and *italic*.

## Subheading

More content...
```

**Special Quarto elements:**

```
:::{.callout-note}
This is a note with special styling
:::

:::{.callout-warning}
This is a warning
:::

| Column 1 | Column 2 |
|---|---|
| Data | Data |
```

**Links:**
```markdown
[Display text](path/to/file.qmd)  → Internal link
[Display text](https://example.com)  → External link
```

### Configuration File (_quarto.yml)

The `_quarto.yml` controls:
- Website title and theme
- Navigation bar structure
- Sidebar organization
- Output directory
- Render options

**Key sections:**
```yaml
project:
  type: website          # This is a website project
  output-dir: docs      # Where to put rendered HTML

website:
  title: "..."          # Browser tab title
  navbar: { ... }       # Top navigation menu
  sidebar: [ ... ]      # Left sidebar sections
```

When adding new pages:
1. Create the `.qmd` file
2. Add to `navbar` (if it should be in top menu) OR `sidebar` (if in left menu)
3. Run `quarto render` to rebuild
4. Check that link appears in site

### Python Script (build_vault.py)

This creates the student Obsidian vault structure.

**Functions:**
- `create_vault_structure()` - Creates all folders and .gitkeep files
- `create_readme_file()` - Creates 00_START_HERE.md orientation file
- `create_journal_template()` - Creates weekly journal template
- `create_data_dictionary_template()` - Creates data definition template
- `zip_vault()` - Zips vault folder for student download

**To regenerate vault:**
```bash
python build_vault.py
```

This recreates the vault, templates, and Liaison_Vault.zip for distribution.

---

## 🎨 Styling & Customization

### Custom CSS (custom-styling.scss)

Contains custom Bootstrap overrides and component styles:

```scss
// Variables - change these to rebrand
$primary-color: #2c3e50;
$accent-color: #e74c3c;

// Phase header cards
.phase-header { ... }

// Learning objectives boxes
.learning-objectives { ... }

// Card grid layouts
.card-grid { ... }
.card { ... }
```

**To modify colors/fonts:**
1. Edit `custom-styling.scss`
2. Run `quarto render`
3. Colors update across the entire site

### Bootstrap Classes

Used throughout for responsive design:
- `container` - Max-width wrapper
- `row` / `col` - Grid system
- `btn btn-primary` - Button styling
- `alert alert-info` - Alert boxes
- `d-none d-md-block` - Hide on mobile, show on desktop

---

## 📝 Content Guidelines

### For Module Pages

Each module should have:

1. **Phase header** - Title, duration, time commitment
2. **Learning objectives** - What students will accomplish (5-8 items)
3. **Overview section** - Conceptual introduction
4. **Activity sections** - Practical work (numbered)
5. **Assessment/deliverables** - What they submit
6. **Resources** - Links to tools, templates, external reading

**Template:**
```yaml
---
title: "🔍 Phase X: [Name]"
---

:::{.phase-header}
# Phase X: [Name]
**Duration:** Weeks X-X | **Time Commitment:** ~X hours
:::

## Learning Objectives
[List 5-8 learning objectives]

## Overview
[Conceptual explanation of this phase]

## Activities
### Activity 1: [Name]
[Instructions and deliverables]

## Resources
[Links to templates, tools, readings]
```

### For Documentation Files

Documentation files use **standard Markdown** with these conventions:

```markdown
# Main Title
**Last Updated:** Date
**Audience:** Who should read this
**Purpose:** Why it exists

## Section 1
### Subsection 1.1

- Bullet point
- Another point
  - Nested point

### Subsection 1.2

**Important:** Highlighted text

> Block quote for emphasis

[Link text](url)
```

---

## 🚀 Deployment Pipeline

### Development Environment

```
Local files (.qmd, .py, .scss, .yml)
         ↓
quarto render
         ↓
_site/ folder (HTML + CSS + JS)
         ↓
Browse locally: _site/index.html
```

### Production Environment (GitHub Pages)

```
Push to GitHub
         ↓
GitHub Actions workflow triggers
         ↓
Runs: quarto render
         ↓
Outputs _site/ folder
         ↓
Deploys to GitHub Pages
         ↓
Live at: https://username.github.io/repo
```

### Alternative Deployments

**Netlify:**
- Connect GitHub repo
- Build command: `quarto render`
- Publish dir: `_site`
- Auto-deploys on push

**University Server:**
- Run `quarto render` locally
- Upload `_site/` folder to server
- Update path in web server config

---

## 🧪 Testing Checklist

Before deployment, verify:

- [ ] **Links work** - Click every nav item, check no 404s
- [ ] **Images load** - Check all images render correctly
- [ ] **Mobile responsive** - Browser DevTools shows content flows on mobile
- [ ] **Search works** - Test search functionality finds content
- [ ] **Templates download** - Resources page downloads work
- [ ] **Vault unpacks** - Liaison_Vault.zip extracts properly
- [ ] **Pages render** - No Quarto errors in console
- [ ] **Navigation consistent** - Navbar/sidebar work from all pages

See [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) for detailed test procedures.

---

## 📋 Current Project Status

### Completed ✅
- Website framework built with Quarto
- Navigation structure implemented
- Phase 1: Orientation (full content)
- Phase 2: Discovery (framework + some content)
- Setup guide for students
- Obsidian vault template system
- Deployment documentation
- Mobile-responsive design

### In Progress 🔄
- UX improvements (see UX_IMPROVEMENT_PLAN.md)
- Content for Phases 3, 4, 5

### Not Started ❌
- Phase 3: The Dictionary (full content)
- Phase 4: Execution (full content)
- Phase 5: Delivery (full content)
- Advanced Obsidian features (community plugins)
- Assessment rubrics

### Known Issues 🐛
- Sidebar duplicates navbar navigation (UX concern)
- Phase 3-5 pages show headers only
- Contact info not in footer
- Generic Bootstrap styling (could be more distinctive)

See [ROADMAP.md](ROADMAP.md) for improvement priorities.

---

## 🔄 Common Tasks

### Adding a New Page

```bash
# 1. Create the .qmd file
touch modules/02_discovery/chapter_02.qmd

# 2. Add header
echo '---
title: "Chapter Title"
---

# Chapter Title

Content here.' > modules/02_discovery/chapter_02.qmd

# 3. Add to _quarto.yml sidebar or navbar

# 4. Render
quarto render

# 5. Test locally
```

### Updating Student Vault Template

```bash
# 1. Edit template in Liaison_Vault/99_Templates/
vim Liaison_Vault/99_Templates/Weekly_Journal_Template.md

# 2. Regenerate vault
python build_vault.py

# 3. Test extraction and usage

# 4. Commit and push
git add Liaison_Vault.zip resources/Liaison_Vault.zip
git commit -m "Update journal template"
git push
```

### Customizing Site Styling

```bash
# 1. Edit custom-styling.scss
vim custom-styling.scss

# 2. Render (Quarto compiles SCSS → CSS)
quarto render

# 3. Check _site/site_libs/quarto.css for changes

# 4. Test in browser
```

### Deploying Updates

```bash
# 1. Make and test changes locally
# 2. Commit changes
git add .
git commit -m "Descriptive commit message"

# 3. Push to GitHub
git push origin main

# 4. GitHub Pages auto-deploys (check Actions tab)

# 5. Verify changes at https://username.github.io/repo
```

---

## 📖 Additional Resources

### Project Documentation
- [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) ← You are here
- [ARCHITECTURE.md](ARCHITECTURE.md) - Tech stack and design decisions
- [ROADMAP.md](ROADMAP.md) - Planned improvements
- [CONTENT_PLAN.md](CONTENT_PLAN.md) - Module content status
- [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) - Instructor setup
- [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) - QA process
- [GIT_WORKFLOW.md](GIT_WORKFLOW.md) - Team collaboration
- [DEPLOYMENT.md](DEPLOYMENT.md) - Production deployment

### External Resources
- [Quarto Documentation](https://quarto.org/docs)
- [Quarto Websites Guide](https://quarto.org/docs/websites)
- [Bootstrap Documentation](https://getbootstrap.com/docs)
- [Obsidian Help](https://help.obsidian.md)
- [SCSS Guide](https://sass-lang.com/guide)
- [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)

---

## ❓ FAQ

**Q: How do I preview changes locally before deploying?**  
A: Run `quarto render`, then open any HTML file from `_site/` folder in your browser. Or run `quarto preview` for live-reload.

**Q: Can students modify the Obsidian vault structure?**  
A: Yes! The vault is theirs after download. The folder structure is just a suggestion. They can reorganize however works for them.

**Q: Do I need to know Python to maintain this?**  
A: Not really. The `build_vault.py` script runs once to create the vault. After that, you mainly edit `.qmd` files (which is Markdown).

**Q: How often should we update the site?**  
A: On a semester schedule:
- Before semester starts: Update syllabus, instructor info
- Weekly: Add module content and announcements
- After semester: Archive, plan improvements

**Q: What if something breaks?**  
A: Check:
1. Did `quarto render` complete without errors?
2. Are all files saved?
3. Did you push the right changes?
4. Check GitHub Actions logs for deployment errors

**Q: Can we use custom JavaScript?**  
A: Yes, via Quarto's script injection in `.qmd` files or custom HTML templates (advanced).

---

## 📞 Getting Help

- **Quarto Issues** → [Quarto GitHub Discussions](https://github.com/quarto-dev/quarto-cli/discussions)
- **Bootstrap Help** → [Bootstrap Docs](https://getbootstrap.com/docs)
- **Obsidian Support** → [Obsidian Help](https://help.obsidian.md)
- **Git Help** → `git help <command>` or [GitHub Guides](https://guides.github.com)

---

## 👋 Handoff Notes

This project was built as an MVP for a single researcher/instructor to deploy course materials. The new team should:

1. **Start here:** Review this DEVELOPER_GUIDE.md completely
2. **Understand the vision:** Read the UX_IMPROVEMENT_PLAN.md for the direction
3. **Set up locally:** Follow the development setup section above
4. **Complete Phase 3-5:** Add the missing course content
5. **Implement UX improvements:** Follow the ROADMAP.md
6. **Deploy:** Use GitHub Pages or your preferred hosting
7. **Iterate:** Use the GIT_WORKFLOW.md for team collaboration

The platform is solid and extensible. Future improvements are well-documented. Good luck! 🚀

---

*Last updated: January 27, 2026*
