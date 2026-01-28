# Project Overview & Architecture

**Last Updated:** January 27, 2026  
**Purpose:** Technical architecture and decision documentation for developers

---

## System Overview

The MC451 Liaison Program is a complete learning platform consisting of:

1. **Static website** (Built with Quarto)
2. **Student workspace vault** (Built with Obsidian)
3. **Content library** (Course modules, guides, resources)
4. **Deployment infrastructure** (GitHub Pages/Netlify)

### Technology Stack

| Component | Technology | Why |
|---|---|---|
| **Website Generator** | Quarto | Professional academic/research sites, excellent documentation, R Markdown ecosystem |
| **Markup Language** | Markdown + YAML | Easy to learn, human-readable, version-control friendly |
| **Frontend Framework** | Bootstrap 5 | Responsive, accessible, extensive component library |
| **Styling** | SCSS/CSS | Variables for theming, mixins for reusable styles |
| **Automation** | Python | Cross-platform file operations, simple vault generation |
| **Version Control** | Git + GitHub | Industry standard, excellent documentation, free hosting |
| **Hosting** | GitHub Pages/Netlify | Free, automatic deployment, no backend needed |
| **Search** | Quarto built-in | Client-side, no server needed, searchable HTML |

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│         DEVELOPER / INSTRUCTOR EDITS FILES           │
│  (QMD files, SCSS styling, Python build script)     │
└──────────────────────┬──────────────────────────────┘
                       │
                       ↓
        ┌──────────────────────────────┐
        │   QUARTO RENDER PROCESS      │
        │  (Converts .qmd → .html)     │
        └──────────────┬───────────────┘
                       │
                       ↓
        ┌──────────────────────────────┐
        │    _site/ FOLDER             │
        │  (Static HTML + CSS + JS)    │
        └──────────────┬───────────────┘
                       │
      ┌────────────────┼────────────────┐
      │                │                │
      ↓                ↓                ↓
 ┌─────────┐    ┌────────────┐   ┌──────────┐
 │ GitHub  │    │  Netlify   │   │University│
 │ Pages   │    │            │   │ Server   │
 └────┬────┘    └──────┬─────┘   └────┬─────┘
      │                │              │
      └────────┬───────┴──────┬───────┘
               │              │
               ↓              ↓
        ┌──────────────────────────────┐
        │   LIVE WEBSITE               │
        │   (Students access here)     │
        └──────────────────────────────┘


SEPARATE PIPELINE:

┌─────────────────────────────────────────────────────┐
│      Python Script (build_vault.py)                 │
│  (Creates Liaison_Vault folder structure)           │
└──────────────────────┬──────────────────────────────┘
                       │
                       ↓
        ┌──────────────────────────────┐
        │    Liaison_Vault/            │
        │  (Local student workspace)   │
        └──────────────┬───────────────┘
                       │
                       ↓
        ┌──────────────────────────────┐
        │    Liaison_Vault.zip         │
        │  (For distribution)          │
        └──────────────┬───────────────┘
                       │
      ┌────────────────┼────────────────┐
      │                │                │
      ↓                ↓                ↓
   GitHub      Resources Page      Email
   Releases    (Website)           Attachment
```

---

## Data Flow

### User Journey: From Learning to Output

```
STUDENT WORKFLOW:

1. Visit Website (index.html)
   ↓
2. Click "Setup Guide"
   ↓
3. Follow Setup Page (setup.qmd)
   ↓
4. Download Liaison_Vault.zip from Resources
   ↓
5. Extract vault locally
   ↓
6. Open in Obsidian
   ↓
7. Follow Phase 1 module instructions
   ↓
8. Create journal entries in vault
   ↓
9. Progress through Phases 2-5
   ↓
10. Submit final project/presentation


DEVELOPER WORKFLOW:

1. Edit .qmd files (content)
   ↓
2. Edit .scss file (styling)
   ↓
3. Run `quarto render`
   ↓
4. Check output in _site/ folder
   ↓
5. Git add, commit, push
   ↓
6. GitHub Pages auto-deploys
   ↓
