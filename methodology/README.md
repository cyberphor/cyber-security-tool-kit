<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/methodology/README.md#contents">Top of Page</a> |
  <a href="/methodology/README.md#bottom-of-page">Bottom of Page</a>
</p>

# Methodolgy
## Contents
* [Mission Requirements](#mission-requirements)
* [Asset Inventory and Baseline](#asset-inventory-and-baseline)
* [Threat Modeling](#threat-modeling)
* [Detection Requirements](#detection-requirements)
  * [Detection Enablers](#detection-enablers)
  * [Security Monitoring Checklist](#security-monitoring-checklist)
* [Response Strategies](#response-strategies) 

## Mission Requirements
Below is an example of a Mission Requirements Survey. As a defender, seek out the stakeholders (a.k.a Information Owners) within your organiation and ask them what services, technology, and information require assurance. Use the inherent security objective to design your defense and detection requirements. 

| Stakeholder | Service | Technology | Information | Security Objective |
| ----------- | ------- | ---------- | ----------- | ------------------ |
| HR | Share Files | Share Drive | PII | Confidentiality |
| Sales | Email | Microsoft Outlook | Sale information | Availability | 
| Finance | Store Data | Microsoft SQL Server | Credit card details | Integrity, Confidentiality |

## Asset Inventory and Baseline
* 

## Threat Modeling
* Attack Surface
  * Data Flow Diagrams
    * Source
    * Data Flow
    * Trust Boundary
    * Target 
* Attack Vectors 
* Impact
* Probability

## Detection Requirements
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

## Security Monitoring Checklist

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

## Response Strategies

<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/methodology/README.md#contents">Top of Page</a> |
  <a href="/methodology/README.m"d#>Bottom of Page</a>
</p>

## Bottom of Page
