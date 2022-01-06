# Linux Tools on non-Linux OSes

Often, you might prefer a commercial OS, rather than Linux (for whatever reason). This used to be a problem, as it locked you out of making use of many useful open source tools -- at least easily.

Nowadays, the situation is quite easy to overcome. See below for instructions for both macOS and Windows.

## Common Linux tools on Windows

If you're on Windows, and haven't already done so, I would strongly encourage you to [install Windows Subsystem for Linux (version 2)](https://docs.microsoft.com/en-us/windows/wsl/install-win10), then install Ubuntu (or whatever your preferred distribution is).

I would also suggest you install the following:

- Chocolatey - a Windows package manager -- lets you install so many things: Python, both of the below tools, VSCode, etc. And it's scriptable! Makes moving to a new machine so easy. [`winget`](https://docs.microsoft.com/en-us/windows/package-manager/winget/) is a brand new alternative direct from MS. Your choice. I generally only use it for one tool (WinDbg) at this point, but eventually could see myself switching to it full time. At least, if it gets all the packages I want. The below 4 *are* included in `winget` repos.
- Windows Terminal - a tabbed interface to a modern console application
- Cross Platform PowerShell - an updated pwsh instance, provides full .NET access from the command line
- VSCode
- Powertoys - a handy little collection of utilities (strictly optional but strong recommended)

This will provide you with a fully usable Linux command line environment within Windows, as well as a better interface to it, a package manager, and an enhanced PowerShell. Running the below commands in an admin level PowerShell will install all of the above (search for PowerShell in your start menu, right click, and select Run As Administrator):

```powershell
> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
> refreshenv
> #feel free to edit the below to only install the parts you want
> choco install -y 7zip notepadplusplus chocolatey-core.extension powershell-core git microsoft-windows-terminal terminal-icons.powershell nerdfont-hack inconsolata firanf powertoys vscode
> Write-Host "Enabling WSL features..."
> if (!((Get-WindowsOptionalFeature -online -FeatureName Microsoft-Windows-Subsystem-Linux).State -eq 'Enabled')) {
    Enable-WindowsOptionalFeature -online -FeatureName Microsoft-Windows-Subsystem-Linux -All -NoRestart
}
> #a reboot will be required if you didn't already have WSL installed
> #install wsl2 with ubuntu-20.04, update it, and then install texlive
> wsl --install --distribution Ubuntu-20.04
> #lauch wsl at least once to initialize it and set username and password
> wsl
> #after configuration is complete, run the below commands ($ is the prompt, don't copy it)
$ sudo apt upgrade
$ #install whatever you like here, these are just examples that I find useful in my own life
$ sudo apt install texlive-full build-essential
```

At this point, you will be able to run an Ubuntu shell from the menu in Windows Terminal. You may want to change one setting in the Ubuntu session within Windows Terminal. Change your "Starting directory" to `\\wsl$\<distro_name>\home\<username>`, replacing `<distro_name>` with whatever you installed, and `<username>` with your actual user name selected.

## Common Linux tools on macOS

macOS has a built in application (in `/Applications/Utilities/`) called Terminal.app. I'd suggest installing Brew in order to get a solid package manager.

From Terminal.app, run

```console
foo@bar:~$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
foo@bar:~$ #if on m1 mac, run `eval "$(/opt/homebrew/bin/brew shellenv)"`
foo@bar:~$ brew install --cask visual-studio-code
foo@bar:~$ #there are many other tools available in brew, including most common Linux utilities. See https://brew.sh/.
foo@bar:~$ #fonts are optional, but are nice to have
foo@bar:~$ brew tap homebrew/cask-fonts
foo@bar:~$ brew install --cask font-hack-nerd-font
foo@bar:~$ brew tap caskroom/fonts
foo@bar:~$ brew cask install font-fira-code font-fira-mono font-fira-mono-for-powerline font-fira-sans
```

If you are using an M1 based Mac, there is one more step. You need to add `eval "$(/opt/homebrew/bin/brew shellenv)"` to your `~/.zprofile`:

```console
foo@bar:~$ # Add Homebrew to your PATH in ~/.zprofile:
foo@bar:~$ echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```

This will obviate the need to run that command every time you open a Terminal session.