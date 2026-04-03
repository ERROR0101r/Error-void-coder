
# ⚡ ERROR VOID CODER

### The First Vibe Coding Tool from Kashmir

<div align="center">
  <img src="https://img.shields.io/badge/Vibe-Coding-brightgreen?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge&logo=openai">
  <img src="https://img.shields.io/badge/CLI-Tool-orange?style=for-the-badge&logo=terminal">
  
  [![Telegram](https://img.shields.io/badge/Telegram-@ERROR0101risback-26A5E4?style=for-the-badge&logo=telegram)](https://t.me/ERROR0101risback)
  [![Instagram](https://img.shields.io/badge/Instagram-@fahad0101r-E4405F?style=for-the-badge&logo=instagram)](https://instagram.com/fahad0101r)
  [![GitHub](https://img.shields.io/badge/GitHub-ERROR0101r-181717?style=for-the-badge&logo=github)](https://github.com/ERROR0101r)
  
  <p><strong>Developer: @ERROR0101risback</strong></p>
  <p><em>Version: 2.0 (Beta)</em></p>
</div>

---

## 📋 TABLE OF CONTENTS
- [What is Error Void Coder?](#what-is-error-void-coder)
- [Important – Beta Version](#important--beta-version)
- [Features](#features)
- [Quick Setup](#quick-setup)
- [Usage Guide](#usage-guide)
- [Installation Details](#installation-details)
- [Step by Step Tutorial](#step-by-step-tutorial)
- [Report Bugs](#report-bugs)
- [Developer Contact](#developer-contact)
- [Repository](#repository)
- [License](#license)

---

## WHAT IS ERROR VOID CODER?

**Error Void Coder** is a CLI-based vibe coding tool that lets you create complete projects just by describing what you want. Just type your idea, and the AI writes all the code for you.

**Create. Edit. Delete. All with AI.**

| Feature | Description |
|---------|-------------|
| **Create Projects** | Enter name + description, AI creates all files |
| **Edit Projects** | Modify, add, or delete files with simple commands |
| **Multiple AI Providers** | Built-in AI (free), Groq API, OpenRouter API |
| **Auto File Management** | Creates folders and files automatically |
| **Plan Saving** | Every project has a plan.txt file |
| **100% CLI** | Works entirely in terminal |

---

## IMPORTANT – BETA VERSION

```

THIS IS THE FIRST VERSION OF ERROR VOID CODER FROM KASHMIR.

This is a beta version. Some features may have bugs.

By using this tool, you agree to:

· Report any bugs you find
· Understand that this is version 2.0 (Beta)
· Expect possible issues or errors

The author (@ERROR0101risback) is working to improve this tool.

If you find any bugs, please report them using the contact info below.

```

---

## FEATURES

| Feature | Description |
|---------|-------------|
| **AI Project Creation** | Describe what you want, AI writes all code |
| **Smart File Management** | Automatically creates folders and files |
| **Multiple AI Providers** | Built-in (free), Groq, or OpenRouter |
| **Edit Existing Projects** | Add, modify, or delete files with simple commands |
| **Plan.txt Saving** | Every project has a detailed plan file |
| **No API Key Needed** | Built-in AI works immediately |

---

## QUICK SETUP

### One Command Setup:
```bash
git clone https://github.com/ERROR0101r/Error-void-coder.git
cd Error-void-coder
pip install -r requirements.txt
python app.py
```

Termux (Android):

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/ERROR0101r/Error-void-coder.git
cd Error-void-coder
pip install -r requirements.txt
python app.py
```

Linux (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install python3 python3-pip git
git clone https://github.com/ERROR0101r/Error-void-coder.git
cd Error-void-coder
pip3 install -r requirements.txt
python3 app.py
```

Windows:

```bash
git clone https://github.com/ERROR0101r/Error-void-coder.git
cd Error-void-coder
pip install -r requirements.txt
python app.py
```

---

USAGE GUIDE

Run the Tool:

```bash
python app.py
```

Step 1: Main Menu

```
1. 🚀 Create New Project
2. ✏️ Edit Existing Project
3. 🔧 Change AI Provider
4. 🚪 Exit
Select (1-4): 1
```

Step 2: Create New Project

```
📁 Enter project name: mycalculator
💡 What do you want to create?
> calculator in python with add, subtract, multiply, divide
```

Step 3: View Results

```
✓ calculator.py created
✓ operations.py created
✓ utils.py created
✅ Project complete! 3 files created
```

Step 4: Edit Existing Project

```
Select "Edit Existing Project"
Choose project from list
Select edit type (1-6):
   1. Add new files
   2. Modify existing files
   3. Delete files
   4. Combine multiple files
   5. Split one file into multiple
   6. Custom edit
📝 Describe changes: add square root function
✅ Edit complete! Modified: 1 file
```

---

AI PROVIDERS SETUP

Provider Setup Models
Built-in AI No API key needed, works immediately Free
Groq API Get key from console.groq.com Llama 3.3, Mixtral, Gemma
OpenRouter API Get key from openrouter.ai/keys GPT-4o, Claude 3.5, Gemini

---

INSTALLATION DETAILS

Requirements:

· Python 3.7 or higher
· requests library
· python-dotenv library

File Structure:

```
Error-void-coder/
├── app.py           # Main tool
├── requirements.txt # Dependencies
├── config.json      # Config (auto-generated)
├── projects/        # All projects folder
└── README.md        # Documentation
```

Project Structure:

```
your-project/
├── plan.txt         # Contains project plan
├── main.py          # Your main code file
└── other files...   # All files AI created
```

---

STEP BY STEP TUTORIAL

Creating Your First Project:

1. Run python app.py
2. Select option 1 (Create New Project)
3. Enter project name (e.g., "myapp")
4. Describe what you want (e.g., "todo list app in python")
5. Wait for AI to generate code
6. Check your project folder

Editing a Project:

1. Run python app.py
2. Select option 2 (Edit Existing Project)
3. Choose project from list
4. Select edit type (1-6)
5. Describe what changes you want
6. AI updates the files

Example Flow:

```
$ python app.py

============================================================
⚡ ERROR VOID CODER v2.0 (Beta)
============================================================

1. 🚀 Create New Project
2. ✏️ Edit Existing Project
3. 🔧 Change AI Provider
4. 🚪 Exit

Select (1-4): 1

📁 Enter project name: mycalc
💡 What do you want to create?
> calculator in python with add, subtract, multiply, divide

[+] AI is creating your project...

✓ calculator.py
✓ operations.py
✓ utils.py

✅ Project complete! 3 files created

============================================================
SCAN COMPLETE
============================================================
Project Name: mycalc
Files Created: 3
Location: projects/mycalc/
============================================================
```

---

REPORT BUGS

```

This is a BETA version (First version from Kashmir).

If you find any bug, issue, or problem:

· Contact the developer directly
· Provide details about the bug
· Mention what you were trying to do

Your reports help improve the tool!

```

---

DEVELOPER CONTACT

<div align="center">
  <p><strong>Name:</strong> ERROR0101risback / Fahad</p>
  <p>
    <a href="https://t.me/ERROR0101risback">Telegram</a> •
    <a href="https://instagram.com/fahad0101r">Instagram</a> •
    <a href="https://github.com/ERROR0101r">GitHub</a>
  </p>
</div>

---

REPOSITORY

· GitHub: https://github.com/ERROR0101r/Error-void-coder
· Download ZIP: https://github.com/ERROR0101r/Error-void-coder/archive/refs/heads/main.zip

---

LICENSE

```
This project is for educational purposes only.
First version from Kashmir - Beta release.

You are free to:
- Use for personal projects
- Modify for personal use
- Report bugs and suggest features

You are NOT permitted to:
- Sell this tool
- Claim as your own
- Use for malicious purposes
```

---

<div align="center">
  <h3>⚡ Create. Edit. Delete. All with AI. ⚡</h3>
  <p><i>Made with ❤️ in Kashmir by @ERROR0101risback</i></p>

  <p>
    <a href="https://t.me/ERROR0101risback"><img src="https://img.shields.io/badge/Telegram-@ERROR0101risback-26A5E4?style=flat-square&logo=telegram"></a>
    <a href="https://instagram.com/fahad0101r"><img src="https://img.shields.io/badge/Instagram-@fahad0101r-E4405F?style=flat-square&logo=instagram"></a>
    <a href="https://github.com/ERROR0101r"><img src="https://img.shields.io/badge/GitHub-ERROR0101r-181717?style=flat-square&logo=github"></a>
  </p>

  <p>© 2026 Error Void Coder | Version 2.0 Beta</p>
</div>