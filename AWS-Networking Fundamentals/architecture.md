**AWS Networking Architecture**

**1. Overview**

This document describes a sample AWS VPC architecture with public and private subnets.

**2. Network Design**

- VPC CIDR: 10.0.0.0/16
- Public Subnet: 10.0.1.0/24
- Private Subnet: 10.0.2.0/24
- Internet Gateway (IGW): Provides a route between the VPC and the internet.
- NAT Gateway: Allows resources in the private subnet to initiate outbound internet connections.

**3. Traffic Flow**

Public Subnet

Internet → Internet Gateway → Public Subnet

The public subnet route table contains a default route (0.0.0.0/0) to the Internet Gateway.

Private Subnet

Private EC2 → NAT Gateway → Internet Gateway → Internet

The private subnet route table contains a default route (0.0.0.0/0) to the NAT Gateway.

**4. Security**

- Use Security Groups to control instance-level traffic.
- Use Network ACLs to control subnet-level traffic.
- Allow only required ports and sources.
- Avoid exposing private resources directly to the internet.

**5. Important Notes**

- The NAT Gateway is placed in a public subnet and requires an Elastic IP for public internet access.
- A public subnet alone does not make an EC2 instance reachable; the instance also needs appropriate routing, a public IP, and security rules.
- This document describes a planned architecture. The design should be validated during hands-on implementation. 
