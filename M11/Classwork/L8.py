import asyncio
from bleak import BleakScanner

async def scan_devices():
    print("Scanning for nearby Bluetooth devices...\n")

    devices = await BleakScanner.discover(timeout=10)

    if not devices:
        print("No Bluetooth devices found.")
        return

    print("Nearby Bluetooth devices:")
    print("-" * 50)

    for i, device in enumerate(devices, 1):
        print(f"{i}. Name: {device.name or 'Unknown'}")
        print(f"   Address: {device.address}")
        print()

asyncio.run(scan_devices())

input("Press Enter to exit...")