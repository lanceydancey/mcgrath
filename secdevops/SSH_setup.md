* auto-gen TOC:
{:toc}

SSH is a critical tool for our purposes in this class. It is the default remote access tool for most UNIX-like systems, including both FreeBSD and Linux. Originally developed for the OpenBSD project, it is now practically a standard. The client is installed by default on Windows, macOS, Linux, all the BSD variants, and basically every other operating system in general use. 

That said, it's a primarily command-line tool. Which means it has a text-based configuration file, and a suite of command-line tools to interact with it. This can be a bit daunting for new users, but it's not too bad once you get the hang of it.

## SSH config file

Below is the same configuration file we constructed in class. It makes a few assumptions:

* Your FreeBSD machine is named `squidbsd05`.
* Your Ubuntu machine is named `raspi01`.
* You have a generated keypair in `~/.ssh/squidbsd05`.
* This keypair is in the `authorized_keys` on both `squidbsd05` and `raspi01`.
* Your usernames on the remote machines are distinct from one another, *and* from your local username.

```ini
Host squidbsd05
    #In this case, squidbsd05 is actually behind a firewall
    Hostname mcgrath-data.cs.pdx.edu
    #The firewall maps port 2222 to port 22 on squidbsd05
    Port 2222
    #We need the path to our keyfile
    #This should work on both Windows and macOS
    IdentityFile ~/.ssh/squidbsd05
    #We only have the root account on the squidbsd05 machine
    User root

Host raspi01
    #raspi01 is behind the squidbsd05 NAT, in its own address space
    Hostname 192.168.33.74
    #we have a unique username
    User student
    #we have to jump through squidbsd05 to get to raspi01
    ProxyJump squidbsd05
    #and this is the same keyfile as before
    IdentityFile ~/.ssh/squidbsd05

#keep this here for problems with proxyjump (older Windows installs have issues)
#Host os2
#    Hostname os2.engr.oregonstate.edu
#    ProxyCommand C:\Windows\System32\OpenSSH\ssh.exe flip1 -W %h:%p

Host ada
    Hostname linux.cs.pdx.edu

#These are the defaults, unless overridden by a more specific entry above
Host *
    #automatically add keys to ssh-agent when used
    AddKeysToAgent yes
    #macOS and linux use UseKeychain, Windows doesn't, so ignore the error
    IgnoreUnknown UseKeychain
    UseKeychain yes
    #default to forwarding X11
    ForwardX11Trusted yes
    #this is my username (almost) everywhere
    User dmcgrath
    #this is my default keyfile
    IdentityFile ~/.ssh/id_rsa
    #keep the connection alive
    ServerAliveInterval 30
    #Allow for 3 missed keepalives before disconnecting
    ServerAliveCountMax 3
```

I've very heavily commented the file, in case the names of parameters aren't clear.

OK, so we have a config file. But it references a keyfile. Do we have one? If so, awesome. If not, keep reading.

## SSH key generation

If you don't already have an SSH key, please see the below links for how to generate and distribute the key files. These are links to the MS documentation, but the instructions are the same on every OS -- these are standard tools.

### [User key generation](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement#user-key-generation)
---

Generating an ssh key is a relatively painless process. This can be run either locally or on the server. If you are running it locally, you will need to copy the public key to the server. If you are running it on the server, you will need to copy the private key to your local machine. `$` is the prompt character, don't type it.

```zsh
$ ssh-keygen -t ed25519
```
By itself, the above command will prompt you for some information, including a (highly encouraged but technically optional) passphrase for the key. If you want to automate the process, you can add the `-f` flag to specify the filename, and the `-N` flag to specify the passphrase. The below command will generate a keypair with no passphrase, and save it to the default location.

```zsh
$ ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
```

Once you have the keypair generated, it's time to move things to destination locations. Depending on where you generated the key, you'll need one of the two sections below.

### [Getting public key to server](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement#standard-user)
---

If you generated the key on your local machine, you need to somehow copy it to `~/.ssh/authorized_keys` *on the server*. This can be accomplished by running:

```zsh
$ cat ~/.ssh/ed_25519.pub | ssh <IP address of your VM> -l <VM_username> 'cat >> ~/.ssh/authorized_keys'
```

This will append the new public key to the `~/.ssh/authorized_keys` file on the server, so that any previous keys aren't overwritten. Replace `<IP address of your VM>` with the...wait for it...IP address of your VM, and replace `<VM_username>` with your username on the VM. Make sure to not include the `<>` characters. You will be prompted for your password on the VM.

### Getting private key to local machine
---

Before we get the private key to our local machine, we need to add our public key to the `~/.ssh/authorized_keys` file.

```zsh
$ cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
```

Then, we make use of whatever file transfer protocol we prefer to copy `~/.ssh/id_ed25519` to our local machine. You can use filezilla, winscp, cyberduck, etc. to move the file to `~/.ssh/id_ed25519` *on your local system*. This can be done via drag and drop, or by using PowerShell/Terminal.app, depending on your platform.

If using the command line, the general form of the command is:

```zsh
$ scp <VM_username>@<IP address of your VM>:~/.ssh/id_ed25519 ~/.ssh/id_ed25519
```
 Replace `<IP address of your VM>` with the IP address of your VM, and replace `<VM_username>` with your username on the VM. Make sure to not include the `<>` characters. You will be prompted for your password on the VM.

### `ssh-agent`
---

If you did the security-conscious thing and set a passphrase on your key, that can get really annoying to enter all the time. Meet [`ssh-agent`](https://www.ssh.com/academy/ssh/agent).

This will allow us to use the key without having to type the passphrase every time we want to use it. This is a security risk, but it's a tradeoff between security and convenience. If you are using a passphrase, you will need to type it once per session, and then you can use the key without having to type it again. If you are not using a passphrase, you will not need to type anything.

On macOS, ssh-agent uses the system keychain. Run `ssh-add --apple-use-keychain ~/.ssh/id_ed25519`, enter your passphrase, and never think about it again.

On Windows, this is a little more complex. You'll need both an admin PowerShell window and a normal PowerShell window. In the admin shell, execute the following:

```powershell
pwsh❯ # By default the ssh-agent service is disabled. Allow it to be manually started for the next step to work.
pwsh❯ # Make sure you're running as an Administrator.'
pwsh❯ Get-Service ssh-agent | Set-Service -StartupType Manual
pwsh❯ 
pwsh❯ # Start the service
pwsh❯ Start-Service ssh-agent
pwsh❯ 
pwsh❯ # This should return a status of Running
pwsh❯ Get-Service ssh-agent

Status   Name               DisplayName
------   ----               -----------
Running  ssh-agent          OpenSSH Authentication Agent
```

And then in the user powershell, run `ssh-add ~\.ssh\id_ed25519`, enter your passphrase, and never think about it again.
