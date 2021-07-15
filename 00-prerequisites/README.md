<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/00-prerequisites/README.md#contents">Top of Page</a> |
  <a href="/00-prerequisites/README.md#bottom-of-page">Bottom of Page</a>
</p>

# Prerequisites
## Contents
* [Framework Comparisons](#framework-comparisons)
* [Mission Requirements](#mission-requirements)
* [Team](#team)
* [Asset Inventory](#asset-inventory)
* [Baselines](#baselines)
* [Threat Model](#threat-model)
* [Battle Rhythm](#battle-rhythm)

## Framework Comparisons
| SANS <br> PICERL | NIST <br> Risk Management Framework | NIST <br> Incident Response Life Cycle  | NIST <br> Cybersecurity Framework |
| ------ | --- | ---- | --------- |
| Prepare | Categorize <br> Select <br> Implement <br> Assess <br> Authorize <br> | Preparation | Identify <br> Protect | 
| Identify | Monitor | Detection & Analysis | Detect |
| Contain | Monitor | Containment, Eradication, and Recovery | Respond |
| Eradicate | Monitor | Containment, Eradication, and Recovery | Respond |
| Recover | Monitor | Containment, Eradication, and Recovery | Recover |
| Lessons Learned | Monitor | Post-Incident Activity | Recov

## Mission Requirements
Below is an example of a Mission Requirements Survey. As a defender, seek out the stakeholders (a.k.a Information Owners) within your organiation and ask them what services, technology, and information require assurance. Use the inherent security objective to design your defense and detection requirements. 

| Stakeholder | Service | Technology | Information | Security Objective |
| ----------- | ------- | ---------- | ----------- | ------------------ |
| HR | Share Files | Share Drive | PII | Confidentiality |
| Sales | Email | Microsoft Outlook | Sale information | Availability | 
| Finance | Store Data | Microsoft SQL Server | Credit card details | Integrity, Confidentiality |

## Team
### Personnel
* ISSM
* ISSO
* System administrator
* Network administrator

## Asset Inventory
| IP Address | Hostname | MAC Address | Serial Number | Last User | Office | Grid Square |
| ---------- | -------- | ----------- | ------------- | --------- | ------ | ----------- |
| 10.11.12.13 | COMPUTER1 | aaaa:bbbb:cccc | 123456 | joe.dee | IT Dept. | C4 |
| 10.11.12.14 | COMPUTER3 | bbbb:cccc:aaaa | 123666 | jim.bean | C-Suite | D9 |
| 10.11.12.15 | COMPUTER5 | cccc:aaaa:bbbb | 696969 | jack.daniel | HR Dept. | A2 |

## Baselines
* List of unique hardware
* List of unique software
* Image
  * Administrators
  * Users
  * Software
  * Services
* Security controls
* Network activity
  * By the hour
  * IP addresses
  * Activity

## Threat Model
* Attack Surface
  * Data Flow Diagrams
    * Source
    * Data Flow
    * Trust Boundary
    * Target 
* Attack Vectors 
* Impact
* Probability

## Battle Rhythm
### Daily
* Network perimeter logs
* Host perimeter logs

### Weekly
* Backups
* Vulnerabilities
* Misconfigurations

### Monthly
* Asset inventory

### Quarterly
* Baseline
* Documentation

### Annually
* Threat model

<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/00-prerequisites/README.md#contents">Top of Page</a> |
  <a href="/00-prerequisites/README.md#bottom-of-page">Bottom of Page</a>
</p>

## Bottom of Page
