<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/so/winlogbeat/README.md#contents">Top of Page</a> |
  <a href="/so/winlogbeat/README.md#bottom-of-page">Bottom of Page</a>
</p>

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

<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/so/winlogbeat/README.md#contents">Top of Page</a> |
  <a href="/so/winlogbeat/README.md#bottom-of-page">Bottom of Page</a>
</p>

## Bottom of Page
