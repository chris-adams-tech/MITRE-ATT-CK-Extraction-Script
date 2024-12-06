---
contributors:
- Regina Elwell
- Sudhanshu Chauhan, @Sudhanshu_C
- Isif Ibrahima, Mandiant
- Austin Clark, @c2defense
data_sources:
- 'User Account: User Account Metadata'
- 'Command: Command Execution'
- 'Process: Process Creation'
id: attack-pattern--b6075259-dba3-44e9-87c7-e954f37ec0d5
mitre_attack_url: https://attack.mitre.org/techniques/T1201
name: Password Policy Discovery
platforms:
- Windows
- Linux
- macOS
- IaaS
- Network
- Identity Provider
- SaaS
- Office Suite
tactics:
- discovery
title: discovery - Password Policy Discovery
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | discovery |
| **Platforms** | Windows, Linux, macOS, IaaS, Network, Identity Provider, SaaS, Office Suite |
| **Data Sources** | User Account: User Account Metadata, Command: Command Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1201](https://attack.mitre.org/techniques/T1201) |

# Password Policy Discovery (attack-pattern--b6075259-dba3-44e9-87c7-e954f37ec0d5)

## Description
Adversaries may attempt to access detailed information about the password policy used within an enterprise network or cloud environment. Password policies are a way to enforce complex passwords that are difficult to guess or crack through [Brute Force](https://attack.mitre.org/techniques/T1110). This information may help the adversary to create a list of common passwords and launch dictionary and/or brute force attacks which adheres to the policy (e.g. if the minimum password length should be 8, then not trying passwords such as 'pass123'; not checking for more than 3-4 passwords per account if the lockout is set to 6 as to not lock out accounts).

Password policies can be set and discovered on Windows, Linux, and macOS systems via various command shell utilities such as <code>net accounts (/domain)</code>, <code>Get-ADDefaultDomainPasswordPolicy</code>, <code>chage -l <username></code>, <code>cat /etc/pam.d/common-password</code>, and <code>pwpolicy getaccountpolicies</code> (Citation: Superuser Linux Password Policies) (Citation: Jamf User Password Policies). Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to discover password policy information (e.g. <code>show aaa</code>, <code>show aaa common-criteria policy all</code>).(Citation: US-CERT-TA18-106A)

Password policies can be discovered in cloud environments using available APIs such as <code>GetAccountPasswordPolicy</code> in AWS (Citation: AWS GetPasswordPolicy).

## Detection
Monitor logs and processes for tools and command line arguments that may indicate they're being used for password policy discovery. Correlate that activity with other suspicious activity from the originating system to reduce potential false positives from valid user or administrator activity. Adversaries will likely attempt to find the password policy early in an operation and the activity is likely to happen with other Discovery activity.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1201)
- [AWS GetPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountPasswordPolicy.html)
- [Jamf User Password Policies](https://www.jamf.com/jamf-nation/discussions/18574/user-password-policies-on-non-ad-machines)
- [Superuser Linux Password Policies](https://superuser.com/questions/150675/how-to-display-password-policy-information-for-a-user-ubuntu)
- [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
