Homework 2
Due Date: 2023-10-30 23:59:59
Submission: via GitLab repo

* auto-gen TOC:
{:toc}

## Introduction

This homework is intended to give you some experience modifying firewall rules by hand, as well as integrating snort into your bastion host environment.

## Tasks

1. Create a firewall rule that will forward `ssh` traffic from bastion host port 22 to your Ubuntu system port 22. Document your entire ruleset in your `hw2.md` file.
2. Modify the local ssh server on the firewall to move it to a different port for management purposes. Document the changes in your `hw2.md` file.
3. Install `snort` on your bastion host. Have it load at boot time so that it's actively protecting your network. Document installation, configuration, and testing in your `hw2.md` file.
4. Ensure `snort` can protect against [SMBGhost](https://github.com/jamf/CVE-2020-0796-RCE-POC) attacks. Document this in your `hw2.md` file.

In the end, you should have documentation that will allow you to recreate your environment from scratch, including all firewall rules and snort configuration. This will come in handy later...

A shell script that handles much of the above is also required. This script should be in your repo, and should be called `hw2.sh`. This script should be able to be run on a fresh install of FreeBSD, and should be able to configure the system to match your environment. You should ensure this script can run multiple times without error.

## Submission

Once you have completed the above, you should have a markdown file in your repo called `hw2/hw2.md` that contains all the requested information above. Commit and push this to your repo. Also commit and include the requested screenshots. Once you have done this, you can consider the assignment submitted.
