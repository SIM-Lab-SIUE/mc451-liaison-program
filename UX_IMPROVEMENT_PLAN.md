# UX & Navigation Improvement Plan
## MC Research Methods: The Liaison Program Website

**Last Updated:** January 20, 2026  
**Prepared By:** UX Expert Review

---

## Executive Summary

Your Liaison Program website has excellent foundational content but needs significant UX improvements to match research lab standards. Inspired by the SIM Lab website design (sim-lab-siue.github.io), this plan addresses:

1. **Navigation clarity** - Streamline multi-level menus
2. **Visual hierarchy** - Add research themes and visual appeal
3. **Accessibility** - Improve readability and navigation flow
4. **Information architecture** - Reorganize content for discovery
5. **Branding** - Create a cohesive research lab aesthetic

---

## Current State Analysis

### Strengths ✅
- Clean Quarto/Bootstrap framework
- Logical five-phase structure
- Good content organization (sidebar + navbar)
- Mobile-responsive design
- Search functionality
- Clear calls-to-action on home page

### Gaps & Issues ❌
- **Navigation overload**: Too many items in navbar (7 items + dropdown)
- **Unclear hierarchy**: Sidebar duplicates navbar; confusing for new users
- **Generic design**: Looks like a generic course site, not a research program
- **Missing context**: No research themes/focus areas like SIM Lab
- **Poor discoverability**: Phase content pages are empty/minimal
- **Mobile experience**: Sidebar navigation not optimized for phones
- **Visual identity**: No branding, icons, or visual differentiation
- **Internal links**: Not all modules have content; broken navigation paths
- **Contact info scattered**: About page isolated; no footer with contact info
- **No visual hierarchy on homepage**: Three buttons look the same; can't scan quickly

---

## Reference Site Analysis: SIM Lab (sim-lab-siue.github.io)

### Key Design Patterns
✅ **Homepage hero section** with lab introduction  
✅ **Research theme cards** - 3 distinct research areas with descriptions  
✅ **Clean navbar** - HOME | ABOUT | PROJECTS | (minimal)  
✅ **Footer with contact** - Email, office hours, social links  
✅ **Project pages** - Individual research projects with details  
✅ **Team/people section** - Director bio, lab members  
✅ **Visual branding** - Consistent colors, imagery, typography  
✅ **Mobile-first layout** - Content reflows well on small screens

---

## Detailed Improvement Recommendations

### SECTION 1: Information Architecture Redesign

#### 1.1 Flatten the Navigation Structure
**Current Problem:** Navbar has "Phases" dropdown + sidebar duplication  
**Impact:** Users don't know which nav to use; mobile nav breaks

**Action Items:**
- [ ] Remove sidebar navigation on mobile (or make collapsible only)
- [ ] Simplify navbar: `HOME | SYLLABUS | PHASES | RESOURCES | ABOUT`
- [ ] Keep "Phases" as a dropdown with 5 items
- [ ] Move "Vault Download" to Resources page (not navbar)
- [ ] Remove "Contact" from navbar; add to footer

**New Navbar Structure:**
```
HOME
├─ Index (Quick start)
├─ Setup Guide

SYLLABUS
├─ Course info, objectives, grading

PHASES (dropdown)
├─ Phase 1: Orientation
├─ Phase 2: Discovery
├─ Phase 3: The Dictionary
├─ Phase 4: Execution
├─ Phase 5: Delivery

RESOURCES
├─ Vault download
├─ Software tools
├─ Setup guides
├─ Templates

ABOUT
├─ Instructor bio
├─ Lab info
├─ Contact
```

#### 1.2 Reorganize Sidebar Content
**Current Problem:** Sidebar lists every page; creates cognitive overload  
**Impact:** Users scroll forever; key pages hidden

**Action Items:**
- [ ] Create distinct sidebar sections for each phase
- [ ] Collapse phases by default on mobile
- [ ] Show expanded current phase only
- [ ] Add visual indicators (icons) for each phase
- [ ] Keep "Start Here" section always visible

