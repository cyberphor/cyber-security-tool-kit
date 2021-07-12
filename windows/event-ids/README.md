<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/windows/event-ids/README.md#contents">Top of Page</a> |
  <a href="/windows/event-ids/README.md#bottom-of-page">Bottom of Page</a>
</p>

# Windows Event IDs
## Contents
* [Firewall](#firewall)
* [Authentication](#authentication)
* [Shares](#shares)
* [Process Execution](#process-execution)
* [AppLocker](#applocker) 
* [Command and Scripting Interpeter](#command-and-scripting-interpeter)
* [Privileged Users](#privileged-users)
* [Scheduled Tasks](#scheduled-tasks)
* [Services](#services)
* [Acccount Management](#account-management)
* [Removable Media](#removable-media)
* [Log Management](#log-management)
* [Printing](#printing)
* [DNS](#dns)
* [Wireless Network Activity](#wireless-network-activity)
* [References](#references)

### Firewall
| Event ID | Log | Description | Evidence of | 
| -------- | --- | ----------- | ----------- | 
| 5152 | Security Log | The Windows Filtering Platform blocked a packet. | Reconnaissance |
| 5156 | Security Log | The Windows Filtering Platform has allowed a connection. | Initial Access |
| 5157 | Security Log | The Windows Filtering Platform has blocked a connection. | Reconnaissance | 

### Authentication
| Event ID | Log | Description | Evidence of | 
| -------- | --- | ----------- | ----------- | 
| 4624 | Security Log | An account was successfully logged on. | Initial Access |
| 4625 | Security Log | An account failed to log on. | Credential Access |

### Shares
| Event ID | Log | Description | Evidence of | 
| -------- | --- | ----------- | ----------- | 
| 5140 | Security Log | A network share was accessed. | Discovery |
| 5145 | Security Log | A network share was checked to see whether the client can be granted desired access. | Discovery |

## References
* https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx
* https://attack.mitre.org/matrices/enterprise/windows/
* https://www.malwarearchaeology.com/cheat-sheets

<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/windows/event-ids/README.md#contents">Top of Page</a> |
  <a href="/windows/event-ids/README.md#bottom-of-page">Bottom of Page</a>
</p>

## Bottom of Page
