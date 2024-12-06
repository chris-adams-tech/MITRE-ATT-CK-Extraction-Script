---
contributors:
- Syed Ummar Farooqh, McAfee
- Prasad Somasamudram, McAfee
- Sekhar Sarukkai, McAfee
- Jon Sternstein, Stern Security
- Yossi Weizman, Azure Defender Research Team
- Netskope
- Mark Wee
- Praetorian
- Menachem Goldstein
data_sources:
- 'Logon Session: Logon Session Creation'
- 'User Account: User Account Authentication'
- 'Logon Session: Logon Session Metadata'
id: attack-pattern--b17a1a56-e99c-403c-8948-561df0cffe81
mitre_attack_url: https://attack.mitre.org/techniques/T1078
name: Valid Accounts
platforms:
- Windows
- SaaS
- IaaS
- Linux
- macOS
- Containers
- Network
- Office Suite
- Identity Provider
tactics:
- defense-evasion
- persistence
- privilege-escalation
- initial-access
title: defense-evasion - Valid Accounts
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion, persistence, privilege-escalation, initial-access |
| **Platforms** | Windows, SaaS, IaaS, Linux, macOS, Containers, Network, Office Suite, Identity Provider |
| **Data Sources** | Logon Session: Logon Session Creation, User Account: User Account Authentication, Logon Session: Logon Session Metadata |
| **Permissions Required** | User, Administrator |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1078](https://attack.mitre.org/techniques/T1078) |

# Valid Accounts (attack-pattern--b17a1a56-e99c-403c-8948-561df0cffe81)

## Description
Adversaries may obtain and abuse credentials of existing accounts as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access, network devices, and remote desktop.(Citation: volexity_0day_sophos_FW) Compromised credentials may also grant an adversary increased privilege to specific systems or access to restricted areas of the network. Adversaries may choose not to use malware or tools in conjunction with the legitimate access those credentials provide to make it harder to detect their presence.

In some cases, adversaries may abuse inactive accounts: for example, those belonging to individuals who are no longer part of an organization. Using these accounts may allow the adversary to evade detection, as the original account user will not be present to identify any anomalous activity taking place on their account.(Citation: CISA MFA PrintNightmare)

The overlap of permissions for local, domain, and cloud accounts across a network of systems is of concern because the adversary may be able to pivot across accounts and systems to reach a high level of access (i.e., domain or enterprise administrator) to bypass access controls set within the enterprise.(Citation: TechNet Credential Theft)

## Detection
Configure robust, consistent account activity audit policies across the enterprise and with externally accessible services.(Citation: TechNet Audit Policy) Look for suspicious account behavior across systems that share accounts, either user, admin, or service accounts. Examples: one account logged into multiple systems simultaneously; multiple accounts logged into the same machine simultaneously; accounts logged in at odd times or outside of business hours. Activity may be from interactive login sessions or process ownership from accounts being used to execute binaries on a remote system as a particular account. Correlate other security systems with login information (e.g., a user has an active login session but has not entered the building or does not have VPN access).

Perform regular audits of domain and local system accounts to detect accounts that may have been created by an adversary for persistence. Checks on these accounts could also include whether default accounts such as Guest have been activated. These audits should also include checks on any appliances and applications for default credentials or SSH keys, and if any are discovered, they should be updated immediately.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1078)
- [volexity_0day_sophos_FW](https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/)
- [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)
- [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)
- [TechNet Audit Policy](https://technet.microsoft.com/en-us/library/dn487457.aspx)