7. Live site updated
```

---

## File Organization Logic

### Why This Structure?

```
project-root/
├── Core Content Files (visible on website)
│   ├── index.qmd              - Homepage (entry point)
│   ├── setup.qmd              - Student onboarding
│   ├── syllabus.qmd           - Course details
│   ├── about.qmd              - Instructor info
│   └── resources/             - Downloads & tools
│
├── Modules (5-phase curriculum)
│   └── modules/
│       ├── 01_orientation/    - Phase 1 (complete)
│       ├── 02_discovery/      - Phase 2 (partial)
│       ├── 03_dictionary/     - Phase 3 (stub)
│       ├── 04_execution/      - Phase 4 (stub)
│       └── 05_delivery/       - Phase 5 (stub)
│
├── Student Workspace (pre-configured)
│   └── Liaison_Vault/
│       ├── 00_Inbox/          - Quick capture
│       ├── 01_Journal/        - Weekly reflections
│       ├── 02_Literature/     - Research notes
│       ├── 03_Project/        - Active work
│       ├── 04_Resources/      - Attachments
│       ├── 99_Templates/      - Reusable templates
│       └── Liaison_Vault.zip  - For distribution
│
├── Configuration
│   ├── _quarto.yml            - Quarto config (navbar, sidebar)
│   ├── custom-styling.scss    - Brand colors, fonts, styles
│   └── build_vault.py         - Vault generation script
│
├── Output (auto-generated)
│   └── _site/ (or docs/)      - Built HTML ready to deploy
│
└── Documentation
    ├── README.md              - Quick start
    ├── DEVELOPER_GUIDE.md     - Technical setup
    ├── ARCHITECTURE.md        - This file
    ├── ROADMAP.md             - Planned improvements
    ├── CONTENT_PLAN.md        - Module completion status
    ├── CUSTOMIZATION_GUIDE.md - For instructors
    ├── TESTING_CHECKLIST.md   - QA process
    ├── GIT_WORKFLOW.md        - Team collaboration
    ├── DEPLOYMENT.md          - Hosting options
    ├── GITHUB_SETUP.md        - GitHub configuration
    └── LAUNCH_CHECKLIST.md    - Pre-launch tasks
```

---

## Technology Decisions & Rationale

### Why Quarto?

**Chosen:** Quarto (Quarto.org)  
**Alternatives:** Jekyll, Hugo, Next.js, Gatsby  

**Decision factors:**
- ✅ Specifically designed for academic/research content
- ✅ Excellent documentation and community support
- ✅ Supports multiple languages (Markdown, R, Python, Julia)
- ✅ Built-in search, responsive design, accessibility
- ✅ Can integrate with RStudio/Jupyter notebooks
- ✅ R Markdown ecosystem backing (mature)
- ✅ Learn once, use for many projects
- ❌ Smaller ecosystem than Jekyll (but growing)
- ❌ Requires Quarto installation (but easy)

**Use case fit:** Perfect for educational/research platforms where content is primary.

### Why Obsidian for Student Vault?

**Chosen:** Obsidian (Obsidian.md)  
**Alternatives:** Notion, Evernote, OneNote, Standard folders  

**Decision factors:**
- ✅ Non-linear note-taking (backlinks, graph view)
- ✅ Free tier adequate for students
- ✅ No account required (can work offline)
- ✅ Local-first (data on student's computer)
- ✅ Plugin ecosystem (future extensibility)
- ✅ Popular in academic community
- ✅ YAML metadata support (research metadata)
- ❌ Requires local installation
- ❌ Learning curve for new users

**Use case fit:** Ideal for organizing research across weeks/phases.

### Why Bootstrap?

**Chosen:** Bootstrap 5  
**Alternatives:** Tailwind, Material UI, custom CSS  

**Decision factors:**
- ✅ Works seamlessly with Quarto
- ✅ Mobile-first responsive design
- ✅ Extensive component library
- ✅ Accessibility built-in (WCAG compliance)
- ✅ Large community and documentation
- ✅ No build process needed
- ❌ Larger file size than minimal CSS frameworks
- ❌ "Bootstrap look" without customization

**Use case fit:** Fast deployment, professional appearance out of the box.

### Why Python for Vault Generation?

**Chosen:** Python  
**Alternatives:** Bash/PowerShell script, Node.js, Go  

**Decision factors:**
- ✅ Cross-platform (Windows, Mac, Linux)
- ✅ Simple, readable code
- ✅ No compilation needed
- ✅ Pathlib library handles file operations elegantly
- ✅ Easy for non-programmers to understand
- ✅ Good for one-time automation scripts
- ❌ Requires Python installation
- ❌ Slightly slower than compiled languages

**Use case fit:** Simple file automation, run once per semester.

---

## Build & Deployment Flow

### Local Development

```bash
# 1. Edit files (developers do this all day)
# 2. Test locally
quarto render          # Builds _site/ folder
quarto preview         # Opens live preview

