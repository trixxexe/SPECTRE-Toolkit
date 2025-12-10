import requests
import time
import os
import sys

# --- Spectre Theme Colors (Purple/Ghost) ---
PURPLE = '\033[95m'
WHITE = '\033[97m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('clear')

def print_banner():
    clear_screen()
    print(PURPLE + BOLD + r"""
   _____ ____  _____ ____ _____ ____  _____ 
  / ____|  _ \| ____/ ___|_   _|  _ \| ____|
 | (___ | |_) |  _|| |     | | | |_) |  _|  
  \___ \|  __/| |__| |___  | | |  _ <| |___ 
  |____/|_|   |_____\____| |_| |_| \_\_____|
    """ + RESET)
    print(WHITE + "    >>> Digital Identity Hunter <<<" + RESET)
    print(PURPLE + "      [ Search for Usernames ]" + RESET)
    print("-" * 45)

def check_site(site_name, url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(GREEN + f"[+] Found on {site_name}: {WHITE}{url}" + RESET)
        elif response.status_code == 404:
            print(RED + f"[-] Not found on {site_name}" + RESET)
        else:
            print(PURPLE + f"[?] {site_name}: Error {response.status_code}" + RESET)
    except:
        print(RED + f"[!] Error connecting to {site_name}" + RESET)

def main():
    print_banner()
    username = input(BOLD + "Enter Username to Hunt: " + RESET)
    
    if not username:
        print("Username cannot be empty.")
        sys.exit()

    print(PURPLE + f"\n[*] Hunting for '{username}' across the web..." + RESET)
    print("-" * 45)
    
    # Dictionary of sites to check
    sites = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "GitHub":    f"https://github.com/{username}",
        "Reddit":    f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Wattpad":   f"https://www.wattpad.com/user/{username}",
        "Pastebin":  f"https://pastebin.com/u/{username}"
    }

    for site, url in sites.items():
        check_site(site, url)
        time.sleep(0.5) # Anti-ban delay

    print("-" * 45)
    print(WHITE + "Search Complete." + RESET)

if __name__ == "__main__":
    main()

