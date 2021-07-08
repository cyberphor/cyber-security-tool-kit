<p align="right">
  <a href="/so/README.md">Home Page</a> |
  <a href="/so/README.md#contents">Top of Page</a> |
  <a href="/so/README.md#bottom-of-page">Bottom of Page</a>
</p>

# Security Onion 

## Contents
* [Suppress Suricata Alerts](#suppress-suricate-alerts)

## Suppress Suricata Alerts
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

## Bottom of Page
