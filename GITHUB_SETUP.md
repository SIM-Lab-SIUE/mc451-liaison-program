# GitHub Deployment Instructions

## Step 1: Create the Repository on GitHub

1. Go to https://github.com/SIM-Lab-SIUE
2. Click the **"New"** button (or go to https://github.com/organizations/SIM-Lab-SIUE/repositories/new)
3. Fill in the repository details:
   - **Repository name**: `mc451-liaison-program` (or your preferred name)
   - **Description**: `Liaison Program course website with Obsidian vault for students`
   - **Visibility**: Choose **Public** (so GitHub Pages works for free)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
4. Click **"Create repository"**

## Step 2: Push Your Code

Once you create the repository, GitHub will show you commands. Use these:

```bash
git remote add origin https://github.com/SIM-Lab-SIUE/mc451-liaison-program.git
git push -u origin main
```

**OR run this command in your terminal:**

```powershell
cd C:\mc451-sp26\quarto_website
git remote add origin https://github.com/SIM-Lab-SIUE/mc451-liaison-program.git
git push -u origin main
```

## Step 3: Enable GitHub Pages

After pushing:

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (in the left sidebar)
3. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/_site`
4. Click **Save**

GitHub will build your site. Wait 2-3 minutes, then your site will be live at:
```
https://sim-lab-siue.github.io/mc451-liaison-program/
```

## Step 4: Share with Students

Copy your GitHub Pages URL and post it in Blackboard:

```
📚 Course Website
Access all Liaison Program materials here:
https://sim-lab-siue.github.io/mc451-liaison-program/

You'll find:
✓ Getting started guide
✓ Liaison Obsidian Vault download
✓ All course modules and materials
✓ Weekly templates and resources

Start with the "Get Started" page!
```

## Updating Your Site Later

Whenever you make changes:

```bash
cd C:\mc451-sp26\quarto_website
quarto render
git add .
git commit -m "Update course materials"
git push
```

GitHub Pages will automatically rebuild in 2-3 minutes.

---

## Repository Name Suggestions

If `mc451-liaison-program` is taken, try:
- `liaison-program-website`
- `mc451-sp26`
- `communication-liaison-course`
- `liaison-research-methods`

---

## Troubleshooting

**Q: GitHub Pages shows 404**
- Make sure you selected `/_site` folder (not root)
- Wait 3-5 minutes for the first build
- Check Settings → Pages for build status

**Q: Push failed - authentication error**
- You may need to set up a Personal Access Token
- Go to GitHub Settings → Developer settings → Personal access tokens
- Create token with `repo` scope
- Use token as password when pushing

**Q: Resource files (Liaison_Vault.zip) not showing**
- The .gitignore should NOT exclude resources/
- Check that resources/Liaison_Vault.zip was committed
- Run: `git ls-files resources/` to verify

---

**Ready to go! Create the repository on GitHub, then run the push commands above.** 🚀
