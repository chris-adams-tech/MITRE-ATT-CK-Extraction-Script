---
contributors:
- Robert Wilson
- Tony Lambert, Red Canary
data_sources:
- 'Process: Process Creation'
- 'File: File Creation'
- 'Command: Command Execution'
- 'File: File Modification'
id: attack-pattern--b63a34e8-0a61-4c97-a23b-bf8a2ed812e2
mitre_attack_url: https://attack.mitre.org/techniques/T1546/004
name: Unix Shell Configuration Modification
platforms:
- Linux
- macOS
tactics:
- privilege-escalation
- persistence
title: privilege-escalation - Unix Shell Configuration Modification
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | privilege-escalation, persistence |
| **Platforms** | Linux, macOS |
| **Data Sources** | Process: Process Creation, File: File Creation, Command: Command Execution, File: File Modification |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1546/004](https://attack.mitre.org/techniques/T1546/004) |

# Unix Shell Configuration Modification (attack-pattern--b63a34e8-0a61-4c97-a23b-bf8a2ed812e2)

## Description
Adversaries may establish persistence through executing malicious commands triggered by a user’s shell. User [Unix Shell](https://attack.mitre.org/techniques/T1059/004)s execute several configuration scripts at different points throughout the session based on events. For example, when a user opens a command-line interface or remotely logs in (such as via SSH) a login shell is initiated. The login shell executes scripts from the system (<code>/etc</code>) and the user’s home directory (<code>~/</code>) to configure the environment. All login shells on a system use /etc/profile when initiated. These configuration scripts run at the permission level of their directory and are often used to set environment variables, create aliases, and customize the user’s environment. When the shell exits or terminates, additional shell scripts are executed to ensure the shell exits appropriately. 

Adversaries may attempt to establish persistence by inserting commands into scripts automatically executed by shells. Using bash as an example, the default shell for most GNU/Linux systems, adversaries may add commands that launch malicious binaries into the <code>/etc/profile</code> and <code>/etc/profile.d</code> files.(Citation: intezer-kaiji-malware)(Citation: bencane blog bashrc) These files typically require root permissions to modify and are executed each time any shell on a system launches. For user level permissions, adversaries can insert malicious commands into <code>~/.bash_profile</code>, <code>~/.bash_login</code>, or <code>~/.profile</code> which are sourced when a user opens a command-line interface or connects remotely.(Citation: anomali-rocke-tactics)(Citation: Linux manual bash invocation) Since the system only executes the first existing file in the listed order, adversaries have used <code>~/.bash_profile</code> to ensure execution. Adversaries have also leveraged the <code>~/.bashrc</code> file which is additionally executed if the connection is established remotely or an additional interactive shell is opened, such as a new tab in the command-line interface.(Citation: Tsunami)(Citation: anomali-rocke-tactics)(Citation: anomali-linux-rabbit)(Citation: Magento) Some malware targets the termination of a program to trigger execution, adversaries can use the <code>~/.bash_logout</code> file to execute malicious commands at the end of a session. 

For macOS, the functionality of this technique is similar but may leverage zsh, the default shell for macOS 10.15+. When the Terminal.app is opened, the application launches a zsh login shell and a zsh interactive shell. The login shell configures the system environment using <code>/etc/profile</code>, <code>/etc/zshenv</code>, <code>/etc/zprofile</code>, and <code>/etc/zlogin</code>.(Citation: ScriptingOSX zsh)(Citation: PersistentJXA_leopitt)(Citation: code_persistence_zsh)(Citation: macOS MS office sandbox escape) The login shell then configures the user environment with <code>~/.zprofile</code> and <code>~/.zlogin</code>. The interactive shell uses the <code>~/.zshrc</code> to configure the user environment. Upon exiting, <code>/etc/zlogout</code> and <code>~/.zlogout</code> are executed. For legacy programs, macOS executes <code>/etc/bashrc</code> on startup.

## Detection
While users may customize their shell profile files, there are only certain types of commands that typically appear in these files. Monitor for abnormal commands such as execution of unknown programs, opening network sockets, or reaching out across the network when user profiles are loaded during the login process.

Monitor for changes to <code>/etc/profile</code> and <code>/etc/profile.d</code>, these files should only be modified by system administrators. MacOS users can leverage Endpoint Security Framework file events monitoring these specific files.(Citation: ESF_filemonitor) 

For most Linux and macOS systems, a list of file paths for valid shell options available on a system are located in the <code>/etc/shells</code> file.


## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1546/004)
- [anomali-linux-rabbit](https://www.anomali.com/blog/pulling-linux-rabbit-rabbot-malware-out-of-a-hat)
- [anomali-rocke-tactics](https://www.anomali.com/blog/illicit-cryptomining-threat-actor-rocke-changes-tactics-now-more-difficult-to-detect)
- [Linux manual bash invocation](https://wiki.archlinux.org/index.php/Bash#Invocation)
- [ScriptingOSX zsh](https://scriptingosx.com/2019/06/moving-to-zsh-part-2-configuration-files/)
- [bencane blog bashrc](https://web.archive.org/web/20220316014323/http://bencane.com/2013/09/16/understanding-a-little-more-about-etcprofile-and-etcbashrc/)
- [macOS MS office sandbox escape](https://cedowens.medium.com/macos-ms-office-sandbox-brain-dump-4509b5fed49a)
- [Magento](https://blog.sucuri.net/2018/05/shell-logins-as-a-magento-reinfection-vector.html)
- [Tsunami](https://unit42.paloaltonetworks.com/unit42-new-iotlinux-malware-targets-dvrs-forms-botnet/)
- [PersistentJXA_leopitt](https://posts.specterops.io/persistent-jxa-66e1c3cd1cf5)
- [code_persistence_zsh](https://github.com/D00MFist/PersistentJXA/blob/master/BashProfilePersist.js)
- [ESF_filemonitor](https://objective-see.com/blog/blog_0x48.html)
- [intezer-kaiji-malware](https://www.intezer.com/blog/research/kaiji-new-chinese-linux-malware-turning-to-golang/)
