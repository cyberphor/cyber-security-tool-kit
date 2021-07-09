<p align="right">
  <a href="/windows/logging/README.md">Home Page</a> |
  <a href="/windows/logging/README.md#contents">Top of Page</a> |
  <a href="/windows/logging/README.md#bottom-of-page">Bottom of Page</a>
</p>

# Windows Logging 

## Contents
* [Audit Policy](#audit-policy)
* [Windows Remote Management (WinRM)](#windows-remote-management-winrm)

## Audit Policy
Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies
* Account Management
  * Audit User Account Management: Success (Event ID 4720, 4722, 4723, 4724)
  * Audit Security Group Management: Success (Event ID 4728, 4732, 4756)
* Detailed Tracking
  * Audit Process Creation: Success (Event ID 4688)
* Logon/Logoff
  * Audit Logon: Success, Failure (Event ID 4624, 4625)
  * Audit Special Logon: Success (Event ID 4672)
* Object Access
  * Audit File Share: Success (Event ID 5140, 5145)
  * Audit File System: Success (Event ID 4663)
* Audit Filtering Platform Connection: Success (Event ID 5152, 5156, 5157)
  * Audit Registry: Success (Event ID 4663)
  * Audit Removable Storage: Success (Event ID 6416)
  * Audit Other Object Access: Success (Event ID 4698)
* Policy Change
  * Audit Policy Change: Success (Event ID 4719)
* System
  * Audit Security System Extension: Success, Failure (Event ID 4697, 7040, 7045)

Computer Configuration > Policies > Administrative Templates > Windows Components > Windows PowerShell
* Turn on Module Logging: Enabled (Event 4103)
* Turn on Script Block Logging: Enabled (Event 4104)

**Script to Enable Logs Not Supported via Group Policy**
```cmd
wevtutil sl "Microsoft-Windows-AppLocker/EXE and DLL" /e:true # 8004 
wevtutil sl "Microsoft-Windows-AppLocker/MSI and Script" /e:true # 8007
wevtutil sl "Microsoft-Windows-DNS-Client/Operational" /e:true # 3006
wevtutil sl "Microsoft-Windows-PrintService/Operational" /e:true # 307
wevtutil sl "Microsoft-Windows-WLAN-AutoConfig/Operational" /e:true # 8001/2
```

## Windows Remote Management (WinRM)
Computer Configuration > Preferences > Control Panel Settings > Services
  * New Service
  * Startup: Automatic
  * Service name: WinRM
  * Service action: Start service
Computer Configuration > Policies > Administrative Templates > Windows Components > Windows Remote Management (WinRM) > WinRM Service
  * Allow remote server management through WinRM: Enabled
  * IPv4 filter: *
Computer Configuration > Policies > Administrative Templates > Network > Network Connections > Windows Defender Firewall > Domain Profile
  * Windows Defender Firewall: Allow inbound remote admin…: Enabled
  * IPv4: *
Computer Configuration > Policies > Windows Settings > Security Settings > Windows Firewall with Advanced Security > Windows Defender Firewall with Advanced Security > Windows Defender Firewall with Advanced Security
  * Inbound Rules: New Rule
  * Predefined:  Windows Remote Management
  * Public: Uncheck
  * Allow the connection: Checked

## References
* https://www.malwarearchaeology.com/s/Windows-Advanced-Logging-Cheat-Sheet_ver_Feb_2019_v12.pdf 
* https://attack.mitre.org/ 
* https://github.com/nsacyber/Event-Forwarding-Guidance/tree/master/Events 

<p align="right">
  <a href="/windows/logging/README.md">Home Page</a> |
  <a href="/windows/logging/README.md#contents">Top of Page</a> |
  <a href="/windows/logging/README.md#bottom-of-page">Bottom of Page</a>
</p>

## Bottom of Page
