VM Setup on Windows without paying for virtualization software

* auto-gen TOC:
{:toc}

## Requirements

In order to use Hyper-V, you need to be running Windows 10 or Windows 11 in Pro, Enterprise, or Education forms. If you are using Windows Home (10 or 11), you need to upgrade your license to one of the higher tiers. "But that costs money!" you say? Normally. But not for you! 

Go to the [Microsoft Software for Students](https://cat.pdx.edu/services/software/users/microsoft-software/) page, and follow the instructions for obtaining an account on the Azure Portal. Once you have access, you can obtain a new license key for Windows 10 or 11 Education, allowing you to use Hyper-V.

![azure portal](img/azure_portal.png)

I would strongly encourage you to move to Windows 11, but that's ultimately your decision.

The commands below will install some useful tooling and then enable the Hyper-V features you need. You'll need to reboot after running it, but once you do, you'll be ready to go! If you decide to run everything in a single go, make sure to edit the script to remove the `❯` character.

```powershell
❯ Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
❯ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
❯ refreshenv
❯ #feel free to edit the below to only install the parts you want
❯ choco install -y 7zip notepadplusplus chocolatey-core.extension powershell-core git microsoft-windows-terminal terminal-icons.powershell nerdfont-hack inconsolata firanf powertoys vscode 
❯ # The below installs texlive if you want a more unix-like tex install
❯ choco install -y texlive --params "'/scheme:full'"
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
❯ if (!((Get-WindowsOptionalFeature -online -FeatureName Microsoft-Hyper-V).State -eq 'Enabled')) {
  Enable-WindowsOptionalFeature -online -FeatureName Microsoft-Hyper-V -All -NoRestart
}
❯ if (!((Get-WindowsOptionalFeature -online -FeatureName VirtualMachinePlatform).State -eq 'Enabled')) {
  Enable-WindowsOptionalFeature -online -FeatureName VirtualMachinePlatform -All -NoRestart
}
❯ if (!((Get-WindowsOptionalFeature -online -FeatureName HypervisorPlatform).State -eq 'Enabled')) {
  Enable-WindowsOptionalFeature -online -FeatureName HypervisorPlatform -All -NoRestart
}
```

## Hyper-V Switch Setup


## VM Installation, Step by Step

1. Download your image:

   ```powershell
   ❯ # xz for windows is a cluster, so just pull down the ISO directly. It's not that big.
   ❯ Invoke-WebRequest -Uri "https://download.freebsd.org/ftp/releases/ISO-IMAGES/13.2/FreeBSD-13.2-RELEASE-amd64-dvd1.iso" -OutFile "FreeBSD-13.2-RELEASE-amd64-dvd1.iso"
   ```
1. Checksum your image:

   ```powershell
   ❯ Get-FileHash -Algorithm SHA512 -Path .\FreeBSD-13.2-RELEASE-amd64-dvd1.iso | Format-List
   
      Algorithm : SHA512
      Hash      : 7C5473B9BBC5CB235329B8FA17FFB690ABBAE67FE5E4BB30260BAA034501D3F23EBA82679A9871AF2F42E9600AFF7E9E810A0B03005AFC24962ED03945171AE1
      Path      : D:\FreeBSD-13.2-RELEASE-amd64-dvd1.iso

   ```