---

### SECTION 2: Homepage Redesign

#### 2.1 Hero Section with Visual Impact
**Current Problem:** Homepage is text-heavy; no visual anchors  
**Impact:** Users don't immediately understand the program value

**Changes:**
- [ ] Add a hero banner with course title + tagline
- [ ] Include an optional hero image (lab photo, abstract design)
- [ ] Create a concise 1-2 sentence tagline about the liaison role
- [ ] Replace three button CTA with visual grid of four key actions:

**Proposed Homepage Grid:**
```
┌──────────────────┬──────────────────┐
│ 📋 GET STARTED   │ 🎯 THE 5 PHASES  │
│ Complete setup   │ View course flow │
│ [Setup Guide]    │ [Phases]         │
├──────────────────┼──────────────────┤
│ 📚 RESOURCES     │ 👤 MEET DR. L    │
│ Vault + tools    │ Instructor info  │
│ [Downloads]      │ [About]          │
└──────────────────┴──────────────────┘
```

#### 2.2 Add Program Overview Section
**Current Problem:** Home page jumps to phases without explaining context  
**Impact:** New students don't understand why this matters

**Changes:**
- [ ] Add section: "Your Role as a Communication Liaison"
- [ ] Explain 3 key competencies you'll develop
- [ ] Show typical career paths or applications
- [ ] Include a visual timeline/roadmap of 5 phases

#### 2.3 Visual Differentiation of Call-to-Actions
**Current Problem:** All buttons look similar; no priority hierarchy  
**Impact:** Users unsure what to do first

**Changes:**
- [ ] Primary CTA: "Get Started" (bright color, prominent)
- [ ] Secondary CTAs: "View Syllabus", "Download Vault", "About"
- [ ] Use badges/labels: "Quick (10 min)", "Download", etc.

---

### SECTION 3: Visual Design & Branding

#### 3.1 Add Lab Branding Elements
**Current Problem:** No visual identity; looks generic  
**Impact:** Doesn't feel like a professional research program

**Changes:**
- [ ] Create a lab name/identifier in header (e.g., "MC Research Methods Lab" or "The Liaison Lab")
- [ ] Add a lab logo or icon (optional but recommended)
- [ ] Create a color scheme inspired by your university branding
- [ ] Use consistent typography for headings

**Implementation in _quarto.yml:**
```yaml
website:
  title: "MC Research Methods: The Liaison Program"
  navbar:
    logo: "images/lab-logo.png"  # Optional
    background: "#2c5aa0"  # University brand color
    
format:
  html:
    theme: cosmo
    css: custom-styling.scss
```

#### 3.2 Add Icons & Visual Indicators
**Current Problem:** Text-only navigation is boring  
**Impact:** Harder to scan; less engaging

**Changes:**
- [ ] Add phase icons (🧭 Orientation, 🔍 Discovery, 📖 Dictionary, ⚙️ Execution, 🎯 Delivery)
- [ ] Add icons to navbar items
- [ ] Use icons in phase index pages
- [ ] Create visual cards for resources instead of plain lists

#### 3.3 Improve Typography & Spacing
**Current Problem:** Dense text blocks; hard to read  
**Impact:** Reduced engagement

**Changes:**
- [ ] Increase line height (1.8 for body text)
- [ ] Add more whitespace between sections
- [ ] Use color for emphasis (highlights, callout boxes)
- [ ] Create visual hierarchy: H1 > H2 > H3 with distinct sizes

---

### SECTION 4: Phase Pages Enhancement

#### 4.1 Create Consistent Phase Templates
**Current Problem:** Phase pages have different structures; some are empty  
**Impact:** Inconsistent user experience

