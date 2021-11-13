### How to Install McAfee ePolicy Orchestrator (ePO)

**Task.** Install McAfee ePolicy Orchestrator (ePO).

**Purpose.** McAfee ePO is a management console for the McAfee Endpoint Security (ENS) Platform. It is also used to manage other modules such as ENS Firewall, ENS Web Control, and ENS Threat Prevention. McAfee ePO is one of the most important components of the Army Enterprise Security System (AESS), formerly known as the Host-Based Security System (HBSS).

**Conditions.** You have two computers.
* Required software:
  * https://www.mcafee.com/enterprise/en-us/downloads/my-products.html 
  * Grant Number: REDACTED	
* Verify compatibility of the McAfee software available with your version of Windows:
  * https://kc.mcafee.com/corporate/index?page=content&id=KB85784
* Microsoft Windows Server 2012 R2: 
  * 8 GBs of RAM
* Microsoft Windows 10: 
  * Version 1507 (Build 10240): ENS 10.1
  * Version 1607 (Build 14393): ENS 10.2
  * Version 1703 (Build 15063): ENS 10.5.1
  * Version 1709 (Build 16299): ENS 10.5.3
  * Version 1809 (Build 17763): ENS 10.5.5
  * Version 21H1 (Build 19043): ENS 10.7.0

**Standard.** You were able to install SQL Server Express, SQL Server Management Studio Express, and McAfee ePO. You were able to use McAfee ePO’s Agent Deployment URL to install Endpoint Security (ENS) onto a client workstation. 

**Step 3.** Download SQL Server 2012 Express and Management Studio.  
https://www.microsoft.com/en-us/download/details.aspx?id=56042

**Step 4.** Download McAfee ePO. 

**Step 5.** Install SQL Server 2012 Express.

**Step 6.** Install SQL Server Management Studio 2012 Express.

**Step 7.** Open “SQL Server Configuration Manager,” navigate to “SQL Server Network Configuration” > “Protocols for MSSQLSERVER,” and then, right-click on “TCP/IP” and select “Properties.” Enable the TCP/IP protocol for this server instance. 

**Step 8.** With “SQL Server Configuration Manager” still open, navigate to “SQL Server Services” and right-click on “SQL Server Browser” and select “Properties.” Under the “Service” tab, set the “Start Mode” to “Automatic” and then close the pop-up window. With “SQL Server Services” still highlighted, right-click “SQL Server (MSSQLSERVER)” and select “Restart.”

**Step 9.** Patch SQL Server 2012 Express.

**Step 10.** Install McAfee ePO. 
* Database Server: WS2012R2\MSSQLSERVER
* Database Name: ePO_WS2012R2
* Windows authentication (same as what you used during the SQL server installation)
  * Domain: REDACTED
  * Username: REDACTED
  * Password: REDACTED
* SQL Server TCP Port (grayed-out): 1433

**Step 10a (Optional).** Enable 8.3 naming convention compliance. Using Regedit, navigate to the key below and update it accordingly. Then, reboot the computer. 
* HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
  * NtfsDisable8dot3NameCreation
    * Set “Value date” to 0

**Step 11.** Configure administrator information.
* Username: victor.fernandez.epo
* Password: REDACTED
* Passphrase (used to encrypt/decrypt server snapshots): 

**Step 12.** Enter the ePO License Key (REDACTED).

**Step 13.** Modify Windows Firewall rules on the McAfee ePO server to allow inbound communication via the Domain profile. 

**Step 14.** Browse to the management console.  
* https://WS2012R2:8443/core/

**Step 15.** Deploy McAfee Updater agent. 

**Step 16.** Deploy McAfee the Endpoint Security Platform. 

**Step 17.** GPO.  
* https://docs.mcafee.com/bundle/agent-5.6.x-installation-guide/page/GUID-43388B39-6623-434D-A354-535DE3805F96.html 
