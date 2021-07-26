<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/00-prerequisites/windows/firewall.md#contents">Top of Page</a> |
  <a href="/00-prerequisites/windows/firewall.md#bottom-of-page">Bottom of Page</a>
</p>

# Windows Firewall

## Contents
* [Block PowerShell](#block-powershell)
* [Block Command Prompt](#block-command-prompt)
* [Block WMIC](#block-wmic)

## Block PowerShell
Computer Configuration > Policies > Windows Settings > Windows Firewall with Advanced Security > Inbound Rules 
  * Rule Type: Program
  * Program: %SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe
  * Action: Allow the connection if it is secure
  * Users: Exceptions - Admins
  * Computers: n/a
  * Profile: Domain, Private, Public
  * Name: Block PowerShell

Computer Configuration > Policies > Windows Settings > Windows Firewall with Advanced Security > Inbound Rules 
  * Rule Type: Program
  * Program: %SystemRoot%\System32\WindowsPowerShell\v1.0\powershell_ise.exe
  * Action: Allow the connection if it is secure
  * Users: Exceptions - Admins
  * Computers: n/a
  * Profile: Domain, Private, Public
  * Name: Block PowerShell ISE

## Block Command Prompt
Computer Configuration > Policies > Windows Settings > Windows Firewall with Advanced Security > Inbound Rules 
  * Rule Type: Program
  * Program: %SystemRoot%\System32\cmd.exe
  * Action: Allow the connection if it is secure
  * Users: Exceptions - Admins
  * Computers: n/a
  * Profile: Domain, Private, Public
  * Name: Block Command Prompt

## Block WMIC
Computer Configuration > Policies > Windows Settings > Windows Firewall with Advanced Security > Inbound Rules 
  * Rule Type: Program
  * Program: %SystemRoot%\Windows\System32\wbem\WMIC.exe
  * Action: Allow the connection if it is secure
  * Users: Exceptions - Admins
  * Computers: n/a
  * Profile: Domain, Private, Public
  * Name: Block WMIC

<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/00-prerequisites/windows/firewall.md#contents">Top of Page</a> |
  <a href="/00-prerequisites/windows/firewall.md#bottom-of-page">Bottom of Page</a>
</p>

## Bottom of Page
