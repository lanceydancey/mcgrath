Homework 4
Due Date: 2023-12-01 23:59:59
Submission: via GitLab repo

* auto-gen TOC:
{:toc}

## Introduction

Let's add some useful services to our lab environment! For this assignment, we will be adding a VPN server to our Ubuntu system. Right behind the firewall is a typical location for a VPN server. This will allow us to access our lab environment from anywhere in the world.

## Tasks

These are high-level requirements, not guidance on the steps to use.

1. Install a containerized Wireguard or OpenVPN VPN server. Document the installation and configuration in your `hw3.md` file.
1. Add to your docker-compose.yml file that will start your VPN. Document the configuration in your `hw4.md` file.
1. Verify that you can connect to this VPN endpoint. You will likely want to do this from your VM host machine, unless you have bridged adapters to your VM. Document the configuration in your `hw4.md` file.
1. Install a containerized [Wazuh](https://wazuh.com/) to provide security monitoring. You want the "all-in-one" version, but you'll also want to install an agent on the FreeBSD system to monitor logs. Document the installation and configuration in your `hw4.md` file.

Keep in mind, this might require additional firewall rules to be added to your bastion host. Document these in your `hw4.md` file.

## Submission

Once you have completed the above, you should have a markdown file in your repo called `hw4/hw4.md` that contains all the requested information above. Commit and push this to your repo. Also commit and include the requested screenshots. Once you have done this, you can consider the assignment submitted.
