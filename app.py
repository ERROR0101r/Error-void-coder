import os
import re
import json
import requests
import sys
import shutil
from datetime import datetime

CONFIG_FILE = "error_void_config.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"provider": None, "api_key": None, "model": None}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def call_ai_api(message, config):
    if config.get("provider") == "groq":
        return call_groq_api(message, config)
    elif config.get("provider") == "openrouter":
        return call_openrouter_api(message, config)
    else:
        return call_builtin_api(message)

def call_builtin_api(message):
    try:
        url = "https://livegemini.fastdevelopers.workers.dev/chat"
        params = {"message": message}
        response = requests.get(url, params=params, timeout=120)
        data = response.json()
        if data.get("status"):
            return data.get("response", "")
        return ""
    except Exception as e:
        print(f"Built-in AI error: {e}")
        return ""

def call_groq_api(message, config):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": config['model'],
            "messages": [{"role": "user", "content": message}],
            "temperature": 0.7,
            "max_tokens": 8000
        }
        response = requests.post(url, json=payload, headers=headers, timeout=120)
        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "")
    except Exception as e:
        print(f"Groq API error: {e}")
        return ""

def call_openrouter_api(message, config):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": config['model'],
            "messages": [{"role": "user", "content": message}],
            "temperature": 0.7,
            "max_tokens": 8000
        }
        response = requests.post(url, json=payload, headers=headers, timeout=120)
        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "")
    except Exception as e:
        print(f"OpenRouter API error: {e}")
        return ""

def setup_ai_provider(first_time=False):
    config = load_config()
    
    if config.get("provider") and not first_time:
        provider_name = config['provider'].upper()
        model_name = config['model']
        print(f"\n✓ Current AI: {provider_name} | Model: {model_name}")
        change = input("\nChange AI provider? (y/n): ").strip().lower()
        if change != 'y':
            return config
    
    clear_screen()
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + " "*15 + "ERROR VOID CODER" + " "*27 + "█")
    print("█" + " "*58 + "█")
    print("█"*60)
    
    print("\n" + "="*50)
    print("        AI PROVIDER SETUP")
    print("="*50)
    print("\nSelect AI Provider:")
    print("  1. Built-in AI (Free, no key required)")
    print("  2. Groq API (Fast, needs API key)")
    print("  3. OpenRouter API (Many models, needs API key)")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        config["provider"] = "builtin"
        config["api_key"] = None
        config["model"] = "builtin-gemini"
        save_config(config)
        print("\n✓ Built-in AI configured successfully!")
        
    elif choice == "2":
        print("\n" + "-"*40)
        print("GROQ API SETUP")
        print("-"*40)
        print("Get your API key from: https://console.groq.com")
        api_key = input("\nEnter your Groq API Key: ").strip()
        if not api_key:
            print("No API key provided, falling back to built-in AI")
            config["provider"] = "builtin"
            config["api_key"] = None
            config["model"] = "builtin-gemini"
        else:
            print("\nAvailable Groq Models:")
            print("  1. llama-3.3-70b-versatile (Best quality, 70B)")
            print("  2. mixtral-8x7b-32768 (Good balance, 47B)")
            print("  3. gemma2-9b-it (Fastest, 9B)")
            print("  4. llama-3.1-8b-instant (Lightweight, 8B)")
            
            model_choice = input("\nSelect model (1-4): ").strip()
            models = {
                "1": "llama-3.3-70b-versatile",
                "2": "mixtral-8x7b-32768",
                "3": "gemma2-9b-it",
                "4": "llama-3.1-8b-instant"
            }
            config["provider"] = "groq"
            config["api_key"] = api_key
            config["model"] = models.get(model_choice, "llama-3.3-70b-versatile")
            save_config(config)
            print(f"\n✓ Groq configured successfully with model: {config['model']}")
            
    elif choice == "3":
        print("\n" + "-"*40)
        print("OPENROUTER API SETUP")
        print("-"*40)
        print("Get your API key from: https://openrouter.ai/keys")
        api_key = input("\nEnter your OpenRouter API Key: ").strip()
        if not api_key:
            print("No API key provided, falling back to built-in AI")
            config["provider"] = "builtin"
            config["api_key"] = None
            config["model"] = "builtin-gemini"
        else:
            print("\nAvailable OpenRouter Models:")
            print("  1. openai/gpt-4o (Best quality, $5/M tokens)")
            print("  2. anthropic/claude-3.5-sonnet (Excellent coding, $3/M)")
            print("  3. google/gemini-2.0-flash-exp (Fast & good, $0.10/M)")
            print("  4. meta-llama/llama-3.3-70b-instruct (Open source, $0.59/M)")
            print("  5. mistralai/mistral-7b-instruct (Lightweight, $0.07/M)")
            print("  6. deepseek/deepseek-chat (Great for code, $0.14/M)")
            print("  7. Custom model ID")
            
            model_choice = input("\nSelect model (1-7): ").strip()
            models = {
                "1": "openai/gpt-4o",
                "2": "anthropic/claude-3.5-sonnet",
                "3": "google/gemini-2.0-flash-exp",
                "4": "meta-llama/llama-3.3-70b-instruct",
                "5": "mistralai/mistral-7b-instruct",
                "6": "deepseek/deepseek-chat"
            }
            
            if model_choice == "7":
                custom_model = input("Enter model ID (e.g., openai/gpt-4): ").strip()
                config["model"] = custom_model
            else:
                config["model"] = models.get(model_choice, "openai/gpt-4o-mini")
            
            config["provider"] = "openrouter"
            config["api_key"] = api_key
            save_config(config)
            print(f"\n✓ OpenRouter configured successfully with model: {config['model']}")
    else:
        print("Invalid choice, using built-in AI")
        config["provider"] = "builtin"
        config["api_key"] = None
        config["model"] = "builtin-gemini"
        save_config(config)
    
    input("\nPress Enter to continue...")
    return config

