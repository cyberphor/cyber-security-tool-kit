### Audit Policy GPO
Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies
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

Computer Configuration > Policies > Administrative Templates > Windows Components > Windows PowerShell
* Turn on Module Logging: Enabled 
* Turn on Script Block Logging: Enabled 
