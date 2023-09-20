* auto-gen TOC:
{:toc}

## Introduction

`tcpdump` is a command line utility for capturing packets. While the name would imply that it can only capture TCP packets, it will also capture UDP based flows. The tool can be used on arbitrary interfaces, capturing either or both directions (in/out), capture only packets which match a filter, etc.

`tcpdump` is one of those foundational tools. While there are newer packet capture tools, including GUI versions (such as `wireshark`), ultimately they all come down to a wrapper around `libpcap` -- of which `tcpdump` is the front-end. With low overhead, lots of flexibility, and a no-frills approach to packet capture, `tcpdump` really is the tool you'll keep coming back to. So many systems I work with don't have any graphical UI -- learning `tcpdump` first has really benefited me over the years. And I've yet to encounter a linux based product that doesn't have it!

Take a look at the following example usages.

[![Take a look at the following example usages](https://asciinema.org/a/qtZ2vHn8jMKDCHyBDZog42Cyg.svg)](https://asciinema.org/a/qtZ2vHn8jMKDCHyBDZog42Cyg?speed=2)

Some specific options to call out here:

* `-c count`: Exit after receiving count packets.
* `--print`: Print parsed packet output, even if the raw packets are being saved to a file with the `-w` flag.
* `-Q direction`/`--direction=direction`: Choose send/receive direction for which packets should be captured. Possible values are `in`, `out` and `inout`.
* `-w file`: Write the raw packets to `file` rather than parsing and printing them out. They can later be printed with the `-r` option. Standard output is used if `file` is `-`.
* `-r file`: Read packets from `file`

## Direction Capture
From the simple options shown above, we can get more complex in terms of capturing. Let's do the same example, but only capture outbound traffic.

[![only capture outbound traffic](https://asciinema.org/a/7u0ceIDd0qILcbYEnHI0dQp71.svg)](https://asciinema.org/a/7u0ceIDd0qILcbYEnHI0dQp71?speed=2)

And now again, but inbound traffic.

[![now again, but inbound traffic](https://asciinema.org/a/wJ13zD7KzjvHttYD9JsHD2t4t.svg)](https://asciinema.org/a/wJ13zD7KzjvHttYD9JsHD2t4t?speed=2)

And again, explicitly capturing both directions.

[![explicitly capturing both directions](https://asciinema.org/a/a1hu60MhoQ6bDX6WPVHKEWabm.svg)](https://asciinema.org/a/a1hu60MhoQ6bDX6WPVHKEWabm?speed=2)

## Filters

`tcpdump` supports the usage of filters to limit what is capture (or displayed). These filters can be applied at the time of capture, or at the time of view (with `tcpdump -r`). Filters are an expression which is passed to `tcpdump` and consists of one or more primitives, where primitives consist of a qualified `id`. Qualifiers take the form of a type (host, port, etc.), a direction (`src`, `dst`, etc.), and a protocol (`tcp`, `udp`, `ether`, etc.). Primitives can be combined with and, or, and not. A quick cast could make this clearer:

[![Filters](https://asciinema.org/a/KJsIN73DArJJA5EaOamc0q2WW.svg)](https://asciinema.org/a/KJsIN73DArJJA5EaOamc0q2WW?speed=2)

Filters use a notation known as `BPF`, or Berkeley packet filter. See `man pcap-filter` for more information. Don't be fooled that there is a `bpf` page in section 4 of the manual. That's for the pseudo-device that the kernel exposes.

Interestingly enough, the Linux kernel supports `eBPF`, which is the extended `BPF`. This provides a Turing-complete language that can be used to instantiate many different, potentially complex, operations. Which, of course, means it is also a security nightmare and the source of many CVEs over the years.

## Interface-specific capture

You can use the `-i` flag to `tcpdump` to specify a particular interface on which to capture. I use this frequently when I am capturing both ends of a conversation, or from multiple taps. Many taps have USB interfaces, and present as a USB ethernet adapter -- this flag allows you to specify that interface, so you can capture from it rather than the default interface.

There's also a special interface called `any` that captures from ALL interfaces. This can be useful in situations where you are unsure which interface is being used, or if you really do want to capture all network traffic hitting your machine.

## Additional resources

There are many online sources of information about tcpdump.

* Online libpcap man page: https://www.tcpdump.org/manpages/pcap.3pcap.html
* Online tcpdump man page: https://www.tcpdump.org/manpages/tcpdump.1.html
* List of many examples: https://danielmiessler.com/study/tcpdump/
