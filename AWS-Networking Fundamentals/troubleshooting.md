# AWS Networking Troubleshooting

## Scenario 1: Private EC2 Instance Cannot Access the Internet

### Expected Configuration
- The private subnet route table has `0.0.0.0/0` pointing to a NAT Gateway.
- The NAT Gateway is placed in a public subnet.
- The public subnet route table has `0.0.0.0/0` pointing to an Internet Gateway.
- The NAT Gateway has an Elastic IP.
- Network security rules permit the required outbound traffic.

### Troubleshooting Checklist
1. Check the private subnet's route table.
2. Verify that the NAT Gateway is available.
3. Check the NAT Gateway's public subnet route table.
4. Verify that the Internet Gateway is attached to the VPC.
5. Review Security Group and Network ACL rules.
6. Check DNS resolution if IP connectivity works but domain names fail.

### Expected Resolution
Correct any missing or incorrect routes and verify the NAT Gateway and Internet Gateway configuration.

### Learning
A private subnet needs a valid path through a NAT Gateway for IPv4 outbound internet access. A route alone does not guarantee connectivity; gateway status, network rules, and DNS may also matter.

### Test Status
Documented as a troubleshooting scenario. Not tested against live AWS resources.
