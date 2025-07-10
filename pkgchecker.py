import requests
from bs4 import BeautifulSoup

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def checkPkg(repository, pkg):
    url = f"https://archlinux.org/packages/{repository}/x86_64/{pkg}/"

    headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ArchLinuxPackageChecker/1.0'
    }

    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    descriptions = soup.find_all(attrs={"itemprop": "description"})

    if response.status_code == 200:
        print(f"\n{GREEN}[✓] Package is exists!\n")
        print(f"[✓] Command for install: sudo pacman -S {pkg}")
        print(f"[✓] Description: {descriptions[0].text}{RESET}\n")
    else:
        print(f"\n{RED}[×] Package is not exists!{RESET}\n")

if __name__ == "__main__":
    repository = input("Enter repository name (extra/core/multilib): ")
    pkg = input("Enter package name: ")
    checkPkg(repository, pkg)
