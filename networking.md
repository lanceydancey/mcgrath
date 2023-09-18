Networking Fundamentals needed for System Administration

* auto-gen TOC:
{:toc}

## TCP, UDP, IP, and ICMP

These protocols form the backbone of the modern Internet. But what are they?

### TCP: Transmission Control Protocol

TCP is what is known as a connection-oriented protocol. This means that it is designed to ensure that data is delivered to the destination in the order it was sent, and that the destination acknowledges receipt of the data. TCP is also designed to ensure that data is not corrupted in transit. TCP is used for a large variety of Internet traffic, including web browsing, email, and file transfers. While the *proportional volume* of Internet traffic that is TCP is shrinking, the *absolute volume* of TCP traffic is increasing, as the Internet grows.

Other services that use TCP as their underlying transport protocol include SSH, FTP, SMB/CIFS, and basically most things outside of streaming.

### UDP: User Datagram Protocol

### IP: Internet Protocol

* IPv4
    * Classes of IPv4 addresses
    * CIDR notation
    * Private IP ranges
* IPv6

### ICMP: Internet Control Message Protocol

Weird stuff here.

---
## Networking Layers

## Network Hardware

### Fabric

### Switches

### Routers

### Wireless Access Points (WAPs)

### Networking PHYs

## Network Services

### DNS

### DHCP

### NTP

### ARP

### SMB

### NFS

### LDAP

## Routing

### Internal routing

### BGP

## Network Address Translation

## vLANs and network management

## The sockets API

## Monitoring a network

### `ip`/`ifconfig`

### `netstat`

`netstat` is an older tool, but has the benefit of being available on most systems. It can be used to display open sockets, routing tables, link statistics, and more. It is especially useful for determining what processes are listening on what ports.

That said, `netstat` is deprecated in favor of `ss`, which is more modern and has more features.

See the `netstat` manpage for what tools replace which pieces of its functionality.

### `ss`

The primary replacement for `netstat`, `ss` is a more modern tool which can display more detailed information about a variety of socket types, including internal kernel data regarding each socket.

Some useful flags include:

- `-l, --listening`: list listening sockets
- `-t, --tcp`: list TCP sockets
- `-u, --udp`: list UDP sockets
- `-x, --unix`: list Unix sockets
- `-p, --processes`: show process information for each socket (requires admin privileges)
- `-n, --numeric`: don't resolve hostnames or ports/services
- `-r, --resolve`: try to resolve hostnames
- `-a, --all`: show all sockets (including those not listening)
- `-i, --info`: show internal TCP information
- `-e, --extended`: show extended socket information

For example, to show the processes with open TCP listen sockets, resolved hostnames and ports, and extended information, you could run:

```sh
❯ sudo ss --processes --tcp --listening --extended --resolve
State        Recv-Q       Send-Q             Local Address:Port               Peer Address:Port      Process                                                                                                                                
LISTEN       0            128                    localhost:ipp                     0.0.0.0:*          users:(("cupsd",pid=48519,fd=7)) ino:191576 sk:300d cgroup:/system.slice/cups.service <->                                             
LISTEN       0            4096                   localhost:33273                   0.0.0.0:*          users:(("containerd",pid=1091,fd=10)) ino:25655 sk:220 cgroup:/system.slice/containerd.service <->                                    
LISTEN       0            4096                localhost%lo:domain                  0.0.0.0:*          users:(("systemd-resolve",pid=993,fd=14)) uid:102 ino:18366 sk:221 cgroup:/system.slice/systemd-resolved.service <->                  
LISTEN       0            128                      0.0.0.0:ssh                     0.0.0.0:*          users:(("sshd",pid=21897,fd=3)) ino:94802 sk:3011 cgroup:/system.slice/ssh.service <->                                                
LISTEN       0            128                ip6-localhost:ipp                        [::]:*          users:(("cupsd",pid=48519,fd=6)) ino:191575 sk:3012 cgroup:/system.slice/cups.service v6only:1 <->                                    
LISTEN       0            50                             *:1716                          *:*          users:(("kdeconnectd",pid=2235,fd=12)) uid:1000 ino:26074 sk:224 cgroup:/user.slice/user-1000.slice/session-3.scope v6only:0 <->      
LISTEN       0            128                         [::]:ssh                        [::]:*          users:(("sshd",pid=21897,fd=4)) ino:94804 sk:3016 cgroup:/system.slice/ssh.service v6only:1 <->
```

### `tcpdump`

### Wireshark

### Other capture tools

* NIDS/NIPS
* Windows NDIS tools
* Darkstat
