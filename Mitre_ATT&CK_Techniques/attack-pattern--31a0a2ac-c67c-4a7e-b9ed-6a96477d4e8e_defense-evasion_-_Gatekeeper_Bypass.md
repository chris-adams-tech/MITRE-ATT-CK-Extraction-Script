---
contributors:
- Brandon Dalton @PartyD0lphin
- Swasti Bhushan Deb, IBM India Pvt. Ltd.
data_sources:
- 'Process: Process Creation'
- 'Command: Command Execution'
- 'File: File Metadata'
- 'File: File Modification'
id: attack-pattern--31a0a2ac-c67c-4a7e-b9ed-6a96477d4e8e
mitre_attack_url: https://attack.mitre.org/techniques/T1553/001
name: Gatekeeper Bypass
platforms:
- macOS
tactics:
- defense-evasion
title: defense-evasion - Gatekeeper Bypass
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | macOS |
| **Data Sources** | Process: Process Creation, Command: Command Execution, File: File Metadata, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1553/001](https://attack.mitre.org/techniques/T1553/001) |

# Gatekeeper Bypass (attack-pattern--31a0a2ac-c67c-4a7e-b9ed-6a96477d4e8e)

## Description
Adversaries may modify file attributes and subvert Gatekeeper functionality to evade user prompts and execute untrusted programs. Gatekeeper is a set of technologies that act as layer of Apple’s security model to ensure only trusted applications are executed on a host. Gatekeeper was built on top of File Quarantine in Snow Leopard (10.6, 2009) and has grown to include Code Signing, security policy compliance, Notarization, and more. Gatekeeper also treats applications running for the first time differently than reopened applications.(Citation: TheEclecticLightCompany Quarantine and the flag)(Citation: TheEclecticLightCompany apple notarization )

Based on an opt-in system, when files are downloaded an extended attribute (xattr) called `com.apple.quarantine` (also known as a quarantine flag) can be set on the file by the application performing the download. Launch Services opens the application in a suspended state. For first run applications with the quarantine flag set, Gatekeeper executes the following functions:

1. Checks extended attribute – Gatekeeper checks for the quarantine flag, then provides an alert prompt to the user to allow or deny execution.(Citation: OceanLotus for OS X)(Citation: 20 macOS Common Tools and Techniques)

2. Checks System Policies - Gatekeeper checks the system security policy, allowing execution of apps downloaded from either just the App Store or the App Store and identified developers.

3. Code Signing – Gatekeeper checks for a valid code signature from an Apple Developer ID.

4. Notarization - Using the `api.apple-cloudkit.com` API, Gatekeeper reaches out to Apple servers to verify or pull down the notarization ticket and ensure the ticket is not revoked. Users can override notarization, which will result in a prompt of executing an “unauthorized app” and the security policy will be modified.

Adversaries can subvert one or multiple security controls within Gatekeeper checks through logic errors (e.g. [Exploitation for Defense Evasion](https://attack.mitre.org/techniques/T1211)), unchecked file types, and external libraries. For example, prior to macOS 13 Ventura, code signing and notarization checks were only conducted on first launch, allowing adversaries to write malicious executables to previously opened applications in order to bypass Gatekeeper security checks.(Citation: theevilbit gatekeeper bypass 2021)(Citation: Application Bundle Manipulation Brandon Dalton)

Applications and files loaded onto the system from a USB flash drive, optical disk, external hard drive, from a drive shared over the local network, or using the curl command may not set the quarantine flag. Additionally, it is possible to avoid setting the quarantine flag using [Drive-by Compromise](https://attack.mitre.org/techniques/T1189).

## Detection
The removal of the <code>com.apple.quarantine</code> flag by a user instead of the operating system is a suspicious action and should be examined further. Monitor and investigate attempts to modify extended file attributes with utilities such as <code>xattr</code>. Built-in system utilities may generate high false positive alerts, so compare against baseline knowledge for how systems are typically used and correlate modification events with other indications of malicious activity where possible. Monitor software update frameworks that strip the <code>com.apple.quarantine</code> flag when performing updates. 

Review <code>false</code> values under the <code>LSFileQuarantineEnabled</code> entry in an application's <code>Info.plist</code> file (required by every application). <code>false</code> under <code>LSFileQuarantineEnabled</code> indicates that an application does not use the quarantine flag. Unsandboxed applications with an unspecified <code>LSFileQuarantineEnabled</code> entry will default to not setting the quarantine flag. 

QuarantineEvents is a SQLite database containing a list of all files assigned the <code>com.apple.quarantine</code> attribute, located at <code>~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2</code>. Each event contains the corresponding UUID, timestamp, application, Gatekeeper score, and decision if it was allowed.(Citation: TheEclecticLightCompany Quarantine and the flag)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1553/001)
- [Application Bundle Manipulation Brandon Dalton](https://redcanary.com/blog/mac-application-bundles/)
- [theevilbit gatekeeper bypass 2021](https://theevilbit.github.io/posts/gatekeeper_not_a_bypass/)
- [OceanLotus for OS X](https://www.alienvault.com/blogs/labs-research/oceanlotus-for-os-x-an-application-bundle-pretending-to-be-an-adobe-flash-update)
- [TheEclecticLightCompany Quarantine and the flag](https://eclecticlight.co/2020/10/29/quarantine-and-the-quarantine-flag/)
- [TheEclecticLightCompany apple notarization ](https://eclecticlight.co/2020/08/28/how-notarization-works/)
- [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
