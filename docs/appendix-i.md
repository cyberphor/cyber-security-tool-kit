**Appendix I**  
**Daily Security Monitoring Checklist**

**I-1. Instructions**  
Perform the checks listed in paragraph J-3 starting top-to-bottom. Annotate everything observed on a blank DA Form 1594. Any check that did not produce anything significant, put “NSTR” (or “Nothing significant to report”). Reference the procedures below and the DA Form 1594 within this appendix for an example of how to annotate a finding. After all checks have been performed, create a case for each on our IMS server to escalate the event to the Cyber Defense Incident Responder. 
* Page Number. Put the page number. 
* Number of Pages. Put the total number of pages. 
* Organization or Installation. Put our section followed by our unit identifier. 
* Location. Put our building number. 
* Period Covered - From. Put the time checks began (use the DD MMM YY date format).
* Period Covered - To. Put the time close-of-business occurred (use the same format).
* Item Number. Put the Item Number of the check. Use the same Item Number for the check you are referencing even if you add entries for other checks. Entries about a check do not need to be consecutive. 
* Time in. Put the time the current observation was added to the journal.
* Time out. Leave this field blank.
* Incidents, Messages, Orders, etc. Record all details relating to the check being executed in this column. A single entry does not need to fit on one line. If a check produces nothing significant, put “NSTR” (or “Nothing significant to report”).
* Action Taken. Put one of the following: logged (L), escalated (E), or false positive (F).
* Initials. Put your initials in this field. 
* Typed Name and Grade of Officer or Official on Duty. Leave this field blank.
* Signature. Leave this field blank.

**I-2. Example Security Monitoring DA Form 1594**  
Image goes here.

**I-3. Daily Security Monitoring Checklist**  
| No. | Source | Check |
| --- | ----------- | ----- |
| 01 | PowerShell | **Asset Inventory:** Use PowerShell to sweep our network and identify computers currently online. The number of replies should match our baseline.   |
| 02 | PowerShell | **Domain Administrators:**  Use PowerShell (or Active Directory) to query our Domain Controller and identify the number of accounts in the Domain Admins group. The number should match our baseline. |
| 03 | PowerShell | **Local Administrators:** Query all computers currently online for members of the local Administrators group. The number of local Administrators from each query should match our baseline. |
| 04 | IDS Alerts | **IDS Alerts:** Login to our SIEM server and query for all IDS alerts. Organize the output into the following columns: source.ip, rule.uuid, rule.name, and rule.rule. |
