### How to Configure an Audit Policy on a Stand-Alone Computer

---

**Task.** Configure an audit policy on a stand-alone computer.

**Purpose.** An audit policy specifies categories of security-related events you want to audit.

**Conditions.** You have domain administrator privileges and access to Remote Server Administration Tools (RSAT).  

**Standard.** You were able to configure an audit policy on a stand-alone computer.

---

```
auditpol /get /category:*
```

The Sexy Six (Event IDs 4624, 4663, 4688, 5140, 5156, 7040, 7045).
```pwsh
auditpol /set /subcategory:"Logon" /success:enable /failue:enable
```
```pwsh
auditpol /set /subcategory:"File System" /success:enable
```
```pwsh
auditpol /set /subcategory:"Process Creation" /success:enable
```
```pwsh
auditpol /set /subcategory:"File Share" /success:enable
```
```pwsh
auditpol /set /subcategory:"Registry" /success:enable
```
```pwsh
auditpol /set /subcategory:"Filtering Platform Connection" /success:enable
```

Scheduled Tasks (Event ID 4698).
```pwsh
auditpol /set /subcategory:"Other Object Access Events" /success:enable
```

Removable Media (Event ID 6416).
```cmd
auditpol /get /subcategory:"Plug and Play Events"
auditpol /set /subcategory:"Plug and Play Events" /success:enable
```

Powershell (Event ID 4103 and 4104).
```pwsh
$BlockLogging = 'HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging' 
New-Item $BlockLogging
New-ItemProperty $BlockLogging -Name 'EnableBlockLogging' -PropertyType Dword
Set-ItemProperty $BlockLogging -Name 'EnableBlockLogging' -Value '1'

$ModuleLogging = 'HKLM:\Software\WOW6432Node\Policies\Microsoft\Windows\PowerShell\ModuleLogging'
New-Item $ModuleLogging
New-ItemProperty $ModuleLogging -Name 'EnableModuleLogging' -PropertyType Dword
Set-ItemProperty $ModuleLogging -Name 'EnableModuleLogging' -Value '1'
```

DNS (Event ID 3006).
```pwsh
wevtutil sl Microsoft-Windows-DNS-Client/Operational /e:true
```
