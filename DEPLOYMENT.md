---
title: "Deployment Guide"
---

## Your Quarto Website is Ready!

Congratulations! Your student resource website has been successfully built. Here's how to deploy it for your students.

---

## What You Have

✅ **Quarto Website** - A fully functional, professional resource site  
✅ **Liaison Vault** - Pre-configured Obsidian vault for students  
✅ **Setup Instructions** - Step-by-step guide for students  
✅ **Built HTML** - Ready to deploy (in the `_site/` folder)

---

## Deployment Options

### Option 1: GitHub Pages (Recommended - FREE)

1. **Create a GitHub repository**
   - Go to [github.com](https://github.com) and create a new public repo named `quarto_website`

2. **Push your site**
   ```bash
   cd C:\mc451-sp26\quarto_website
   git init
   git add .
   git commit -m "Initial commit: Liaison Program website"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/quarto_website.git
   git push -u origin main
   ```

3. **Enable GitHub Pages**
   - Go to your repo Settings → Pages
   - Set Source to "Deploy from a branch"
   - Set Branch to `main` and folder to `_site`
   - Your site will be live at: `https://YOUR_USERNAME.github.io/quarto_website`

4. **Share the link in Blackboard**
   - Copy the GitHub Pages URL
   - Add it to your Blackboard course as a web link or announcement

### Option 2: Netlify (FREE, Easier Setup)

1. Go to [netlify.com](https://netlify.com) and sign up
2. Click "New site from Git" and connect your GitHub repo
3. Set Build Command to: `quarto render`
4. Set Publish Directory to: `_site`
5. Deploy automatically on every push

### Option 3: University Server/Portal

Contact your IT department about hosting the `_site/` folder on your institution's server.

---

## What Students See

When students visit your site, they'll find:

1. **Home page** - Welcome and quick-start buttons
2. **Setup instructions** - How to install and configure Obsidian
3. **Resources page** - Downloads (Liaison_Vault.zip and tools)
4. **Five phase modules** - Course content (01_orientation through 05_delivery)
5. **Sidebar navigation** - Easy access to all sections

---

## After Deployment

### Share with Students

Add this to your **Blackboard Course**:

```
📚 Course Resources
Welcome! Access all course materials here: [YOUR_WEBSITE_URL]

On this site you'll find:
✓ Your Liaison Obsidian Vault (download & setup)
✓ Step-by-step getting started guide
✓ All course modules and materials
✓ Weekly templates and tools

Start with the Setup page if this is your first time!
```

### Keep It Updated

After deployment, whenever you update content:

1. Edit your `.qmd` files in VS Code
2. Run `quarto render` to rebuild
3. Git commit and push to update the live site
   ```bash
   git add .
   git commit -m "Update course materials"
   git push
   ```

---

## Customization Tips

### Update Your Course Info
Edit `index.qmd` to add:
- Instructor name and contact info
- Meeting times and location
- Office hours

### Add More Content
Create new `.qmd` files in the `modules/` folder and add them to `_quarto.yml` sidebar

### Change the Theme
In `_quarto.yml`, change the theme from `cosmo` to:
- `darkly` - Dark theme
- `readable` - High contrast
- `lumen` - Light and clean
- `spacelab` - Modern

### Add Syllabus
Create `syllabus.qmd` (it's already referenced in the sidebar!)

---

## File Structure

```
quarto_website/
├── _quarto.yml          # Site config & navigation
├── index.qmd            # Home page
├── setup.qmd            # Getting started guide
├── syllabus.qmd         # Add your course syllabus here
├── build_vault.py       # Script that created your vault
├── resources/
│   ├── index.qmd        # Resources page
│   └── Liaison_Vault.zip # Student download
├── modules/             # Course content (5 phases)
├── slides/              # Presentation slides (optional)
├── assignments/         # Assignment details (optional)
└── _site/               # Built website (don't edit directly)
```

---

## Next Steps

1. **Add your syllabus** - Create/edit `syllabus.qmd`
2. **Customize home page** - Edit `index.qmd` with your details
3. **Add module content** - Fill in each phase (01-05) modules
4. **Deploy** - Choose Option 1, 2, or 3 above
5. **Share link** - Post in Blackboard for your students

---

**Questions or need help?** Let me know - I can help you customize this further!
