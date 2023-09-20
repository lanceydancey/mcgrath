Networking Fundamentals needed for System Administration

* auto-gen TOC:
{:toc}

## TCP, UDP, IP, and ICMP

These protocols form the backbone of the modern Internet. But what are they?

### IP: Internet Protocol

The internet protocol is the underlying 

* IPv4
    * Classes of IPv4 addresses
    * CIDR notation
    * Private IP ranges
* IPv6

### ICMP: Internet Control Message Protocol

Weird stuff here. While ICMP is typically considered part of the Internet layer, it's encapsulated within an IP packet...but it isn't really the same type of protocol as TCP or UDP. It's a control protocol rather than a transport protocol, and so is rightfully considered part of the 

### TCP: Transmission Control Protocol

TCP is what is known as a connection-oriented protocol. This means that it is designed to ensure that data is delivered to the destination in the order it was sent, and that the destination acknowledges receipt of the data. TCP is also designed to ensure that data is not corrupted in transit. TCP is used for a large variety of Internet traffic, including web browsing, email, and file transfers. While the *proportional volume* of Internet traffic that is TCP is shrinking, the *absolute volume* of TCP traffic is increasing, as the Internet grows.

Other services that use TCP as their underlying transport protocol include SSH, FTP, SMB/CIFS, and basically most things outside of streaming. 

TCP is protocol number `0x6` in the IP suite.

<table class="wikitable" style="margin: 0 auto; text-align:center">
<caption>TCP segment header
</caption>
<tbody><tr>
<th colspan="2"><i>Offsets</i>
</th>
<th colspan="8" style="border-left:1px; text-align:left;">0
</th>
<th colspan="8" style="border-left:1px; text-align:left;">1
</th>
<th colspan="8" style="border-left:1px; text-align:left;">2
</th>
<th colspan="8" style="border-left:1px; text-align:left;">3
</th></tr>
<tr>
<th><a href="/wiki/Octet_(computing)" title="Octet (computing)">Octet</a></th>
<th><a href="/wiki/Bit" title="Bit">Bit</a>
</th>
<th style="text-align:left;">0</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>0</th>
<th>1
</th>
<th style="text-align:left;">2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>0</th>
<th>1</th>
<th>2</th>
<th>3
</th>
<th style="text-align:left;">4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>0</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5
</th>
<th style="text-align:left;">6</th>
<th>7
</th></tr>
<tr>
<th>0
</th>
<th>0
</th>
<td colspan="16">Source port</td>
<td colspan="16">Destination port
</td></tr>
<tr>
<th>4
</th>
<th>32
</th>
<td colspan="32">Sequence number
</td></tr>
<tr>
<th>8
</th>
<th>64
</th>
<td colspan="32">Acknowledgment number (if ACK set)
</td></tr>
<tr>
<th>12
</th>
<th>96
</th>
<td colspan="4">Data offset</td>
<td colspan="4">Reserved<br><b>0 0 0 0</b></td>
<td><span style="writing-mode: vertical-lr; text-orientation: upright; letter-spacing: -0.12em; line-height:1em; width:1em;">CWR</span></td>
<td><span style="writing-mode: vertical-lr; text-orientation: upright; letter-spacing: -0.12em; line-height:1em; width:1em;">ECE</span></td>
<td><span style="writing-mode: vertical-lr; text-orientation: upright; letter-spacing: -0.12em; line-height:1em; width:1em;">URG</span></td>
<td><span style="writing-mode: vertical-lr; text-orientation: upright; letter-spacing: -0.12em; line-height:1em; width:1em;">ACK</span></td>
<td><span style="writing-mode: vertical-lr; text-orientation: upright; letter-spacing: -0.12em; line-height:1em; width:1em;">PSH</span></td>
<td><span style="writing-mode: vertical-lr; text-orientation: upright; letter-spacing: -0.12em; line-height:1em; width:1em;">RST</span></td>
<td><span style="writing-mode: vertical-lr; text-orientation: upright; letter-spacing: -0.12em; line-height:1em; width:1em;">SYN</span></td>
<td><span style="writing-mode: vertical-lr; text-orientation: upright; letter-spacing: -0.12em; line-height:1em; width:1em;">FIN</span></td>
<td colspan="16">Window Size
</td></tr>
<tr>
<th>16
</th>
<th>128
</th>
<td colspan="16">Checksum</td>
<td colspan="16">Urgent pointer (if URG set)
</td></tr>
<tr>
<th>20<br>
</th>
<th>160<br>
</th>
<td colspan="32" rowspan="3" style="background:#ffd0d0;">Options (if <i>data offset</i> &gt; 5. Padded at the end with "0" bits if necessary.)<br>
</td></tr>
<tr>
<th>⋮
</th>
<th>⋮
</th></tr>
<tr>
<th>56
</th>
<th>448
</th></tr></tbody></table>

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

   The 4-tuple of *(IP<sub>src</sub>, port<sub>src</sub>, IP<sub>dest</sub>, port<sub>dest</sub>)* is the unique identifier of a network conversation. The ports in question can be either UDP or TCP (both the same), depending on the application in use. Certain applications are so well known that they have defined names (`/etc/services`) that are used interchangeably with the port number. For example, port 80 is the standard HTTP port, and port 443 is the standard HTTPS port. Other services are equally well-defined.

   Ports are divided into three ranges:

   * 0-1023: well-known ports, reserved for system services
   * 1024-49151: registered ports, reserved for user services
   * 49152-65535: dynamic ports, used for ephemeral services
  
   Administrative access is required to make use of a well-known port. The distinction between registered and dynamic ports is purely one of convention. It is neither enforced nor observed by most developers in practice, though IANA does maintain a list of registered ports.

   The transport layer is pretty much where network engineering stops. Higher layers in the stack are primarily the domain of software engineers.

