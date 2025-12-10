import os
import sys
import time

# --- Import your tools ---
# Note: We use os.system to run them to keep the screen clears working cleanly
# This is the simplest way to link separate scripts

# --- Colors ---
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('clear')

def main_menu():
    while True:
        clear_screen()
        print(PURPLE + BOLD + r"""
   _____ ____  _____ ____ _____ ____  _____ 
  / ____|  _ \| ____/ ___|_   _|  _ \| ____|
 | (___ | |_) |  _|| |     | | | |_) |  _|  
  \___ \|  __/| |__| |___  | | |  _ <| |___ 
  |____/|_|   |_____\____| |_| |_| \_\_____|
    """ + RESET)
        print(WHITE + "      >>> The OSINT Collection <<<" + RESET)
        print(PURPLE + "       [ v1.0 | Coded by Trixx ]" + RESET)
        print("-" * 45)
        
        print(f" {BOLD}[1]{RESET} Username Hunter    {CYAN}(spectreuser){RESET}")
        print(f" {BOLD}[2]{RESET} HTTP Header Check  {CYAN}(spectrehead){RESET}")
        print(f" {BOLD}[3]{RESET} Phone Recon        {CYAN}(spectrephone){RESET}")
        print(f" {BOLD}[4]{RESET} MAC Address Lookup {CYAN}(spectremac){RESET}")
        print(f" {BOLD}[5]{RESET} Link Tracer        {CYAN}(spectrelink){RESET}")
        print(f" {BOLD}[6]{RESET} Fake Identity Gen  {CYAN}(spectreid){RESET}")
        print(f" {BOLD}[99]{RESET} Exit")
        print("-" * 45)
        
        choice = input(PURPLE + "spectre > " + RESET)
        
        if choice == '1':
            os.system('python spectreuser.py')
            input(PURPLE + "\nPress Enter to return..." + RESET)
        elif choice == '2':
            os.system('python spectrehead.py')
            input(PURPLE + "\nPress Enter to return..." + RESET)
        elif choice == '3':
            os.system('python spectrephone.py')
            input(PURPLE + "\nPress Enter to return..." + RESET)
        elif choice == '4':
            os.system('python spectremac.py')
            input(PURPLE + "\nPress Enter to return..." + RESET)
        elif choice == '5':
            os.system('python spectrelink.py')
            input(PURPLE + "\nPress Enter to return..." + RESET)
        elif choice == '6':
            os.system('python spectreid.py')
            input(PURPLE + "\nPress Enter to return..." + RESET)
        elif choice == '99':
            print("Exiting SPECTRE...")
            break
        else:
            print(RED + "Invalid Option" + RESET)
            time.sleep(1)

if __name__ == "__main__":
    main_menu()

