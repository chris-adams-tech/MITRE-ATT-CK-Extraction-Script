---
contributors:
- Jeremy Galloway
- Red Canary
id: attack-pattern--6be14413-578e-46c1-8304-310762b3ecd5
mitre_attack_url: https://attack.mitre.org/techniques/T1215
name: Kernel Modules and Extensions
platforms:
- Linux
- macOS
tactics:
- persistence
title: persistence - Kernel Modules and Extensions
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Linux, macOS |
| **Permissions Required** | root |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1215](https://attack.mitre.org/techniques/T1215) |

# Kernel Modules and Extensions (attack-pattern--6be14413-578e-46c1-8304-310762b3ecd5)

## Description
Loadable Kernel Modules (or LKMs) are pieces of code that can be loaded and unloaded into the kernel upon demand. They extend the functionality of the kernel without the need to reboot the system. For example, one type of module is the device driver, which allows the kernel to access hardware connected to the system. (Citation: Linux Kernel Programming) When used maliciously, Loadable Kernel Modules (LKMs) can be a type of kernel-mode [Rootkit](https://attack.mitre.org/techniques/T1014) that run with the highest operating system privilege (Ring 0). (Citation: Linux Kernel Module Programming Guide) Adversaries can use loadable kernel modules to covertly persist on a system and evade defenses. Examples have been found in the wild and there are some open source projects. (Citation: Volatility Phalanx2) (Citation: CrowdStrike Linux Rootkit) (Citation: GitHub Reptile) (Citation: GitHub Diamorphine)

Common features of LKM based rootkits include: hiding itself, selective hiding of files, processes and network activity, as well as log tampering, providing authenticated backdoors and enabling root access to non-privileged users. (Citation: iDefense Rootkit Overview)

Kernel extensions, also called kext, are used for macOS to load functionality onto a system similar to LKMs for Linux. They are loaded and unloaded through <code>kextload</code> and <code>kextunload</code> commands. Several examples have been found where this can be used. (Citation: RSAC 2015 San Francisco Patrick Wardle) (Citation: Synack Secure Kernel Extension Broken) Examples have been found in the wild. (Citation: Securelist Ventir)

## Detection
LKMs are typically loaded into <code>/lib/modules</code> and have had the extension .ko ("kernel object") since version 2.6 of the Linux kernel. (Citation: Wikipedia Loadable Kernel Module)

Many LKMs require Linux headers (specific to the target kernel) in order to compile properly. 
These are typically obtained through the operating systems package manager and installed like a normal package.

Adversaries will likely run these commands on the target system before loading a malicious module in order to ensure that it is properly compiled. (Citation: iDefense Rootkit Overview)

On Ubuntu and Debian based systems this can be accomplished by running: <code>apt-get install linux-headers-$(uname -r)</code>

On RHEL and CentOS based systems this can be accomplished by running: <code>yum install kernel-devel-$(uname -r)</code>

Loading, unloading, and manipulating modules on Linux systems can be detected by monitoring for the following commands:<code>modprobe insmod lsmod rmmod modinfo</code> (Citation: Linux Loadable Kernel Module Insert and Remove LKMs)

For macOS, monitor for execution of <code>kextload</code> commands and correlate with other unknown or suspicious activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1215)
- [Linux Kernel Programming](https://www.tldp.org/LDP/lkmpg/2.4/lkmpg.pdf)
- [Linux Kernel Module Programming Guide](http://www.tldp.org/LDP/lkmpg/2.4/html/x437.html)
- [Volatility Phalanx2](https://volatility-labs.blogspot.com/2012/10/phalanx-2-revealed-using-volatility-to.html)
- [CrowdStrike Linux Rootkit](https://www.crowdstrike.com/blog/http-iframe-injecting-linux-rootkit/)
- [GitHub Reptile](https://github.com/f0rb1dd3n/Reptile)
- [GitHub Diamorphine](https://github.com/m0nad/Diamorphine)
- [iDefense Rootkit Overview](http://www.megasecurity.org/papers/Rootkits.pdf)
- [RSAC 2015 San Francisco Patrick Wardle](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
- [Synack Secure Kernel Extension Broken](https://www.synack.com/2017/09/08/high-sierras-secure-kernel-extension-loading-is-broken/)
- [Securelist Ventir](https://securelist.com/the-ventir-trojan-assemble-your-macos-spy/67267/)
- [Wikipedia Loadable Kernel Module](https://en.wikipedia.org/wiki/Loadable_kernel_module#Linux)
- [Linux Loadable Kernel Module Insert and Remove LKMs](http://tldp.org/HOWTO/Module-HOWTO/x197.html)
