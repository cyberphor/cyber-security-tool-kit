# Chapter 4  
## Analysis Procedures  

### 4-1. Overview  
The Analysis sub-phase of incident handling is when we investigate and then triage escalated events. An event triaged as a false positive does not require Containment, Eradication, or Recovery procedures. Yet, the Post-Incident Activity phase should still be executed for optimization and training purposes. An event triaged as a true positive will be declared as an incident.

### 4-2. Investigation Procedures  
The goal of an investigation is to collect evidence and use it to bridge the gap between perception and reality. The receipt of an IDS alert does not always mean an incident actually occurred. Additional context is required. Context is achieved by compounding and weaving together metadata about an event. Examples of metadata are the date and time of event, or the identity used to launch a suspicious process into memory. In order to collect metadata, build context, and determine if an event is benign or not, Cyber Defense personnel will use two methodologies championed by Chris Sanders: the Universal Investigative Process and RECAP. Chris Sanders is the author of multiple references listed in appendix A.
* The Universal Investigative Process. The Universal Investigative Process involves questioning existing observations, developing hypotheses, searching related data sources for answers, and generating conclusions.
* RECAP (Reduce, Expand, Chart, Aggregate, and Pivot). RECAP is a collection of techniques for transforming data. By changing the form of data, we can gain new perspectives and develop better questions about the same event.
  * Reduce. Filter out data (focus on a specific time period, computers, etc).
  * Expand. Filter in data (review a bigger time period, include more computers, etc.). This technique is comparable to long-tail analysis or ranking events to identify outliers.  
  * Chart. Visual data using bars, lines, and graphs.
  * Aggregate. Organize data based on their unique data fields.
  * Pivot. Search a data source, pick a field and value of interest, and then see if they can be found in other data sources. Examples of values one can pivot with are IP addresses, ports, domain names, usernames, file hashes, and process names. Examples of data sources are alerts, netflow, transaction logs, trends, Packet Capture (PCAP) files, open source intelligence, Windows events, Registry keys, and file systems.  

### 4-3. Triage Procedures  
True positives are events that were confirmed to be computer security violations while false positives are not. Cyber Defense personnel will triage events into one of these two categories by comparing what happened to what is allowed to happen. For example, someone accessing another person’s account without authorization is a computer security policy violation. Yet, a USB connection could be considered benign if the culprit had permission. Cyber Defense personnel will consult with the ISSO, Acceptable Use Policies (AUPs), Non-Disclosure Agreements (NDAs), Privileged Access Agreements (PAAs), etc. to make their determinations.  
