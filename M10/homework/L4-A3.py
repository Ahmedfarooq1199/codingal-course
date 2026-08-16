print("My Secret Code Bit Scanner")

secret_code = int(input("Enter a secret code: "))
access_key = int(input("Enter an access key: "))

print("\nSecret Code in Binary:", bin(secret_code))
print("Access Key in Binary:", bin(access_key))

if secret_code == access_key:
    print("Access Granted")
else:
    print("Access Denied")