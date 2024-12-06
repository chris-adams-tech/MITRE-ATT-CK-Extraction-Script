---
contributors:
- Tony Lambert, Red Canary
- Dror Alon, Palo Alto Networks
- Or Kliger, Palo Alto Networks
- Austin Clark, @c2defense
- Arad Inbar, Fidelis Security
data_sources:
- 'Command: Command Execution'
- 'Process: Process Creation'
- 'File: File Modification'
id: attack-pattern--6b57dc31-b814-4a03-8706-28bc20d739c4
mitre_attack_url: https://attack.mitre.org/techniques/T1098/004
name: SSH Authorized Keys
platforms:
- Linux
- macOS
- IaaS
- Network
tactics:
- persistence
- privilege-escalation
title: persistence - SSH Authorized Keys
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence, privilege-escalation |
| **Platforms** | Linux, macOS, IaaS, Network |
| **Data Sources** | Command: Command Execution, Process: Process Creation, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1098/004](https://attack.mitre.org/techniques/T1098/004) |

# SSH Authorized Keys (attack-pattern--6b57dc31-b814-4a03-8706-28bc20d739c4)

## Description
Adversaries may modify the SSH <code>authorized_keys</code> file to maintain persistence on a victim host. Linux distributions and macOS commonly use key-based authentication to secure the authentication process of SSH sessions for remote management. The <code>authorized_keys</code> file in SSH specifies the SSH keys that can be used for logging into the user account for which the file is configured. This file is usually found in the user's home directory under <code>&lt;user-home&gt;/.ssh/authorized_keys</code>.(Citation: SSH Authorized Keys) Users may edit the system’s SSH config file to modify the directives PubkeyAuthentication and RSAAuthentication to the value “yes” to ensure public key and RSA authentication are enabled. The SSH config file is usually located under <code>/etc/ssh/sshd_config</code>.

Adversaries may modify SSH <code>authorized_keys</code> files directly with scripts or shell commands to add their own adversary-supplied public keys. In cloud environments, adversaries may be able to modify the SSH authorized_keys file of a particular virtual machine via the command line interface or rest API. For example, by using the Google Cloud CLI’s “add-metadata” command an adversary may add SSH keys to a user account.(Citation: Google Cloud Add Metadata)(Citation: Google Cloud Privilege Escalation) Similarly, in Azure, an adversary may update the authorized_keys file of a virtual machine via a PATCH request to the API.(Citation: Azure Update Virtual Machines) This ensures that an adversary possessing the corresponding private key may log in as an existing user via SSH.(Citation: Venafi SSH Key Abuse)(Citation: Cybereason Linux Exim Worm) It may also lead to privilege escalation where the virtual machine or instance has distinct permissions from the requesting user.

Where authorized_keys files are modified via cloud APIs or command line interfaces, an adversary may achieve privilege escalation on the target virtual machine if they add a key to a higher-privileged user. 

SSH keys can also be added to accounts on network devices, such as with the `ip ssh pubkey-chain` [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) command.(Citation: cisco_ip_ssh_pubkey_ch_cmd)

## Detection
Use file integrity monitoring to detect changes made to the <code>authorized_keys</code> file for each user on a system. Monitor for suspicious processes modifying the <code>authorized_keys</code> file. In cloud environments, monitor instances for modification of metadata and configurations.

Monitor for changes to and suspicious processes modifiying <code>/etc/ssh/sshd_config</code>.

For network infrastructure devices, collect AAA logging to monitor for rogue SSH keys being added to accounts.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1098/004)
- [Venafi SSH Key Abuse](https://www.venafi.com/blog/growing-abuse-ssh-keys-commodity-malware-campaigns-now-equipped-ssh-capabilities)
- [Google Cloud Privilege Escalation](https://about.gitlab.com/blog/2020/02/12/plundering-gcp-escalating-privileges-in-google-cloud-platform/)
- [cisco_ip_ssh_pubkey_ch_cmd](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/d1/sec-d1-cr-book/sec-cr-i3.html#wp1254331478)
- [Cybereason Linux Exim Worm](https://www.cybereason.com/blog/new-pervasive-worm-exploiting-linux-exim-server-vulnerability)
- [Google Cloud Add Metadata](https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata)
- [Azure Update Virtual Machines](https://docs.microsoft.com/en-us/rest/api/compute/virtual-machines/update)
- [SSH Authorized Keys](https://www.ssh.com/ssh/authorized_keys/)
