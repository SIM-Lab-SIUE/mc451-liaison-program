# Testing Checklist & QA Guide

**Last Updated:** January 27, 2026  
**Purpose:** Ensure website quality, functionality, and user experience before each release

---

## Pre-Deployment Testing

Use this checklist before deploying any changes to production.

### ✅ Build & Rendering

- [ ] Run `quarto render` without errors
  ```bash
  quarto render
  # Should complete with no errors or warnings
  ```
- [ ] Check console output for warnings
  - ⚠️ If warnings appear, investigate and fix
  - 🟢 Some Quarto warnings are harmless; document if known
- [ ] Verify `_site/` folder was created/updated
- [ ] Check that `_site/index.html` exists
- [ ] File sizes are reasonable (not unexpectedly large)

### 🔗 Navigation Testing

Test from every page to ensure no broken links:

- [ ] **Home page** (`index.qmd`)
  - [ ] "Setup Guide" button → `setup.qmd`
  - [ ] "View Phases" button → `modules/01_orientation/index.qmd`
  - [ ] "Resources" button → `resources/index.qmd`
  
- [ ] **Navbar menu items** (visible on every page)
  - [ ] Home → `index.qmd`
  - [ ] Syllabus → `syllabus.qmd`
  - [ ] Phases dropdown:
    - [ ] Phase 1 → `modules/01_orientation/index.qmd`
    - [ ] Phase 2 → `modules/02_discovery/index.qmd`
    - [ ] Phase 3 → `modules/03_dictionary/index.qmd`
    - [ ] Phase 4 → `modules/04_execution/index.qmd`
    - [ ] Phase 5 → `modules/05_delivery/index.qmd`
  - [ ] Resources → `resources/index.qmd`
  - [ ] About → `about.qmd`

- [ ] **Sidebar navigation** (if present)
  - [ ] All sidebar links work
  - [ ] No duplicate navigation with navbar

- [ ] **Footer links** (if present)
  - [ ] Contact links work
  - [ ] Social media links work
  - [ ] External resource links work

- [ ] **Internal links within content**
  - [ ] Links to other phases work
  - [ ] Links to resources page work
  - [ ] Links to templates work
  - [ ] No 404 errors in browser console

### 📥 Resource Downloads

- [ ] **Liaison_Vault.zip**
  - [ ] Download link visible on Resources page
  - [ ] File downloads without errors
  - [ ] File size is reasonable (~20-30 KB)
  - [ ] File can be extracted/unzipped
  - [ ] Extracted vault has expected structure:
    - [ ] `00_Inbox/` folder exists
    - [ ] `01_Journal/` folder exists
    - [ ] `02_Literature/` folder exists
    - [ ] `03_Project/` with subfolders exists
    - [ ] `04_Resources/` folder exists
    - [ ] `99_Templates/` with templates exists
    - [ ] `00_START_HERE.md` file exists
  - [ ] Templates have expected content

- [ ] **Other downloads**
  - [ ] Any textbook/resource files download properly
  - [ ] File sizes are not corrupted
  - [ ] PDFs render correctly

### 🎨 Visual & Layout Testing

**Desktop (1920x1200 resolution):**
- [ ] Homepage displays properly
  - [ ] Hero section is visible and attractive
  - [ ] Cards are aligned in grid
  - [ ] Text is readable with good contrast
  - [ ] Images load without broken image icons
  - [ ] Buttons are clickable and styled correctly
  
- [ ] Module pages display properly
  - [ ] Phase header section looks good
  - [ ] Learning objectives are formatted correctly
  - [ ] Activity sections are clear and organized
  - [ ] Tables display properly (if present)
  - [ ] Code blocks (if present) are readable

- [ ] Typography and spacing
  - [ ] Headings are hierarchy is clear (H1 > H2 > H3)
  - [ ] Paragraphs have good line-height
  - [ ] Lists are properly indented
  - [ ] Adequate whitespace between sections

**Tablet (768x1024 resolution):**
- [ ] Navbar doesn't wrap unexpectedly
- [ ] Cards stack properly (2-column → 1-column)
- [ ] Sidebar is accessible (hidden or collapsible)
- [ ] Touch targets are large enough (buttons, links)
- [ ] No horizontal scrolling needed

**Mobile (375x667 resolution):**
- [ ] Navbar is hamburger menu or single column
- [ ] All content is readable without zooming
- [ ] No horizontal scrolling
- [ ] Buttons are large enough to tap
- [ ] Images scale properly
- [ ] Tables are readable (horizontal scroll if needed)
- [ ] Footer is accessible

### 🔍 Search Functionality

