## Blue Team Cheat Sheet

**Windows**  
Log Network Connections
```
auditpol.exe /set /subcategory:"Filtering Platform Connection" /success:enable
```

**Linux**  
Backup a Directory and Serve it
```
sudo tar -zcvf /tmp/minecraft.tar.gz /minecraft/
cd /tmp
sudo python3 -m http.server 4444
```
