# Chapter 5
## Containment Procedures

### 5-1. Overview
The Containment sub-phase begins when an incident is declared and ends when computers impacted can be taken offline for clean-up. During this incident handling phase, short-term containment and evidence collection procedures are executed. In situations where affected computers must remain available to the organization, long-term containment procedures will be performed. The purpose of the Containment phase is to control the spread of an incident.  

### 5-2. Short-Term Containment Procedures
Cyber Defense personnel must execute the procedures below when containing an incident.
* Characterize the incident. 
* Assign a primary and assistant handler to the incident.
* Notify the ISSO.
* Update the case file within our IMS server.
* Get approval from the ISSO to disconnect and/or disable those impacted.
* Disconnect any impacted computer from the network.
* Disable any account abused during the incident.

### 5-3. Evidence Collection Procedures
Cyber Defense personnel must execute the procedures below when performing digital forensics. The purpose of this sub-phase is to collect evidence and facilitate the selection of a response plan.
* Connect a hardware write-blocker to the impacted computer. 
* Collect memory data. If the computer was powered-off, collect memory data from crash, hibernation, and/or page files. 
* Check for disk encryption. 
* Create a triage image. Collect the Registry, .lnk files, jump lists, prefetch files, logs, browser data, the Recycle Bin, the Master File Table, and hibernation files.  
* Analyze the triage image and determine if an image of the entire computer is necessary. If yes, image the entire computer. 
* Determine if the impacted computer can be unavailable for an extended period of time. If yes, skip the long-term containment phase and begin executing eradication procedures. If no, begin executing long-term containment procedures. 

### 5-4. Long-Term Containment Procedures
Cyber Defense personnel must execute the procedures below to contain incidents where affected computers cannot be taken offline. 
* Change the password to any account abused during the incident. 
* Stop any unauthorized processes on the impacted computer. 
* Patch the computers impacted as well as any nearby (within the same Virtual Local Area Network or subnet) computers if a vulnerability was exploited. 
