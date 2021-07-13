# Incident Handling Playbook Design

XYZ triggers the defender to invoke a incident detection/response play from their playbook.

## Contents
* [Naming Convention](#naming-convention)
  * [Unique Identifier](#unique-identifier)
  * [Confidence Level](#confidence-level)
  * [Data Source Identifier](#data-source-identifer)
  * [Incident Category](#incident-category)
  * [Description](#description)
* [Objective](#objective)
* [Analysis](#analysis)
* [Query](#query)
* [Notes](#notes)

## Naming Convention
```
<uid>-<cl>-<dsid>-<cat>: <desc>
```

### Examples
* 200-sus-nid-cat6: Detect a network scan
  * Requires the analyst to confirm there as a unauthorized network scan.
* 200-mal-sys-cat5: Respond to a USB violation
  * Requires the analyst to remediate a policy violation.

### Unique Identifer
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

### Confidence Level
#### Suspicious (SUS)
n/a

#### Malicious (MAL)
n/a

### Incident Category
| Category (CAT) | Incident |
| -------------- | -------- |
| CAT0 | Exercise |
| CAT1 | Root-Level Intrusion |
| CAT2 | User-Level Intrusion | 
| CAT3 | Unsuccesful Activity Attempt |
| CAT4 | Denial of Service |
| CAT5 | Non-Compliance Activity | 
| CAT6 | Reconnaissance |
| CAT7 | Malicious Logic |
| CAT8 | Investigating |
| CAT9 | Explained Anonmaly | 

### Description
The Description element summarizes what the play is seeking to address.

# Objective

# Result Analysis

# Query

# Notes
