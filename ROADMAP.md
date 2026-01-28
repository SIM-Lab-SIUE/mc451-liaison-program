# UX & Development Roadmap

**Last Updated:** January 27, 2026  
**Vision:** Evolve the Liaison Program website from MVP to research-lab-quality platform

---

## Overview

The Liaison Program website is a solid foundation built for student success. This roadmap prioritizes improvements based on:
1. **User experience** (student friction points)
2. **Feature completeness** (missing content and functionality)
3. **Visual identity** (research lab branding)
4. **Operational scalability** (supporting multiple cohorts)

---

## 🎯 Roadmap Priorities

### Phase 1: CRITICAL (Complete in next sprint)

These are blocking issues that reduce student success:

#### 1.1 Complete Module Content ⚠️ HIGH URGENCY
- **Status:** Phases 3, 4, 5 are stubs
- **Impact:** Students can't progress through course
- **Effort:** 30-40 hours total
- **Action:**
  - Fill in Phase 2: Discovery (4-6 hours)
  - Fill in Phase 3: Dictionary (8-10 hours)
  - Fill in Phase 4: Execution (10-12 hours)
  - Fill in Phase 5: Delivery (8-10 hours)
- **Owner:** Instructor + Content Dev
- **Deadline:** Before course start date
- **Reference:** [CONTENT_PLAN.md](CONTENT_PLAN.md)

#### 1.2 Fix Navigation Duplication
- **Status:** Sidebar + navbar both navigate to same pages
- **Problem:** Confuses users; mobile nav breaks
- **Impact:** Poor UX, especially on mobile
- **Effort:** 2-3 hours
- **Action:**
  - Remove sidebar (sidebar duplicates navbar)
  - Make navbar cleaner: HOME | SYLLABUS | PHASES | RESOURCES | ABOUT
  - Add footer with instructor contact info
  - Test on mobile devices
- **Owner:** Frontend Dev
- **Priority:** HIGH

#### 1.3 Add Missing Pages/Sections
- **Status:** About page, contact info scattered
- **Problem:** Students can't find instructor info
- **Impact:** Support requests, missing office hours
- **Effort:** 2-3 hours
- **Action:**
  - Create/enhance [about.qmd](about.qmd) with:
    - Instructor bio
    - Office hours and location
    - Email and contact method
    - Lab/program description
  - Add footer with contact info on every page
  - Add FAQ section (anticipated student questions)
- **Owner:** Content + Frontend Dev
- **Priority:** HIGH

---

### Phase 2: IMPORTANT (Next 2-4 sprints)

#### 2.1 Improve Visual Design & Branding 🎨
- **Status:** Generic Bootstrap look (not distinctive)
- **Problem:** Looks like a course site, not a research program
- **Impact:** Professional impression, student engagement
- **Effort:** 6-8 hours
- **Action:**
  - Define visual brand (colors, fonts, logo)
  - Inspire by: [SIM Lab](sim-lab-siue.github.io), professional university research lab sites
  - Update [custom-styling.scss](custom-styling.scss):
    - Custom color palette
    - Custom fonts (Google Fonts)
    - Logo/branding header
    - Research theme styling
  - Create visual hierarchy:
    - Hero section on homepage with dramatic imagery
    - Phase cards with icons and descriptions
    - Research theme/focus areas prominent
  - Ensure accessibility (contrast, readable fonts)
- **Owner:** UX/Design Dev
- **Priority:** HIGH
- **Estimated Timeline:** Sprint 2

#### 2.2 Enhance Homepage
- **Status:** Simple 3-card layout; adequate but not inspiring
- **Problem:** Doesn't communicate program value or prestige
- **Impact:** First impression for prospective students
- **Effort:** 4-6 hours
- **Action:**
  - Hero section:
    - Compelling headline about research impact
    - Background image/visual
    - Call-to-action (Get Started button)
  - Section 1: "What You'll Learn"
    - 5 learning outcome bullets
    - Icons or small graphics
  - Section 2: "The Five Phases"
    - Cards for each phase (Orientation → Delivery)
    - Visual progression
  - Section 3: "Join Our Lab"
    - Community/cohort messaging
    - Recent student projects (optional)
  - Footer with: Instructor, contact, social links
