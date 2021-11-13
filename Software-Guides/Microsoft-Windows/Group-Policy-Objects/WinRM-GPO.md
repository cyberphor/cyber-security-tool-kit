### WinRM
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
