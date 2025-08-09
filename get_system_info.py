from netmiko import ConnectHandler

device = {
    "device_type": "aruba_aoscx",
    "ip": "10.1.1.129",
    "username": "admin",
    "password": "admin",
}

try:
    connection = ConnectHandler(**device)
    output = connection.send_command("show version")
    print(output)
    connection.disconnect()
except Exception as e:
    print(f"Connection failed: {e}")