- **Owner:** UX Dev + Content
- **Priority:** MEDIUM-HIGH
- **Estimated Timeline:** Sprint 2-3

#### 2.3 Create Interactive Course Timeline/Roadmap Page
- **Status:** Content exists in individual modules; no overview
- **Problem:** Students don't see full arc of the semester
- **Impact:** Better orientation, time management
- **Effort:** 3-4 hours
- **Action:**
  - New page: "Course Timeline" or "Your Journey"
  - Visual timeline showing:
    - Week numbers
    - Phase names and duration
    - Key milestones (proposals due, etc.)
    - Current phase highlight (Weeks X-Y)
  - Timeline format: Horizontal bar or vertical cards
  - Links to each phase
  - Syllabus deadlines integrated
- **Owner:** Frontend Dev + Content
- **Priority:** MEDIUM
- **Estimated Timeline:** Sprint 3

#### 2.4 Implement Customizable Instructor Panel
- **Status:** No admin interface; edits require file edits
- **Problem:** New instructors must understand Quarto/Git
- **Impact:** Easier handoff to instructors
- **Effort:** 8-12 hours (or use template)
- **Action:**
  - Option A (Recommended): Create clear [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md)
    - Step-by-step for instructor to edit key files
    - Template files for common customizations
    - Screenshots of what changes where
  - Option B (Future): Build simple web form for customization
    - Name, contact, office hours
    - Generates updated _quarto.yml
    - For future iteration
  - Store instructor settings in a variables file (`instructor.yml`)
  - Reference throughout site
- **Owner:** Dev + Content
- **Priority:** MEDIUM
- **Estimated Timeline:** Sprint 2 (Guide), Sprint 4+ (Form UI)

---

### Phase 3: NICE-TO-HAVE (Future iterations)

#### 3.1 Add Assessment Tools
- **Status:** No built-in rubrics or grading
- **Impact:** Helps instructors assess student work
- **Effort:** 10-15 hours
- **Ideas:**
  - Rubric builder / rubric templates
  - Downloadable assessment guides
  - Sample student work (with permission)
  - Peer review protocols
- **Priority:** LOW-MEDIUM
- **Estimated Timeline:** Sprint 5+

#### 3.2 Integrate Discussion Forum or Comments
- **Status:** No built-in collaboration space
- **Impact:** Student discussion, questions, community
- **Options:**
  - GitHub Discussions (free, integrated)
  - Disqus (third-party comments)
  - Discord server (external)
  - Quarto native comments (future)
- **Effort:** 2-4 hours (GitHub Discussions), 6-8 hours (custom)
- **Priority:** LOW-MEDIUM
- **Estimated Timeline:** Sprint 4-5

#### 3.3 Add Resource Repository
- **Status:** Resources page has basic downloads
- **Impact:** Central hub for all learning materials
- **Ideas:**
  - Readings database (filterable by phase, topic)
  - Video tutorials (screencasts of tools)
  - Code snippets (R, Python examples)
  - Data sources (sample datasets for analysis)
  - Tool recommendations (comparison tables)
- **Priority:** MEDIUM
- **Estimated Timeline:** Sprint 4-5

#### 3.4 Create Student Showcase
- **Status:** No mechanism to share student work
- **Impact:** Celebrates student success, motivates others
- **Ideas:**
  - Gallery of student projects (with permission)
  - Short case studies of exemplary work
  - Student testimonials
  - "Spotlight: Student of the Week" section
- **Effort:** 4-6 hours + ongoing content curation
- **Priority:** LOW
- **Estimated Timeline:** Sprint 6+

