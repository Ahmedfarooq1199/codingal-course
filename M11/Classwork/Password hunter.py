import keyring

service = input("Enter service/app name: ")
username = input("Enter username/email: ")

password = keyring.get_password(service, username)

if password:
    print(f"\n[+] Password found for {service} ({username})")
    print(f"Password: {password}")
else:
    print("\n[-] No password found!")

input("\nPress Enter to exit...")