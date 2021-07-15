<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/00-prerequisites/security-onion/suricata.md#contents">Top of Page</a> |
  <a href="/00-prerequisites/security-onion/suricata.md#bottom-of-page">Bottom of Page</a>
</p>

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

<p align="right">
  <a href="/README.md">Home Page</a> |
  <a href="/00-prerequisites/security-onion/suricata.md#contents">Top of Page</a> |
  <a href="/00-prerequisites/security-onion/suricata.md#bottom-of-page">Bottom of Page</a>
</p>

## Bottom of Page
