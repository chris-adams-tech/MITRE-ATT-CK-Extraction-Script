---
data_sources:
- 'Command: Command Execution'
- 'Script: Script Execution'
id: attack-pattern--afddee82-3385-4682-ad90-eeced33f2d07
mitre_attack_url: https://attack.mitre.org/techniques/T1059/011
name: Lua
platforms:
- Linux
- macOS
- Windows
- Network
tactics:
- execution
title: execution - Lua
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | execution |
| **Platforms** | Linux, macOS, Windows, Network |
| **Data Sources** | Command: Command Execution, Script: Script Execution |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1059/011](https://attack.mitre.org/techniques/T1059/011) |

# Lua (attack-pattern--afddee82-3385-4682-ad90-eeced33f2d07)

## Description
Adversaries may abuse Lua commands and scripts for execution. Lua is a cross-platform scripting and programming language primarily designed for embedded use in applications. Lua can be executed on the command-line (through the stand-alone lua interpreter), via scripts (<code>.lua</code>), or from Lua-embedded programs (through the <code>struct lua_State</code>).(Citation: Lua main page)(Citation: Lua state)

Lua scripts may be executed by adversaries for malicious purposes. Adversaries may incorporate, abuse, or replace existing Lua interpreters to allow for malicious Lua command execution at runtime.(Citation: PoetRat Lua)(Citation: Lua Proofpoint Sunseed)(Citation: Cyphort EvilBunny)(Citation: Kaspersky Lua)

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1059/011)
- [Kaspersky Lua](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07190154/The-ProjectSauron-APT_research_KL.pdf)
- [Lua main page](https://www.lua.org/start.html)
- [Lua state](https://pgl.yoyo.org/luai/i/lua_State)
- [Cyphort EvilBunny](https://web.archive.org/web/20150311013500/http:/www.cyphort.com/evilbunny-malware-instrumented-lua/)
- [PoetRat Lua](https://blog.talosintelligence.com/poetrat-update/)
- [Lua Proofpoint Sunseed](https://www.proofpoint.com/us/blog/threat-insight/asylum-ambuscade-state-actor-uses-compromised-private-ukrainian-military-emails)
