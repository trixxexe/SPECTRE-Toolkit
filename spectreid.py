import requests
import os
import time

# --- Spectre Colors ---
PURPLE = '\033[95m'
WHITE = '\033[97m'
CYAN = '\033[96m'
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
        | |                           
        |_|                           
    """ + RESET)
    print(WHITE + "    >>> Fake Identity Generator <<<" + RESET)
    print("-" * 45)

def generate_id():
    print(PURPLE + "[*] Fabricating new identity..." + RESET)
    time.sleep(1)
    
    try:
        url = "https://randomuser.me/api/?nat=us,gb"
        response = requests.get(url).json()
        user = response['results'][0]
        
        print("\n" + CYAN + "[ IDENTITY CREATED ]" + RESET)
        print("-" * 45)
        print(f"{BOLD}Name:{RESET}     {user['name']['first']} {user['name']['last']}")
        print(f"{BOLD}Gender:{RESET}   {user['gender']}")
        print(f"{BOLD}Location:{RESET} {user['location']['city']}, {user['location']['country']}")
        print(f"{BOLD}Email:{RESET}    {user['email']}")
        print(f"{BOLD}Username:{RESET} {user['login']['username']}")
        print(f"{BOLD}Password:{RESET} {user['login']['password']}")
        print(f"{BOLD}DOB:{RESET}      {user['dob']['date'][:10]} (Age: {user['dob']['age']})")
        print("-" * 45)
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    print_banner()
    generate_id()

if __name__ == "__main__":
    main()

