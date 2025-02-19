---
contributors:
- Matt Graeber, @mattifestation, SpecterOps
data_sources:
- 'Windows Registry: Windows Registry Key Modification'
- 'Module: Module Load'
- 'File: File Modification'
id: attack-pattern--543fceb5-cb92-40cb-aacf-6913d4db58bc
mitre_attack_url: https://attack.mitre.org/techniques/T1553/003
name: SIP and Trust Provider Hijacking
platforms:
- Windows
tactics:
- defense-evasion
title: defense-evasion - SIP and Trust Provider Hijacking
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | defense-evasion |
| **Platforms** | Windows |
| **Data Sources** | Windows Registry: Windows Registry Key Modification, Module: Module Load, File: File Modification |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1553/003](https://attack.mitre.org/techniques/T1553/003) |

# SIP and Trust Provider Hijacking (attack-pattern--543fceb5-cb92-40cb-aacf-6913d4db58bc)

## Description
Adversaries may tamper with SIP and trust provider components to mislead the operating system and application control tools when conducting signature validation checks. In user mode, Windows Authenticode (Citation: Microsoft Authenticode) digital signatures are used to verify a file's origin and integrity, variables that may be used to establish trust in signed code (ex: a driver with a valid Microsoft signature may be handled as safe). The signature validation process is handled via the WinVerifyTrust application programming interface (API) function,  (Citation: Microsoft WinVerifyTrust) which accepts an inquiry and coordinates with the appropriate trust provider, which is responsible for validating parameters of a signature. (Citation: SpectorOps Subverting Trust Sept 2017)

Because of the varying executable file types and corresponding signature formats, Microsoft created software components called Subject Interface Packages (SIPs) (Citation: EduardosBlog SIPs July 2008) to provide a layer of abstraction between API functions and files. SIPs are responsible for enabling API functions to create, retrieve, calculate, and verify signatures. Unique SIPs exist for most file formats (Executable, PowerShell, Installer, etc., with catalog signing providing a catch-all  (Citation: Microsoft Catalog Files and Signatures April 2017)) and are identified by globally unique identifiers (GUIDs). (Citation: SpectorOps Subverting Trust Sept 2017)

Similar to [Code Signing](https://attack.mitre.org/techniques/T1553/002), adversaries may abuse this architecture to subvert trust controls and bypass security policies that allow only legitimately signed code to execute on a system. Adversaries may hijack SIP and trust provider components to mislead operating system and application control tools to classify malicious (or any) code as signed by: (Citation: SpectorOps Subverting Trust Sept 2017)

* Modifying the <code>Dll</code> and <code>FuncName</code> Registry values in <code>HKLM\SOFTWARE[\WOW6432Node\]Microsoft\Cryptography\OID\EncodingType 0\CryptSIPDllGetSignedDataMsg\{SIP_GUID}</code> that point to the dynamic link library (DLL) providing a SIP’s CryptSIPDllGetSignedDataMsg function, which retrieves an encoded digital certificate from a signed file. By pointing to a maliciously-crafted DLL with an exported function that always returns a known good signature value (ex: a Microsoft signature for Portable Executables) rather than the file’s real signature, an adversary can apply an acceptable signature value to all files using that SIP (Citation: GitHub SIP POC Sept 2017) (although a hash mismatch will likely occur, invalidating the signature, since the hash returned by the function will not match the value computed from the file).
* Modifying the <code>Dll</code> and <code>FuncName</code> Registry values in <code>HKLM\SOFTWARE\[WOW6432Node\]Microsoft\Cryptography\OID\EncodingType 0\CryptSIPDllVerifyIndirectData\{SIP_GUID}</code> that point to the DLL providing a SIP’s CryptSIPDllVerifyIndirectData function, which validates a file’s computed hash against the signed hash value. By pointing to a maliciously-crafted DLL with an exported function that always returns TRUE (indicating that the validation was successful), an adversary can successfully validate any file (with a legitimate signature) using that SIP (Citation: GitHub SIP POC Sept 2017) (with or without hijacking the previously mentioned CryptSIPDllGetSignedDataMsg function). This Registry value could also be redirected to a suitable exported function from an already present DLL, avoiding the requirement to drop and execute a new file on disk.
* Modifying the <code>DLL</code> and <code>Function</code> Registry values in <code>HKLM\SOFTWARE\[WOW6432Node\]Microsoft\Cryptography\Providers\Trust\FinalPolicy\{trust provider GUID}</code> that point to the DLL providing a trust provider’s FinalPolicy function, which is where the decoded and parsed signature is checked and the majority of trust decisions are made. Similar to hijacking SIP’s CryptSIPDllVerifyIndirectData function, this value can be redirected to a suitable exported function from an already present DLL or a maliciously-crafted DLL (though the implementation of a trust provider is complex).
* **Note:** The above hijacks are also possible without modifying the Registry via [DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1574/001).

Hijacking SIP or trust provider components can also enable persistent code execution, since these malicious components may be invoked by any application that performs code signing or signature validation. (Citation: SpectorOps Subverting Trust Sept 2017)

## Detection
Periodically baseline registered SIPs and trust providers (Registry entries and files on disk), specifically looking for new, modified, or non-Microsoft entries. (Citation: SpectorOps Subverting Trust Sept 2017)

Enable CryptoAPI v2 (CAPI) event logging (Citation: Entrust Enable CAPI2 Aug 2017) to monitor and analyze error events related to failed trust validation (Event ID 81, though this event can be subverted by hijacked trust provider components) as well as any other provided information events (ex: successful validations). Code Integrity event logging may also provide valuable indicators of malicious SIP or trust provider loads, since protected processes that attempt to load a maliciously-crafted trust validation component will likely fail (Event ID 3033). (Citation: SpectorOps Subverting Trust Sept 2017)

Utilize Sysmon detection rules and/or enable the Registry (Global Object Access Auditing) (Citation: Microsoft Registry Auditing Aug 2016) setting in the Advanced Security Audit policy to apply a global system access control list (SACL) and event auditing on modifications to Registry values (sub)keys related to SIPs and trust providers: (Citation: Microsoft Audit Registry July 2012)

* HKLM\SOFTWARE\Microsoft\Cryptography\OID
* HKLM\SOFTWARE\WOW6432Node\Microsoft\Cryptography\OID
* HKLM\SOFTWARE\Microsoft\Cryptography\Providers\Trust
* HKLM\SOFTWARE\WOW6432Node\Microsoft\Cryptography\Providers\Trust

**Note:** As part of this technique, adversaries may attempt to manually edit these Registry keys (ex: Regedit) or utilize the legitimate registration process using [Regsvr32](https://attack.mitre.org/techniques/T1218/010). (Citation: SpectorOps Subverting Trust Sept 2017)

Analyze Autoruns data for oddities and anomalies, specifically malicious files attempting persistent execution by hiding within auto-starting locations. Autoruns will hide entries signed by Microsoft or Windows by default, so ensure “Hide Microsoft Entries” and “Hide Windows Entries” are both deselected. (Citation: SpectorOps Subverting Trust Sept 2017)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1553/003)
- [Entrust Enable CAPI2 Aug 2017](http://www.entrust.net/knowledge-base/technote.cfm?tn=8165)
- [GitHub SIP POC Sept 2017](https://github.com/mattifestation/PoCSubjectInterfacePackage)
- [SpectorOps Subverting Trust Sept 2017](https://specterops.io/assets/resources/SpecterOps_Subverting_Trust_in_Windows.pdf)
- [Microsoft Catalog Files and Signatures April 2017](https://docs.microsoft.com/windows-hardware/drivers/install/catalog-files)
- [Microsoft Audit Registry July 2012](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd941614(v=ws.10))
- [Microsoft Registry Auditing Aug 2016](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn311461(v=ws.11))
- [Microsoft Authenticode](https://msdn.microsoft.com/library/ms537359.aspx)
- [Microsoft WinVerifyTrust](https://msdn.microsoft.com/library/windows/desktop/aa388208.aspx)
- [EduardosBlog SIPs July 2008](https://blogs.technet.microsoft.com/eduardonavarro/2008/07/11/sips-subject-interface-package-and-authenticode/)
