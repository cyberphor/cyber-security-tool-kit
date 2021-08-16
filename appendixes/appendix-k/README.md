# Appendix K
## Case Templates

### K-1. Overview
Our case templates represent what we plan to do if we detect something suspicious or malicious within the network. Every Task Group below represents a different phase of the incident handling process. 

### K-2. Case Templates
* Template name: Suspicious activity 
* Title prefix: Case: 
* Severity: Medium
* TLP: Amber
* PAP: Amber
* Tags: triage
* Description: Suspicious activity has been detected.
* Tasks. See below. 

| Phase | Task | Description |
| ---------- | ---------- | ---------------- |
| Detection | Check | Identify what check (by number) from the Daily Security Monitoring Checklist produced something worth investigating. Describe as much as possible. If available, provide the IP address, port, protocol, hostname, username, activity, etc. |
| Analysis | Investigate | Question existing observations, develop a hypothesis, search related data sources for answers, and generate a conclusion on what happened. |
| Analysis | Triage | Compare what happened to what is allowed to happen. Consult with the ISSO, AUP, NDA, PAA, etc. to make a determination. Annotate if the event is a true or false positive within the case file. If it is a false positive, delete the Containment, Eradication, and Recovery tasks from the case and transition to tasks in the Post-Incident Activity Task Group. If it is a true positive, ensure to complete all Task Groups. |
