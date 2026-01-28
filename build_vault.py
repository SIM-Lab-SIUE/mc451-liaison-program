"""
Liaison Program Vault Builder

This script generates the Liaison_Vault folder structure and templates for students.
The vault is a pre-configured Obsidian workspace for organizing research.

Functions:
    create_vault_structure() - Creates folders and .gitkeep files
    create_readme_file() - Creates vault orientation file
    create_journal_template() - Creates weekly reflection template
    create_data_dictionary_template() - Creates data definition template
    zip_vault() - Zips vault for student distribution

Usage:
    python build_vault.py

Output:
    - Liaison_Vault/ folder (student workspace)
    - Liaison_Vault.zip (for download distribution)
    - resources/Liaison_Vault.zip (for website deployment)
"""

import os
import shutil
from pathlib import Path

def create_readme_file():
    """
    Create the 00_START_HERE.md file in the vault root.
    
    This file is the first thing students see when opening their vault.
    It explains the folder structure and provides initial setup instructions.
    
    Location: Liaison_Vault/00_START_HERE.md
    """
    
    vault_path = Path("Liaison_Vault")
    readme_path = vault_path / "00_START_HERE.md"
    
    content = """# Welcome to your Digital Office

* **00_Inbox**: Quick notes and rough thoughts.
* **01_Journal**: Your weekly field notes.
* **02_Literature**: Notes from Zotero and readings.
* **03_Project**: Your active research work.
* **99_Templates**: Copy these files to start your assignments.

## Task 1: Configure Obsidian Settings

Go to Settings > Files & Links > Default location for new attachments → set to '04_Resources'.
"""
    
    readme_path.write_text(content, encoding='utf-8')


def create_vault_structure():
    """
    Create the Liaison_Vault directory structure.
    
    This creates the folder hierarchy that students will use for organizing their research:
    - 00_Inbox: Quick capture for daily thoughts
    - 01_Journal: Weekly reflection entries
    - 02_Literature: Research notes from readings
    - 03_Project: Active research work (with 4 subfolders)
    - 04_Resources: Attachments, images, PDFs
    - 99_Templates: Reusable templates for assignments
    
    Each folder includes a .gitkeep file so empty folders are tracked by Git.
    
    Location: Creates Liaison_Vault/ at project root
    """
    
    # Define the base vault path
    vault_path = Path("Liaison_Vault")
    
    # Define the main folders
    main_folders = [
        "00_Inbox",
        "01_Journal",
        "02_Literature",
        "03_Project",
        "04_Resources",
        "99_Templates"
    ]
    
    # Define subfolders within 03_Project
    project_subfolders = [
        "01_Prospectus",
        "02_Codebook",
        "03_Data",
        "04_Drafts"
    ]
    
    # Create main folders and .gitkeep files
    for folder in main_folders:
        folder_path = vault_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # Create .gitkeep file
        gitkeep_path = folder_path / ".gitkeep"
        gitkeep_path.touch()
    
    # Create subfolders within 03_Project and their .gitkeep files
    project_path = vault_path / "03_Project"
    for subfolder in project_subfolders:
        subfolder_path = project_path / subfolder
        subfolder_path.mkdir(parents=True, exist_ok=True)
        
        # Create .gitkeep file
        gitkeep_path = subfolder_path / ".gitkeep"
        gitkeep_path.touch()
    
    print("Vault structure created successfully!")


def create_journal_template():
    """
    Create the Weekly_Journal_Template.md file in the 99_Templates folder.
    
    This template guides students in weekly reflection using three thinking paths:
    1. The Connector - Relating theory to their project
    2. The Troubleshooter - Problem-solving and fixes
    3. The Critic - Evaluating claims against experience
    
    Students copy this template to 01_Journal/ and fill it in each week.
    
    Location: Liaison_Vault/99_Templates/Weekly_Journal_Template.md
    Note: Only creates if file doesn't exist (doesn't overwrite custom versions)
    """
    
    vault_path = Path("Liaison_Vault")
    template_path = vault_path / "99_Templates" / "Weekly_Journal_Template.md"
    
    # Only create if it doesn't exist - don't overwrite manually edited versions
    if not template_path.exists():
        content = """# Week X: [Title Here]

**Date:** [Insert Date]
**Reading:** [Insert Chapter]

## The Reflection

*(Choose one path below and delete the others)*

### Path 1: The Connector

*How does this week's theory specifically apply to the project I am building?*

### Path 2: The Troubleshooter

*What went wrong in the Lab this week, and exactly how did I fix it?*

### Path 3: The Critic

*The author claims X, but does that hold true in my experience/modern media?*

---

**Tags:** #journal #weekX
"""
        
        template_path.write_text(content, encoding='utf-8')


def create_data_dictionary_template():
    """
    Create the Data_Dictionary_Template.md file in the 99_Templates folder.
    
    This template helps students document their data codebook with:
    - Variable names (database column names)
    - Conceptual definitions (what the variable means theoretically)
    - Operational definitions (how it's measured/coded)
    - Measurement levels (nominal, ordinal, interval, ratio)
    
    Students use this when analyzing datasets and creating their codebook.
    
    Location: Liaison_Vault/99_Templates/Data_Dictionary_Template.md
    Note: Only creates if file doesn't exist (doesn't overwrite custom versions)
    """
    
    vault_path = Path("Liaison_Vault")
    template_path = vault_path / "99_Templates" / "Data_Dictionary_Template.md"
    
    # Only create if it doesn't exist - don't overwrite manually edited versions
    if not template_path.exists():
        content = """# Data Dictionary

| Variable Name | Conceptual Definition (The Dictionary) | Operational Definition (The Checklist) | Levels of Measurement |
| :--- | :--- | :--- | :--- |
| `frame_type` | The dominant angle of the story. | 1 = Economic, 2 = Conflict, 3 = Human Interest | Nominal |
| `tone` | The emotional feeling of the text. | Count of negative words vs positive words. | Ratio |
"""
        
        template_path.write_text(content, encoding='utf-8')


def zip_vault():
    """
    Zip the entire Liaison_Vault folder into Liaison_Vault.zip.
    
    This creates a compressed archive that students can easily download from the
    Resources page of the website. When they extract it, they get the full vault
    structure ready to configure in Obsidian.
    
    The zip is created at the project root and then copied to:
    - resources/Liaison_Vault.zip (for website deployment)
    
    This allows GitHub Pages to serve the download to students.
    
    Outputs:
    - Liaison_Vault.zip (15-25 KB compressed)
    - resources/Liaison_Vault.zip (copy for website deployment)
    """
    
    vault_path = Path("Liaison_Vault")
    output_path = "Liaison_Vault"
    
    # Create zip file - zip the contents directly without the outer folder
    shutil.make_archive(output_path, "zip", vault_path)
    
    # Copy to resources folder for website deployment
    resources_path = Path("resources") / "Liaison_Vault.zip"
    shutil.copy2("Liaison_Vault.zip", resources_path)
    
    print("Vault creation complete")
    print(f"ZIP copied to {resources_path}")


if __name__ == "__main__":
    create_vault_structure()
    create_readme_file()
    create_journal_template()
    create_data_dictionary_template()
    zip_vault()

