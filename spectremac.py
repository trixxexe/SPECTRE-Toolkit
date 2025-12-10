import requests
import os
import sys

# --- Spectre Colors ---
PURPLE = '\033[95m'
WHITE = '\033[97m'
RED = '\033[91m'
CYAN = '\033[96m'
GREEN = '\033[92m'  # <--- Added this missing color
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
    print(WHITE + "    >>> MAC Address Lookup <<<" + RESET)
    print("-" * 45)

def lookup_mac():
    mac = input(BOLD + "Enter MAC Address (e.g. 00:11:22:33:44:55): " + RESET)
    
    if len(mac) < 8:
        print(RED + "Invalid MAC address format." + RESET)
        return

    print(PURPLE + "\n[*] Querying Manufacturing Database..." + RESET)
    
    try:
        url = f"https://api.macvendors.com/{mac}"
        response = requests.get(url)
        
        print("-" * 45)
        if response.status_code == 200:
            print(f"{BOLD}Device Manufacturer:{RESET} {GREEN}{response.text}{RESET}")
        else:
            print(RED + "Vendor not found or Limit Exceeded." + RESET)
        print("-" * 45)
        
    except Exception as e:
        print(RED + f"Error: {e}" + RESET)

def main():
    print_banner()
    lookup_mac()

if __name__ == "__main__":
    main()

