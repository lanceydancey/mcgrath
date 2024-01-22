# Network Reconnaissance

* auto-gen TOC:
{:toc}

This page really takes a strong view of nmap, and attempts to make you as comfortable as possible with the tool. It's quite often one of the first tools you will pull out when looking at a network target -- what services, ports, protocols, etc. are running on the target?

Often the prelude to a packet capture, this does sometimes go in the other direction. If we can hang the target device off a network link we control, it's possible to tap the link and observe any and all traffic that terminates or originates with the target machine. Ofttimes though, network targets are passively listening, waiting for inbound connections. A packet capture can't tell you that, but an nmap scan can!

And sure, you absolutely could write your own tools for this. Sometimes that's even the only way to do what you want -- nmap is so well known in the industry that some network stacks identify and ignore the packets it creates. In those cases, you really do need to craft a scanner yourself. In an ideal world, nmap would never work. Fortunately for security researchers, the world is not perfect and nmap works more often than it fails!

## `nmap`

Nmap is a network mapping tool which runs on many different platforms. Below you can see a simple asciinema recording of it's help documentation (no audio).

As a tool, nmap has operational modes including (but not limited to)

scanning a single host for open TCP ports
scanning a single host for open UDP ports
scanning a network for active hosts
in depth scanning a network
Because of the sheer scope of capability, some of the functionality requires root privileges. Because we are running as root on our Kali VMs, this isn't something that you will need to worry too much about.

A simple example, taken from the manpage (man nmap) can be see below.