#### 3.5 Mobile App (Future)
- **Status:** Website is mobile-responsive
- **Impact:** Better offline access, push notifications
- **Ideas:**
  - Simple read-only app (Flutter/React Native)
  - Sync with Obsidian vault
  - Notifications for deadlines
  - Offline content access
- **Effort:** 40+ hours
- **Priority:** LOW
- **Estimated Timeline:** Year 2+

---

## 📋 Detailed Action Items by Role

### For Product Manager / Instructor
- [ ] Approve visual design direction (brand colors, fonts)
- [ ] Provide instructor bio and contact info
- [ ] Review and approve Phase 2-5 content
- [ ] Identify key dates and deadlines for timeline
- [ ] Gather student feedback on usability
- [ ] Prioritize "nice-to-have" features

### For Frontend Developer
- [ ] Refactor navbar/sidebar navigation structure
- [ ] Implement improved homepage design
- [ ] Add footer with contact info
- [ ] Update custom-styling.scss for new brand
- [ ] Optimize mobile responsive behavior
- [ ] Add interactive course timeline
- [ ] Create responsive image handling

### For Content Developer
- [ ] Complete Phase 2-5 module content (CRITICAL)
- [ ] Create activity templates and examples
- [ ] Write CUSTOMIZATION_GUIDE.md for instructors
- [ ] Develop assessment rubrics
- [ ] Source or create visual assets (icons, images)
- [ ] Compile recommended resources
- [ ] Create FAQ section

### For DevOps / Tech Lead
- [ ] Set up GitHub Actions for automated testing
- [ ] Configure GitHub Pages deployment
- [ ] Create development branch strategy
- [ ] Document deployment procedures
- [ ] Set up monitoring/analytics
- [ ] Plan content backup strategy

---

## 🎯 Sprint Planning Template

### Sprint 1 (Week 1-2) - CRITICAL CONTENT
**Goal:** Get Phases 2-5 to playable state

- **Phase 2:** Discovery content completion (4-6 hours)
- **Phase 3:** Dictionary content completion (8-10 hours)
- **Navigation fix:** Remove sidebar duplication (2-3 hours)
- **Contact info:** Complete About page (2-3 hours)

**Deliverable:** All 5 phases have content; students can progress through course

### Sprint 2 (Week 3-4) - UX POLISH & BRANDING
**Goal:** Create cohesive, professional visual identity

- **Visual design:** Brand refresh (6-8 hours)
- **Homepage:** Enhanced hero and layout (4-6 hours)
- **Footer:** Add contact info to all pages (1-2 hours)
- **Mobile testing:** Fix responsive issues (2-3 hours)

**Deliverable:** Beautiful, cohesive website that feels like a research program

### Sprint 3 (Week 5-6) - COMPLETE CONTENT
**Goal:** Finish Phase 4-5 content; add interactive timeline

- **Phase 4:** Execution content completion (10-12 hours)
- **Phase 5:** Delivery content completion (8-10 hours)
- **Course timeline:** Interactive page (3-4 hours)
- **Testing:** Full walkthrough as student (3-4 hours)

**Deliverable:** All course content complete; students can finish entire program

### Sprint 4 (Week 7-8) - INSTRUCTOR TOOLS & POLISH
**Goal:** Make site maintainable and customizable

- **CUSTOMIZATION_GUIDE:** Clear instructions (3-4 hours)
- **Assessment rubrics:** Downloadable templates (4-6 hours)
- **FAQ section:** Anticipated questions (2-3 hours)
- **Performance optimization:** Speed and accessibility (2-3 hours)

**Deliverable:** Instructors can customize and maintain site independently

---

## 🎨 Design Inspiration & References

