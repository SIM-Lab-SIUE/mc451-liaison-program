import os
import shutil
from pathlib import Path

def create_readme_file():
    """Create the 00_START_HERE.md file in the vault root."""
    
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
    """Create the Liaison_Vault directory structure."""
    
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
    """Create the Weekly_Journal_Template.md file in the 99_Templates folder."""
    
    vault_path = Path("Liaison_Vault")
    template_path = vault_path / "99_Templates" / "Weekly_Journal_Template.md"
    
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
    """Create the Data_Dictionary_Template.md file in the 99_Templates folder."""
    
    vault_path = Path("Liaison_Vault")
    template_path = vault_path / "99_Templates" / "Data_Dictionary_Template.md"
    
    content = """# Data Dictionary

| Variable Name | Conceptual Definition (The Dictionary) | Operational Definition (The Checklist) | Levels of Measurement |
| :--- | :--- | :--- | :--- |
| `frame_type` | The dominant angle of the story. | 1 = Economic, 2 = Conflict, 3 = Human Interest | Nominal |
| `tone` | The emotional feeling of the text. | Count of negative words vs positive words. | Ratio |
"""
    
    template_path.write_text(content, encoding='utf-8')


def zip_vault():
    """Zip the entire Liaison_Vault folder into Liaison_Vault.zip."""
    
    vault_path = Path("Liaison_Vault")
    output_path = "Liaison_Vault"
    
    # Create zip file
    shutil.make_archive(output_path, "zip", ".", "Liaison_Vault")
    
    print("Vault creation complete")


if __name__ == "__main__":
    create_vault_structure()
    create_readme_file()
    create_journal_template()
    create_data_dictionary_template()
    zip_vault()

