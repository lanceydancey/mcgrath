Homework 1
Due Date: 2021-10-09 23:59:59
Submission: via GitLab repo

* auto-gen TOC:
{:toc}

## Introduction

This homework is intended for you to provide verification of a functional mini-lab environment. You will be using this environment for the rest of the term. In theory, you have already completed nearly all of this. However, I want to make sure that you have a working environment before we get too far into the term.

All work will be submitted via MarkDown documents within a gitlab repo. You will be using this repo for the rest of the term. This repo exists on the CECS intranet.

## Tasks

1. Create a [GitLab repo](https://gitlab.cecs.pdx.edu/) called `secdevops-<CECS>` (replace <CECS> with your actual MCECS username) and clone it to your local machine. You will be using this repo for the rest of the term. This repo exists on the CECS intranet, and uses your CECS credentials for authentication.
1. Create a folder within the repo called `hw1`. This is where you will add documentation regarding this assignment.
1. Now that you have your repo set up, we'll be turning to the VMs. Follow one of the [macOS](../vms_on_macos.md) or [Windows](../hyper-v.md) instructions to get a pair of VMs setup and configured. I would suggest you document everything you did in a markdown file in your repo called `hw1.md`.
   1. Take a screenshot of the FreeBSD VM with the output of the command `ifconfig` showing. Add this to your repo and include it in your `hw1.md` file.
   1. Take a screenshot of the Ubuntu VM with the output of the command `ip a s` showing. Add this to your repo and include it in your `hw1.md` file.
1. Follow the instructions on the [Ubuntu configuration](../ubuntu.md) page to configure the Ubuntu VM. Document this in your `hw1.md` file.
1. Include the contents of your `~/.ssh/config` file in your `hw1.md` file, to show you have a bastion or jump host configured.

## Submission

Once you have completed the above, you should have a markdown file in your repo called `hw1/hw1.md` that contains all the requested information above. Commit and push this to your repo. Also commit and include the requested screenshots. Once you have done this, you can consider the assignment submitted.