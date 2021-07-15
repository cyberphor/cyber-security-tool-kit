# Daily Security Checklist
**Instructions**  
1. Perform the checks below, starting top-to-bottom. 
2. Once all checks have been performed, annotate in the SOC journal (i.e. DA 1594) anything marked "Yes."
3. For every check marked "yes", select and execute the appropiate play from our Incident Response Playbook.

## Network Perimeter
| Security Check | No | Yes |
| -------------- | --- | --- | 
| Number of computers online changed?
| Any NIDS alerts?
| Any abnormal network connections?
| Any indicators of a host discovery scan?

## Host Perimeter
| Security Check | No | Yes |
| -------------- | --- | --- |
| Any HIDS alerts?
| Any abnormal network connections?
| Any indicators of a host discovery scan?
| Any indicators of lateral movement?

## System-Level
| Security Check | No | Yes |
| -------------- | --- | --- | 
| Any SIEM alarms trip?
| Any removable media violations?
| Number of administrators changed? 
| Number of users changed?
| Any group membership changes?
| Any failed logins?
| Any password changes? 
| Any indicators of command/scripting interpreter abuse?
| Any indicators the application whitelist policy was enforced?
| Any software installations?

## Application-Level
| Security Check | Yes | No |
| -------------- | --- | --- 
| Any abnormal DNS queries?
| Any abnormal HTTP queries?
| Any abnormal SMB queries?
| Any abnormal LDAP queries?

## Human-Level
| Security Check | No | Yes |
| -------------- | --- | --- |
| Any trouble tickets assigned to our section?
| Any IAVMs relating to technology we use been published?
