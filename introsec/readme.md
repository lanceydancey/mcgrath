# CS 491/591: Introduction to Security

## Course Description

This class provides an overview of computer security intended for a broad audience. Topics covered include basic security principles, access control, cryptography, authentication, network security, host security, application security, and privacy and anonymity with a focus on how they are embodied in actual systems.

### Course objectives

1. Explain the concepts of confidentiality, availability and integrity.
1. Explain standard access control mechanisms (mandatory, discretionary, originator controlled) and how they can be used in conjunction with security models.
1. Describe use of cryptographic algorithms in various secure protocols including digital signatures, hash functions, symmetric key, and public key cryptography.
1. Explain various forms of authentication and identify social engineering attacks.
1. Explain security issues in networks, hosts, and applications and how they can be addressed
1. Identify privacy issues in computing systems and how they can be addressed

### Policies

|-|-|-|-|
|Grading|Attendance and participation|Academic Misconduct|
|Attendance&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5%<br>Lab&nbsp;notebooks&nbsp;&nbsp;&nbsp;65%<br>Final&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;30%|Attendance is required and will be taken each class. If you miss class, extra credit will be given back for outside communication that indicates you are keeping up with the material. You are expected to follow this [code of conduct](https://www.mozilla.org/en-US/about/governance/policies/participation/) when communicating.| Includes allowing another student to copy your work unless specifically allowed by the instructor.<br>Results in a grade of 0 for the assignment or exam.<br>Results in the initiation of disciplinary action at the [university level](https://www.pdx.edu/dos/academic-misconduct).

## Schedule

| Week | Topic | Labs | Due on Monday |
| ---- | ----- | ---- | ------------- |
| 1 | Introduction<br>Careers and Roles in Cybersecurity (CyberPDX)<br>Principles and Approaches<br>Access Control and Authorization<br>Linux Basics (files, commands)| [Labs #1](https://codelabs.cs.pdx.edu/cs491/?cat=Nb01)| |
| 2 | Linux basics (command I/O, shell navigation, advanced files)<br>Basics (regex, file utilities, network commands, processes) | [Labs #2](https://codelabs.cs.pdx.edu/cs491/?cat=Nb02)|Labs #1|
| 3 | Linux Access Control (permissions, setuid, sudo)<br>Applied cryptography: Encoding, Hash functions, Message Authentication Codes<br>Applied Cryptography: Symmetric, Asymmetric (Public-Key) encryption | | |
| 4 | Applied Cryptography: Digital signatures, Certificates, Key exchange protocols, Perfect Forward Secrecy, Future Secrecy, Signal protocol<br>Authentication: Password security, Multi-factor authentication | [Labs #3](https://codelabs.cs.pdx.edu/cs491/?cat=Nb03)| Lab #2|
| 5 | Authentication: FIDO/Passkeys (Passwordless authentication), Zero-trust and continuous authentication<br>Social engineering (Spam, Phishing, Business Email Compromise, Scams, Fraud)<br>Network security: Data-link layer (802.11, WPA2)| [Labs #4](https://codelabs.cs.pdx.edu/cs491/?cat=Nb04) | Labs #3 |
| 6 | Network Security: Data-link layer (ARP), Network layer (IP, CIDR, Sniffing, Spoofing, Hijacking)<br>Network Security: Network layer (DDoS, IPSec/VPNs, firewalls and filtering, network segmentation, network intelligence, ICMP) | [Labs #5](https://codelabs.cs.pdx.edu/cs491/?cat=Nb05) | Labs #4 |
| 7 | Network Security: Transport layer (TCP, TLS, certificate authorities and transparency, certificate revocation), Application layer: DNS security (DNS, DNSSEC) <br> Network Security: Application layer - DNS security (DoH, DoT, Oblivious DNS), E-mail security (SMTP/IMAP/POP over TLS, DKIM, SPF, DMARC)<br>Host Security: Host attacks (Initial access, Privilege escalation)| | |
| 8 | Host attacks (Internal recon, Lateral movement, Persistence, Impact)<br>Host defenses (IDS/IPS/EDR, signature detection, anomaly detection, blocklisting and allowlisting, Software signing, Virtualization and isolation techniques, File system backup and encryption)<br>Application security: DevSecOps| [Labs #6](https://codelabs.cs.pdx.edu/cs491/?cat=Nb06)| Labs #5 |
| 9 | Programming language and CPU security, Memory corruption, Return-oriented Programming, Canaries, ASLR, Control-Flow Integrity | [Labs #7](https://codelabs.cs.pdx.edu/cs491/?cat=Nb07)| Labs #6 |
| 10 | Supply-chain security <br> Privacy and anonymity security| | |
| Finals week | | | |
| | | | |

We will not be meeting the week of finals, and I will not be holding office hours. I will be available via email, but may not reply immediately, or even the same day.

## Assignments

### Labs and notebook

Lab assignments will be given each class covering the course material. You will perform each one, while maintaining a lab notebook in markdown that documents your progress via screenshots with your OdinID in them. The notebook should also include answers to any questions in the labs. Notebooks should be done in Markdown in their respective folders. Submission will be done via adding, committing and pushing the files to your private GitLab repository.

Please add myself (dkmcgrath) and your TA as collaborators to your private repo. You can do this by going to the settings page for your repo, clicking on the "Manage access" tab, and then clicking on the "Invite a collaborator" button. You will need to add both myself and your TA as collaborators.

Always turn in what you have done on-time. Late work throughout the quarter may be compiled into a single submission that will be graded at the end of the last week of class in a file named notebooks/LateLabs.pdf. The notebook will be graded based upon the following rubric:

* Neatness and organization
* Completeness
* Inclusion of OdinID or project identifier in screenshots

## Useful links for learning

* [tmux cheatsheet](https://tmuxcheatsheet.com/)
* [Linux Handbook on tmux](https://linuxhandbook.com/tmux/)
* [Markdown](https://guides.github.com/features/mastering-markdown/)
* [The C Book](https://publications.gbdirect.co.uk/c_book/)
* [The GNU `make` manual](https://www.gnu.org/software/make/manual/make.pdf)
* [Managing projects with `make`](https://github.com/Vauteck/docs_utils/blob/master/autotools/Oreilly%20-%20Managing%20Projects%20With%20Gnu%20Make%203Rd%20Edition.pdf)
* [The `chmod` calculator](https://chmod-calculator.com/)
* [The Python tutor](https://pythontutor.com/)
* [_The Linux Command Line_](http://linuxcommand.org/tlcl.php) (Direct [PDF link](https://sourceforge.net/projects/linuxcommand/files/TLCL/19.01/TLCL-19.01.pdf/download))
* [_Adventures with the Linux Command Line_](https://sourceforge.net/projects/linuxcommand/files/AWTLCL/21.10/AWTLCL-21.10.pdf/download)
* [_The Linux Development Platform_](https://archive.org/details/ost-computer-science-0130091154/mode/1up)
* [gdb tutorial](http://www.cs.cmu.edu/~gilpin/tutorial/)
* [gef manual](https://hugsy.github.io/gef/)
