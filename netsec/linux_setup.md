Kali Configuration

* auto-gen TOC:
{:toc}

At this point, you should have an Ubuntu Server VM running. If you don't, go back and do that. I'll wait. If you do, then you're ready to start configuring it.

## System configuration

First, let's make sure it's up to date:

```sh
$ sudo apt update
$ sudo apt upgrade -y
```

You may have seen these commands before, but if you haven't, here is what's happening. `apt update` pulls down new package index files for any and all repositories that you have defined. If you haven't added any yet, it will just update the default set. `apt upgrade` will then upgrade any packages that have updates available. The `-y` flag tells it to apply the upgrades without awaiting confirmation. This is useful for scripting, but not so much for interactive use. If you want to see what it's going to do before it does it, just leave off the `-y`.

### Install useful tools

OK, so we're likely still sitting on a barebones kali install. We should fix that.

There is a script in this repo that will install a bunch of useful tools. You can run it with:

```zsh
$ curl 
```
