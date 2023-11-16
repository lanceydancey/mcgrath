Final Project
Due Date: 2023-12-08 23:59:59
Submission: via GitLab repo

* auto-gen TOC:
{:toc}

## Introduction

And now it is time to add more services! For this assignment, you will be doing one several tasks, depeding on if you registered for CS410 or CS510.

## Tasks

These are high-level requirements, not guidance on the steps to use.

1. CS410/510: Install a gitlab instance on your ubuntu system. This should be fully containerized and added to your docker-compose.yml file. Document the installation and configuration in your `final.md` file.
1. CS410/510: Install a dockerized, self-hosted bitwarden instance. You aren't required to make use of it, but it needs to be there. This will allow you to keep all your passwords in one place -- *that you control*. Configuration files should live on a mapped volume. Document the installation and configuration in your `final.md` file.
1. CS410/510: Install a containerized ZoneMinder, for security camera monitoring. This should be configured to use a mapped volume for storage. Document the installation and configuration in your `final.md` file.
1. CS510: This last task is a bit more nuanced and will require some research. Take a look at how GitHub generates static pages for githubio. You will be creating something similar with the gitlab instance you set up. This will require you to create a static site generator (e.g. Jekyll) and have it generate a static site from a gitlab repo via some form of CI/CD pipeline. This should be fully containerized and added to your docker-compose.yml file. Document the installation and configuration in your `final.md` file.


Keep in mind, this might require additional firewall rules to be added to your bastion host. Document these in your `final.md` file.

## Submission

Once you have completed the above, you should have a markdown file in your repo called `final/final.md` that contains all the requested information above. Commit and push this to your repo. Also commit and include the requested screenshots. Once you have done this, you can consider the assignment submitted.
 