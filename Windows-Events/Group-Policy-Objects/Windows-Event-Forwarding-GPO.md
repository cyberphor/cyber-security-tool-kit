### Windows Event Forwarding
Computer Configuration > Policies > Administrative Templates > Windows Components > Event Forwarding
* Configure target Subscription Manager
  * SubscriptionManagers: 
```
Server=http://SERVERNAME:5985/wsman/SubscriptionManager/WEC
```

Computer Configuration > Policies > Administrative Templates > Windows Components > Event Log Service > Security
* Configure log access: Enabled
* Log Access:
```
O:BAG:SYD:(A;;0xf0007;;;SY)(A;;0x7;;;BA)(A;;0x1;;;BO)(A;;0x1;;;SO)(A;;0x1;;;S-1-5-32-573)(A;;0x1;;;S-1-5-20)
```
