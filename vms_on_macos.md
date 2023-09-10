# VM Setup on macOS without paying for virtualization software

## Common tools

Setting up a VM on macOS is relatively straightforward. While you could spend lots of money to get a commercial hypervisor like Parallels Desktop or VMware Fusion, that's...ridiculous. Sure, they can do some fancy stuff, but we are sticking with open source solutions! Plus, they cost lots of money, and that's just wrong.

So, what can we use? Well, there's the option of VirtualBox if you're on an Intel Mac. But a) that requires you are on an Intel Mac, b) that requires you interact with Oracle, and c) it has been nothing but trouble in my past classes. So, don't use it. Instead, we'll use the [Universal Turing Machine (UTM)](https://github.com/utmapp/UTM/releases) software. It's free, it's open source, and it's pretty easy to use. It's also a Universal app, so it runs on both Intel and Apple Silicon Macs. More importantly, it provides an easy-to-use wrapper around the QEMU hypervisor, which is what we'll be using to run our VMs.

Alternatively, if you're a brew user, you can use

```sh
$ brew install --cask utm
```

to get UTM installed. If you're really feeling like you want to do things "The Linux Way", you can install `libvirt` and `virt-manager` via brew, and use that to manage your VMs. I'm not going to cover that here, but it's an option. 

Or, you can go full masochist and use `qemu` directly. I'm not going to cover that here, either. And if you think it makes sense, why are you here? Go away. Or better yet, talk to me about becoming a TA.

## Running on Intel

If you're using an Intel Mac, you're in luck. You can take the easy road for the virtual network setup. Well, mostly easy. You could use [pfSense](https://www.pfsense.org/) directly, rather than using FreeBSD and then setting up tools yourself. But, that just isn't nearly as much fun. So read the next section and do it that way. Yes, I'm serious. You had to actually learn math before you got to use the calculator, right? Same thing here. And if that wasn't the case for you, just smile, nod, and pretend it was.

## Running on Apple Silicon (M1+)

Alas, you don't get to take the easy road, because for reasons that escape me, Netgate doesn't build ARM versions of pfSense except for their own hardware. And building pfSense for ARM is an exercise in frustration, because they go so far as to tell you to just purchase their hardware when you try. Blah, annoying. But hey, even if we could use pfSense, we aren't going to, because the Intel folks don't get to either.

So, instead of installing pfSense, just install [FreeBSD](https://download.freebsd.org/ftp/releases/ISO-IMAGES/13.2/FreeBSD-13.2-RELEASE-arm64-aarch64-dvd1.iso.xz), which is what pfSense runs on anyway. This is actually better, because we get to run on a more up-to-date platform, and we aren't missing a bunch of useful tools like the pfSense folks. Plus, we get to learn how to do things the hard way, which is always fun, right?

Once you have the freeBSD machine up and running, you can use [this script](freebsd_setup.sh) to do most of what we get from pfSense. You didn't think I was actually going to make you do all of this by hand, did you? That's just cruel. And part of what you get to do if you take my network security class. So, you know, you can do it then. But not now. Now, you get to use the script. And you'll be happy about it.

## Virtual Network Setup

In either case, once you have the basic VMs, you still need networking setup. Since we want to use the BSD machine as a virtual router/switch/firewall, we need to make sure other VMs can see it, and only try to connect through it. To do this, we need to create a virtual network adapter. This is done by clicking on the "Network" tab in UTM, and then clicking the "+" button in the bottom left corner. This will create a new network interface, which we can then configure. We'll want to set the "Network Mode" to "Host Only".

At this point, you should have two network interfaces: one for the WAN, and one for the LAN. The WAN interface should be configured as a "Shared Network" for "Network Mode" -- unless you have multiple Wireless NICs, in which case you can totally go "Bridged (Advanced)," but that's not too likely on laptop hardware. I would recommend the first network device be you WAN, and the second be your LAN, which should be the one you just created.

