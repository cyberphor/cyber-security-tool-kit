### How to Configure Windows Event Forwarding

---

**Task.** Configure Windows Event Forwarding (WEF).

**Purpose.** WEF allows you to read and collect logs from computers running Microsoft Windows and forward them to a Windows Event Collector (WEC) server of your choosing. 

**Conditions.** You have domain administrator privileges and access to Remote Server Administration Tools (RSAT).  

**Standard.** You were able to create a Group Policy Object (GPO) for WEF.

**Note.** When performing this procedure, replace “evil.corp” with your domain’s actual name and “SITEAAAAAAB6WEC” with your WEC server’s actual hostname. 

---

**Step 1.** Open the “Group Policy Management” snap-in. 

**Step 2.** Navigate to the “Group Policy Objects” container under the path below. Click-on “New.”
* Forest > Domains > evil.corp

**Step 3.** Name the GPO “Windows Event Forwarding (WEF)” when prompted. 

**Step 4.** Navigate to the “Windows Event Forwarding (WEF)” GPO under the path below, right click-on it, and then, select “Edit.”
* Forest > Domains > evil.corp > Group Policy Objects 

**Step 5.** Within the GPO open, navigate to the path below. 
* Computer Configuration > Policies > Administrative Templates > Windows Components > Event Forwarding

**Step 6.** Configure the GPO with the settings listed below. 
* Configure target Subscription Manager
  * Subscription Managers: Server=http://SITEAAAAAAB6WEC:5985/wsman/SubscriptionManager/WEC

**Step 7.** Within the GPO still open, navigate to the path below. 
* Computer Configuration > Policies > Administrative Templates > Windows Components > Event Log Service > Security

**Step 8.** Configure the GPO with the settings listed below. 
* Log Access: O:BAG:SYD:(A;;0xf0007;;;SY)(A;;0x7;;;BA)(A;;0x1;;;BO)(A;;0x1;;;SO)(A;;0x1;;;S-1-5-32-573)(A;;0x1;;;S-1-5-20)

**Step 9.** Navigate to your desired Organizational Unit (OU) container, select “Link an Existing GPO…” and then, select “Windows Event Forwarding (WEF)” when prompted. 
