---
contributors:
- Brandon Dalton @PartyD0lphin
- Rodchenko Aleksandr
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'File: File Creation'
id: attack-pattern--da051493-ae9c-4b1b-9760-c009c46c9b56
mitre_attack_url: https://attack.mitre.org/techniques/T1546/016
name: Installer Packages
platforms:
- Linux
- macOS
- Windows
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - Installer Packages
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | Linux, macOS, Windows |
| **Data Sources** | Process: Process Creation, Command: Command Execution, File: File Creation |
| **Permissions Required** | User |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/016](https://attack.mitre.org/techniques/T1546/016) |

# Installer Packages (attack-pattern--da051493-ae9c-4b1b-9760-c009c46c9b56)

## Description
Adversaries may establish persistence and elevate privileges by using an installer to trigger the execution of malicious content. Installer packages are OS specific and contain the resources an operating system needs to install applications on a system. Installer packages can include scripts that run prior to installation as well as after installation is complete. Installer scripts may inherit elevated permissions when executed. Developers often use these scripts to prepare the environment for installation, check requirements, download dependencies, and remove files after installation.(Citation: Installer Package Scripting Rich Trouton)

Using legitimate applications, adversaries have distributed applications with modified installer scripts to execute malicious content. When a user installs the application, they may be required to grant administrative permissions to allow the installation. At the end of the installation process of the legitimate application, content such as macOS `postinstall` scripts can be executed with the inherited elevated permissions. Adversaries can use these scripts to execute a malicious executable or install other malicious components (such as a [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)) with the elevated permissions.(Citation: Application Bundle Manipulation Brandon Dalton)(Citation: wardle evilquest parti)(Citation: Windows AppleJeus GReAT)(Citation: Debian Manual Maintainer Scripts)

Depending on the distribution, Linux versions of package installer scripts are sometimes called maintainer scripts or post installation scripts. These scripts can include `preinst`, `postinst`, `prerm`, `postrm` scripts and run as root when executed.

For Windows, the Microsoft Installer services uses `.msi` files to manage the installing, updating, and uninstalling of applications. These installation routines may also include instructions to perform additional actions that may be abused by adversaries.(Citation: Microsoft Installation Procedures)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/016)
- [Application Bundle Manipulation Brandon Dalton](https://redcanary.com/blog/mac-application-bundles/)
- [Debian Manual Maintainer Scripts](https://www.debian.org/doc/debian-policy/ch-maintainerscripts.html#s-mscriptsinstact)
- [Windows AppleJeus GReAT](https://securelist.com/operation-applejeus/87553/)
- [Microsoft Installation Procedures](https://learn.microsoft.com/windows/win32/msi/installation-procedure-tables-group)
- [wardle evilquest parti](https://objective-see.com/blog/blog_0x59.html)
- [Installer Package Scripting Rich Trouton](https://cpb-us-e1.wpmucdn.com/sites.psu.edu/dist/4/24696/files/2019/07/psumac2019-345-Installer-Package-Scripting-Making-your-deployments-easier-one-at-a-time.pdf)
