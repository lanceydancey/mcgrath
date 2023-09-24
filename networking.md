Networking Fundamentals needed for System Administration

* auto-gen TOC:
{:toc}

## TCP, UDP, IP, and ICMP

These protocols form the backbone of the modern Internet. But what are they?

### IP: Internet Protocol

The internet protocol is the underlying protocol of the Internet. One of the fun aspects of IP is that it guarantees nothing. It simply provides an identification scheme for nodes on the Internet. It does not guarantee delivery, it does not guarantee order, it does not guarantee anything. It is a best-effort protocol, and that's it.

There are two main variants of IP in use today: IPv4 and IPv6. IPv6 was created to accommodate the rising number of devices on the Internet -- some estimates put the number of interconnected digital devices at well over 10 billion, with Cisco estimating 5.3 billion individual users. IPv4 only allows for 4.3 billion unique addresses, which is clearly insufficient (pigeon hole principle!!!). IPv6 allows for three hundred and forty undecillion, two hundred and eighty-two decillion, three hundred and sixty-six nonillion, nine hundred and twenty octillion, nine hundred and thirty-eight septillion, four hundred and sixty-three sextillion, four hundred and sixty-three quintillion, three hundred and seventy-four quadrillion, six hundred and seven trillion, four hundred and thirty-one billion, seven hundred and sixty-eight million, two hundred and eleven thousand, four hundred and fifty-six unique addresses, which should be enough for a while ($\approx 3.4e^{38}$). IPv4, by contrast, supports *only* 4.3 billion unique addresses ($\approx 4.3e^9$). 

To compare, IPv6 has enough address to give roughly 100 addresses to *each atom on the surface of the Earth*. IPv4 barely has enough addresses to share one address per two people on Earth. IPv6 is a *lot* of addresses.

Assume that someone has invented nanites, small, self-controlled swarm robots on the nanometer scale. This puts them roughly the size of atoms. Next, assume that a swarm can replicate the functionality of arbitrary bacteria, at roughly 50 billion nanites per bacterium. The human body contains on the order of 50 trillion bacteria. There are roughly 8 billion people on Earth. If all the bacteria in all the humans on Earth were replaced by nanites, with each nanite assigned an IPv6 address, it would consume roughly $\frac{1}{10,000}$ of the available IPv6 addresses. In math:
$$
\left(\frac{50e12\ \mathrm{bacteria}}{\mathrm{human}}\right) \times \left(\frac{8e9\ \mathrm{humans}}{\mathrm{Earth}}\right) \times \left(\frac{50e9\ \mathrm{nanites}}{\mathrm{bacteria}}\right) \approx \left(\frac{2e^{34}\ \mathrm{nanites}}{\mathrm{Earth}}\right)
$$

Since $\displaystyle \frac{3.4e^{38}}{2e^{34}}$ is roughly $10e^3$, each nanite could have $10,000$ IPv6 addresses.

While the above is mostly for amusement value, we won't be discussing IPv6 much. While the Internet Society measures IPv6 adoption rate at 46%, the reality is that all of those systems also run IPv4. We will be focusing on IPv4, as it is the primary protocol in use today. IPv4 is also the default on most systems and networks.

### IPv4

IPv4 addresses are 32 bits in length, and are typically represented in dotted decimal notation. Each segment is one octet (8 bits) of the address: $a.b.c.x$. The first three octets are the network address, and the last octet is the host address. The network address is used to identify the network, and the host address is used to identify the host on the network. 

Each subnet, or collection of addresses contained within the network address, can be classified based on size. 

* Class A: addresses of the form $a.x.y.z$, where $a$ is the network address and $x.y.z$ is the host address. Technically $a < 127$, but in practice, any value of $a$ was considered a class A address. These were for large networks, consisting of $2^{24}$ hosts.
* Class B: addresses of the form $a.b.x.y$, where $a.b$ is the network address. Contains $2^{16}$ hosts.
* Class C: addresses of the form $a.b.c.x$, where $a.b.c$ is the network address. Contains $2^8$ hosts.

