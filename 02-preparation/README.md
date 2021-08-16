# Chapter 2
## Preparation Procedures

### 2-1. Overview
The Preparation phase is when we take actions to establish, maintain, sustain, and/or improve our incident handling capability. Capabilities are represented by the people, processes, and technology an organization has available to achieve an effect. The authority for our Cyber Defense personnel to conduct incident handling originates from our organization’s Operating Forces Security Plan (OFSP) and Incident Response Plan (IRP). This chapter identifies additional requirements for detecting, analyzing, and responding to incidents. 

### 2-1. People
The Information Systems Security Manager (ISSM), Information Systems Security Officer (ISSO), Cyber Defense Infrastructure Support Specialist, and Cyber Defense Incident Responder are responsible for the implementation and execution of the SOPs contained within this document. The ISSM and ISSO will ensure our organization is compliant with the Risk Management Framework while Cyber Defense personnel will detect, analyze, and respond to incidents. For more information on the definition, separation, and responsibilities of these work roles see appendix B, NIST SP 800-181, DoD 8570.01-M, AR 25-2, and DA PAM 25-2-6. 

### 2-2. Processes
* Incident Handling. Cyber Defense personnel will perform incident handling procedures using the process illustrated in Figure 1. 
* Threat Modeling. Our security monitoring requirements originate from the organization’s threat model. A threat model describes the organization’s attack surface, the attack vectors a threat actor might use, and the impact if an incident occurs. Our unit’s threat model is represented by the Data Flow Diagram (DFD) in appendix C, the STRIDE Matrix in appendix D, and the four Detection Zones discussed in chapter 3.
* Asset Inventory. Cyber Defense personnel will coordinate with the ISSO to develop and maintain an Asset Inventory. An Asset Inventory is a list of network-connected computers belonging to the organization. For every computer on the Asset Inventory, the following information must be identified: IP address, hostname, MAC address, serial number, manufacturer, model, current user, building number, and room number. See appendix E for a PowerShell script that automates collecting some of this information. The Asset Inventory must be reviewed monthly. 
* Baselines. Cyber Defense personnel will coordinate with the ISSO to identify and maintain baselines for the information listed in appendix F. Baselines help detect unauthorized changes, anomalous activity, and vulnerabilities. See appendix F for a list of helpful queries to run (NOTE: some of these queries require third-party software such as the Windows Sysinternals Suite).
* Battle Rhythm. A battle rhythm identifies the working groups necessary to assist the organization make decisions. It arranges the sequence and timing of reports, meetings, and briefings based on leadership preferences and the mission. There is no standard battle rhythm for all organizations. See appendix G for the battle rhythm Cyber Defense personnel will follow. 
* Case Management.  
  * TLP.
  * PAP.

### 2-3. Technology
Incident handling technology includes, but is not limited to directory servers, configuration management servers, log servers, Security Incident and Event Management (SIEM), Incident Management System (IMS) servers, Security Admin Workstations (SAWs), Threat Intelligence Platforms (TIPs), and a deployable incident response toolkit. See appendix H for the hardware and software list that represents our technology requirements and solutions. See appendix I for the corresponding procedures on installing, operating, and maintaining these technology requirements. 
* Directory Servers. Directory servers allow Cyber Defense personnel to lookup metadata about objects that represent and describe users and computers. 
* Configuration Management Servers. Configuration management servers allow Cyber Defense personnel to ensure protective, detective, and reactive measures are enabled and configured. Examples of protective measures are host-based firewalls and application whitelisting programs. Examples of detective measures are logging and log forwarding. Examples of reactive measures are survey tools and remote access programs. 
* Log Servers. Log servers allow Cyber Defense personnel to collect logs for compliance and optimization. It is more efficient to send logs to one or more log servers instead of having all computers bombard a single SIEM server. 
* SIEM Servers. A SIEM server allows Cyber Defense personnel to normalize, filter, analyze, and correlate events. IMS Server. An IMS server allows Cyber Defense personnel to create case files, task incident handlers, document event details, store digital evidence, and guide response actions. 
* SAWs. SAWs provide Cyber Defense personnel the ability to query the network, remotely access other computers, and investigate suspicious activity. 
* TIPs. TIPs allow Cyber Defense personnel to automate the receipt, consolidation and integration of threat data into incident handling. 
* Deployable Incident Response Toolkit. A deployable incident response toolkit is a self-contained collection of incident handling technology and supplies. It allows Cyber Defense personnel to detect, analyze, and respond to incidents within operating environments outside their normal battlespace. 
