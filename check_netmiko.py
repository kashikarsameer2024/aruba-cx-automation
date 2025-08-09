from netmiko.ssh_dispatcher import CLASS_MAPPER_BASE

print("Supported Netmiko platforms:\n")
for platform in sorted(CLASS_MAPPER_BASE.keys()):
    print("-", platform)