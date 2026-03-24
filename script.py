import requests
import re
from colorama import Fore, init

init(autoreset=True)

def find_all_subdomains():
    print(f"{Fore.CYAN}==================================================")
    print(f"{Fore.WHITE}      ULTRA FULL SUBDOMAIN SCANNER v3.0")
    print(f"{Fore.CYAN}==================================================")
    print(f"{Fore.CYAN}Donate wity solona:2R8s8z7cEiUVs44BGq5dsz3XhnvyXpirqk7bLieC2q4y")
    print("")
    domain = input(f"{Fore.YELLOW}[?] Enter Domain (e.g. google.com): {Fore.WHITE}").strip()
    output_file = input(f"{Fore.YELLOW}[?] Output file (default: all_subs.txt): {Fore.WHITE}").strip() or "all_subs.txt"

    print(f"\n{Fore.BLUE}[*] Searching global certificate databases for {domain}...")

    try:
        # crt.sh üzerinden tüm kayıtlı alt alan adlarını çeker (En etkili yöntem)
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=15)

        if response.status_code == 200:
            data = response.json()
            subdomains = set()

            for entry in data:
                # Alt alan adlarını temizle ve listeye ekle
                name = entry['name_value'].lower()
                if "\n" in name:
                    for sub in name.split("\n"):
                        subdomains.add(sub)
                else:
                    subdomains.add(name)

            # Temizleme ve Filtreleme
            final_list = sorted([s for s in subdomains if "*" not in s])

            if final_list:
                print(f"{Fore.GREEN}[+] SUCCESS: Found {len(final_list)} unique subdomains!\n")

                with open(output_file, "w") as f:
                    for sub in final_list:
                        print(f"{Fore.WHITE}{sub}")
                        f.write(sub + "\n")

                print(f"\n{Fore.CYAN}==================================================")
                print(f"{Fore.WHITE}[#] All {len(final_list)} subdomains saved to {output_file}")
                print(f"{Fore.CYAN}==================================================")
            else:
                print(f"{Fore.RED}[!] No subdomains found for this domain.")
        else:
            print(f"{Fore.RED}[!] Database busy. Try again in a few minutes.")

    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}")

if __name__ == "__main__":
    find_all_subdomains()
