```markdown
# ⚡ ERROR VOID CODER

### The First Vibe Coding Tool from Kashmir

![Version](https://img.shields.io/badge/version-2.0-brightgreen)
![Beta](https://img.shields.io/badge/beta-testing-orange)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.7+-blue)

## 🎯 What is Error Void Coder?

Error Void Coder is a **CLI-based vibe coding tool** that lets you create complete projects just by describing what you want. Just type your idea, and the AI writes all the code for you.

**Create. Edit. Delete. All with AI.**

---

## ✨ Features

- 🚀 **Create Projects** - Enter name + description, AI creates all files
- ✏️ **Edit Projects** - Modify, add, or delete files with simple commands
- 🤖 **Multiple AI Providers** - Built-in AI (free), Groq API, OpenRouter API
- 📁 **Auto File Management** - Creates folders and files automatically
- 💾 **Plan Saving** - Every project has a plan.txt file
- 🖥️ **100% CLI** - Works entirely in terminal

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ERROR0101r/Error-void-coder.git
cd Error-void-coder
```

2. Install Requirements

```bash
pip install -r requirements.txt
```

3. Run the Tool

```bash
python app.py
```

---

📋 requirements.txt

```
requests
python-dotenv
```

---

🚀 How to Use

Create New Project

```
1. Select "Create New Project"
2. Enter project name (e.g., "mycalculator")
3. Describe what you want (e.g., "calculator in python")
4. AI generates plan and writes all code files
5. Done! Files are created in project folder
```

Edit Existing Project

```
1. Select "Edit Existing Project"
2. Choose project from list
3. Select edit type (1-6):
   - Add new files
   - Modify existing files
   - Delete files
   - Combine multiple files
   - Split one file into multiple
   - Custom edit
4. Describe changes
5. AI updates the files automatically
```

Change AI Provider

```
1. Select "Change AI Provider"
2. Choose from:
   - Built-in AI (Free)
   - Groq API
   - OpenRouter API
3. Enter API key (if needed)
4. Select model
```

---

🔧 AI Providers Setup

Built-in AI (Default - Free)

· No API key needed
· Works immediately

Groq API

· Get key: https://console.groq.com
· Models: Llama 3.3 70B, Mixtral 8x7B, Gemma 2 9B, Llama 3.1 8B

OpenRouter API

· Get key: https://openrouter.ai/keys
· Models: GPT-4o, Claude 3.5 Sonnet, Gemini 2.0 Flash, Llama 3.3 70B, DeepSeek, Mistral 7B

---

📁 Project Structure

After creating a project:

```
your-project/
├── plan.txt          # Contains project plan
├── main.py           # Your main code file
└── other files...    # All files AI created
```

Example:

```
calculator/
├── plan.txt
├── calculator.py
├── operations.py
└── utils.py
```

---

💡 Example Usage

Create a calculator:

```
📁 Enter project name: mycalc
💡 What do you want to create?
> calculator in python with add, subtract, multiply, divide
```

AI creates:

```
✓ calculator.py
✓ operations.py
✓ utils.py
✅ Project complete! 3 files created
```

Edit it:

```
📝 Describe changes: add square root function
✅ Edit complete! Modified: 1 file
```

---

🎮 Main Menu Options

```
1. 🚀 Create New Project
2. ✏️ Edit Existing Project
3. 🔧 Change AI Provider
4. 🚪 Exit
```

Edit Options (When Editing)

```
1. Add new files
2. Modify existing files
3. Delete files
4. Combine multiple files into one
5. Split one file into multiple
6. Custom edit (AI decides)
```

---

🐛 Report Bugs

This is a beta version. Found a bug? Report here:

· Telegram: @ERROR0101risback
· Instagram: @fahad0101r

---

⚠️ Beta Notice

This is the first version of Error Void Coder from Kashmir. Some features may have bugs. Please report any issues you find!

---

📝 Example Prompts

```
calculator in python
flask blog with 3 pages
todo list app
weather api client
password generator
file organizer script
web scraper for quotes
```

---

🔄 How It Works

1. You describe what you want
2. AI creates a plan (files, structure, dependencies)
3. Plan saved to plan.txt
4. AI writes complete code for all files
5. Files are saved to project folder
6. You can edit anytime with new prompts

---

🤝 Contributing

Open source! Feel free to:

· Fork the repo
· Create pull requests
· Report issues
· Suggest features

---

📄 License

MIT License - Free for everyone

---

🌟 Star This Repo

If you like this tool, please star it on GitHub!

---

Made with ❤️ in Kashmir

GitHub Repo | Report Bug

```

---

## requirements.txt

```txt
requests
python-dotenv
```

---

Run Commands

```bash
# Install
pip install -r requirements.txt

# Run
python app.py
```