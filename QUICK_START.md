# Quick Reference Guide

## Your Complete Student Resource Website

Built with Quarto, featuring the Liaison Obsidian Vault for student success.

---

## 📊 What's Included

### Website Pages
```
Home Page (index.qmd)
├── Getting Started (setup.qmd)
├── Resources & Downloads (resources/index.qmd)
│   ├── Liaison_Vault.zip ⬇️
│   └── 05_Textbook.zip (optional) ⬇️
├── Phase 1: Orientation (modules/01_orientation/)
├── Phase 2: Discovery (modules/02_discovery/)
├── Phase 3: Dictionary (modules/03_dictionary/)
├── Phase 4: Execution (modules/04_execution/)
└── Phase 5: Delivery (modules/05_delivery/)
```

### Liaison Obsidian Vault
```
Liaison_Vault/
├── 00_Inbox/          (Quick capture)
├── 01_Journal/        (Weekly reflections)
├── 02_Literature/     (Research notes)
├── 03_Project/        (Active work)
│   ├── 01_Prospectus/
│   ├── 02_Codebook/
│   ├── 03_Data/
│   └── 04_Drafts/
├── 04_Resources/      (Media & attachments)
├── 99_Templates/      (Reusable templates)
└── 00_START_HERE.md   (Student orientation)
```

---

## 🚀 Three Ways to Deploy

### 1. GitHub Pages (⭐ Recommended)
- **Cost**: FREE
- **Setup**: 15 minutes
- **URL Pattern**: `https://yourname.github.io/quarto_website`
- **Best for**: Easy updates, automatic deployment

### 2. Netlify
- **Cost**: FREE
- **Setup**: 10 minutes
- **Best for**: Even easier, fancy features

### 3. University Server
- **Cost**: Usually FREE (already hosted)
- **Setup**: Contact IT
- **Best for**: Keeping everything institutional

See DEPLOYMENT.md for detailed instructions.

---

## 📋 Setup Checklist

- [ ] **Customize home page** - Add your name, meeting time, office hours
- [ ] **Create syllabus** - Fill in `syllabus.qmd`
- [ ] **Add module content** - Fill in each Phase (1-5)
- [ ] **Pick deployment** - GitHub, Netlify, or University server
- [ ] **Deploy** - Follow your chosen method
- [ ] **Test as student** - Download vault and follow setup guide
- [ ] **Post to Blackboard** - Share the URL
- [ ] **Share with students** - Done! ✅

---

## 🔄 Keep It Updated

After deployment, making changes is easy:

1. **Edit** `.qmd` files in VS Code
2. **Build** by running `quarto render`
3. **Push** to GitHub with git (if using GitHub Pages)
4. **Done** - Live updates automatically!

```bash
# Standard update workflow
quarto render
git add .
git commit -m "Update course materials"
git push
```

---

## 💡 Content Tips

### For Students New to Obsidian
- Make the Getting Started page prominent
- Include screenshots in setup.qmd
- Link to Obsidian help resources
- Create a "Common Issues" section

### For Each Module (1-5)
- Start with learning objectives
- Include readings, videos, and activities
- Add reflection prompts
- Link to templates in the vault
- Include due dates and deadlines

### For Resources Page
- List all required software with download links
- Provide quick reference guides
- Link to external tools (Zotero, GitHub, etc.)
- Create a FAQ section

---

## 📚 Example Module Structure

Each Phase module should include:

```markdown
# Phase X: [Title]

## Learning Objectives
- Objective 1
- Objective 2
- Objective 3

## Key Concepts
- Concept A: explanation
- Concept B: explanation

## Activities
1. Activity name
   - Step 1
   - Step 2
   - Due date

## Resources
- Reading 1
- Video 1
- Template link

## Reflection Prompt
[Use the three thinking paths]
```

---

## 🎨 Customization Options

### Change the Theme
Edit `_quarto.yml`:
```yaml
format:
  html:
    theme: cosmo  # Try: darkly, lumen, readable, spacelab
```

### Add More Pages
1. Create new `file.qmd`
2. Add to `_quarto.yml` sidebar
3. Run `quarto render`
4. Redeploy!

### Add Your Logo
Place image in `images/` folder and reference in setup.

---

## ✅ Student Experience

When students visit your site:

1. **Land on home page** → See course overview
2. **Click "Get Started"** → View step-by-step setup
3. **Go to Resources** → Download Liaison_Vault.zip
4. **Follow setup guide** → Install Obsidian & vault
5. **Enter Phase 1** → Begin course content
6. **Use templates** → Weekly journals, data dictionaries
7. **Learn through 5 phases** → Complete program
8. **Succeed!** → Ready for future careers

---

## 📞 Support

- **Quarto help**: https://quarto.org/docs
- **Obsidian tutorials**: https://obsidian.md/
- **GitHub Pages**: https://pages.github.com/
- **Your students**: Use Blackboard announcements

---

## 🎉 You're Ready!

Your professional student resource website is built, tested, and ready to deploy. 

**Next step**: Pick your deployment option and share with your students.

See README.md and DEPLOYMENT.md for detailed guidance.

---

**Questions?** Check the detailed guides or customize to fit your needs.

## Textbook Website

For more information, visit the textbook's official website: [Vibes to Variables](https://sim-lab-siue.github.io/vibes-to-variables/)
