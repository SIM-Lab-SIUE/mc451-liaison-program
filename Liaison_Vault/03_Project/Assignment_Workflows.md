# Assignment Workflow Guide

This guide shows exactly where each assignment goes and how to use Obsidian ↔ RStudio effectively.

## 📋 Early Phase Assignments (Obsidian Primary)

| Assignment | Folder | Tool Workflow | Output | Due | Points |
|------------|--------|---------------|--------|-----|--------|
| **Topic Selection & RQs** | `01_Prospectus/` | Obsidian only | Text submission to Blackboard | - | 25 |
| **Definitions Practice** | `02_Codebook/` | Obsidian only | Markdown table screenshot | - | 25 |
| **Archivist Report** | `01_Prospectus/` | Obsidian draft → RStudio render | PDF: `Lastname_ArchivistReport.pdf` | - | 25 |
| **Annotated Manuscript** | `../02_Literature/` | Zotero annotate → Export PDF | PDF: `Lastname_AnnotatedManuscript.pdf` | Feb 13, 2026 | 25 |

## 📊 Analysis Phase Assignments (RStudio Primary)

| Assignment | Folder | Tool Workflow | Output | Due | Points |
|------------|--------|---------------|--------|-----|--------|
| **Project Prospectus** | `01_Prospectus/` | Obsidian draft → RStudio render | PDF: `Lastname_ProjectProspectus.pdf` | Feb 20, 2026 | 25 |
| **Codebook & Qual Memo** | `02_Codebook/` | Obsidian draft → RStudio render | PDF: `Lastname_Codebook.pdf` | - | 50 |
| **Sampling Plan & Pilot** | `02_Codebook/` | Obsidian draft → RStudio render | PDF | - | 75 |
| **Data Wrangling [R]** | `03_Data/` | RStudio only | RDS file | - | 50 |
| **Describing Data [R]** | `03_Data/` | RStudio only | PDF with charts | - | 75 |
| **Inferencing Data [R]** | `03_Data/` | RStudio only | PDF with stats | - | 100 |

## 🎨 Final Phase Assignments (RStudio + GitHub)

| Assignment | Folder | Tool Workflow | Output | Due | Points |
|------------|--------|---------------|--------|-----|--------|
| **Professional Web Portfolio** | `04_Drafts/` | RStudio render + publish | PDF + live website | - | 250 |

## Step-by-Step Workflow for Quarto Assignments

### Phase 1: Draft in Obsidian
1. Create new `.qmd` file in appropriate folder
2. Write content using Markdown
3. Add code chunks for R analysis (if needed)
4. Save and preview in Obsidian

### Phase 2: Move to RStudio
1. Copy `.qmd` file to your R project folder
2. Open in RStudio
3. Install any required R packages
4. Run code chunks to test

### Phase 3: Render & Polish
1. Click "Render" button in RStudio
2. Check PDF output for formatting
3. Fix any errors or formatting issues
4. Re-render as needed

### Phase 4: Submit
1. Rename file with your last name
2. Upload PDF to Blackboard
3. For final portfolio: publish to GitHub Pages

## File Naming Convention

- **PDFs**: `Lastname_AssignmentName.pdf`
- **R Scripts**: `01_import.R`, `02_clean.R`, etc.
- **Data Files**: `raw_data.csv`, `clean_data.RDS`
- **Quarto Files**: `assignment_draft.qmd`, `assignment_final.qmd`

## Common Issues & Solutions

### "My Quarto file won't render!"
- Check that all R packages are installed
- Verify file paths are correct
- Make sure you're in the right working directory

### "Images don't show in PDF!"
- Use relative paths: `images/chart.png`
- Or embed with `![](images/chart.png)`

### "R code runs in RStudio but not when rendering!"
- Set working directory in Quarto YAML
- Use `here::here()` for file paths

### "My vault is getting too big!"
- Move large data files to R project folder
- Use Git LFS for big files
- Store raw data externally

## Pro Tips

- **Start assignments early** - Draft in Obsidian first
- **Version control** - Keep `v1.qmd`, `v2.qmd`, etc.
- **Test rendering frequently** - Don't wait until deadline
- **Link between tools** - Reference Obsidian notes in RStudio
- **Backup everything** - Use GitHub for version control

---

**Remember**: Obsidian for thinking/writing, RStudio for analysis/rendering. This workflow will make your research process smooth and professional.