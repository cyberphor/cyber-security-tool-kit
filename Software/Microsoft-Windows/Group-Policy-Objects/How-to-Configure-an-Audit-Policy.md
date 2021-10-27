### How to Configure an Audit Policy


**Task.** Configure an Audit Policy.

**Purpose.** An audit policy specifies categories of security-related events you want to audit.

**Conditions.** You have domain administrator privileges and access to Remote Server Administration Tools (RSAT).  

**Standard.** You were able to create a Group Policy Object (GPO) for auditing.

---

**Step 1.** Open the “Group Policy Management” snap-in. 

**Step 2.** Navigate to the “Group Policy Objects” container under the path below. Click-on “New.”
* Forest > Domains > evil.corp

**Step 3.** Name the GPO “Audit Policy” when prompted. 

**Step 4.** Navigate to the “Audit Policy” GPO under the path below, right click-on it, and then, select “Edit.”
* Forest > Domains > evil.corp > Group Policy Objects 

**Step 5.** Within the GPO open, navigate to the path below. 
Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies

**Step 6.** Configure the GPO with the settings listed below. 
* Account Management
  * Audit User Account Management: Success
  * Audit Security Group Management: Success
* Detailed Tracking
  * Audit Process Creation: Success
  * Logon/Logoff
  * Audit Logon: Success, Failure
  * Audit Special Logon: Success
* Object Access
  * Audit File Share: Success
  * Audit File System: Success
  * Audit Filtering Platform Connection: Success
  * Audit Registry: Success
  * Audit Removable Storage: Success
  * Audit Other Object Access: Success
* Policy Change
  * Audit Policy Change: Success
* System
  * Audit Security System Extension: Success, Failure

**Step 7.** Within the GPO still open, navigate to the path below. 
* Computer Configuration > Policies > Administrative Templates > Windows Components > Windows PowerShell

**Step 8.** Configure the GPO with the settings listed below. 
* Turn on Module Logging: Enabled
* Turn on Script Block Logging: Enabled

**Step 9.** Navigate to your desired Organizational Unit (OU) container, select “Link an Existing GPO…” and then, select “Audit Policy” when prompted. 
