import requests
import os
import sys

# --- Spectre Colors ---
PURPLE = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'

def clear_screen():
    os.system('clear')

def print_banner():
    clear_screen()
    print(PURPLE + BOLD + r"""
   _____                 _              
  / ____|               | |             
 | (___  _ __   ___  ___| |_ _ __ ___  
  \___ \| '_ \ / _ \/ __| __| '__/ _ \ 
  ____) | |_) |  __/ (__| |_| | |  __/ 
 |_____/| .__/ \___|\___|\__|_|  \___| 
        | |                            
        |_|                            
    """ + RESET)
    print(CYAN + "    >>> HTTP Header Analyzer <<<" + RESET)
    print("-" * 45)

def analyze_headers():
    target = input(BOLD + "Enter Target URL (e.g. google.com): " + RESET)
    
    if not target:
        return

    # Add https if missing
    if not target.startswith("http"):
        target = "https://" + target

    print(YELLOW + "\n[*] Intercepting headers..." + RESET)
    
    try:
        # We only need the HEAD, not the whole page body
        response = requests.head(target, timeout=5)
        
        print("\n" + PURPLE + "[ SERVER RESPONSE HEADERS ]" + RESET)
        print("-" * 45)
        
        for key, value in response.headers.items():
            print(f"{BOLD}{key}:{RESET} {value}")
            
        print("-" * 45)
        
        # Security Check
        if 'X-Frame-Options' in response.headers:
            print(CYAN + "[+] Security: Anti-Clickjacking (X-Frame) is ON." + RESET)
        else:
            print(YELLOW + "[-] Security: X-Frame-Options missing (Potential Risk)." + RESET)
            
    except Exception as e:
        print(f"Error: {e}")

# This was the missing part!
def main():
    print_banner()
    analyze_headers()

if __name__ == "__main__":
    main()

