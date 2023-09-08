# Host Configuration

***AR: ensure you can connect to the server!***

For this class, we will be using a specific server -- [linux.cs.pdx.edu](ssh://linux.cs.pdx.edu) (the previous link uses the ssh:// scheme -- your browser may not support it). To access it, you will need to use some form of SSH client. The actual hostname of this server is `ada`. Login details are provided by the College IT. If you haven't created your account yet, please contact IT Support.

Each OS has the ability to make use of a terminal-type program. Each will be discussed a bit in the below sections, but the only variance is the actual name of the tool used. In all cases, you will be editing code (somewhere), but compiling and running on `ada`. In all cases below, the command within the specific terminal emulator you are using should look something like (replace the "\<MCECS username>" with your actual MCECS username (not your ODIN!).

```zsh
$ ssh linux.cs.pdx.edu -l <MCECS username>
```

When we get to the VScode discussion, I will explain how to use the ssh config file to create bookmarks with specific configurations.

---
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
$ cat ~/.ssh/ed_25519.pub | ssh linux.cs.pdx.edu 'cat >> ~/.ssh/authorized_keys'
```

This will append the new public key to the `~/.ssh/authorized_keys` file on the server, so that any previous keys aren't overwritten.

### Getting private key to local machine
---

Before we get the private key to our local machine, we need to add our public key to the `~/.ssh/authorized_keys` file.

```zsh
$ cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
```

Then, we make use of whatever file transfer protocol we prefer to copy `~/.ssh/id_ed25519` to our local machine. You can use filezile, winscp, cyberduck, etc. to move the file to `~/.ssh/id_ed25519` *on your local system*. This can be done via drag and drop, or by using PowerShell/Terminal.app, depending on your platform.

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

---
## Configuring Windows
---
***AR: If on windows, configure PowerShell OR get WSL2 up and running!***

I would suggest you install the following:

- [Chocolatey](https://chocolatey.org/) - a Windows package manager -- lets you install so many things: 
  - Python, 
  - all of the below tools, 
  - VSCode, etc. 
  - And it's scriptable! It makes moving to a new machine so easy. 
- `winget` is a brand new alternative direct from MS. Your choice. I generally only use it for one tool (WinDbg) at this point but eventually could see myself switching to it full-time. At least, if it gets all the packages I want. The below four are included in `winget` repos.

- Windows Terminal - a tabbed interface to a modern console application (`choco install microsoft-windows-terminal`)
- Cross-Platform PowerShell - an updated pwsh instance, provides full .NET access from the command line (`choco install powershell-core`)
- VSCode (`choco install visualstudiocode`)
- Powertoys - a handy little collection of utilities (strictly optional but strongly recommended, mostly for the FancyZones tool) (`choco install powertoys`)

***AR: If on windows, get WSL2 up and running or a fully configured PowerShell!***

If you're on Windows and haven't already done so, I would strongly encourage you to install Windows Subsystem for Linux (version 2), then install Ubuntu (or whatever your preferred distribution is).

This will provide you with a package manager and an enhanced PowerShell. Running the below commands (each starts with ❯, do not copy that character) in an admin level PowerShell (search for PowerShell in your start menu, right-click, and select Run As Administrator):

```powershell
❯ Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
❯ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
❯ refreshenv
❯ #feel free to edit the below to only install the parts you want
❯ choco install -y 7zip notepadplusplus chocolatey-core.extension powershell-core git microsoft-windows-terminal terminal-icons.powershell nerdfont-hack inconsolata firanf powertoys vscode 
❯ # The below installs texlive if you want a more unix-like tex install
❯ choco install -y texlive --params "'/scheme:full'"
❯ # The below installs miktex if you want a smaller install and a more windows-like tex install
❯ choco install -y miktex
❯  # The below is to setup the PowerShell prompt to be more useful to you
❯ Install-Module -Name ImportExcel
❯ Install-Module -Name Pansies -AllowClobber
❯ Install-Module -Name Pscx -AllowPrerelease
❯ Install-Module -Name PowerColorLS
❯ Install-Module -Name Posh-Git
❯ Install-Module -Name PSReadLine -AllowPrerelease -Force
❯ # This may or may not work on the version of windows you have installed:
❯ winget install JanDeDobbeleer.OhMyPosh 
❯ # if the above failed, install https://www.microsoft.com/en-us/p/app-installer/9nblggh4nns1?rtc=1&activetab=pivot:overviewtab and try again


❯ # The above commands will enable powershell, while the below commands will set up and configure WSL. Only pick the WSL option if you have an active interest


❯ # in using WSL for your development. If you don't know what WSL is, you probably don't want to use it.
❯ Write-Host "Enabling WSL features..."
❯ if (!((Get-WindowsOptionalFeature -online -FeatureName Microsoft-Windows-Subsystem-Linux).State -eq 'Enabled')) {
    Enable-WindowsOptionalFeature -online -FeatureName Microsoft-Windows-Subsystem-Linux -All -NoRestart
}
❯ #a reboot will be required if you didn't already have WSL installed
❯ #install wsl2 with ubuntu-20.04, update it, and then install useful/necessary tools for xv6 development
❯ wsl --install --distribution Ubuntu-22.04
❯ #lauch wsl at least once to initialize it and set username and password
❯ wsl
❯ #after configuration is complete, run the below commands in WSL ($ is the prompt, don't copy it) 
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install texlive-full build-essential bat tmux zsh git build-essential gdb-multiarch qemu-system-misc gcc-riscv64-linux-gnu binutils-riscv64-linux-gnu 
$ gem install colorls
$ #add alias for colorls to your startup script:
$ echo "alias less=bat" >> $HOME/.$(basename $SHELL)rc
$ echo 'alias ls="colorls --gs"' >> $HOME/.$(basename $SHELL)rc
```

To configure your PowerShell to do what you'll need for command-line access, see below, adding the contents to your $PROFILE file. If you have VScode installed, you can edit this file easily from PowerShell by running `code $PROFILE`, which will create the file if it doesn't already exist.

[***PowerShell Profile***](powershell_profile.md)

---
## macOS Setup
---

macOS has an inbuilt application (in /Applications/Utilities/) called Terminal.app. I'd suggest installing Brew to get a solid package manager. As a note, if you don't already have the command line utilities from Xcode installed, the command to install Brew can take a while and look totally stuck. This is because if you've never opened Xcode before, it is trying to get you to accept a license -- which it doesn't show you. I've broken that out as a specific call as an edit to this page. This also requires that you have Xcode installed, which I admit I assumed was the case.

From Terminal.app, run

```zsh
$ xcode-select --install
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
$ brew install --cask visual-studio-code
$ brew tap homebrew/cask-fonts
$ brew install --cask font-hack-nerd-font
$ brew tap caskroom/fonts
$ brew install --cask font-fira-code font-fira-mono font-fira-mono-for-powerline font-fira-sans
$ brew install texlive #this is for the technical writing portion, but useful to take care of now
```

Linux Setup
Linux has a variety of terminal emulators. I would recommend one of Konsole, Gnome Terminal, or RXVT. I will be assuming you are either running a Debian-based distribution (such as Ubuntu or Kali), or you know enough about your distribution that you can handle the installs.

```zsh
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install fonts-firacode fonts-inconsolata git gdb-multiarch texlive-full build-essential
$ curl -o vscode.deb -L https://go.microsoft.com/fwlink/\?LinkID\=760868
$ sudo apt install ./vscode.deb
```

The above are the package names for Ubuntu. If you are using a different distribution, some hints are below:

[VScode install instructions](https://code.visualstudio.com/docs/setup/linux)

`apt search <name>` to find packages in `apt` based distributions.

---
## Remote Editing in VSCode
---
