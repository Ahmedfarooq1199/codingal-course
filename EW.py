import subprocess
profiles = subprocess.check_output("netsh wlan show profiles",shell=True).decode()
names = [line.split(":")[1].strip() for line in profiles.split("\n") if "All User Profile" in line]
print("Available Wi-Fi Profiles:/n")
for i, name in enumerate(names):
    print("{i+1}. {name}")
input("/nPress Enter to exit...")

