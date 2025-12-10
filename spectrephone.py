import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import os
import sys

# --- Spectre Colors ---
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
   _____                      
  / ____|                     
 | (___  _ __   ___  ___      
  \___ \| '_ \ / _ \/ __|     
  ____) | |_) |  __/ (__      
 |_____/| .__/ \___|\___|     
        | |                   
        |_|                   
    """ + RESET)
    print(WHITE + "    >>> Phone Number Recon <<<" + RESET)
    print("-" * 45)

def scan_number():
    number_input = input(BOLD + "Enter Number (with +CountryCode): " + RESET)
    
    try:
        # Parse the number
        phone_number = phonenumbers.parse(number_input)
        
        # Check if valid
        is_valid = phonenumbers.is_valid_number(phone_number)
        
        if not is_valid:
            print(RED + "\n[!] Invalid Phone Number." + RESET)
            return

        print(PURPLE + "\n[*] Extracting Signal Data..." + RESET)
        
        # Get Data
        # 'en' means English language results
        location = geocoder.description_for_number(phone_number, "en")
        service_provider = carrier.name_for_number(phone_number, "en")
        time_zones = timezone.time_zones_for_number(phone_number)
        
        # Display Results
        print("\n" + GREEN + "[+] TARGET IDENTIFIED:" + RESET)
        print("-" * 45)
        print(f"{BOLD}Format:{RESET}       {phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        print(f"{BOLD}Location:{RESET}     {location}")
        print(f"{BOLD}Carrier:{RESET}      {service_provider}")
        print(f"{BOLD}Timezone:{RESET}     {time_zones}")
        print("-" * 45)

    except Exception as e:
        print(RED + f"\n[!] Error: {e}" + RESET)
        print("Make sure you included the '+' sign (e.g. +91...)")

def main():
    print_banner()
    scan_number()

if __name__ == "__main__":
    main()