This is great, as far as it goes, but it turned out this was simply too inflexible. Classless inter-domain routing, or CIDR (pronounced like cider), was created to increase flexibility in IP address block purchasing. CIDR notation is of the form $a.b.c.d/y$, where $a.b.c.d$ is the network address and $y$ is the number of bits in the network address. This allows for arbitrary network sizes, and is the standard notation used today. 

How CIDR actually works is by defining a fixed portion (the network address) and a mask. For instance, a common private range in use is 10.0.0.0/8. This means that the first 8 bits of the address are fixed, and the remaining 24 bits are variable. "But wait", you say, "this looks just like a Class A network from above!" And it does. But CIDR is much more flexible than the class system. For instance, another private range is 172.16.0.0/12. This means the first 12 bits are fixed, and all other bits are variable. This is midway between a Class A and a Class B network, containing $2^{20}$ hosts.

Any value of $y$ is valid, from 0 to 32. A value of 32 means that the entire address is fixed, and there are no hosts on the network. A value of 0 means that the entire address is variable, and the network is the Internet. A value of 31 is technically valid, but is not used in practice. A value of 31 would mean that there are only two hosts on the network, which is not enough to be useful. A value of 30 is the smallest useful network, containing 4 hosts. A value of 29 contains 8 hosts, and so on.

