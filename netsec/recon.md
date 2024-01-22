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

A simple example, taken from the manpage (man nmap) can be seen below:

[![asciicast](https://asciinema.org/a/CmhLzEBrcMo0pfI5N4ujVggfQ.svg)](https://asciinema.org/a/CmhLzEBrcMo0pfI5N4ujVggfQ)

While the above example is simplistic (and taken from the manpage, as described in the cast), it should give you a sense of the scope of nmap. By the way, try copy/pasting the example given in the cast into a terminal session on your Kali VM.

For the immense documentation, please see the [Nmap docs](https://nmap.org/book/man.html).

## Things to try yourself!

1. Simple scans
   1. Take a look at the nmap man page (man nmap), and then perform the following scans on host scanme.nmap.org:
       * a TCP connect() scan of ports 20-100, 130-150, and 400-500
       * a UDP scan of the top 100 ports
       * an OS detection scan
       * an IP protocol scan
   1. Try at least 2 output modes, as well. Personally, I find the s|\<rIpt kIddi3 output amusing.
1. Scans using CIDR notation
   1. Try scanning your VM's subnet, on TCP ports 20-25. What do you see?
   1. Take a look at nmap manpage again, under TARGET SPECIFICATION. Try some of the other options:
        * combine CIDR notation and an exclude list specified on the command line
        * create a list of hosts to scan and pass that
        * any other option that captures your interest
1. Scan your VM's subnet on both TCP and UDP, all ports, OS detection enabled with aggressive guessing. Again, take a look at the manpage for how to do some of these.

    I would STRONGLY recommend you start with a simple discovery scan to identify live targets on the network, then use an input host file to narrow the scope of your scanning to only those hosts. With this optimization, my subnet took about 3 minutes for a complete scan. YMMV.

I'll be going over these exercises in class, but I would encourage you to try them on your own first. If you get stuck, please reach out for assistance! I'm happy to help. I'll be recording a screen capture as usual, but will also post an asciinema link below.
