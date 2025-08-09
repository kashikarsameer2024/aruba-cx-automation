import requests
import urllib3

# Disable SSL cert warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Aruba CX switch connection info
switch_ip = "10.1.1.129"
username = "admin"
password = "admin"

# VLAN details
vlan_id = 20
vlan_name = "Test_VLAN_20"

url = f"https://{switch_ip}/v1/configuration/vlan"

headers = {
    "Content-Type": "application/json"
}

data = {
    "vlan_id": vlan_id,
    "name": vlan_name
}

# Send request
response = requests.post(
    url,
    auth=(username, password),
    headers=headers,
    json=data,
    verify=False
)

# Handle response
if response.status_code in [200, 201, 204]:
    print(f"✅ VLAN {vlan_id} created successfully.")
else:
    print(f"❌ Failed to create VLAN {vlan_id}. Status: {response.status_code}")
    print(response.text)