def get_all_project_files(project_path):
    all_files = {}
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file == 'plan.txt':
                continue
            filepath = os.path.join(root, file)
            relpath = os.path.relpath(filepath, project_path)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    all_files[relpath] = f.read()
            except:
                all_files[relpath] = "[Binary or unreadable file]"
    return all_files

def create_project():
    clear_screen()
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + "*"*15 + " CREATE NEW PROJECT " + "*"*15 + "█")
    print("█" + " "*58 + "█")
    print("█"*60 + "\n")
    
    config = load_config()
    if not config.get("provider"):
        config = setup_ai_provider(first_time=True)
    
    project_name = input("📁 Enter project name: ").strip()
    if not project_name:
        print("❌ Project name cannot be empty")
        input("\nPress Enter to continue...")
        return
    
    project_path = os.path.join(os.getcwd(), project_name)
    try:
        os.makedirs(project_path, exist_ok=False)
        print(f"✓ Created folder: {project_path}\n")
    except FileExistsError:
        print(f"❌ Folder '{project_name}' already exists!")
        input("\nPress Enter to continue...")
        return
    
    description = input("💡 What do you want to create?\n> ").strip()
    if not description:
        print("❌ Description cannot be empty")
        input("\nPress Enter to continue...")
        return
    
    print("\n🤖 Generating development plan...\n")
    
    plan_prompt = f"""You are an expert software architect. Create a detailed development plan for: {description}

Respond with ONLY a JSON object in this exact format:
{{
    "project_type": "web app / cli tool / api / desktop app / game",
    "total_files": number,
    "files": [
        {{"path": "main.py", "purpose": "Main entry point"}},
        {{"path": "module/file.py", "purpose": "Description"}}
    ],
    "structure": "detailed folder structure",
    "dependencies": ["package1", "package2"],
    "setup_instructions": "how to run the project"
}}"""
    
    plan_response = call_ai_api(plan_prompt, config)
    plan_data = extract_json_from_response(plan_response)
    
    if not plan_data:
        print("⚠️ Using default plan structure")
        plan_data = {
            "project_type": "Application",
            "total_files": 1,
            "files": [{"path": "main.py", "purpose": "Main application"}],
            "structure": "Single file",
            "dependencies": [],
            "setup_instructions": f"python {project_name}/main.py"
        }
    
    plan_file = os.path.join(project_path, "plan.txt")
    with open(plan_file, "w", encoding="utf-8") as f:
        f.write(f"PROJECT: {project_name}\n")
        f.write(f"DESCRIPTION: {description}\n")
        f.write(f"TYPE: {plan_data.get('project_type', 'Unknown')}\n")
        f.write(f"TOTAL FILES: {plan_data.get('total_files', 0)}\n\n")
        f.write("FILES:\n")
        for file_info in plan_data.get('files', []):
            f.write(f"- {file_info.get('path', 'unknown')}: {file_info.get('purpose', '')}\n")
        f.write(f"\nSTRUCTURE:\n{plan_data.get('structure', '')}\n")
        f.write(f"\nDEPENDENCIES:\n{', '.join(plan_data.get('dependencies', []))}\n")
        f.write(f"\nSETUP:\n{plan_data.get('setup_instructions', '')}\n")
    
    print(f"✓ Plan saved to: {plan_file}\n")
    print("✍️ Writing code files...\n")
    
    files_list = json.dumps(plan_data.get('files', []), indent=2)
    code_prompt = f"""You are an expert senior developer. Write COMPLETE production-ready code for:

PROJECT: {description}
TYPE: {plan_data.get('project_type', 'Application')}
FILES TO CREATE: {files_list}

CRITICAL INSTRUCTIONS:
1. Write EVERY file listed above with COMPLETE working code
2. Each file must be fully functional and runnable
3. Include all imports, error handling, and comments
4. Code must be ready to execute immediately
5. Do NOT leave TODO placeholders - write actual code

FORMAT EXACTLY LIKE THIS FOR EACH FILE:
---FILENAME: path/to/file.ext---
[complete code content here]
---END---

No extra text, no explanations, just the code blocks."""
    
    code_response = call_ai_api(code_prompt, config)
    files_created = parse_and_save_files(code_response, project_path)
    
    if files_created == 0 and plan_data.get('files'):
        print("\n⚠️ Direct fallback generation...")
        for file_info in plan_data.get('files', []):
            filename = file_info.get('path', '')
            if filename:
                ext = os.path.splitext(filename)[1]
                fallback_prompt = f"Write complete working code for {filename} in a {plan_data.get('project_type', 'Application')} project: {description}. Purpose: {file_info.get('purpose', '')}. Return ONLY the raw code, no markdown, no explanations."
                code = call_ai_api(fallback_prompt, config)
                if code:
                    code = clean_code_response(code)
                    filepath = os.path.join(project_path, filename)
                    os.makedirs(os.path.dirname(filepath), exist_ok=True)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(code)
                    print(f"  ✓ {filename}")
                    files_created += 1
    
    print(f"\n✅ Project complete! {files_created} files created")
    print(f"📁 Location: {project_path}")
    
    if plan_data.get('dependencies'):
        print(f"\n📦 Install dependencies: pip install {' '.join(plan_data.get('dependencies', []))}")
    if plan_data.get('setup_instructions'):
        print(f"🚀 Run: {plan_data.get('setup_instructions')}")
    
    input("\nPress Enter to continue...")

