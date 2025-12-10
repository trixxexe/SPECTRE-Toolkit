import requests
import os

# --- Spectre Colors ---
PURPLE = '\033[95m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

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
    """ + RESET)
    print(YELLOW + "    >>> Link Redirection Tracer <<<" + RESET)
    print("-" * 45)

def trace_link():
    url = input(BOLD + "Enter Suspicious Link: " + RESET)
    
    if not url.startswith("http"):
        url = "http://" + url

    print(PURPLE + "\n[*] Tracing hops..." + RESET)
    
    try:
        # We allow redirects and track the history
        response = requests.head(url, allow_redirects=True, timeout=10)
        
        # Show the path
        if response.history:
            count = 1
            for resp in response.history:
                print(f"{YELLOW}[Hop {count}]{RESET} {resp.status_code} -> {resp.url}")
                count += 1
            
            print("-" * 45)
            print(GREEN + f"[FINAL DESTINATION]: {response.url}" + RESET)
            print("-" * 45)
        else:
            print(GREEN + "\n[+] No redirects found. This is the direct link." + RESET)
            
    except Exception as e:
        print(RED + f"[!] Error: {e}" + RESET)

def main():
    print_banner()
    trace_link()

if __name__ == "__main__":
    main()

