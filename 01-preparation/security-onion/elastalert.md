<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/00-prerequisites/security-onion/elastalert.md#contents">Top of Page</a> |
  <a href="/00-prerequisites/security-onion/elastalert.md#bottom-of-page">Bottom of Page</a>
</p>

# ElastAlert
## Contents
* [Whitelist - IP Addresses](#whitelist-ip-addresses)
* [Whitelist - Ports](#whitelist-ports)
* [Whitelist - DNS Queries](#whitelist-dns-queries)
* [Frequency - Logon Failures](#frequency-logon-failures)

## Whitelist IP Addresses
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

<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/00-prerequisites/security-onion/elastalert.md#contents">Top of Page</a> |
  <a href="/00-prerequisites/security-onion/elastalert.md#bottom-of-page">Bottom of Page</a>
</p>

## Bottom of Page