The two examples I chose were from the private address space defined in [RFC6890](https://www.rfc-editor.org/rfc/rfc6890). Specifically, those ranges marked for "Private-Use". These ranges are

* 10.0.0.0/8
* 172.16.0.0/12
* 192.168.0.0/16

You've likely encountered the first and the third, while the second range, for reasons that are not entirely clear, is not used much in practice.

Now, I know some of you are running a fairly large number of connected devices in your household. And if everyone was doing that, how can we possibly still be running on IPv4? The answer, such as it is, is NAT -- Network Address Translation. Combined with private-use ranges above, NAT allows for a large private network to be behind a single globally routable IP address.

The way NAT works is to translate from the global IP range outside your router to the private IP range on the inside of your router. It does this by rewriting packets as they pass through the router, changing both the source IP address and the source port. It maintains a table of these mappings so that packets returning to the host inside the network can be translated back to the original source IP address and port. This is why you can have multiple devices on your home network all using the same IP address -- the router is rewriting the packets to make it appear as if they are all coming from the same device. This is also why if you purchase a gift for your partner, they often start getting ads for that gift -- since all devices on your private network are a single device outside your network. Ad networks are stupid.

### ICMP: Internet Control Message Protocol

Weird stuff here. While ICMP is typically considered part of the Internet layer, it's encapsulated within an IP packet...but it isn't really the same type of protocol as TCP or UDP. It's a control protocol rather than a transport protocol, and so is rightfully considered part of the 

### TCP: Transmission Control Protocol

TCP is what is known as a connection-oriented protocol. This means that it is designed to ensure that data is delivered to the destination in the order it was sent, and that the destination acknowledges receipt of the data. TCP is also designed to ensure that data is not corrupted in transit. TCP is used for a large variety of Internet traffic, including web browsing, email, and file transfers. While the *proportional volume* of Internet traffic that is TCP is shrinking, the *absolute volume* of TCP traffic is increasing, as the Internet grows.

Other services that use TCP as their underlying transport protocol include SSH, FTP, SMB/CIFS, and basically most things outside of streaming.

TCP is protocol number `0x6` in the IP suite.

### UDP: User Datagram Protocol

UDP is a connectionless protocol -- it's very much a fire-and-forget protocol. Pretty much as simple as it gets in terms of transport protocols. UDP is often used for streaming media, where minor packet loss or mis-ordering is acceptable. UDP is also used for DNS, DHCP, and other services where a single packet is often sufficient.

UDP is protocol number `0x11` in the IP suite.

---

## Networking Layers

Networking is a complex topic, requiring support across the entire computing stack. From physical hardware to drivers, to how to get packets from point A to point B, and who is listening for what data, there's a lot to cover. Typically, networking is discussed in terms of layers.

### OSI Model

Probably the least useful but weirdly pervasive models of the network is the 7-layer OSI model.

1. Physical

   The physical layer is the electrical, mechanical, and procedural view of the network. This layer is concerned with number of wires, physical connectors used, voltage levels, transmission mode (simplex, half- or full-duplex), etc. of the networking technology in use. Other considerations include data encoding and modulation, frequency within the EM spectrum, and more. 

   This layer, in concrete terms, is the combination of the logic implemented on an ASIC and the PHY/transceiver where you can connect a cable. For ethernet, the PHY is the RJ-45 socket combined with the ethernet controller chip on the circuit board. 

1. Data Link

   The data link layer is concerned with the logical transmission of data between two nodes on a network. For an ethernet network, this layer consists of how to find other nodes on the network, how to put data on the wire, and how to interpret received data -- in other words, the ethernet protocol, distinct from the ethernet electro-mechanical standard. Protocols that live at this layer include ARP.

   This layer of the network is all about the movement of data between two nodes on the same network. This is the layer where MAC addresses are used to identify nodes on the network rather than IP addresses. Nodes are strictly NICs, not computers. A computer with 2 NICs is seen as 2 nodes on the data link layer.

   Level 2 switches switch strictly on MAC addresses, and can only operate within the confines of a single network. They perform no routing, and are not aware of IP addresses.

1. Network

   The network layer is where IP comes into play. 

   Level 3 switches switch on IP addresses, and can operate across multiple networks. They perform routing, and are aware of IP addresses. Level 3 switches are technically routers, but in common usage routers exist on the network boundary, rather than within the network. Level 3 switches are also known as multilayer switches. Notice any terminology conflation yet?

   The primary distinction between hardware dubbed a router and hardware dubbed a level 3 switch, at the technical level, is one of provided services. A router typically runs a more general purpose OS and provides a variety of services, while a level 3 switch typically runs a more specialized OS and provides a more limited set of services. The distinction is not always clear, and the terms are often used interchangeably.

1. Transport

   TCP and UDP are the primary protocols of the transport layer. This layer is concerned with the reliable delivery of data between two nodes on a network. This is the layer where ports come into play. Ports are used to identify services on a node, and are used to multiplex multiple services on a single node. 

   The 4-tuple of $(IP_{src}, port_{src}, IP_{dest}, port_{dest})$ is the unique identifier of a network conversation. The ports in question can be either UDP or TCP (both the same), depending on the application in use. Certain applications are so well known that they have defined names (`/etc/services`) that are used interchangeably with the port number. For example, port 80 is the standard HTTP port, and port 443 is the standard HTTPS port. Other services are equally well-defined.

   Ports are divided into three ranges:

   * 0-1023: well-known ports, reserved for system services
   * 1024-49151: registered ports, reserved for user services
   * 49152-65535: dynamic ports, used for ephemeral services
  
   Administrative access is required to make use of a well-known port. The distinction between registered and dynamic ports is purely one of convention. It is neither enforced nor observed by most developers in practice, though IANA does maintain a list of registered ports.

   The transport layer is pretty much where network engineering stops. Higher layers in the stack are primarily the domain of software engineers.

1. Session

   Something, something, web application, something, something. Supposedly used for something. Ignore it.

1. Presentation

   Some sort of translation layer between the application and the network. This is where things like encryption and compression supposedly live. In practice, this layer is often ignored.

1. Application

   Everything above TCP really lives here. Application logic, user interfaces, everything. The Web is just an application living on the Internet, after all.

The OSI model isn't really useful in reality, but for some reason is part of nearly every certification exam. It's fine as an abstraction, but terribly for actually understanding how networks work. It's also not how networks are actually implemented.

At least, not how the word "network" is used within the industry.

### TCP/IP Model

The TCP/IP model is a 4-layer model, which is much more useful in practice. It is also the model used by the Linux kernel, and is the model we will use for this course. Basically, ignore layers 1, 5, and 6 of the OSI model, and you're good to go.

Because of the way network technology is defined, the physical layer is really just the physical portion of the link layer. Ethernet, as a standard, defines both physical and link layers of the OSI model. So why separate them? The TCP/IP models calls this the **link layer**.

The OSI network layer is basically IP and ICMP, and is called the **internet layer** in TCP/IP. Same layer, different name.

The transport layer is basically TCP and UDP. The application layer is everything layered on top of TCP or UDP.

It's worth pointing out here that from a networking perspective, there's no distinction between HTTP, DNS, or SSH. They are just applications running on top of TCP/IP. At the networking level, I don't care if you set up a DNS server or a gitlab instance. I just care what ports they are running on and what transport protocol they are using. Everything else is handled by the application logic.

## Network Hardware

### Switches

Technically operating purely at level 2 of the network stack, switches are used to connect multiple network nodes together. While historically networks could be a variety of topologies, the most common topology today is a star topology, where each node is connected to a central switch. A few variants exist:

* The hub-and-spoke topology, where multiple switches (each with many nodes) are connected to a central point, which is then connected to the rest of the network. This is the topology used in most enterprise networks.
* A sort of switch mesh, where multiple switches are connected to each other, and each switch is connected to multiple nodes. This is the topology used in most home networks. Topologically identical to the above, but with a different physical layout, mostly due to the needs of a home network.
* A ring topology (AKA a bus), where each switch is connected to two other switches, and the last switch is connected to the first switch. This is the topology used in most industrial networks.
* A mesh, where nodes are directly connected to other nodes, with each node acting as a switch. This is the topology used in most sensor networks.

Switches technically only operate on MAC addresses.

### Routers

Routers are just switches that operate at level 3 of the network stack, and can be used to connect multiple networks together. While in common usage, *router* is used to denote a gateway between networks, any device that uses IP addresses to switch (or route) traffic is a router. What this means in context is that a router is aware of the greater network topology.

When used internally to a network, routers are typically called level 3 switches. When used to connect networks across logical entity boundaries, they are typically called routers. The primary difference is one of software, not hardware. Routers are usually running BGP, a more general purpose OS, and often offering additional services on the network. Switches are usually running OSPF or another internal routing protocol, a more specialized OS, and offering fewer services on the network.

The distinction between an internal routing algorithm and an external routing algorithm is based on policy, knowledge of the network, and visibility. External routing algorithms have more a sense of "the thing I want is *that way*" while internal routing algorithms know all the exact paths to travel between any two points. Scale is obviously of concern. We cover this more below.

### Wireless Access Points (WAPs)

WAPs are just switches that operate over a wireless medium, typically some variant of IEEE 802.11. Topologies get really wild here due to the nature of RF communication, but the most common topology is a star topology, where each node is connected to a central WAP.

WAPs aren't typically used within home networks. The added complexity simply isn't worth it for most users. Instead, most home networks use a router with a built-in WAP. This is also the case for most small business networks. Larger businesses will typically use dedicated WAPs, as they can be more easily managed and scaled.

Most home routers are combination devices, with the functionality of a router, a switch, and a WAP all-in-one. Easy for the ISP to give to non-technical users, but terrible for anyone who wants to do anything more than the bare minimum.

### Networking Fabrics

Networks take many forms. Odds are good you interact with at 3, possibly 4, primary network technologies in everyday life:

* Ethernet/WiFi for home, school, or work networks
* LTE/5G for mobile networks
* Bluetooth for personal device networks (e.g. headphones, smartwatches, etc.)
* Controller area networks (CAN) for any car built in this century. And many built last century, too!

Each of these technologies uses a different physical layer, each with its own mechanical and electrical properties. Each is standardized by a different standards body, and each has its own quirks, limitations, and advantages. In the case of mobile networks, the business needs drive its distinction from WiFi, despite the fact that they are both based on the same underlying technology (digital RF). Bluetooth differs from WiFi in terms of power, bandwidth, and range, but is otherwise very similar. CAN is a completely different beast, and is used for very different purposes.

Each physical layer used is a different *fabric*, or the physical object that provides interconnection between nodes. It can be fiber optic cabling, copper wire (as in ethernet), coaxial wire, RF waves, etc. Basically, if you can use it for some signaling, you can probably use it for networking in some fashion.

Then there are the more "exotic" networks, such as those based on RS-485, RS-232, or other serial protocols. BACnet -- the building automation and control network -- connects industrial systems such as HVAC and access control and runs over a variety of physical network media.

Oh, and then we have mesh networks operating over wireless (not WiFi) signals, such as LoRaWAN, Zigbee, Zwave, Thread, etc. These are typically used for IoT devices, and are often proprietary. 

And let's not forget the really unusual stuff, like digital modes over HAM radio. In many cases, these are based on the same precursors as the Internet, but are not the Internet. Some connect to the Internet. Most don't. People often ignore this aspect of networking, but in an emergency, it might be the only thing we have left for area-wide communication.

Yes, we could have an entire term dedicated to this topic. Anyone interested?

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

One of the most basic things we need to know about a system on the network is its IP address. Assuming you have access to the host, the simplest way to find the IP address is with one of the following commands:

```sh
$ ifconfig
docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        inet6 fe80::42:82ff:fea4:7efd  prefixlen 64  scopeid 0x20<link>
        ether 02:42:82:a4:7e:fd  txqueuelen 0  (Ethernet)
        RX packets 29  bytes 1828 (1.8 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 66  bytes 7787 (7.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

enp0s1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.37.129.2  netmask 255.255.255.0  broadcast 10.37.129.255
        inet6 fe80::746d:65ff:fe10:9ea1  prefixlen 64  scopeid 0x20<link>
        ether 76:6d:65:10:9e:a1  txqueuelen 1000  (Ethernet)
        RX packets 766  bytes 394784 (394.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 111  bytes 25678 (25.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 28672  bytes 2123134 (2.1 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 28672  bytes 2123134 (2.1 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

veth60197a2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::d8e9:e3ff:fe07:6b1c  prefixlen 64  scopeid 0x20<link>
        ether da:e9:e3:07:6b:1c  txqueuelen 0  (Ethernet)
        RX packets 29  bytes 2234 (2.2 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 101  bytes 11689 (11.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

```

```sh
$ ip address show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 76:6d:65:10:9e:a1 brd ff:ff:ff:ff:ff:ff
    inet 10.37.129.2/24 metric 100 brd 10.37.129.255 scope global dynamic enp0s1
       valid_lft 85641sec preferred_lft 85641sec
    inet6 fe80::746d:65ff:fe10:9ea1/64 scope link 
       valid_lft forever preferred_lft forever
3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:82:a4:7e:fd brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:82ff:fea4:7efd/64 scope link 
       valid_lft forever preferred_lft forever
5: veth60197a2@if4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default 
    link/ether da:e9:e3:07:6b:1c brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::d8e9:e3ff:fe07:6b1c/64 scope link 
       valid_lft forever preferred_lft forever

```

### `netstat`

`netstat` is an older tool, but has the benefit of being available on most systems. It can be used to display open sockets, routing tables, link statistics, and more. It is especially useful for determining what processes are listening on what ports.

```sh
$ #get numeric list of listening TCP and UDP sockets
$ sudo netstat -tunl
```

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

See the [tcpdump](tcpdump.md) page.

### Wireshark

See the [wireshark](wireshark.md) page.

### Other capture tools

* NIDS/NIPS
* Windows NDIS tools
* Darkstat
