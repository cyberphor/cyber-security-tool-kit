**Task.** Collect cyber threat intelligence from the CrowdStrike Falcon X platform and MITRE ATT&CK framework. 

**Purpose.** Using cyber threat intelligence platforms like CrowdStrike Falcon X allows you to enhance endpoint security, automate investigations, and reduce response times. MITRE ATT&CK is a curated knowledge base and model for cyber adversary behavior, reflecting the various phases of an adversary’s attack lifecycle and the platforms they are known to target.

**Conditions.** CrowdStrike Falcon X platform account

**Standard.** You were able to collect cyber threat intelligence about a specific Advanced Persistent Threat (APT) group and improve your incident detection and response playbooks. 

**Step 1.** Login. 
* URL: https://falcon.crowdstrike.com/login/ 
  * Username: REDACTED
  * Password: REDACTED

**Step 2.** Click-on the falcon icon in the top-left corner. 

**Step 3.** Click-on “Actors” under the “Intelligence” column. 

**Step 4.** Select the options below.
* Target Countries: United States
* Target Industries: Government, Military
* Origin: China, Russia, North Korea, Iran
  * References
    * https://us-cert.cisa.gov/china
    * https://us-cert.cisa.gov/russia
    * https://us-cert.cisa.gov/northkorea
    * https://us-cert.cisa.gov/iran 
* Motivation: State-Sponsored

**Step 5.** Click-on “View Profile” under your APT group of focus (ex: Fancy Bear). 

**Step 6.** Review available reports by type (ex: Periodic Report, Alert, Tipper, Intelligence Report). 

**Step 7.** Review the APT group’s metadata under “Kill Chain” and “Community Identifiers.”
Map the APT group’s methodology and techniques to the MITRE ATT&CK framework (see next page for an example). Use these mappings to enhance your incident detection and response playbooks. 
* https://attack.mitre.org/matrices/enterprise/ 