# 3. Commit and push
git add .
git commit -m "message"
git push origin feature-branch

# 4. Create pull request on GitHub (web UI)
# 5. Team reviews code
# 6. Merge to main

# AUTOMATIC FROM HERE:

# 7. GitHub Actions triggers
# 8. Runs `quarto render` on GitHub's servers
# 9. Outputs to _site/ (or docs/)
# 10. GitHub Pages serves the HTML
# 11. Live site updates in 1-2 minutes
```

### Deployment Targets

#### Option 1: GitHub Pages (Current)
- Free, automatic, no configuration needed
- Site lives at: `https://username.github.io/repo`
- Deploy on push to `main` branch
- SSL certificate included

#### Option 2: Netlify
- Free tier, easy to set up
- Custom domain support
- Deploy previews for pull requests
- Better build caching

#### Option 3: University Server
- Institutional control
- Custom domain (e.g., `research.university.edu`)
- May require manual uploads
- More control over infrastructure

---

## Configuration Management

### _quarto.yml (Quarto Configuration)

Controls:
- Website title, navbar, sidebar
- Project type (website, book, presentation)
- Output directory (_site/ or docs/)
- Render options (CSS, JavaScript, extensions)

**Key sections:**
```yaml
project:
  type: website                    # Type of project
  output-dir: docs                # Where to put HTML
  
website:
  title: "Course Title"           # Browser tab title
  navbar: { ... }                 # Top navigation
  sidebar: [ ... ]                # Left sidebar (optional)
  
format:
  html:
    theme: bootstrap              # Bootstrap theme
    css: custom-styling.scss      # Custom styles
```

### custom-styling.scss (Brand Styling)

Controls:
- Colors (primary, accent, secondary)
- Fonts and typography
- Component styling (.phase-header, .card, etc.)
- Responsive breakpoints

**Variables to customize:**
```scss
$primary-color: #2c3e50;          // Brand primary
$accent-color: #e74c3c;           // Brand accent
$heading-font: Georgia, serif;     // Heading font
$body-font: -apple-system, sans;   // Body font
```

### build_vault.py (Vault Generation)

Runs once per semester to:
1. Create folder structure
2. Generate template files
3. Create README for students
4. Zip for distribution

**To regenerate:**
```bash
python build_vault.py
# Creates/updates Liaison_Vault and Liaison_Vault.zip
```

---

## Content Organization

### Module Structure

Each module (Phase) has:
```
modules/
├── 01_orientation/
│   ├── index.qmd              # Phase overview
│   ├── chapter_01.qmd         # Supporting content
│   └── README.md              # Dev notes
├── ...
```

**index.qmd contains:**
- Phase header (title, duration, time commitment)
- Learning objectives (list)
- Overview/rationale
- Activities (numbered, with instructions)
- Resources (links, templates)
- Assessment criteria

### Cross-linking

Pages link to each other:
- Module pages link to: Setup guide, Resources, other phases
- Navbar provides: Navigation to all major pages
- Sidebar provides: Additional organization (optional)
- Footer provides: Contact info, links

---

## Templating System

### Quarto Divs (Custom Styling)

```qmd
:::{.phase-header}
# Phase 1: Orientation

Styled with CSS class .phase-header
:::

:::{.learning-objectives}
- Objective 1
- Objective 2
:::
```

These divs get custom styling from `custom-styling.scss`.

### Variables (Reusable Content)

Future enhancement: Variables for:
- Instructor name, email, office hours
- Course meeting times
- Grading scale
- Key dates

