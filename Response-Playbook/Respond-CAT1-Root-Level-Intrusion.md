### CAT 1 (Root-Level Intrusion)

---

**Play ID.** Respond-CAT1-Root-Level-Intrusion.

**Task.** Respond to a CAT 1 (Root-Level Intrusion) cyber incident.

**When to Run This Play.** Run this play if one or more of the following is detected: (1) unauthorized privileged access to a computer, (2) unauthorized access to credentials that could be used to perform administrative functions (e.g., domain administrator), or (3) if a computer is compromised with malware that provides remote access. 

**Purpose.** The purpose of this play is to preserve evidence and minimize operational impact while guiding the Incident Response Team through containment, eradication, and recovery efforts during a root-level intrusion. 

**Conditions.** An audit policy has been configured and WinRM is enabled across the network. You are given a list of computer names, domain administrator permissions, access to PowerShell, and knowledge of the accepted configuration baseline (ex: STIGs, SHB, etc.). 

**Standards.** The Incident Response Team was able to contain, eradicate, and recover from a CAT 1 cyber incident.

---

### Containment

**Step 1.** Unplug the computer from the network.

**Step 2.** Block network connections to the compromised computer(s) and threat actor using host-level firewalls. 

**Step 2a.** Declare your variables. 
```pwsh
$ComputersCompromised = ""
$IpAddressToBlock = ""
```

**Step 2b.** Run the code below. 
```pwsh
Invoke-Command -ComputerName $Computers -ArgumentList $IpAddressToBlock -ScriptBlock {
    New-NetFirewall -DisplayName "Block $args[0]" -Direction Outbound -Action Block -RemoteAddress $args[0]
}
```

**Step 3.** Collect forensic evidence (based on volatility) required to conduct a root-cause analysis. 
```pwsh
# Detecting unusual network activity
netstat -na 5 # prints all TCP/UDP ports every 5 seconds
netstat -nao # prints all TCP/UDP ports & related owning/parent PID
netstat -naob # (run as admin) prints all ports, owning PID, related .exe
# cross-reference output with 'tasklist' or 'wmic' to double-check

# Detecting unusual processes 
taskmgr.exe # [GUI] look at the 'Details' tab to view each PID
tasklist /v # prints user related to process & other info (tab separated)
wmic process list full # prints cmd that invoked ea proc (CRLF separated)
wmic startup list full # shows startup apps (cmds used & related user)

# Detecting unusual services
services.msc # [GUI]
sc query | more # page through services
tasklist /svc # show tasks & the services that started them

# Detecting unusual scheduled tasks
schtasks | more # prints scheduled tasks
schtasks /delete /tn <task_name> # deletes a task specified by name

# Detecting unusual accounts
lusrmgr.msc # opens Local Users and Groups GUI app; check for bogus accts
net localgroup administrators # shows local Administrators group members

# Detecting unusual files
# [WINDOWS FILE EXPLORER, GUI] finds files greater than 10MBs
size:>10M

# [CLI one-liner] finds files greater than 10MBs
FOR /R C:\ %i in (*) do @if %~zi gtr 10000000 echo %i %~zi

# [CLI one-liner w/explanations] find files greater than 10MBs 
FOR /R C:\ ^ # for every file under the C: drive
%i in (*) do @if %~zi gtr 10000000 ^ # if size is > 10000000 bytes (10MB)
echo %i %~zi # print the filename & size

# Detecting unusual Registry key settings (ASEPs; AutoStart Entry Points)
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

--- 

### Eradication

**Step 1.** Conduct a root-cause analysis.

**Step 1a.** Identify the vulnerability/misconfiguration and exploit used by the threat actor. 

**Step 1b.** Identify additional indicators of compromise that will enhance future incident handling activities. 

**Step 2.** Develop and implement a mitigation strategy for other computers yet to be compromised. 

**Step 2a.** Modify applicable access controls.

**Step 2b.** Fix the vulnerability/misconfiguration across the network.

**Step 2c.** Fix the vulnerability/misconfiguration on the baseline computer image. 

---

### Recovery

**Step 1.** Shutdown the computer(s) compromised.

**Step 2.** Reimage the computer(s) compromised.

**Step 3.** Reload and verify user data meets mission requirements.

**Step 4.** Reconnect the restored computer(s).

---
