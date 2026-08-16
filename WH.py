import subprocess

# Get saved Wi-Fi profiles
profiles = subprocess.check_output(
    "netsh wlan show profiles",
    shell=True,
    text=True,
    errors="ignore"
)

names = [
    line.split(":", 1)[1].strip()
    for line in profiles.splitlines()
    if "All User Profile" in line
]

print("\nAvailable Wi-Fi Profiles:\n")

for i, name in enumerate(names, 1):
    print(f"{i}. {name}")

print("\nSaved passwords:\n")

for name in names:
    try:
        result = subprocess.check_output(
            f'netsh wlan show profile name="{name}" key=clear',
            shell=True,
            text=True,
            errors="ignore"
        )

        password = "Not found"

        for line in result.splitlines():
            if "Key Content" in line:
                password = line.split(":", 1)[1].strip()
                break

        print(f"Wi-Fi: {name}")
        print(f"Password: {password}")
        print("-" * 40)

    except subprocess.CalledProcessError:
        print(f"Could not read profile: {name}")

input("\nPress Enter to exit...")