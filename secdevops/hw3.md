Homework 3
Due Date: 2023-11-13 23:59:59
Submission: via GitLab repo

* auto-gen TOC:
{:toc}

## Introduction

As of now, the Ubuntu machine you are using isn't really doing anything useful. Let's fix that!

## Tasks

These are high-level requirements, not guidance on the steps to use.

1. Install a containerized samba server on your Ubuntu machine. This should be configured to share a directory on your Ubuntu machine via a mapped volume in your container. This directory should be accessible from your host machine. Document the installation and configuration in your `hw3.md` file.
1. Install a containerized pi-hole DNS server on your Ubuntu machine. Document the installation and configuration in your `hw3.md` file.
1. Create a docker-compose.yml file that will start both of these containers. Document the configuration in your `hw3.md` file.

Keep in mind, this might require additional firewall rules to be added to your bastion host. Document these in your `hw3.md` file.

## Submission

Once you have completed the above, you should have a markdown file in your repo called `hw3/hw3.md` that contains all the requested information above. Commit and push this to your repo. Also commit and include the requested screenshots. Once you have done this, you can consider the assignment submitted.