**Template Structure for Each Phase:**
```
PHASE [N]: [TITLE]
─────────────────

🎯 LEARNING OBJECTIVES
├─ What you'll learn
├─ What you'll create
└─ How long it takes

📚 CONTENT MODULES
├─ Module 1: [Title]
│   ├─ Lesson overview
│   ├─ Key concepts
│   └─ Assignment
├─ Module 2: [Title]
│   └─ ...
└─ Module 5: [Title]

✅ DELIVERABLES
├─ What to submit
├─ Due date
└─ How you'll be evaluated

🔗 NAVIGATION
← Previous Phase | Next Phase →
```

#### 4.2 Add Content Structure to Each Phase
**Current Problem:** Most phase index pages are placeholders  
**Impact:** Users can't tell what comes in each phase

**Changes:**
- [ ] Add 3-5 learning objectives per phase
- [ ] Add section descriptions (what will students do?)
- [ ] Add time estimates per phase
- [ ] Create individual lesson/chapter pages
- [ ] Add preview of assignments/deliverables

#### 4.3 Add Navigation Between Phases
**Current Problem:** No "Next Phase" buttons; hard to flow through course  
**Impact:** Students get stuck; have to use sidebar

**Changes:**
- [ ] Add footer nav: `← Phase [N-1] | Phase [N+1] →`
- [ ] Make footer nav sticky on mobile
- [ ] Add progress indicator (e.g., "Phase 2 of 5")

---

### SECTION 5: Resources Page Overhaul

#### 5.1 Reorganize by Category
**Current Problem:** Resources are mixed (downloads, tools, guides)  
**Impact:** Hard to find what you need

**New Structure:**
```
RESOURCES & DOWNLOADS
─────────────────────

🎯 QUICK START
├─ [5 min] Download Your Vault
├─ [10 min] Set Up Obsidian
└─ [15 min] Configure Your Tools

⚙️ REQUIRED SOFTWARE (with links)
├─ Obsidian
├─ Git
├─ R & RStudio
└─ [Setup guides for each]

🎨 TEMPLATES
├─ Weekly Journal Template
├─ Data Dictionary Template
└─ Project proposal template

📖 LEARNING GUIDES
├─ Obsidian Setup Guide
├─ GitHub Quickstart
├─ R & RStudio Installation
└─ VS Code Setup

❓ GETTING HELP
├─ FAQ
├─ Troubleshooting
├─ Email support
```

#### 5.2 Create Resource Cards Instead of Lists
**Current Problem:** Plain list format; hard to scan  
**Impact:** Reduced discoverability

**Changes:**
- [ ] Convert links to visual cards with icons
- [ ] Add time estimates per resource
- [ ] Add difficulty level (Beginner/Intermediate/Advanced)
- [ ] Use consistent card styling

---

### SECTION 6: Accessibility Improvements

#### 6.1 Fix Color Contrast
**Current Problem:** Some text may not meet WCAG AA standards  
**Impact:** Hard to read for low-vision users

**Changes:**
- [ ] Run site through WAVE or Axe accessibility checker
- [ ] Ensure 4.5:1 contrast ratio for all body text
- [ ] Use color + icons (not color alone) for important info

#### 6.2 Improve Mobile Navigation
**Current Problem:** Sidebar doesn't collapse well on mobile  
**Impact:** Unusable on phones

**Changes:**
- [ ] Hide sidebar on screens <768px
- [ ] Use hamburger menu for main nav
- [ ] Make navbar items larger for touch targets (48px minimum)
- [ ] Test on iPhone, Android, tablet

#### 6.3 Add ARIA Labels & Skip Links
**Current Problem:** Screen readers can't navigate efficiently  
**Impact:** Inaccessible to blind/visually impaired users

**Changes:**
- [ ] Add skip-to-content link at top of page
- [ ] Add proper ARIA labels to navbar items
- [ ] Use semantic HTML (nav, main, footer, article)
- [ ] Add alt text to all images

#### 6.4 Improve Link Clarity
**Current Problem:** Some links are unclear (e.g., "here" is a link)  
**Impact:** Screen reader users confused

**Changes:**
- [ ] Make all link text descriptive
- [ ] Example: Change "Preview it here" → "Preview Weekly Journal Template"
- [ ] Add (external) indicator to external links