Referenced throughout, update once to change everywhere.

---

## Security & Data Considerations

### What's Public?
- All `.qmd` files (curriculum content)
- All generated `.html` files (website)
- GitHub repository (open source)
- No student data collection

### What's Private?
- Instructor's contact info (encrypted in email)
- Student work (stays in their Obsidian vault, not on server)
- GitHub repository settings (if private)

### No Backend Database
- **Advantage:** No server to maintain, hack, or pay for
- **Advantage:** Students' data stays on their computers
- **Limitation:** Can't track student progress server-side
- **Solution:** Rely on learning management system (Blackboard, Canvas) for tracking if needed

---

## Scalability Considerations

### Current Scale
- 1 instructor
- 20-50 students per semester
- No authentication needed

### Future Scale (Multi-instructor, Multi-cohort)

**Needed:**
- Multiple instructor profiles
- Cohort management (Section A, B, C run differently)
- Student progress tracking
- Peer collaboration/discussion tools
- Assessment tools

**Options:**
- Keep static site, add backend (Node/Python server)
- Integrate with university LMS (Blackboard, Canvas)
- Build admin dashboard for instructors
- Add student authentication

---

## Performance Metrics

### Current Performance
- Page load: <1 second (static HTML)
- Search: Instant (client-side)
- Mobile responsiveness: All breakpoints tested
- Accessibility: WCAG AA compliant (with minor improvements needed)

### Future Optimization
- Image optimization (compress PNGs/JPGs)
- CSS minification (already done by Quarto)
- Service workers (offline access)
- Analytics (Google Analytics, optional)

---

## Version History

### MVP (January 2026)
- ✅ Basic Quarto website
- ✅ Phase 1 complete with activities
- ✅ Obsidian vault generation
- ✅ GitHub Pages deployment
- ✅ Mobile responsive design

### Current Status
- Phase 2 partial content
- UX improvements planned
- Navigation could be streamlined
- Visual branding could be enhanced

### Roadmap
- **Sprint 1:** Complete Phases 2-5 content
- **Sprint 2:** Visual redesign & branding
- **Sprint 3:** Interactive timeline, enhanced UX
- **Sprint 4:** Instructor customization tools
- **Future:** Multi-cohort support, assessment tools

---

## Testing Strategy

### Types of Testing

1. **Functionality Testing**
   - Links work correctly
   - Downloads function
   - Navigation works
   - Vault extracts properly

2. **UI/UX Testing**
   - Responsive design (mobile, tablet, desktop)
   - Visual consistency
   - Accessibility (keyboard, screen readers)
   - Performance

3. **Content Testing**
   - No typos or errors
   - Links correct
   - Images display
   - Formatting correct

4. **Integration Testing**
   - Quarto render completes
   - GitHub Pages deployment succeeds
   - Live site matches local preview

See [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) for detailed procedures.

---

## Maintenance & Support

### Regular Tasks
- **Weekly:** Update module content (during semester)
- **Monthly:** Check for broken links, update resources
- **Semester-end:** Archive course, plan improvements
- **Off-season:** Major feature development, redesigns

### Common Issues & Fixes

| Issue | Cause | Fix |
|---|---|---|
| Site not updating | Changes not pushed | Run `git push origin main` |
| Broken link | Bad file path | Use relative paths, test links |
| Mobile nav broken | CSS conflict | Check custom-styling.scss |
| Vault won't unzip | Corrupted file | Regenerate with `python build_vault.py` |
| Images not loading | Wrong path | Use relative paths from project root |

---

## Resources for Developers

### Official Documentation
- [Quarto Documentation](https://quarto.org/docs)
- [Bootstrap Documentation](https://getbootstrap.com/docs)
- [Obsidian Help](https://help.obsidian.md)
- [GitHub Docs](https://docs.github.com/)

### Project Documentation
- [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) - Setup & workflows
- [ROADMAP.md](ROADMAP.md) - Future improvements
- [CONTENT_PLAN.md](CONTENT_PLAN.md) - Content status
- [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) - For instructors
- [GIT_WORKFLOW.md](GIT_WORKFLOW.md) - Team collaboration
- [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) - QA process

---

*Last updated: January 27, 2026*
