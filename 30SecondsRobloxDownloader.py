import os
import requests
import subprocess
import time
import msvcrt
import psutil

def kill_roblox():
    print("Closing Roblox if it's running...")
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] and ('RobloxPlayerBeta.exe' in proc.info['name'] or 'RobloxStudioBeta.exe' in proc.info['name']):
            try:
                proc.kill()
                print(f"Process {proc.info['name']} killed.")
            except Exception as e:
                print(f"Failed to kill {proc.info['name']}: {e}")

try:
    print("Downloading full Roblox installer...")
    exe_url = "https://www.roblox.com/download/client"
    exe_name = "RobloxInstaller.exe"

    response = requests.get(exe_url, allow_redirects=True)
    with open(exe_name, 'wb') as f:
        f.write(response.content)

    print("Installer downloaded. Launching...")
    # Lancer le setup
    process = subprocess.Popen([exe_name], shell=True)

    print("Waiting for installer to finish...")
    # Boucle qui attend la fin du processus installateur
    while process.poll() is None:
        time.sleep(0.5)  # Check toutes les 0.5 sec

    print("Installer finished.")

    # Fermer Roblox direct après l'installation
    kill_roblox()

    # Supprimer l'installeur
    print("Cleaning up installer...")
    if os.path.exists(exe_name):
        os.remove(exe_name)
        print("Installer deleted.")

    print("Roblox Client + Studio are installed!")
    print("Press SPACE to close this window...")

    while True:
        if msvcrt.kbhit() and msvcrt.getch() == b' ':
            break

except Exception as e:
    print(f"[ERROR] {e}")
