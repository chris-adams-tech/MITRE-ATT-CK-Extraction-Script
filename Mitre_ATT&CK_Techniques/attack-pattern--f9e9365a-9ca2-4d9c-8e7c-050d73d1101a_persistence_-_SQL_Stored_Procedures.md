---
contributors:
- Carlos Borges, @huntingneo, CIP
- Lucas da Silva Pereira, @vulcanunsec, CIP
- Kaspersky
data_sources:
- 'Application Log: Application Log Content'
id: attack-pattern--f9e9365a-9ca2-4d9c-8e7c-050d73d1101a
mitre_attack_url: https://attack.mitre.org/techniques/T1505/001
name: SQL Stored Procedures
platforms:
- Windows
- Linux
tactics:
- persistence
title: persistence - SQL Stored Procedures
---

## Technical Details

| Attribute | Details |
|-----------|----------|
| **Tactics** | persistence |
| **Platforms** | Windows, Linux |
| **Data Sources** | Application Log: Application Log Content |
| **MITRE ATT&CK URL** | [https://attack.mitre.org/techniques/T1505/001](https://attack.mitre.org/techniques/T1505/001) |

# SQL Stored Procedures (attack-pattern--f9e9365a-9ca2-4d9c-8e7c-050d73d1101a)

## Description
Adversaries may abuse SQL stored procedures to establish persistent access to systems. SQL Stored Procedures are code that can be saved and reused so that database users do not waste time rewriting frequently used SQL queries. Stored procedures can be invoked via SQL statements to the database using the procedure name or via defined events (e.g. when a SQL server application is started/restarted).

Adversaries may craft malicious stored procedures that can provide a persistence mechanism in SQL database servers.(Citation: NetSPI Startup Stored Procedures)(Citation: Kaspersky MSSQL Aug 2019) To execute operating system commands through SQL syntax the adversary may have to enable additional functionality, such as xp_cmdshell for MSSQL Server.(Citation: NetSPI Startup Stored Procedures)(Citation: Kaspersky MSSQL Aug 2019)(Citation: Microsoft xp_cmdshell 2017) 

Microsoft SQL Server can enable common language runtime (CLR) integration. With CLR integration enabled, application developers can write stored procedures using any .NET framework language (e.g. VB .NET, C#, etc.).(Citation: Microsoft CLR Integration 2017) Adversaries may craft or modify CLR assemblies that are linked to stored procedures since these CLR assemblies can be made to execute arbitrary commands.(Citation: NetSPI SQL Server CLR) 

## Detection
On a MSSQL Server, consider monitoring for xp_cmdshell usage.(Citation: NetSPI Startup Stored Procedures) Consider enabling audit features that can log malicious startup activities.

## External References
- [mitre-attack](https://attack.mitre.org/techniques/T1505/001)
- [Microsoft CLR Integration 2017](https://docs.microsoft.com/en-us/sql/relational-databases/clr-integration/common-language-runtime-integration-overview?view=sql-server-2017)
- [Microsoft xp_cmdshell 2017](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/xp-cmdshell-transact-sql?view=sql-server-2017)
- [Kaspersky MSSQL Aug 2019](https://securelist.com/malicious-tasks-in-ms-sql-server/92167/)
- [NetSPI Startup Stored Procedures](https://www.netspi.com/blog/technical-blog/network-penetration-testing/sql-server-persistence-part-1-startup-stored-procedures/)
- [NetSPI SQL Server CLR](https://www.netspi.com/blog/technical-blog/adversary-simulation/attacking-sql-server-clr-assemblies/)