1. Session

   Something, something, web application something. Supposedly used for something. Ignore it.

1. Presentation

   Some sort of translation layer between the application and the network. This is where things like encryption and compression supposedly live. In practice, this layer is often ignored.

1. Application

   Everything above TCP really lives here. Application logic, user interfaces, everything. The Web is just an application living on the Internet, after all.

The OSI model isn't really useful in reality, but for some reason is part of nearly every certification exam. It's fine as an abstraction, but terribly for actually understanding how networks work. It's also not how networks are actually implemented.

At least, not how the word "network" is used within the industry.

### TCP/IP Model

The TCP/IP model is a 4-layer model, which is much more useful in practice. It is also the model used by the Linux kernel, and is the model we will use for this course. Basically, ignore layers 1, 5, and 6 of the OSI model, and you're good to go.

Because of the way network technology is defined, the physical layer is really just the physical portion of the link layer. Ethernet, as a standard, defines both physical and link layers of the OSI model. So why separate them?

The network layer is basically IP and ICMP. The transport layer is basically TCP and UDP. The application layer is everything layered on top of TCP or UDP.

It's worth pointing out here that from a networking perspective, there's no distinction between HTTP, DNS, or SSH. They are just applications running on top of TCP/IP. At the networking level, I don't care if you set up a DNS server or a gitlab instance. I just care what ports they are running on and what transport protocol they are using. Everything else is handled by the application logic.

## Network Hardware

### Fabric

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

### Networking PHYs

Networks take many forms. Odds are good you interact with at 3, possibly 4, primary network technologies in everyday life:

* Ethernet/WiFi for home, school, or work networks
* LTE/5G for mobile networks
* Bluetooth for personal device networks (e.g. headphones, smartwatches, etc.)
* Controller area networks (CAN) for any car built in this century. And many built last century, too!

Each of these technologies uses a different physical layer, each with its own mechanical and electrical properties. Each is standardized by a different standards body, and each has its own quirks, limitations, and advantages. In the case of mobile networks, the business needs drive its distinction from WiFi, despite the fact that they are both based on the same underlying technology (digital RF). Bluetooth differs from WiFi in terms of power, bandwidth, and range, but is otherwise very similar. CAN is a completely different beast, and is used for very different purposes.

Then there are the more "exotic" networks, such as those based on RS-485, RS-232, or other serial protocols. BACnet -- the building automation and control network -- connects industrial systems such as HVAC and access control...and runs over a variety of physical network media.

Oh, and then we have mesh networks operating over wireless (not WiFi) signals, such as LoRaWAN, Zigbee, Zwave, Thread, etc. These are typically used for IoT devices, and are often proprietary.

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
