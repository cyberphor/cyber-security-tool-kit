<p align="right">
  <a href="/windows/applocker/README.md">Home Page</a> |
  <a href="/windows/applocker/README.md#contents">Top of Page</a> |
  <a href="/windows/applocker/README.md#bottom-of-page">Bottom of Page</a>
</p>

# Windows AppLocker
## Contents
* [Configure Default Rules](#configure-default-rules)
* [Allow Admins Access to PowerShell](#allow-admins-access-to-powershell)
* [Deny Users Access to PowerShell, Command Prompt, and WMIC](#deny-users-access-to-powershell-command-prompt-and-wmic)

## Configure Default Rules
Computer Configuration > Policies > Windows Settings > Security Settings > System Services
* Application Identity: Automatic

Computer Configuration > Policies > Windows Settings > Security Settings > Application Control Policies > AppLocker
* Configure Rule Enforcement
  * Executable Rules: Configured, Enforce rules
  * Windows Installer Rules: Configured, Enforce rules
  * Script Rules: Configured, Enforce rules
  * Packaged app Rules: Configured, Enforce rules
* Executable Rules > Create Default Rules
* Windows Installer Rules > Create Default Rules
* Script Rules > Create Default Rules
* Packaged app Rules > Create Default Rules

## Allow Admins Access to PowerShell
Computer Configuration > Policies > Windows Settings > Security Settings > Application Control Policies > AppLocker > Executable Rules
* Create New Rule…
  * Action: Allow
  * User: Administrators
  * Conditions:
    * Path: %SYSTEM32%\WindowsPowerShell\v1.0\*
    * Exceptions: n/a 
  * Name: Allow Admins Access to PowerShell

## Deny Users Access to PowerShell, Command Prompt, and WMIC
Modify the default “All files located in the Windows folder” rule so users have access to all binaries except PowerShell. Repeat for cmd.exe, wmic.exe, etc. 

Computer Configuration > Policies > Windows Settings > Security Settings > Application Control Policies > AppLocker > Executable Rules
* (Default Rule) All files located in the Windows folder > Properties > Exceptions
* Add exception: Path
  * Add > Browse Folders: %SYSTEM32%\cmd.exe
  * Add > Browse Folders: %SYSTEM32%\wbem\WMIC.exe
  * Add > Browse Folders: %SYSTEM32%\WindowsPowerShell\v1.0\*


<p align="right">
  <a href="/windows/applocker/README.md">Home Page</a> |
  <a href="/windows/applocker/README.md#contents">Top of Page</a> |
  <a href="/windows/applocker/README.md#bottom-of-page">Bottom of Page</a>
</p>

## Bottom of Page
