routes = {
    "public": {
        "0.0.0.0/0": "igw"
    },
    "private": {
        "0.0.0.0/0": "nat"
    }
}

checks = [
    ("Public subnet uses Internet Gateway",
     routes["public"].get("0.0.0.0/0") == "igw"),

    ("Private subnet uses NAT Gateway",
     routes["private"].get("0.0.0.0/0") == "nat")
]

for description, passed in checks:
    print(f"{'PASS' if passed else 'FAIL'}: {description}")

if all(passed for _, passed in checks):
    print("\nSUCCESS: Route validation passed.")
else:
    print("\nERROR: Review the route configuration.")