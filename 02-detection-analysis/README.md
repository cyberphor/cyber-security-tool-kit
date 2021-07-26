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


## Contents
* [Triggers](#triggers)
* [Naming Convention](#naming-convention)
  * [Unique Identifier](#unique-identifier)
  * [Confidence Level](#confidence-level)
  * [Incident Category](#incident-category)
  * [Description](#description)
* [Objective](#objective)
  * [Example Objective](#example-objective)
* [Analysis](#analysis)
  * [Example Analysis](#example-analysis)
* [Query](#query)
  * [Example Query](#example-query)
* [Notes](#notes)

## Triggers
Below is a list of events that should trigger a defender to invoke a play from their playbook.
* NIDS alert
* AV alert
* Server crash (Denial of Service)
* Users complain of slow network access
* System administrator notices unusual filename
* User reports a suspicious email message
* Computer records a suspicious configuration change
* Computer records multiple failed logins from a remote IP address
* Email administrator notices deviations from the expected baseline for network traffic
* Network administrator notices unauthorized, outbound network connections

## Naming Convention
```
<uid>-<et>-<dsid>-<cat>: <desc>
```

### Examples
* 200-sus-nid-cat6: Detect a network scan
* 201-mal-nid-cat6: Respond to an unauthorized network scan
* 500-mal-sys-cat5: Detect a USB violation
* 501-mal-sys-cat5: Respond to a USB violation

### Unique Identifier
| Unique Identifier (UID) Range | Data Source (DS) | DS Identifier (DSID) |
| ----------------------------- | ---------------- | -------------------- |
| 000 - 099 | Reserved | RES |
| 100 - 199 | Network Perimeter Logs | NFW |
| 200 - 299 | NIDS Alerts | NID |
| 300 - 399 | Host Perimeter Logs | HFW |
| 400 - 499 | HIDS Alerts | HID |
| 500 - 599 | System Logs | SYS |
| 600 - 699 | Application Logs | APP |
| 700 - 799 | Service Logs | SRV |
| 800 - 899 | Human | HUM |
| 900 - 999 | Multiple | MUL |

### Event Type
#### Suspicious (SUS)
Any event that is neither benign or confirmed as malicious to the Confidentiality, Integrity, or Availability of a computer/service will be handled as "Suspicious."

#### Malicious (MAL)
Any event confirmed to be malicious to the Confidentiality, Integrity, or Availability of a computer/service will be handled as such.

### Incident Category
| Category (CAT) | Incident |
| -------------- | -------- |
| CAT1 | Root-Level Intrusion |
| CAT2 | User-Level Intrusion |
| CAT3 | Unsuccesful Activity Attempt |
| CAT4 | Denial of Service |
| CAT5 | Non-Compliance Activity |
| CAT6 | Reconnaissance |
| CAT7 | Malicious Logic |

### Description
The Description element summarizes what the play is seeking to address.

# Objective
The Objective of a play is written for the average stakeholder. It is represents the best way to find and present information, given a scenario. It is an endstate and should be written in a way that makes its purpose obvious. It should also achieve one of the following:
* Explains how a machine was infected (by virus, worm, trojan, etc.)
* Explains suspicious network activity
* Helps the defender detect suspicious logon attempts
* Summarizes information such as trends, and/or statistics
* Provides a tailored view of a specifc topic (vulnerability, exploit, technique, etc.)

## Example Objective
> The first phase an attack cycle is reconnaissance. During this phase, attackers use network scans to learn about the scale and characteristics of their target environment. The host/network perimeter logs and Network Intrusion Detection Systems (NIDS) alerts generated by our security infrastructure allow us to detect this activity. This play looks for indicators of someone attempting to gather information about the network and/or the computers, applications, and users it supports in preparation of an attack.

# Analysis
The Analysis section is written for a junior security analyst. It documents how the queries work, why they are written in the way they are, and how to interpret their results. It also describes what a true positive looks like, where a false positive may occur, and how to discern between the two. The Analysis section of events with an Event Type of "Malicious" should focus on what to do with the query results more than the analysis of them.

## Example Analysis
> Scans generates can logs with multiple "one-to-many" network connections in a short amount of time. Yet, attackers have also been observed using "low and slow" techniques to avoid detection. This play looks for IP addresses sending network traffic to multiple computers. The following IP addresses belong to our organization's vulnerability scanners and are known for generating false positives.
> * Logs with the source IP address of a computer outside the 10.11.12.0/24 network are true positives.
> * Reference our Asset Inventory to identify the hostname, user, and department for computers relevant to the investigation.
> * We have observed TCP port 0 in Windows Event logs where ICMP was used.
> * Search online for any port you cannot identify.

# Query
The Query section implements the Objective and produces results for Analysis. Remember, everything needed to understand the *results* are documented in the Analysis section.

## Example Query
> 1. Login to Kibana
> 2. Navigate to the Discover tab
> 3. Add the following fields to the default Visualization: source.ip, source.port, destination.ip, destination.port
> 4. Add the following filter to the default Visualization: Field = source.ip, Operator = exists
> 5. Input the query below into the search bar and then, click-on the Refresh button on the top-right of the screen
> ```
> # insert query here
> ```

# Notes
The Notes section represents an opportunity to disuss ideas for reducing false positives and improving the play. It may also contain other information that doesn't fit into sections above and/or greater clarification for the queries used. 

## References
* https://www.jcs.mil/Portals/36/Documents/Library/Manuals/m651001.pdf?ver=zbA7MXUXDcB9-se9hOxsIA%3d%3d
* https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf

<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/incident-handling/02-identify/README.md#contents">Top of Page</a> |
  <a href="/incident-handling/02-identify/README.md#bottom-of-page">Bottom of Page</a>
</p>

## Bottom of Page
