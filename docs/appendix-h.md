**Appendix H**  
**Incident Handling Tools**

**H-1. Requirements**
| Requirement | Solution | Prerequisities |
| ----------- | -------- | -------------- |
| Directory Server | Microsoft Active Directory | The ability to remotely query the primary Domain Controller.  |
| Configuration Management Server | Group Policy Management Console (GPMC) | An audit policy Group Policy Object (GPO), a Windows Remote Management (WinRM) GPO, and Windows Event Forwarding (WEF) GPO. |
| Log Server | Microsoft Windows Event Collector (WEC) service | The Microsoft Windows Server Operating System (OS), the WEC service is running, event subscriptions are configured, Winlogbeat is installed, configured, and running, and external Hard Disk Drives (HDDs) are available for archiving old logs. | 
| SIEM Server | The Elastic Stack via Security Onion | Security Onion and analyst accounts for every Cyber Defense person. |
| IMS Server | TheHive via Security Onion | Security Onion, analyst accounts for every Cyber Defense person, and incident case templates. |
| SAW | A domain-joined computer running the Microsoft Windows OS | PowerShell, the Firefox web browser, Microsoft Windows Remote Server Administration Tool (RSAT), the Sysinternals Suite, the PuTTY Secure Shell (SSH) client program, and Wireshark. |
| TIP | CrowdStrike | CrowdStrike accounts for every Cyber Defense person and web-browser access to CrowdStrike. |
| Deployable Incident Response Toolkit | Jump bag | Blank HDDs, hardware write-blocker, SANS Investigative Forensic Toolkit (SIFT), network tap, network cables, computer repair tools, and incident response forms. |

**H-2. Windows Event**
| Group Policy Option | Event IDs Generated | 
| ------------------- | ------------------- |
| User Account Management | 4720, 4722, 4723, 4724 |
| Security Group Management | 4728, 4732, 4756 |
| Process Creation | 4688 |
| Logon | 4624, 4625 |
| Special Logon | 4672 |
| File Share | 5140, 5145 |
| File System | 4663 |
| Filtering Platform Connection | 5152, 5156, 5157 |
| Registry | 4663 |
| Removable Storage | 6416 |
| Other Object Access | 4698 |
| Policy Change | 4719 |
| Security System Extension | 4697, 7040, 7045 |
| PowerShell Module Logging | 4103 |
| PowerShell Script Block | 4104 |

**H-3. Group Policy Objects**  
Create each of the GPOs below using Microsoft Management Console (MMC) and the GPMC snap-in. If said snap-in is unavailable, ensure RSAT is installed. Keep in mind, you should be executing these procedures from the SAW. For ease-of-use, consider the following naming convention for the GPOs:
* Cyber - Audit Policy
* Cyber - WinRM
* Cyber - WEF

**Audit Policy GPO**  
Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies
* Account Management
  * Audit User Account Management: Success
  * Audit Security Group Management: Success
* Detailed Tracking
  * Audit Process Creation: Success 
* Logon/Logoff
  * Audit Logon: Success, Failure 
  * Audit Special Logon: Success 
* Object Access
  * Audit File Share: Success 
  * Audit File System: Success 
  * Audit Filtering Platform Connection: Success 
  * Audit Registry: Success
  * Audit Removable Storage: Success 
  * Audit Other Object Access: Success 
* Policy Change
  * Audit Policy Change: Success 
* System
  * Audit Security System Extension: Success, Failure 

Computer Configuration > Policies > Administrative Templates > Windows Components > Windows PowerShell
* Turn on Module Logging: Enabled 
* Turn on Script Block Logging: Enabled 

**ElastAlert**  
**Contents**
* [Whitelist - IP Addresses](#whitelist-ip-addresses)
* [Whitelist - Ports](#whitelist-ports)
* [Whitelist - DNS Queries](#whitelist-dns-queries)
* [Frequency - Logon Failures](#frequency-logon-failures)

**Whitelist IP Addresses**  
Create a whitelist file under /etc/elastalert/rules/ called _authorized_ips.txt
```
192.168.56.1
192.168.56.2
192.168.56.3
```

Create a rule configuration file (called ‘winlogbeat.yml’).
```yaml
es_host: elasticsearch
es_host: 9200
name: Unknown IP address detected!
index: "*:logstash-*"
type: whitelist
compare_key: source_ip
ignore_null: true
whitelist:
    - "!file /etc/elastalert/rules/_authorized_ips.txt"
alert:
    - debug
```

## Whitelist - Ports
Create a whitelist file under /etc/elastalert/rules/ called _authorized_ports.txt
```
22
53
80
```

Create a rule configuration file (called ‘winlogbeat.yml’).
```yaml
es_host: elasticsearch
es_host: 9200
name: Abnormal outbound network connection detected!
index: "*:logstash-*"
type: whitelist
compare_key: destination_port
ignore_null: true
whitelist:
    - "!file /etc/elastalert/rules/_authorized_ports.txt"
alert:
    - debug
```

## Whitelist - DNS Queries
Create a whitelist file under /etc/elastalert/rules/ called _normal_domains.txt
```
github.com
google.com
cyberphor.com
```

Create a rule configuration file (called ‘winlogbeat.yml’).
```yaml
es_host: elasticsearch
es_host: 9200
name: Abnormal DNS query detected!
index: "*:logstash-*"
type: whitelist
compare_key: query
ignore_null: true
whitelist:
    - "!file /etc/elastalert/rules/_normal_domains.txt"
filter:
    - wildcard:
        event_type: "bro_dns"
alert:
    - debug
```

## Frequency - Logon Failures
Create a rule configuration file (called ‘winlogbeat.yml’).
```yaml
es_host: elasticsearch
es_host: 9200
name: Possible brute-force attempt detected!
type: frequency
index: "*:logstash-*"
num_events: 3
timeframe:
  minutes: 1
filter:
- term:
    some_field: "some_value"
alert:
- "debug"
```

# Suricata

## Contents
* [Suppress Alerts](#suppress-alerts)

## Suppress Alerts
```bash
sudo vi /opt/so/saltstack/local/pillar/global.sls
```
```yaml
thresholding:
  sids:
    0123456789:
      - suppress:
        gen_id: 1
        track: by_src
        ip: 10.11.12.13
```
```bash
sudo salt \* state.highstate
```
```bash
cat /opt/so/conf/suricata/threshold.conf
```

# Winlogbeat
## Contents
* [Installing Winlogbeat on a WEC Server](#installing-winlogbeat-on-a-wec-server)
* [Filtering Events](#filtering-events)

## Installing Winlogbeat on a WEC Server
Download Winlogbeat onto your Windows Event Collector (WEC) server.  
https://artifacts.elastic.co/downloads/beats/winlogbeat/winlogbeat-7.9.3-windows-x86_64.zip 

Modify the default configuration file so it reflects what is below (called ‘winlogbeat.yml’).
```yaml
winlogbeat.event_logs:
  - name: ForwardedEvents
tags: ['winlogbeat']
output.logstash:
  hosts: ['10.10.10.21:5044']
```

Run the installation script.
```pwsh
./install-winlogbeat.ps1
```

Start the Winlogbeat service.
```pwsh
Start-Service winlogbeat
```

## Filtering Events
See below.

## References
* https://www.elastic.co/guide/en/beats/winlogbeat/current/drop-event.html 
