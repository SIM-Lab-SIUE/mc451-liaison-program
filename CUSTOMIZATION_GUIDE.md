# Customization Guide for Instructors

**Last Updated:** January 27, 2026  
**Audience:** Instructors who want to customize the Liaison Program website for their course  
**Time Estimate:** 30-45 minutes for basic customization

---

## Quick Start: Personalize Your Course in 5 Steps

If you're in a hurry, do these 5 things first:

1. **Edit home page** with your name and brief welcome
2. **Edit syllabus** with course details and grading
3. **Edit about page** with your bio and contact info
4. **Update office hours** in footer/navbar
5. **Rebuild and deploy** (run `quarto render`, push to GitHub)

**Total time: 15 minutes** ⏱️

For more customization options, keep reading!

---

## 📋 Pre-Customization Checklist

Before you start editing:

- [ ] You have edit access to the GitHub repository
- [ ] You have Quarto installed locally ([quarto.org](https://quarto.org/docs/get-started/))
- [ ] You have VS Code or a text editor
- [ ] You have Git installed and configured
- [ ] You can run `quarto render` without errors
- [ ] You have access to your personal information (bio, office hours, contact)
- [ ] You have any branding/logo files ready (optional)

---

## 🏠 Step 1: Customize the Home Page

**File:** [index.qmd](index.qmd)

This is the first page students see. Make it welcoming!

### What to Change

#### 1.1 Welcome Message

**Find this:**
```yaml
---
title: "Home"
---

:::{.hero-section}
# MC Research Methods: The Liaison Program

**Bridging Data Science and Creative Communication**
...
:::
```

**Change to:**
```yaml
---
title: "Home"
---

:::{.hero-section}
# MC Research Methods: The Liaison Program
## [Add tagline about your research focus]

**Bridging Data Science and Creative Communication**

Welcome to Professor [Your Name]'s research methods course. 
This semester, you'll learn to [describe what they'll learn].
```

**Personalization tips:**
- Add your research area or specialty
- Add a personal welcome message
- Keep it to 2-3 sentences
- Make students feel excited about the course

#### 1.2 Update Course Cards

The three main cards on the homepage. You can change the order, icons, or text.

**Find:**
```yaml
::: {.card}
<span class="card-icon">📋</span>

### Get Started
Complete your workspace setup in 15 minutes...
:::
```

**Customize:**
- Change emoji icon to match your theme
- Update description to reflect what students do
- Keep buttons pointing to same pages

---

## 📚 Step 2: Create Your Syllabus

**File:** [syllabus.qmd](syllabus.qmd)

Students need to know course basics: contact, schedule, grading, policies.

### Minimum Content to Add

```yaml
---
title: "Syllabus"
---

# MC Research Methods: Liaison Program
## [Your Name] | Spring 2026

### Course Information

**Meeting Times:** [Days/Times]  
**Location:** [Building, Room]  
**Office Hours:** [Times], or by appointment  
**Email:** [Your Email]  
**Phone:** [Optional]

### Course Description

[1-2 paragraphs about the course]

### Learning Objectives

By the end of this course, students will be able to:

- Objective 1
- Objective 2
- Objective 3
- Objective 4
- Objective 5

### Course Requirements & Grading

| Assignment | Weight |
|---|---|
| Phase 1 Completion | 15% |
| Phase 2 Proposal | 20% |
| Phase 3 Codebook | 20% |
| Phase 4 Analysis | 25% |
| Phase 5 Presentation | 20% |

### Grading Scale

| Grade | Range |
|---|---|
| A | 90-100% |
| B | 80-89% |
| C | 70-79% |
| D | 60-69% |
| F | <60% |

### Course Policies

- **Attendance:** [Your attendance policy]
- **Late Work:** [Your late work policy]
- **Academic Integrity:** [Reference university policy]
- **Accommodations:** [Statement about ADA/disability accommodations]
- **Office Hours:** [When available, how to schedule]

### Required Materials

- Obsidian (free, downloaded during Phase 1)
- R or Python (free, installed during Phase 1)
- [Any required textbooks or readings]

### Course Schedule

| Week | Phase | Topic | Due |
|---|---|---|---|
| 1-2 | 1 | Orientation | Vault setup |
| 3-4 | 2 | Discovery | Research proposal |
| 5-7 | 3 | Dictionary | Data dictionary |
| 8-10 | 4 | Execution | Analysis report |
| 11-13 | 5 | Delivery | Final presentation |

### Contact & Support

[Add how students should contact you, office hours, etc.]
```

### Tips for Great Syllabus
- Be clear and specific (dates, times, percentages)
- Include your personality (brief intro about yourself and why you teach)
- Make policies fair and transparent
- Include accessibility statement
- Link to university resources (disability services, counseling, etc.)

---

## 👤 Step 3: Personalize the About Page

**File:** [about.qmd](about.qmd)

Students want to know who you are and how to reach you.

### What to Include

```yaml
---
title: "About"
---

# About the Instructor

## [Your Name]

[1-2 paragraphs about your background, research interests, and teaching philosophy]

### Research Interests

- Topic 1
- Topic 2
- Topic 3

### Education

- PhD in [Field], [University]
- Master's degree in [Field], [University]
- Bachelor's degree in [Field], [University]

### Office Hours

**Location:** [Building] Room [Number]  
**Times:** [Days and Times]  
**How to Schedule:** [Email, sign-up sheet, online calendar]

### Contact Information

**Email:** [Your Email]  
**Phone:** [Optional]  
**Office:** [Building, Room Number]

### Why I Teach This Course

[2-3 sentences about why you believe in research methods education and what you want students to get from the course]

### The Liaison Program

The Liaison Program teaches students to be bridges between data and communication.
We believe that [your philosophy about research and communication].

Through this five-phase model, you'll learn to...
[1-2 sentences about course goals]

---

## 🎯 Step 4: Update Key Information Throughout

These pieces of info appear in multiple places. Update them everywhere:

### Your Name
- [ ] [index.qmd](index.qmd) - Welcome message
- [ ] [syllabus.qmd](syllabus.qmd) - Course header
- [ ] [about.qmd](about.qmd) - Page title
- [ ] [_quarto.yml](_quarto.yml) - Optional, in config

### Office Hours
- [ ] [about.qmd](about.qmd) - Full details
- [ ] [syllabus.qmd](syllabus.qmd) - Quick reference
- [ ] [index.qmd](index.qmd) - Optional, in footer

### Email Address
- [ ] [about.qmd](about.qmd) - Contact section
- [ ] [syllabus.qmd](syllabus.qmd) - Course info
- [ ] Consider footer (optional)

### Meeting Times & Location
- [ ] [syllabus.qmd](syllabus.qmd) - Course information
- [ ] [index.qmd](index.qmd) - Optional, hero section

---

## 🎨 Step 5: Optional Customizations

### A. Update Course Title/Tagline

**File:** [_quarto.yml](_quarto.yml)

```yaml
project:
  type: website
  title: "MC Research Methods: The Liaison Program"  # ← Change this
  
website:
  title: "MC Research Methods: The Liaison Program"  # ← And this
```

And in [index.qmd](index.qmd) hero section.

### B. Change Colors & Branding

**File:** [custom-styling.scss](custom-styling.scss)

This file controls colors, fonts, and visual styling.

**Find:**
```scss
// Brand colors - change these!
$primary-color: #2c3e50;
$accent-color: #e74c3c;
```

**Change to your colors:**
```scss
$primary-color: #1a5490;    // Your brand blue
$accent-color: #ff6b35;     // Your brand accent
```

**To find colors:**
- Use Google's color picker
- [Adobe Color Picker](https://color.adobe.com/)
- [Coolors](https://coolors.co/) - Generate color palettes
- Keep [WCAG contrast](https://webaim.org/resources/contrastchecker/) in mind

### C. Add Your Logo

If you have a logo (PNG, JPG, SVG):

1. **Place the file** in the project root or `resources/` folder
2. **Add to index.qmd** hero section:
```yaml
:::{.hero-section}
![Program Logo](path/to/logo.png)

# MC Research Methods: The Liaison Program
...
:::
```

3. **Render and check:** `quarto render`

### D. Update Resources Page

**File:** [resources/index.qmd](resources/index.qmd)

Add any tools, textbooks, or resources specific to your course:

```yaml
## Recommended Tools

### Data Analysis
- [R & RStudio](resources/install-r-rstudio.qmd) - Free statistical software
- [Python](https://www.python.org/) - Programming language
- [Tableau Public](https://public.tableau.com/) - Data visualization

### Writing & Organization
- [Obsidian](https://obsidian.md/) - Digital note-taking (configured in Phase 1)
- [Zotero](https://www.zotero.org/) - Citation management

### Recommended Readings

- [Reading 1 Title](http://link)
- [Reading 2 Title](http://link)
- [Reading 3 Title](http://link)
```

### E. Customize Module Content (Advanced)

Each phase can be customized with examples, readings, and tools specific to your research area.

**Phase 1:** [modules/01_orientation/](modules/01_orientation/)  
**Phase 2:** [modules/02_discovery/](modules/02_discovery/)  
**Phase 3:** [modules/03_dictionary/](modules/03_dictionary/)  
**Phase 4:** [modules/04_execution/](modules/04_execution/)  
**Phase 5:** [modules/05_delivery/](modules/05_delivery/)

For each:
1. Open the [index.qmd](modules/01_orientation/index.qmd) file
2. Add examples relevant to your field
3. Add readings or resources
4. Adjust time estimates if needed
5. Rebuild and test

---

## 🛠️ Rebuilding & Deploying Your Changes

After making edits:

### 1. Build Locally (Test)

```bash
# From project root directory
quarto render
```

This creates the HTML in the `_site/` folder.

### 2. Preview (Optional)

```bash
quarto preview
```

This opens a preview of your site in your browser. Ctrl+C to stop.

### 3. Commit Changes (Git)

```bash
git add .
git commit -m "Customize course for Spring 2026"
```

Examples of good commit messages:
- "Add instructor info and syllabus"
- "Update office hours and contact info"
- "Customize Phase 2 with field-specific examples"

### 4. Push to GitHub

```bash
git push origin main
```

This sends changes to GitHub.

### 5. Wait for Deployment

If using GitHub Pages:
- GitHub automatically rebuilds your site
- Check "Actions" tab in GitHub for build status
- Site updates within 1-2 minutes
- Visit your live URL to verify changes

If using Netlify:
- Automatic deployment happens on push
- Check Netlify dashboard for build status
- Site updates within 1-2 minutes

---

## ⚡ Common Customizations Quick Reference

### Change course meeting times
→ Edit [syllabus.qmd](syllabus.qmd) "Course Information" section

### Change instructor contact info
→ Edit [about.qmd](about.qmd) "Contact Information" section  
→ Also edit [syllabus.qmd](syllabus.qmd)

### Add a reading to Phase 2
→ Edit [modules/02_discovery/index.qmd](modules/02_discovery/index.qmd)  
→ Add link in "Recommended Resources" section

### Change grading percentages
→ Edit [syllabus.qmd](syllabus.qmd) "Grading" table

### Add new activity to Phase 4
→ Edit [modules/04_execution/index.qmd](modules/04_execution/index.qmd)  
→ Copy structure of existing activity  
→ Add your activity after Activity 5

### Change the due dates
→ Edit [syllabus.qmd](syllabus.qmd) "Course Schedule" table

### Update course tagline
→ Edit [index.qmd](index.qmd) hero section

### Change brand colors
→ Edit [custom-styling.scss](custom-styling.scss) color variables

---

## 🐛 Troubleshooting Customization

### Problem: Changes don't appear after rebuild

**Solutions:**
1. Did `quarto render` complete without errors?
2. Did you save the file before running render?
3. Check `_site/` folder - is there an updated HTML file?
4. Hard refresh browser: Ctrl+Shift+R (or Cmd+Shift+R on Mac)

### Problem: Formatting looks broken

**Solutions:**
1. Check for typos in QMD syntax
2. Look for unclosed code blocks (```)
3. Check YAML is correct (title: "text", no quotes missing)
4. Run `quarto render` - error messages will help

### Problem: Links are broken

**Solutions:**
1. Check file path is correct: `modules/01_orientation/index.qmd`
2. Use relative paths (not absolute paths)
3. Link format: `[Display Text](path/to/file.qmd)`
4. Test link after rebuild

### Problem: Can't push to GitHub

**Solutions:**
1. Check you have permission to edit the repo
2. Verify you're in the right directory: `git status`
3. Make sure changes are committed: `git commit -m "message"`
4. Check internet connection
5. Try: `git push origin main` (specify branch explicitly)

### Problem: GitHub Pages site doesn't update

**Solutions:**
1. Check "Actions" tab - did build succeed?
2. Wait 1-2 minutes for deployment
3. Hard refresh your browser
4. Check GitHub Pages settings (Settings → Pages)
5. Verify `_site/` folder was created locally

---

## 📖 Advanced Customizations

These require more Quarto knowledge. See [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) for details:

- [ ] Add custom JavaScript
- [ ] Create new page layouts
- [ ] Implement custom CSS classes
- [ ] Modify build process
- [ ] Add interactive elements

---

## 🎓 Getting Help

### Stuck on QMD syntax?
→ [Quarto Markdown Guide](https://quarto.org/docs/authoring/markdown-basics.html)

### Need color inspiration?
→ [Coolors](https://coolors.co/) or [Adobe Color](https://color.adobe.com/)

### Want to customize more?
→ Read [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) for technical details

### Found a bug or issue?
→ Create a GitHub Issue with:
- What you were trying to do
- What happened
- Steps to reproduce
- Screenshots if helpful

### Team member can help?
→ Contact the development team with your question

---

## ✅ Customization Checklist

Before launching your course, verify:

- [ ] Course title and tagline are personalized
- [ ] Your name appears on home and about pages
- [ ] Contact information is correct and current
- [ ] Office hours are clearly stated
- [ ] Syllabus is complete with grading, schedule, policies
- [ ] Course meeting times/location are listed
- [ ] Any custom readings or resources are added
- [ ] Colors/branding match your program (optional)
- [ ] All links work (test in browser)
- [ ] Mobile version looks good (test on phone)
- [ ] Site is live and updated
- [ ] Students have the URL
- [ ] You can make updates (git push works)

---

## 📞 Support & Feedback

As you customize, note:
- What was easy/hard
- What you needed but couldn't find
- Suggestions for improvement

Share feedback with the development team so we can improve this guide!

---

*Last updated: January 27, 2026*