---

### SECTION 7: Footer & Contact Section

#### 7.1 Create Comprehensive Footer
**Current Problem:** No footer; contact info only on About page  
**Impact:** Hard to reach instructor; no site-wide context

**New Footer Structure:**
```
FOOTER (4 columns)
─────────────────

QUICK LINKS          RESOURCES           CONTACT             SOCIAL
├─ Home             ├─ Setup Guide      ├─ Email: ...       ├─ GitHub
├─ Phases           ├─ Vault Download   ├─ Office Hours:    ├─ Website
├─ Syllabus         ├─ Templates        │   MW 10-11:30am   └─ ORCID
└─ Resources        └─ Tool Guides      │   & 1:30-3pm       
                                        │   (or by appt)
                                        └─ Office: [Bldg]

© 2026 MC Research Methods Lab | SIUE
Made with Quarto | Last updated: [date]
```

#### 7.2 Add Contact Info to Navbar
**Current Problem:** Contact info hidden on About page  
**Impact:** New students can't find how to reach you

**Changes:**
- [ ] Add email link in navbar (right side)
- [ ] Add office hours in footer
- [ ] Make footer sticky on mobile so contact is always visible

---

## Implementation Priority & Timeline

### PHASE 1: Foundation (Weeks 1-2) - HIGHEST PRIORITY
These changes provide immediate UX improvements:

- [ ] **Simplify navbar** - Remove duplication with sidebar
- [ ] **Create footer** with contact info
- [ ] **Add visual icons** to phases and navbar items
- [ ] **Improve homepage** - Add phase grid/cards
- [ ] **Fix mobile nav** - Collapse sidebar on mobile

**Estimated Effort:** 4-6 hours  
**Impact:** High - Immediate usability improvement

### PHASE 2: Content Enhancement (Weeks 2-3) - MEDIUM PRIORITY
Improve content and information architecture:

- [ ] **Flesh out phase pages** - Add learning objectives, modules
- [ ] **Reorganize Resources page** - Create card layout
- [ ] **Add phase navigation** - Previous/Next buttons
- [ ] **Create templates** for consistent page structure
- [ ] **Add progress indicators** - Show user position in course

**Estimated Effort:** 6-8 hours  
**Impact:** Medium - Better content discovery and flow

### PHASE 3: Visual Design (Weeks 3-4) - MEDIUM PRIORITY
Polish visual design and branding:

- [ ] **Create custom CSS** for brand colors and typography
- [ ] **Add lab branding** - Logo, colors, consistent design
- [ ] **Improve Typography** - Better spacing, contrast
- [ ] **Create resource cards** - Visual redesign of downloads
- [ ] **Add hero section** - Homepage visual appeal

**Estimated Effort:** 6-8 hours  
**Impact:** Medium-High - Professional appearance

### PHASE 4: Accessibility & Testing (Week 4) - LOWER PRIORITY BUT IMPORTANT
Ensure accessibility and test across devices:

- [ ] **Run accessibility audit** - WAVE, Axe tools
- [ ] **Fix color contrast** issues
- [ ] **Test mobile** - iPhone, Android, tablet
- [ ] **Add ARIA labels** for screen readers
- [ ] **Test keyboard navigation** - Can tab through all content?

**Estimated Effort:** 4-6 hours  
**Impact:** High - Legal compliance + inclusive design

---

## Specific File Changes Required

### Files to Modify:

1. **`_quarto.yml`** - Navbar structure, styling
2. **`index.qmd`** - Homepage redesign
3. **`setup.qmd`** - Improve styling
4. **`resources/index.qmd`** - Complete reorganization
5. **`about.qmd`** - Move to footer, create more comprehensive contact
6. **`modules/*/index.qmd`** (all 5 phases) - Add learning objectives, structure
7. **`custom-styling.scss`** (NEW) - Brand colors, typography, layout

### Files to Create:

