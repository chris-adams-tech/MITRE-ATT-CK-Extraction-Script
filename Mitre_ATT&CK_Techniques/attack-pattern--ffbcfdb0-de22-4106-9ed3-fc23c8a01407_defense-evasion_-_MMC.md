---
contributors:
- Wes Hurd
data_sources:
- 'Command: Command Execution'
- 'File: File Creation'
- 'Process: Process Creation'
id: attack-pattern--ffbcfdb0-de22-4106-9ed3-fc23c8a01407
mitre_attack_url: https://attack.mitre.org/techniques/T1218/014
name: MMC
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - MMC
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Command: Command Execution, File: File Creation, Process: Process Creation |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1218/014](https://attack.mitre.org/techniques/T1218/014) |

# MMC (attack-pattern--ffbcfdb0-de22-4106-9ed3-fc23c8a01407)

## Description
Adversaries may abuse mmc.exe to proxy execution of malicious .msc files. Microsoft Management Console (MMC) is a binary that may be signed by Microsoft and is used in several ways in either its GUI or in a command prompt.(Citation: win_mmc)(Citation: what_is_mmc) MMC can be used to create, open, and save custom consoles that contain administrative tools created by Microsoft, called snap-ins. These snap-ins may be used to manage Windows systems locally or remotely. MMC can also be used to open Microsoft created .msc files to manage system configuration.(Citation: win_msc_files_overview)

For example, <code>mmc C:\Users\foo\admintools.msc /a</code> will open a custom, saved console msc file in author mode.(Citation: win_mmc) Another common example is <code>mmc gpedit.msc</code>, which will open the Group Policy Editor application window. 

Adversaries may use MMC commands to perform malicious tasks. For example, <code>mmc wbadmin.msc delete catalog -quiet</code> deletes the backup catalog on the system (i.e. [Inhibit System Recovery](https://attack.mitre.org/techniques/T1490)) without prompts to the user (Note: <code>wbadmin.msc</code> may only be present by default on Windows Server operating systems).(Citation: win_wbadmin_delete_catalog)(Citation: phobos_virustotal)

Adversaries may also abuse MMC to execute malicious .msc files. For example, adversaries may first create a malicious registry Class Identifier (CLSID) subkey, which uniquely identifies a [Component Object Model](https://attack.mitre.org/techniques/T1559/001) class object.(Citation: win_clsid_key) Then, adversaries may create custom consoles with the “Link to Web Address” snap-in that is linked to the malicious CLSID subkey.(Citation: mmc_vulns) Once the .msc file is saved, adversaries may invoke the malicious CLSID payload with the following command: <code>mmc.exe -Embedding C:\path\to\test.msc</code>.(Citation: abusing_com_reg)

## Detection
Monitor processes and command-line parameters for suspicious or malicious use of MMC. Since MMC is a signed Windows binary, verify use of MMC is legitimate and not malicious. 

Monitor for creation and use of .msc files. MMC may legitimately be used to call Microsoft-created .msc files, such as <code>services.msc</code> or <code>eventvwr.msc</code>. Invoking non-Microsoft .msc files may be an indicator of malicious activity. 

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1218/014)
- [abusing_com_reg](https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/)
- [mmc_vulns](https://research.checkpoint.com/2019/microsoft-management-console-mmc-vulnerabilities/)
- [win_msc_files_overview](https://www.ghacks.net/2017/06/10/windows-msc-files-overview/)
- [win_mmc](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/mmc)
- [win_wbadmin_delete_catalog](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/wbadmin-delete-catalog)
- [win_clsid_key](https://docs.microsoft.com/en-us/windows/win32/com/clsid-key-hklm)
- [what_is_mmc](https://docs.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/what-is-microsoft-management-console)
- [phobos_virustotal](https://www.virustotal.com/gui/file/0b4c743246478a6a8c9fa3ff8e04f297507c2f0ea5d61a1284fe65387d172f81/detection)
