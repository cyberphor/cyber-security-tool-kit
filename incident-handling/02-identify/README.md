<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/incident-handling/02-identify/README.md#contents">Top of Page</a> |
  <a href="/incident-handling/02-identify/README.md#bottom-of-page">Bottom of Page</a>
</p>

# Identify
## Contents
* [Detection Requirements](#detection-requirements)
  * [Policy Violations](#policy-violations)
  * [Incident Categories](#incident-categories)
  * [Adversarial TTPs](#adversarial-ttps)
* [Detection Zones](#detection-zones)
* [Detection Enablers](#detection-enablers)
* [Checklists](#checklists)
  * [Daily Checklist](#daily-checklist)
  * [Weekly Checklist](/incident-handling/02-identify/checklists/weekly-checklist.md)
  * [Monthly Checklist](/incident-handling/02-identify/checklists/monthly-checklist.md)
  * [Quarterly Checklist](/incident-handling/02-identify/checklists/quarterly-checklist.md)
  * [Annual Checklist](/incident-handling/02-identify/checklists/annual-checklist.md)
* [Analysis](#analysis)
  * [The Universal Investigation Process](#the-universal-investigation-process)
  * [The Diamond Model of Intrusion Analysis](#the-diamond-model-of-intrusion-analysis)
  * [Detection Plays](#detection-plays)
* [Incident Management](#incident-management)
* [References](#references)

## Detection Requirements
### Policy Violations
* Non-Disclosure Agreement (NDA)
* Acceptable Use Policy (AUP)
* Privileged Access Agreement (PAA)

### Incident Categories
The Incident Categories apply to the Department of Defense and come from CJCSM 6510.0B, "Cyber Incident Handling Program."
| Category | Type | Description |
| -------- | ---- | ----------- |
| 0 | n/a | Training and Exercises |
| 1 | Incident | Root-Level Intrusion |
| 2 | Incident | User-Level Intrusion |
| 3 | Event | Unsuccesful Activity Attempt |
| 4 | Incident | Denial of Service | 
| 5 | Event | Non-Compliance Activity | 
| 6 | Event | Reconnaissance |
| 7 | Incident | Malicious Logic |
| 8 | Event | Investigating | 
| 9 | Event | Explained Anonmaly |

### Adversarial TTPs
Below is a list of adversary activities similar to those outlined in the MITRE ATT&CK framework. Use either source to develop your detection requirements. For example, as an organization you should want the ability to quickly confirm (distill and coorelate) port scans when they occur. Port scans enable an adversary to fingerprint your network and select their attack vector. Catching a bad guy earlier in his attack cycle means you will have less to clean-up during incident response. For the average stakeholder, this means risk gets addressed before it becomes fully realized. 
* Host Discovery Scans
* Port Scans
  * One-to-many 
* Service Enumeration
* Exploitation
  * Password Guessing
  * Vulnerabilties
  * Misconfigurations
* Privilege Escalation
  * Software Installations
* Lateral Movement    
* Cyber Effects

## Detection Zones
* Network Perimeter
  * Inbound IP addresses, ports, and protocols
  * Outbound IP addresses, ports, and protocols
* Host Perimeter
  * Lateral movement 
* System
  * Domain administrators
  * Local administrators
  * Removable media
  * Command/scripting interpreter abuse
  * Whitelisting 
  * Software installations
* Application
  * DNS
  * MSRPC
  * NetBIOS
  * SMB
  * LDAP
  * HTTP
  * CPOF 

## Detection Enablers
In order to detect suspicious or malicious activity, a defender should implement and/or be aware of the following:
* Logging Infrastructure
  * Audit Policy Group Policy Objects
  * Windows Event Forwarding
  * Windows Event Collector and Subscriptions 
  * Winlogbeat
* Windows Event IDs 
* Security Incident & Event Management (SIEM)
  * Security Onion Console (SOC)
  * Security Onion: Kibana
* Incident Management System (IMS)
  * Security Onion: TheHive

## Checklists
Below is an example of a Daily Checklist, see the [Checklists](/incident-handling/02-identify/checklists/) folder for Weekly, Monthly, Quarterly, and Annual Checklists. This is where your baselines will become helpful. Use them to find precursors and/or indicators of an incident. If something is found, start a Detection Play (see below).

### Daily Checklist
|     | Monday | Tuesday | Wednesday | Thursday | Friday |
| --- | ------ | ------- | --------- | -------- | ------ |
| NIDS Alerts |
| Flow Records |
| DNS Queries |
| HTTP Queries |
| LDAP Queries | 
| SMB Queries | 
| Vulnerabilities |
| Misconfigurations | 
| Domain Admins | 
| Local Admins | 
| USB Violations | 
| PowerShell Abuse |
| AppLocker Blocks | 
| Software Installations |

## Analysis
According to the Computer Security Incident Handling Guide (NIST SP 800-61 Revision 2), published by the National Institute of Standards and Technology, signs of an incident are either:
* Precursors
* Indicators

### The Universal Investigation Process
- n/a

### The Diamond Model of Intrusion Analysis
- n/a

### Detection Plays
- n/a

## Incident Management
- n/a

## References
* https://www.jcs.mil/Portals/36/Documents/Library/Manuals/m651001.pdf?ver=zbA7MXUXDcB9-se9hOxsIA%3d%3d
* https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf

<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/incident-handling/02-identify/README.md#contents">Top of Page</a> |
  <a href="/incident-handling/02-identify/README.md#bottom-of-page">Bottom of Page</a>
</p>

## Bottom of Page