1. **`custom-styling.scss`** - Custom CSS for branding
2. **`_includes/footer.html`** - Custom footer template
3. **`images/`** folder - Store icons, logo, images
4. **`resources/setup-guides/`** - Separate guide files for each tool

---

## Design Decisions

### Color Palette (Suggested)
Based on academic/research lab aesthetic:
- **Primary**: Dark blue (#2c5aa0) - Authority, trustworthiness
- **Secondary**: Teal (#17a2b8) - Innovation, growth
- **Accent**: Orange (#fd7e14) - Engagement, energy
- **Text**: Dark gray (#212529) - Readability
- **Background**: Off-white (#f8f9fa) - Reduced eye strain

### Typography
- **Headings**: System fonts (font-family: -apple-system, BlinkMacSystemFont, "Segoe UI")
- **Body**: 18px/1.8 line-height for accessibility
- **Code**: Monospace (maintain readability)

### Layout
- **Max content width**: 900px (readable line length)
- **Sidebar width**: 280px (scannability)
- **Mobile breakpoint**: 768px
- **Spacing**: 1.5rem base unit (consistent rhythm)

---

## Link Audit Summary

### Current Internal Links (Working ✅)
- Home → Setup → Resources
- Navbar "Phases" dropdown → All 5 phase pages
- Sidebar → All major sections
- Resources page → Download links
- Footer (none) - **MISSING**

### Broken/Missing Links (⚠️)
- Sidebar "Orientation" → Chapter 01 link exists but page may be empty
- Phase pages → No forward/back navigation
- Footer → No footer exists
- Contact → Only on About page (not in navbar)

### Recommendations
- [ ] Add footer navigation with key links
- [ ] Add Previous/Next phase buttons on each phase page
- [ ] Test all internal links for validity
- [ ] Create breadcrumb navigation on nested pages

---

## Metrics to Track (After Implementation)

- **Bounce rate** - Are new users staying longer?
- **Average session duration** - Deeper engagement?
- **Page depth** - Are users exploring more pages?
- **Mobile traffic %** - Is mobile usability improving?
- **Accessibility score** - Run Lighthouse audit
- **Search functionality usage** - Are students using search?

---

## Quick Wins (You Can Do Today)

1. **Add footer with contact info** (30 min)
   - Email, office hours, social links
   
2. **Add phase icons to navbar** (30 min)
   - Use Unicode emojis: 🧭 🔍 📖 ⚙️ 🎯

3. **Collapse sidebar on mobile** (1 hour)
   - Use Quarto's responsive sidebar config

4. **Add "Previous/Next Phase" nav** (1 hour)
   - Add at bottom of each phase page

5. **Improve homepage with grid layout** (1-2 hours)
   - Replace three buttons with 2×2 grid

---

## Resources for Implementation

### Quarto Customization
- Quarto HTML customization: https://quarto.org/docs/output-formats/html-basics.html
- Navbar configuration: https://quarto.org/docs/websites/website-navigation.html
- Sidebar options: https://quarto.org/docs/websites/website-navigation.html#sidebars
- Custom CSS: https://quarto.org/docs/output-formats/html-basics.html#custom-css

### Accessibility Standards
- WCAG 2.1 Level AA: https://www.w3.org/WAI/WCAG21/quickref/
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- WAVE Accessibility Tool: https://wave.webaim.org/

### Design Inspiration
- SIM Lab: https://sim-lab-siue.github.io/
- Quarto Gallery: https://quarto.org/docs/gallery/
- Beautiful academic sites: https://www.awwwards.com/

---

## Next Steps

1. **Review this plan** - Do the recommendations align with your vision?
2. **Prioritize changes** - Which items matter most to your students?
3. **Set timeline** - When can you dedicate time to implement?
4. **Start with Phase 1** - Quick wins for immediate impact
5. **Test with users** - Get student feedback on changes

---

**Need help implementing? This plan is detailed enough to hand to a developer or work through yourself. Each section has specific, actionable items with time estimates.**

Last updated: January 20, 2026
e