# UFW (Uncomplicated Firewall) Configuration and Port Forwarding

## Introduction

This README provides essential information on configuring UFW (Uncomplicated Firewall) on Linux systems. UFW simplifies firewall management by offering an easy-to-use command-line interface. Additionally, we'll cover port forwarding using UFW.

## UFW Commands (task 0-block_all_incoming_traffic_but)

### Enable UFW
```bash
sudo ufw enable
```
- Enables the firewall.

### Check UFW Status
```bash
sudo ufw status
```
- Displays existing rules and whether the firewall is active.

### Disable UFW
```bash
sudo ufw disable
```
- Disables the firewall.

### Reload UFW Rules
```bash
sudo ufw reload
```
- Reloads the firewall rules without disabling it.

### Reset UFW Rules
```bash
sudo ufw reset
```
- Resets UFW to default rules (deny incoming/outgoing).

### Set Default Policies
```bash
sudo ufw default deny incoming
sudo ufw default deny outgoing
```
- Sets default policies to deny incoming and outgoing traffic.

### Allow/Deny Specific IP Addresses
```bash
sudo ufw allow from 1.1.1.1
sudo ufw deny from 203.0.113.100
```
- Allows or denies traffic from specific IP addresses.

### Allow Specific Ports
```bash
sudo ufw allow 993  # IMAPS
sudo ufw allow 6969  # BitTorrent
sudo ufw allow 22/tcp  # SSH
sudo ufw allow 443/tcp  # HTTPS
sudo ufw allow 80/tcp  # HTTP
```
- Allows traffic on specific ports (e.g., SSH, HTTPS, HTTP).

### Allow Outgoing Services
```bash
sudo ufw allow out 53  # DNS
sudo ufw allow out http  # HTTP
sudo ufw allow out https  # HTTPS
```
- Allows outgoing traffic for DNS, HTTP, and HTTPS.

## Port Forwarding (task 100-port_forwarding)

### Edit `before.rules` File
```bash
sudo vi /etc/ufw/before.rules
```
- Open the `before.rules` file for editing.

### Add Port Forwarding Rules
Add the following lines at the top of the file (before the `COMMIT` line):
```bash
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
```
- Redirects incoming traffic from external ports 8080 to an internal server on port 80.

Remember to adjust IP addresses, ports, and services as needed for your specific setup.

---
