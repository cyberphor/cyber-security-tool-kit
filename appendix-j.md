**Appendix J**  
**Case Templates**  

**J-1. Overview**  
Our case templates represent what we plan to do if we detect something suspicious or malicious within the network. Each task group below represents a different phase of the incident handling process. 

**J-2. Case Templates**  
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
| Containment | Characterize the incident | Describe the incident category and operational impact level. Incident categories are CAT 1: Root-Level Intrusion, CAT 2: User-Level Intrusion, CAT 3: Unsuccessful Activity Attempt, CAT 4: Denial of Service, CAT 5: Non-Compliance Activity, CAT 6: Reconnaissance, and CAT 7: Malicious Logic. Operational impact levels are high, medium, and low. High operational impact is when a warfighting function is no longer available to any user. Medium operational impact is when a warfighting function is no longer available to some users. Low operational impact is when a warfighting function has lost efficiency. |
