**Appendix H**  
**Incident Handling Technology**

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
