# 📋 Website Launch Checklist

## Before You Deploy (Customize These)

### 1. Home Page Customization
**File**: `index.qmd`

- [ ] Add your instructor name
- [ ] Add meeting time and location
- [ ] Add your office hours
- [ ] Add contact email/phone
- [ ] Customize the course description
- [ ] Review the quick-start buttons

### 2. Create Your Syllabus
**File**: `syllabus.qmd` (create this file)

Add:
- [ ] Course title and number
- [ ] Course description
- [ ] Learning objectives
- [ ] Required materials
- [ ] Grading breakdown
- [ ] Attendance policy
- [ ] Academic integrity statement
- [ ] Disability services info
- [ ] Office hours and contact info

### 3. Add Module Content
**Files**: `modules/01_orientation/index.qmd` through `modules/05_delivery/index.qmd`

For each phase:
- [ ] Update learning objectives
- [ ] Add readings/videos
- [ ] Add activities with due dates
- [ ] Add reflection prompts
- [ ] Link to templates
- [ ] Add resources

(Phase 1 has an example you can follow!)

---

## Deployment Options (Pick ONE)

### Option A: GitHub Pages ⭐ (Easiest)
Steps in DEPLOYMENT.md:
1. Create GitHub account & repository
2. Push your code
3. Enable GitHub Pages in settings
4. Share URL: `https://yourname.github.io/quarto_website`

**Time**: ~15 minutes  
**Cost**: FREE  
**Updates**: Automatic when you push

### Option B: Netlify
Steps in DEPLOYMENT.md:
1. Sign up at netlify.com
2. Connect GitHub repo
3. Configure build settings
4. Deploy!

**Time**: ~10 minutes  
**Cost**: FREE  
**Updates**: Automatic when you push

### Option C: University Server
Steps in DEPLOYMENT.md:
1. Contact your IT department
2. Get FTP/server access
3. Upload `_site/` folder
4. Get your URL

**Time**: ~30 minutes  
**Cost**: Usually FREE  
**Updates**: Manual FTP upload

---

## Testing Before Launch

Test the student experience:

1. **Download Vault**
   - [ ] Go to Resources page
   - [ ] Download Liaison_Vault.zip
   - [ ] Verify it downloads and extracts

2. **Follow Setup Guide**
   - [ ] Go to "Getting Started" page
   - [ ] Follow ALL steps yourself
   - [ ] Verify each step works
   - [ ] Note any issues

3. **Use Obsidian**
   - [ ] Open vault in Obsidian
   - [ ] Check all 6 folders exist
   - [ ] Verify templates are there
   - [ ] Create a test note
   - [ ] Verify 00_START_HERE.md is readable

4. **Test as a Student**
   - [ ] Open site in private/incognito browser
   - [ ] Try clicking all links
   - [ ] Try downloading the vault
   - [ ] Try following the setup guide
   - [ ] Pretend you're a new student

---

## Launch Sequence

### Week Before Launch
- [ ] Finalize all customizations
- [ ] Test everything thoroughly
- [ ] Fix any broken links
- [ ] Get feedback from a colleague

### Launch Day
- [ ] Run `quarto render` one final time
- [ ] Deploy (GitHub, Netlify, or server)
- [ ] Test the live URL
- [ ] Verify Vault downloads correctly

### After Launch
- [ ] Post URL to Blackboard
- [ ] Send announcement to students
- [ ] Monitor for questions/issues
- [ ] Update content as needed

---

## Keep It Fresh

Every time you update:

```bash
# 1. Make your changes to .qmd files in VS Code
# 2. Build the site
quarto render

# 3. If using GitHub:
git add .
git commit -m "Update course materials"
git push

# 4. If using Netlify:
# (Automatic! Just push to GitHub)

# 5. If using university server:
# Upload _site/ folder via FTP
```

---

## Troubleshooting Quick Links

**Website won't build:**
- Check `_quarto.yml` for syntax errors
- Run `quarto render` again
- See DEPLOYMENT.md

**Links are broken:**
- Check file paths in `.qmd` files
- Use relative paths: `setup.qmd`, `resources/Liaison_Vault.zip`
- Never use absolute paths

**Vault won't download:**
- Verify `resources/Liaison_Vault.zip` exists
- Check file permissions
- Try manually downloading from resources page

**Looks weird on mobile:**
- Quarto is responsive by default
- Clear browser cache
- Try different browser
- Check for custom CSS conflicts

---

## Key Deadlines (Example)

Set your own dates:

- [ ] **Week 1**: Customization complete, deployed
- [ ] **Week 2**: Module 1 content added
- [ ] **Week 3**: Module 2 content added
- [ ] **Week 4**: Module 3 content added
- [ ] **Week 5**: Module 4 content added
- [ ] **Week 6**: Module 5 content added

---

## Success Indicators

After launch, you'll know it's working when:

✅ Students access the website  
✅ Students download the Vault  
✅ Students complete setup  
✅ Students ask informed questions  
✅ Students use templates  
✅ Students progress through phases  

---

## Remember

This is YOUR site. Feel free to:
- Change colors/themes
- Add more content
- Create custom templates
- Link to external resources
- Update weekly
- Gather student feedback
- Iterate and improve

**Your students have access to a professional learning environment. Great job! 🎉**

---

**Quick Links to Guides:**
- **START_HERE.md** - Complete overview
- **README.md** - Full project guide  
- **DEPLOYMENT.md** - Deployment instructions
- **QUICK_START.md** - Visual reference
