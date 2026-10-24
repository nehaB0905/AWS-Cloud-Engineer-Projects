
# AWS Networking Fundamentals
# Local simulation of network security rules

security_group = {
    "allow_ssh_from_trusted_ip": True,
    "allow_https_outbound": True
}

network_acl = {
    "allow_inbound_https": True,
    "allow_outbound_ephemeral_ports": True
}

checks = [
    ("SSH restricted to trusted IP", 
     security_group["allow_ssh_from_trusted_ip"]),
    ("HTTPS outbound allowed by Security Group",
     security_group["allow_https_outbound"]),
    ("Inbound HTTPS allowed by Network ACL",
     network_acl["allow_inbound_https"]),
    ("Outbound ephemeral ports allowed by Network ACL",
     network_acl["allow_outbound_ephemeral_ports"])
]

for description, passed in checks:
    status = "PASS" if passed else "FAIL"
    print(f"{status}: {description}")

if all(passed for _, passed in checks):
    print("\nSUCCESS: All simulated security checks passed.")
