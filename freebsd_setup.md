```sh
#!/bin/sh
#
# To download this script directly from freeBSD:
# $ pkg install curl
# $ curl -LO https://raw.githubusercontent.com/dkmcgrath/Tools-and-Tips/main/freebsd_setup.sh
#
#The following features are added:
# - switching (internal to the network) via FreeBSD pf
# - DHCP server, DNS server via dnsmasq
# - firewall via FreeBSD pf
# - NAT layer via FreeBSD pf
#

# Set your network interfaces names; set these as they appear in ifconfig
# they will not be renamed during the course of installation
WAN="hn0"
LAN="hn1"

# Install dnsmasq
pkg install -y dnsmasq

# Enable forwarding
sysrc gateway_enable="YES"
# Enable immediately
sysctl net.inet.ip.forwarding=1

# Set LAN IP
ifconfig ${LAN} inet 192.168.33.1 netmask 255.255.255.0
# Make IP setting persistent
sysrc "ifconfig_${LAN}=inet 192.168.33.1 netmask 255.255.255.0"

ifconfig ${LAN} up
ifconfig ${LAN} promisc

# Enable dnsmasq on boot
sysrc dnsmasq_enable="YES"

# Edit dnsmasq configuration
echo "interface=${LAN}" >> /usr/local/etc/dnsmasq.conf
echo "dhcp-range=192.168.33.50,192.168.33.150,12h" >> /usr/local/etc/dnsmasq.conf
echo "dhcp-option=option:router,192.168.33.1" >> /usr/local/etc/dnsmasq.conf

# Configure PF for NAT
echo "
ext_if=\"${WAN}\"
int_if=\"${LAN}\"
nat on \$ext_if from \$int_if:network to any -> (\$ext_if)

include \"/etc/pf.blockrules.conf\"

pass in on \$int_if from \$int_if:network to any
pass out on \$ext_if from any to any
" >> /etc/pf.conf

#Firewall rules go in /etc/pf.blockrules.conf
#use the quick keyword to drop packet immediately
#block all icmp from google dns (8.8.8.8) as example
#int_if is lAN , ext_if is WAN

echo "
#Usage: pf firewall, use quick keyword here
#\$int_if
#\$ext_if

block in quick on \$ext_if proto icmp from 8.8.8.8 to any
block out quick on \$ext_if proto icmp from any to 8.8.8.8
" > /etc/pf.blockrules.conf

# Start dnsmasq
service dnsmasq start

# Enable PF on boot
sysrc pf_enable="YES"

# Start PF
service pf start

# Load PF rules
pfctl -f /etc/pf.conf
```
