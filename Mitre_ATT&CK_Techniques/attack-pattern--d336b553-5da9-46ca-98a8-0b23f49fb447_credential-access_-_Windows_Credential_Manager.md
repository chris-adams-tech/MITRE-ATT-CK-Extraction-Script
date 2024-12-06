---
contributors:
- Bernaldo Penas Antelo
- Mugdha Peter Bansode
- Uriel Kosayev
- Vadim Khrykov
data_sources:
- 'File: File Access'
- 'Command: Command Execution'
- 'Process: OS API Execution'
- 'Process: Process Creation'
id: attack-pattern--d336b553-5da9-46ca-98a8-0b23f49fb447
mitre_attack_url: https://attack.mitre.org/techniques/T1555/004
name: Windows Credential Manager
platforms:
- Windows
tactics:
- credential-access
title: credential-access - Windows Credential Manager
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | credential-access |
| **Platforms** | Windows |
| **Data Sources** | File: File Access, Command: Command Execution, Process: OS API Execution, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1555/004](https://attack.mitre.org/techniques/T1555/004) |

# Windows Credential Manager (attack-pattern--d336b553-5da9-46ca-98a8-0b23f49fb447)

## Description
Adversaries may acquire credentials from the Windows Credential Manager. The Credential Manager stores credentials for signing into websites, applications, and/or devices that request authentication through NTLM or Kerberos in Credential Lockers (previously known as Windows Vaults).(Citation: Microsoft Credential Manager store)(Citation: Microsoft Credential Locker)

The Windows Credential Manager separates website credentials from application or network credentials in two lockers. As part of [Credentials from Web Browsers](https://attack.mitre.org/techniques/T1555/003), Internet Explorer and Microsoft Edge website credentials are managed by the Credential Manager and are stored in the Web Credentials locker. Application and network credentials are stored in the Windows Credentials locker.

Credential Lockers store credentials in encrypted `.vcrd` files, located under `%Systemdrive%\Users\\[Username]\AppData\Local\Microsoft\\[Vault/Credentials]\`. The encryption key can be found in a file named <code>Policy.vpol</code>, typically located in the same folder as the credentials.(Citation: passcape Windows Vault)(Citation: Malwarebytes The Windows Vault)

Adversaries may list credentials managed by the Windows Credential Manager through several mechanisms. <code>vaultcmd.exe</code> is a native Windows executable that can be used to enumerate credentials stored in the Credential Locker through a command-line interface. Adversaries may also gather credentials by directly reading files located inside of the Credential Lockers. Windows APIs, such as <code>CredEnumerateA</code>, may also be absued to list credentials managed by the Credential Manager.(Citation: Microsoft CredEnumerate)(Citation: Delpy Mimikatz Crendential Manager)

Adversaries may also obtain credentials from credential backups. Credential backups and restorations may be performed by running <code>rundll32.exe keymgr.dll KRShowKeyMgr</code> then selecting the “Back up...” button on the “Stored User Names and Passwords” GUI.

Password recovery tools may also obtain plain text passwords from the Credential Manager.(Citation: Malwarebytes The Windows Vault)

## Detection
Monitor process and command-line parameters of <code>vaultcmd.exe</code> for suspicious activity, such as listing credentials from the Windows Credentials locker (i.e., <code>vaultcmd /listcreds:“Windows Credentials”</code>).(Citation: Malwarebytes The Windows Vault)

Consider monitoring API calls such as <code>CredEnumerateA</code> that may list credentials from the Windows Credential Manager.(Citation: Microsoft CredEnumerate)(Citation: Delpy Mimikatz Crendential Manager)

Consider monitoring file reads to Vault locations, <code>%Systemdrive%\Users\\[Username]\AppData\Local\Microsoft\\[Vault/Credentials]\</code>, for suspicious activity.(Citation: Malwarebytes The Windows Vault)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1555/004)
- [Malwarebytes The Windows Vault](https://blog.malwarebytes.com/101/2016/01/the-windows-vaults/)
- [Delpy Mimikatz Crendential Manager](https://github.com/gentilkiwi/mimikatz/wiki/howto-~-credential-manager-saved-credentials)
- [Microsoft Credential Locker](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-8.1-and-8/jj554668(v=ws.11)?redirectedfrom=MSDN)
- [Microsoft Credential Manager store](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh994565(v=ws.11)#credential-manager-store)
- [Microsoft CredEnumerate](https://docs.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-credenumeratea)
- [passcape Windows Vault](https://www.passcape.com/windows_password_recovery_vault_explorer)
