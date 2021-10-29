### How to Configure Windows Remote Management (WinRM)

---

**Task.** Configure Windows Remote Management (WinRM).

**Purpose.** WinRM allows you to remotely access computers and exchange software/hardware information.

**Conditions.** You have domain administrator privileges and access to Remote Server Administration Tools (RSAT).  

**Standard.** You were able to create a Group Policy Object (GPO) for WinRM.

**Note.** When performing this procedure, replace “evil.corp” with your domain’s actual name.

---

**Step 1.** Open the “Group Policy Management” snap-in. 

**Step 2.** Navigate to the “Group Policy Objects” container under the path below. Click-on “New.”
* Forest > Domains > evil.corp

**Step 3.** Name the GPO “Windows Remote Management (WinRM)” when prompted. 

**Step 4.** Navigate to the “Windows Remote Management (WinRM)” GPO under the path below, right click-on it, and then, select “Edit.”
* Forest > Domains > evil.corp > Group Policy Objects 

**Step 5.** Within the GPO open, navigate to the path below. 
* Computer Configuration > Preferences > Control Panel Settings > Services

**Step 6.** Configure the GPO with the settings listed below. 
* New Service
* Startup: Automatic
* Service name: WinRM
* Service action: Start service

**Step 7.** Within the GPO still open, navigate to the path below. 
* Computer Configuration > Policies > Administrative Templates > Windows Components > Windows Remote Management (WinRM) > WinRM Service

**Step 8.** Configure the GPO with the settings listed below.
* Allow remote server management through WinRM: Enabled
* IPv4 filter: *

**Step 9.** Within the GPO still open, navigate to the path below. 
* Computer Configuration > Policies > Administrative Templates > Network > Network Connections > Windows Defender Firewall > Domain Profile

**Step 10.** Configure the GPO with the settings listed below.
* Windows Defender Firewall: Allow inbound remote admin…: Enabled
* IPv4: *

**Step 11.** Within the GPO still open, navigate to the path below. 
* Computer Configuration > Policies > Windows Settings > Security Settings > Windows Firewall with Advanced Security > Windows Defender Firewall with Advanced Security > Windows Defender Firewall with Advanced Security

**Step 12.** Configure the GPO with the settings listed below.
* Inbound Rules: New Rule
* Predefined: Windows Remote Management
* Public: Uncheck
* Allow the connection: Checked

**Step 13.** Navigate to your desired Organizational Unit (OU) container, select “Link an Existing GPO…” and then, select “Audit Policy” when prompted. 