def edit_existing_project():
    clear_screen()
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + "*"*15 + " EDIT EXISTING PROJECT " + "*"*15 + "█")
    print("█" + " "*58 + "█")
    print("█"*60 + "\n")
    
    config = load_config()
    if not config.get("provider"):
        config = setup_ai_provider(first_time=True)
    
    projects = [d for d in os.listdir() if os.path.isdir(d) and os.path.exists(os.path.join(d, "plan.txt"))]
    
    if not projects:
        print("❌ No existing projects found with plan.txt")
        input("\nPress Enter to continue...")
        return
    
    print("📁 Available projects:\n")
    for i, proj in enumerate(projects, 1):
        files_count = len([f for r, d, files in os.walk(proj) for f in files if f != 'plan.txt'])
        print(f"   {i}. {proj} ({files_count} files)")
    
    try:
        choice = int(input("\n🔢 Select project number: ")) - 1
        if choice < 0 or choice >= len(projects):
            print("❌ Invalid selection")
            input("\nPress Enter to continue...")
            return
        project_name = projects[choice]
    except:
        print("❌ Invalid input")
        input("\nPress Enter to continue...")
        return
    
    project_path = os.path.join(os.getcwd(), project_name)
    plan_file = os.path.join(project_path, "plan.txt")
    
    with open(plan_file, "r", encoding="utf-8") as f:
        plan_content = f.read()
    
    all_files = get_all_project_files(project_path)
    
    print(f"\n📁 Project: {project_name}")
    print(f"📄 Total files: {len(all_files)}\n")
    print("Current files:")
    for filename in sorted(all_files.keys()):
        print(f"  📄 {filename}")
    
    print("\n" + "-"*50)
    print("EDIT OPTIONS:")
    print("  1. Add new files")
    print("  2. Modify existing files")
    print("  3. Delete files")
    print("  4. Combine multiple files into one")
    print("  5. Split one file into multiple")
    print("  6. Custom edit (AI decides)")
    print("-"*50)
    
    edit_type = input("\nSelect edit type (1-6): ").strip()
    
    edit_request = input("\n📝 Describe what changes you want:\n> ").strip()
    if not edit_request:
        print("❌ No changes requested")
        input("\nPress Enter to continue...")
        return
    
    print("\n🤖 Analyzing and applying changes...\n")
    
    files_json = json.dumps(all_files, indent=2)
    
    edit_prompt = f"""You are an expert developer making precise edits to an existing project.

PROJECT: {project_name}
ORIGINAL PLAN:
{plan_content}

CURRENT FILES WITH COMPLETE CODE:
{files_json}

USER REQUEST: {edit_request}
EDIT TYPE: {edit_type}

CRITICAL INSTRUCTIONS:
1. For MODIFY: Output COMPLETE updated file with ---FILENAME: path--- and ---END--- tags
2. For CREATE: Output new file with complete code using the same format
3. For DELETE: Output ---DELETE: path/to/file.ext---
4. For COMBINE: Create ONE new file containing merged code, mark old files for deletion
5. For SPLIT: Create multiple new files from the original
6. ALWAYS preserve existing functionality unless asked to change it
7. NEVER output files that don't need changes
8. You MUST create new files when combining or splitting - don't just describe

FORMAT FOR EACH ACTION:
---FILENAME: path/to/file.ext---
[complete code]
---END---

OR FOR DELETION:
---DELETE: path/to/file.ext---

Output ONLY the actions, no explanations."""
    
    response = call_ai_api(edit_prompt, config)
    
    if not response:
        print("❌ Failed to get response from AI")
        input("\nPress Enter to continue...")
        return
    
    modified_count = 0
    created_count = 0
    deleted_count = 0
    
    delete_pattern = r'---DELETE:\s*([^\n]+)---'
    deletes = re.findall(delete_pattern, response, re.DOTALL)
    
    for filename in deletes:
        filename = filename.strip()
        filepath = os.path.join(project_path, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"  🗑️ Deleted: {filename}")
            deleted_count += 1
            if filename in all_files:
                del all_files[filename]
    
    file_pattern = r'---FILENAME:\s*([^\n]+)---\s*(.*?)\s*---END---'
    matches = re.findall(file_pattern, response, re.DOTALL)
    
    for filename, code in matches:
        filename = filename.strip()
        code = code.strip()
        
        if not filename or not code:
            continue
        
        code = clean_code_response(code)
        
        filepath = os.path.join(project_path, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        is_new = not os.path.exists(filepath)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        
        if is_new:
            print(f"  ✨ Created: {filename}")
            created_count += 1
        else:
            print(f"  📝 Modified: {filename}")
            modified_count += 1
    
    if modified_count == 0 and created_count == 0 and deleted_count == 0:
        print("\n⚠️ No changes were applied. Trying direct execution...")
        
        direct_prompt = f"""Based on: "{edit_request}"

For project files: {list(all_files.keys())}

Write the complete updated code for the file(s) that need to change. Format each as:
---FILENAME: path/file.ext---
[complete code]
---END---"""
        
        direct_response = call_ai_api(direct_prompt, config)
        direct_matches = re.findall(file_pattern, direct_response, re.DOTALL)
        
        for filename, code in direct_matches:
            filename = filename.strip()
            code = code.strip()
            if filename and code:
                code = clean_code_response(code)
                filepath = os.path.join(project_path, filename)
                os.makedirs(os.path.dirname(filepath), exist_ok=True)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(code)
                print(f"  ✓ Updated: {filename}")
                modified_count += 1
    
    print(f"\n✅ Edit complete!")
    print(f"   📝 Modified: {modified_count} files")
    print(f"   ✨ Created: {created_count} files")
    print(f"   🗑️ Deleted: {deleted_count} files")
    
    with open(plan_file, "a", encoding="utf-8") as f:
        f.write(f"\n\n--- EDIT LOG [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ---\n")
        f.write(f"Request: {edit_request}\n")
        f.write(f"Modified: {modified_count}, Created: {created_count}, Deleted: {deleted_count}\n")
    
    input("\nPress Enter to continue...")

def clean_code_response(code):
    code = re.sub(r'^```\w*\n?', '', code)
    code = re.sub(r'\n?```$', '', code)
    code = code.replace('```python', '').replace('```', '')
    return code.strip()

def extract_json_from_response(text):
    try:
        json_match = re.search(r'\{[^{}]*"total_files"[^{}]*\}', text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        
        start = text.find('{')
        end = text.rfind('}') + 1
        if start != -1 and end != 0:
            return json.loads(text[start:end])
    except:
        pass
    return None

def parse_and_save_files(response_text, project_path):
    if not response_text:
        return 0
    
    pattern = r'---FILENAME:\s*([^\n]+)---\s*(.*?)\s*---END---'
    matches = re.findall(pattern, response_text, re.DOTALL)
    
    if not matches:
        return 0
    
    file_count = 0
    for filename, code in matches:
        filename = filename.strip()
        code = code.strip()
        
        if not filename or not code:
            continue
        
        code = clean_code_response(code)
        
        filepath = os.path.join(project_path, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        
        print(f"  ✓ {filename}")
        file_count += 1
    
    return file_count

def change_ai():
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)
    clear_screen()
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + "*"*15 + " CHANGE AI PROVIDER " + "*"*15 + "█")
    print("█" + " "*58 + "█")
    print("█"*60)
    setup_ai_provider(first_time=True)

def main():
    while True:
        clear_screen()
        print("\n" + "█"*60)
        print("█" + " "*58 + "█")
        print("█" + " "*10 + "ERROR VOID CODER v2.0" + " "*27 + "█")
        print("█" + " "*58 + "█")
        print("█"*60)
        
        config = load_config()
        if config.get("provider"):
            provider_display = config['provider'].upper()
            model_display = config['model'][:20]
            print(f"\n   🤖 ACTIVE AI: {provider_display} | {model_display}")
        else:
            print("\n   ⚠️ AI NOT CONFIGURED")
        
        print("\n" + "─"*50)
        print("\n   📦 MAIN MENU\n")
        print("   1. 🚀 Create New Project")
        print("   2. ✏️ Edit Existing Project")
        print("   3. 🔧 Change AI Provider")
        print("   4. 🚪 Exit")
        print("\n" + "─"*50)
        
        choice = input("\n   ➤ Enter choice (1-4): ").strip()
        
        if choice == "1":
            create_project()
        elif choice == "2":
            edit_existing_project()
        elif choice == "3":
            change_ai()
        elif choice == "4":
            clear_screen()
            print("\n" + "█"*60)
            print("█" + " "*58 + "█")
            print("█" + "*"*15 + " GOODBYE! " + "*"*15 + "█")
            print("█" + " "*58 + "█")
            print("█"*60 + "\n")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()