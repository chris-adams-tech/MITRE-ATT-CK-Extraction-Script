---
data_sources:
- 'Active Directory: Active Directory Object Modification'
- 'Command: Command Execution'
- 'User Account: User Account Metadata'
- 'Script: Script Execution'
id: attack-pattern--d50955c2-272d-4ac8-95da-10c29dda1c48
mitre_attack_url: https://attack.mitre.org/techniques/T1556/005
name: Reversible Encryption
platforms:
- Windows
tactics:
- credential-access
- defense-evasion
- persistence
title: credential-access - Reversible Encryption
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access, defense-evasion, persistence |
| **Platforms** | Windows |
| **Data Sources** | Active Directory: Active Directory Object Modification, Command: Command Execution, User Account: User Account Metadata, Script: Script Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1556/005](https://attack.mitre.org/techniques/T1556/005) |

# Reversible Encryption (attack-pattern--d50955c2-272d-4ac8-95da-10c29dda1c48)

## Description
An adversary may abuse Active Directory authentication encryption properties to gain access to credentials on Windows systems. The <code>AllowReversiblePasswordEncryption</code> property specifies whether reversible password encryption for an account is enabled or disabled. By default this property is disabled (instead storing user credentials as the output of one-way hashing functions) and should not be enabled unless legacy or other software require it.(Citation: store_pwd_rev_enc)

If the property is enabled and/or a user changes their password after it is enabled, an adversary may be able to obtain the plaintext of passwords created/changed after the property was enabled. To decrypt the passwords, an adversary needs four components:

1. Encrypted password (<code>G$RADIUSCHAP</code>) from the Active Directory user-structure <code>userParameters</code>
2. 16 byte randomly-generated value (<code>G$RADIUSCHAPKEY</code>) also from <code>userParameters</code>
3. Global LSA secret (<code>G$MSRADIUSCHAPKEY</code>)
4. Static key hardcoded in the Remote Access Subauthentication DLL (<code>RASSFM.DLL</code>)

With this information, an adversary may be able to reproduce the encryption key and subsequently decrypt the encrypted password value.(Citation: how_pwd_rev_enc_1)(Citation: how_pwd_rev_enc_2)

An adversary may set this property at various scopes through Local Group Policy Editor, user properties, Fine-Grained Password Policy (FGPP), or via the ActiveDirectory [PowerShell](https://attack.mitre.org/techniques/T1059/001) module. For example, an adversary may implement and apply a FGPP to users or groups if the Domain Functional Level is set to "Windows Server 2008" or higher.(Citation: dump_pwd_dcsync) In PowerShell, an adversary may make associated changes to user settings using commands similar to <code>Set-ADUser -AllowReversiblePasswordEncryption $true</code>.

## Detection
Monitor property changes in Group Policy: <code>Computer Configuration\Windows Settings\Security Settings\Account Policies\Password Policy\Store passwords using reversible encryption</code>. By default, the property should be set to Disabled.

Monitor command-line usage for <code>-AllowReversiblePasswordEncryption $true</code> or other actions that could be related to malicious tampering of user settings (i.e. [Group Policy Modification](https://attack.mitre.org/techniques/T1484/001)). Furthermore, consider monitoring and/or blocking suspicious execution of Active Directory PowerShell modules, such as <code>Set-ADUser</code> and <code>Set-ADAccountControl</code>, that change account configurations. 

Monitor Fine-Grained Password Policies and regularly audit user accounts and group settings.(Citation: dump_pwd_dcsync)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1556/005)
- [dump_pwd_dcsync](https://adsecurity.org/?p=2053)
- [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)
- [how_pwd_rev_enc_1](http://blog.teusink.net/2009/08/passwords-stored-using-reversible.html)
- [how_pwd_rev_enc_2](http://blog.teusink.net/2009/08/passwords-stored-using-reversible_26.html)