- [ ] Search box is visible and accessible
- [ ] Search works on home page
- [ ] Search works on module pages
- [ ] Searching for common terms returns results
  - [ ] Searching "orientation" finds Phase 1
  - [ ] Searching "data" finds relevant pages
  - [ ] Searching "template" finds template downloads
- [ ] No results shown gracefully for empty search
- [ ] Results are clickable and navigate correctly

### 🖼️ Images & Media

- [ ] All images load (no broken image icons)
- [ ] Images are properly sized (not pixelated or huge)
- [ ] Alt text is present (for accessibility)
  - Open DevTools → Inspector
  - Check `<img>` tags have `alt=` attribute
- [ ] Videos (if present) play without errors
- [ ] Responsive images scale on mobile

### 🎯 Accessibility Testing

**Keyboard Navigation:**
- [ ] Can navigate entire site with keyboard (Tab key)
- [ ] Tab order is logical (top to bottom, left to right)
- [ ] Focus is visible (can see where keyboard is)
- [ ] Can interact with all buttons/links via keyboard
- [ ] Skip navigation links work (if present)

**Color & Contrast:**
- [ ] Text has sufficient contrast with background
  - Use: [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
  - Minimum: WCAG AA (4.5:1 for body text, 3:1 for large text)
- [ ] Color is not the only way to convey information
  - Links aren't only distinguished by color
  - Error messages use icon + text, not just red

**Screen Reader:**
- [ ] Headings are properly nested (don't skip levels)
- [ ] Images have meaningful alt text
- [ ] Links have descriptive text (not "click here")
- [ ] Form labels are associated with inputs
- [ ] Tables have headers (`<th>` tags)

**WCAG 2.1 Level AA Compliance:**
- [ ] Provide [WCAG accessibility statement](https://www.w3.org/WAI/test-evaluate/) (future nice-to-have)

### 📱 Browser Compatibility

Test in multiple browsers (use online tools if needed):

**Desktop Browsers:**
- [ ] Chrome/Edge (latest)
- [ ] Firefox (latest)
- [ ] Safari (Mac, if available)

**Mobile Browsers:**
- [ ] Chrome Android
- [ ] Safari iOS

For each browser:
- [ ] Homepage displays correctly
- [ ] Navigation works
- [ ] No JavaScript errors in console (F12)
- [ ] Responsive design works
- [ ] Buttons are clickable

### ⚡ Performance

- [ ] Page load time is reasonable (<3 seconds)
  - DevTools → Network tab
  - Check total page size
  - Identify any large resources (images, JS, CSS)

- [ ] No console JavaScript errors
  - Open DevTools (F12)
  - Check Console tab
  - Should be clean (no red error messages)

- [ ] Images are optimized
  - Use [ImageOptim](https://imageoptim.com/) or similar
  - PNGs should be <200 KB
  - JPGs should be <150 KB

### 🚀 Deployment

Before pushing to GitHub Pages / Netlify:

- [ ] All changes are committed (`git status` is clean)
- [ ] Last commit message is descriptive
- [ ] Branch is correct (usually `main`)
- [ ] No sensitive info in committed files
- [ ] `.gitignore` is configured properly

After pushing:
- [ ] GitHub Actions build succeeds (check Actions tab)
- [ ] Live site updates within 1-2 minutes
- [ ] Live site shows all changes correctly
- [ ] No deployment errors in GitHub Pages settings

---

## Regression Testing

After each update, verify previous functionality still works:

### Content Changes
- [ ] Previous module still displays
- [ ] Previous links still work
- [ ] No formatting broken from previous versions

### Navigation Changes
- [ ] Previous navigation paths still work
- [ ] Redirects in place for moved pages (if any)
- [ ] Sidebar and navbar match expected structure

### Design/Style Changes
- [ ] All pages have consistent styling
- [ ] New styles don't break old pages
- [ ] Colors are used consistently
- [ ] Mobile responsiveness still works

### Vault Changes
- [ ] Previously generated vault still valid
- [ ] New vault structure is backwards compatible
- [ ] Templates can still be found/used

---

## Manual Testing Scenarios

Walk through these realistic student workflows:

### Scenario 1: First-Time Student Setup
1. [ ] Student visits homepage
2. [ ] Clicks "Setup Guide"
3. [ ] Reads setup instructions clearly
4. [ ] Downloads Liaison_Vault.zip
5. [ ] Extracts vault to Documents
6. [ ] Opens Obsidian
7. [ ] Configures vault (all instructions clear)
8. [ ] Opens 00_START_HERE.md
9. [ ] Explores each folder
10. [ ] Can find Weekly_Journal_Template.md
11. [ ] Can duplicate template to create first entry

### Scenario 2: Student Navigating Phases
1. [ ] From home, click "View Phases"
2. [ ] Lands on Phase 1: Orientation
3. [ ] Can read all content clearly
4. [ ] Can access all activities
5. [ ] Can find templates linked
6. [ ] Clicks to Phase 2 (navigation works)
7. [ ] Can read Phase 2 content
8. [ ] Can return to Phase 1
9. [ ] Can jump to any phase from navbar

### Scenario 3: Instructor Finding Customization Info
1. [ ] Goes to Resources page
2. [ ] Finds CUSTOMIZATION_GUIDE link
3. [ ] Opens and reads clear instructions
4. [ ] Can follow steps to customize (test with one change)
5. [ ] Changes are reflected on website after rebuild

### Scenario 4: Mobile User Experience
1. [ ] Opens site on mobile phone
2. [ ] Can see navbar (hamburger menu or clean)
3. [ ] Can navigate to all pages
4. [ ] Content is readable without horizontal scroll
5. [ ] Images load and display properly
6. [ ] Can download vault.zip (download works on mobile)
7. [ ] Can tap all buttons/links accurately

---

## Automated Testing (Optional, Future)

For tech-savvy team:

### HTML Validation
```bash
# Validate HTML (requires w3.org connection)
# Check _site/ folder at https://validator.w3.org/
```

### Link Checking
```bash
# Option 1: GitHub Action (set up workflow)
# Option 2: Local tool like linkchecker
# Catch broken links before deployment
```

### Accessibility Audit
```bash
# Use Lighthouse in DevTools
# Target: 90+ score for Accessibility
```

### Performance Audit
```bash
# Use Lighthouse in DevTools
# Target: 80+ score for Performance
```

---

## Bug Tracking Template

When you find an issue, document it:

```markdown
**Title:** [Brief description]

**Severity:** Critical | High | Medium | Low
- Critical: Blocks student workflow (can't access content, can't download vault)
- High: Major UX issue (broken links, confusing navigation)
- Medium: Minor UX issue (styling problem, typo)
- Low: Polish (could be better but doesn't block work)

**Steps to Reproduce:**
1. Start here
2. Do this
3. Then this
4. Observe issue

**Expected Behavior:**
[What should happen]

**Actual Behavior:**
[What actually happens]

**Environment:**
- Browser: [Chrome/Firefox/Safari]
- Device: [Desktop/Tablet/Mobile]
- OS: [Windows/Mac/iOS/Android]

**Screenshot:** [If applicable]

**Assignment:**
[Who should fix this]

**Priority:**
[Due date if critical/high]
```

---

## Testing Cadence

### Before Each Release
- Run full checklist above
- Estimated time: 30-45 minutes

### Weekly (If making changes)
- Quick smoke test (page loads, links work, mobile OK)
- Estimated time: 10-15 minutes

### Monthly (Or before course starts)
- Full regression test
- Browser compatibility test
- Performance audit
- Estimated time: 2-3 hours

### Quarterly (Or each semester)
- Accessibility audit (WCAG compliance)
- User testing with actual students
- Performance optimization review
- Plan improvements

---

## Tools & Resources

### Browser DevTools
- **Chrome/Edge:** F12 or Right-click → Inspect
- **Firefox:** F12 or Right-click → Inspect Element
- **Safari:** Develop menu (enable in Preferences)

### Accessibility Tools
- [WebAIM Color Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [WAVE Accessibility Tool](https://wave.webaim.org/) - Browser extension
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - Built into Chrome
- [NVDA Screen Reader](https://www.nvaccess.org/) - Free, Windows
- [AXE DevTools](https://www.deque.com/axe/devtools/) - Browser extension

### Performance Tools
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [WebPageTest](https://www.webpagetest.org/)
- Chrome DevTools → Performance tab

### Link Checking
- [Broken Link Checker](https://www.brokenlinkcheck.com/) - Online tool
- [linkchecker](https://linkchecker.github.io/linkchecker/) - Command line

### Responsive Design Testing
- [Responsively App](https://responsively.app/) - Desktop app
- Chrome DevTools → Device toolbar (F12)
- [BrowserStack](https://www.browserstack.com/) - Real devices (paid)

---

## Checklist for Final Launch

Before going live with the website:

- [ ] All content is complete and reviewed
- [ ] All links are tested and working
- [ ] Mobile design is responsive and tested
- [ ] Accessibility meets WCAG AA standards
- [ ] Performance is optimized
- [ ] Browser compatibility verified
- [ ] Vault downloads and extracts properly
- [ ] Contact information is visible and correct
- [ ] All documentation is updated
- [ ] Deployment process is documented
- [ ] Backup is in place
- [ ] Analytics are set up (optional)
- [ ] Team has been trained on maintaining site
- [ ] Contact info for technical support is established

---

*Last updated: January 27, 2026*
