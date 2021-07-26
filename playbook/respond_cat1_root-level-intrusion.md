# CAT 1: Root-Level Intrusion

## Containment 
* Disconnect all impacted nodes.
* Disable the compromised administrator account.
* Transition to the next phase once all impacted nodes have been addressed using the procedures above (i.e., do not begin a phase on another computer without first completing the current phase for all computers). 

## Eradication
* Develop a timeline, collect evidence, and determine the root cause using digital forensics. When performing digital forensics, collect volatile data before checking for disk encryption, creating/analyzing the triage image, and imaging the entire drive.   
* Reimage all impacted nodes to remove the tools used to cause the incident (i.e., malware, removable media, etc.). 
* Transition to the next phase once all impacted nodes have been addressed using the procedures above. NOTE: digital forensics may become unnecessary once the root cause has been determined. 

## Recovery
* Change the password of all compromised accounts. 
* Patch all nodes vulnerable to exploits used during the incident. 
* Update all Intrusion Detection Systems (IDS) with the signatures could have detected the incident before it occurred. NOTE: it may be necessary to tune existing signatures or develop custom ones depending on what and how the incident happened.  
* Transition to the next phase once all impacted nodes have been addressed using the procedures above. 

## Post-Incident Activity
* Conduct an After Action Review with the personnel who responded during the incident and generate an executive summary in memorandum format. Ensure to record lessons learned and recommendations for improving prevention, detection, and response capabilities. 
* Submit the generated executive summary to the Information Systems Security Manager (ISSM) for review and action. 
