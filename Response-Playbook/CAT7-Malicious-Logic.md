### CAT 7 (Malicious Logic)

---

**Play ID.** CAT7-Malicious-Logic.

**Task.** Respond to a CAT 7 (Malicious Logic) cyber incident.

**When to Run This Play.** Run this play if one or more of the following is detected: the installation of software designed and/or deployed by threat actors with malicious intention (i.e., gaining non-interactive access to information or resources without the consent or knowledge of the user).

**Purpose.** The purpose of this play is to preserve evidence and minimize operational impact while guiding the Incident Response Team through containment, eradication, and recovery efforts during the spread of malware. 

**Conditions.** An audit policy has been configured and WinRM is enabled across the network. You are given a list of computer names, domain administrator permissions, access to PowerShell, and knowledge of the accepted configuration baseline (ex: STIGs, SHB, etc.). 

**Standards.** The Incident Response Team was able to contain, eradicate, and recover from a CAT 7 cyber incident.

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
