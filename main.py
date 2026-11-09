import sys
import os
from colorama import init, Fore

init(autoreset=True)

def analyze_code(file_path):
    if not os.path.exists(file_path):
        print(Fore.RED + f"[!] File not found: {file_path}")
        return

    print(Fore.CYAN + f"\n[*] Analyzing code file: {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    issues = 0
    for idx, line in enumerate(lines, 1):
        # Rule 1: Line length check
        if len(line) > 80:
            print(Fore.YELLOW + f"[Warning] Line {idx}: Line exceeds 80 characters limit.")
            issues += 1
        # Rule 2: Unused print statements
        if "print(" in line and not line.strip().startswith("#"):
            print(Fore.BLUE + f"[Info] Line {idx}: Contains debug print statement.")
            issues += 1
        # Rule 3: Missing docstrings in functions
        if line.strip().startswith("def ") and ":" in line:
            print(Fore.GREEN + f"[Tip] Line {idx}: Ensure function has a proper docstring.")
            issues += 1

    print(Fore.CYAN + f"\n[V] Review complete. Found {issues} suggestions/warnings.")

def main():
    print(Fore.MAGENTA + "=" * 50)
    print(Fore.WHITE + "      AI PYTHON CODE STATIC REVIEWER")
    print(Fore.MAGENTA + "=" * 50)
    
    target = input(Fore.YELLOW + "\nEnter Python file path to review: ").strip()
    analyze_code(target)

if __name__ == "__main__":
    main()
