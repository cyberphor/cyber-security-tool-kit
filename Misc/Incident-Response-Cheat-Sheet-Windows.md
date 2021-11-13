### Incident Response Cheat-Sheet: Windows

Detecting unusual network activity
```bash
netstat -na 5 # prints all TCP/UDP ports every 5 seconds
netstat -nao # prints all TCP/UDP ports & related owning/parent PID
netstat -naob # (run as admin) prints all ports, owning PID, related .exe
# cross-reference output with 'tasklist' or 'wmic' to double-check
```

Detecting unusual processes 
```bash
taskmgr.exe # [GUI] look at the 'Details' tab to view each PID
tasklist /v # prints user related to process & other info (tab separated)
wmic process list full # prints cmd that invoked ea proc (CRLF separated)
wmic startup list full # shows startup apps (cmds used & related user)
```

Detecting unusual services
```bash
services.msc # [GUI]
sc query | more # page through services
tasklist /svc # show tasks & the services that started them
```

Detecting unusual scheduled tasks
```bash
schtasks | more # prints scheduled tasks
schtasks /delete /tn <task_name> # deletes a task specified by name
```

Detecting unusual accounts
```bash
lusrmgr.msc # opens Local Users and Groups GUI app; check for bogus accts
net localgroup administrators # shows local Administrators group members
```

Detecting unusual files
```bash
# [WINDOWS FILE EXPLORER, GUI] finds files greater than 10MBs
size:>10M

# [CLI one-liner] finds files greater than 10MBs
FOR /R C:\ %i in (*) do @if %~zi gtr 10000000 echo %i %~zi

# [CLI one-liner w/explanations] find files greater than 10MBs 
FOR /R C:\ ^ # for every file under the C: drive
%i in (*) do @if %~zi gtr 10000000 ^ # if size is > 10000000 bytes (10MB)
echo %i %~zi # print the filename & size
```

Detecting unusual Registry key settings (ASEPs; AutoStart Entry Points)
```bash
# REGEDIT (GUI): analyze these keys (copy/paste into text-box on top)
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnceEx
# RunOnceEx is only populated when an "autorun task" is created

# REG (CLI)
# use ‘reg’ to query system ASEPs
reg query HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce

# use ‘reg’ to query user ASEPs
reg query HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce

# TASK MANAGER (GUI)
taskmgr.exe # look at the Startup tab
```
