
import ipaddress

# Define the AWS network
vpc = ipaddress.ip_network("10.0.0.0/16")
public_subnet = ipaddress.ip_network("10.0.1.0/24")
private_subnet = ipaddress.ip_network("10.0.2.0/24")

print("=== AWS Networking Fundamentals ===")
print(f"VPC CIDR: {vpc}")
print(f"Total VPC addresses: {vpc.num_addresses}")

for name, subnet in [
    ("Public", public_subnet),
    ("Private", private_subnet),
]:
    print(f"\n{name} subnet: {subnet}")
    print(f"Inside VPC: {subnet.subnet_of(vpc)}")
    print(f"Total addresses: {subnet.num_addresses}")
    print(f"AWS usable IPv4 addresses: {subnet.num_addresses - 5}")

assert public_subnet.subnet_of(vpc), "Public subnet is outside VPC"
assert private_subnet.subnet_of(vpc), "Private subnet is outside VPC"
assert not public_subnet.overlaps(private_subnet), "Subnets overlap"

print("\nSUCCESS: Both subnets are valid and non-overlapping.")