### Research Lab Sites (High Quality)
- [SIM Lab (SIUE)](https://sim-lab-siue.github.io/) - Excellent design
- [HCI Lab (CMU)](https://www.hcilab.cmu.edu/) - Professional layout
- [Media Lab MIT](https://www.media.mit.edu/) - Cutting edge
- [Stanford Data Lab](https://data.stanford.edu/) - Clean academic design

### Features to Adopt
- ✅ Hero section with compelling visuals
- ✅ Clear research focus areas/themes
- ✅ Team/people section
- ✅ Project showcase
- ✅ Clean, minimal navbar
- ✅ Footer with contact and social
- ✅ Responsive grid layouts
- ✅ Professional imagery

### Color/Typography Considerations
- Modern, accessible color palette (WCAG AA contrast minimum)
- Readable serif or sans-serif fonts (Google Fonts)
- Enough whitespace for visual breathing room
- Consistent icon set (Font Awesome or similar)
- Dark or light theme toggle (future nice-to-have)

---

## 🚀 Success Metrics

How will we know we've succeeded?

### For MVP Phase (Weeks 1-2)
- ✅ All 5 phases have complete content (students can finish course)
- ✅ Navigation is intuitive (no sidebar/navbar confusion)
- ✅ Student can contact instructor (visible contact info)
- ✅ Mobile view works (tested on phone browsers)

### For Launch Phase (Weeks 3-6)
- ✅ Site looks professional and distinctive
- ✅ Homepage inspires interest (compelling hero section)
- ✅ Students understand full scope (timeline visible)
- ✅ Setup is smooth (Phase 1 → Phase 2 transition easy)

### For Maintenance Phase (Weeks 7-8)
- ✅ Instructors can customize without code (CUSTOMIZATION_GUIDE works)
- ✅ Assessment is clear (rubrics provided)
- ✅ Common questions answered (FAQ complete)
- ✅ Site is fast and accessible (performance metrics good)

---

## 📊 Resource Allocation

### Estimated Total Effort
- **Critical tasks:** 35-45 hours
- **Important tasks:** 25-35 hours
- **Nice-to-have tasks:** 30-50 hours (optional)

### Suggested Team
- **1 Content Developer** (Full-time Phases 1-3)
- **1 Frontend Developer** (Part-time navigation, design)
- **1 Instructor/Product Manager** (Content review, direction)

### Timeline
- **Sprint 1 (Weeks 1-2):** 15-20 hrs/dev
- **Sprint 2 (Weeks 3-4):** 12-15 hrs/dev
- **Sprint 3 (Weeks 5-6):** 20-25 hrs/dev
- **Sprint 4 (Weeks 7-8):** 10-12 hrs/dev

**Total: 8-10 weeks for full feature parity**

---

## 🔄 Feedback & Iteration

### Gather User Feedback
- **Week 2:** Soft launch to test cohort
- **Week 4:** Gather feedback after Phase 1-2
- **Week 6:** Refine based on student experience
- **Week 8:** Final polish before full launch

### Feedback Channels
- Quick survey after each phase (2-3 questions)
- Office hours discussion
- Anonymous feedback form
- GitHub issues for bugs

---

## 🏁 Definition of Done

A feature or phase is "done" when:
- [ ] Content is complete and reviewed
- [ ] Links are tested and working
- [ ] Mobile view is responsive
- [ ] Search functionality works (if applicable)
- [ ] Accessibility standards met (WCAG AA)
- [ ] Documentation is updated
- [ ] Changes are committed and deployed
- [ ] Stakeholders have approved

---

## 🔮 Future Enhancements (Beyond 8 Weeks)

### Year 2
- Multi-cohort support (running course in parallel)
- Student portfolio system
- Automated rubric grading
- Integration with university systems (LMS sync)
- Advanced Obsidian plugins guide

### Year 3
- Mobile app for iOS/Android
- Community forum or discussion space
- Video course content
- Interactive data analysis labs
- Capstone project showcase

### Year 4+
- Research collaboration platform
- Conference submission tracker
- Publication management
- Alumni network integration

---

*Last updated: January 27, 2026*
