
## J-3. Daily Security Monitoring Checklist
| No. | Data Source | Check |
| --- | ----------- | ----- |
| 01 | PowerShell | **Asset Inventory:** Use PowerShell to sweep our network and identify computers currently online. The number of replies should match our baseline.   |
| 02 | PowerShell | **Domain Administrators:**  Use PowerShell (or Active Directory) to query our Domain Controller and identify the number of accounts in the Domain Admins group. The number should match our baseline. |
| 03 | PowerShell | **Local Administrators:** Query all computers currently online for members of the local Administrators group. The number of local Administrators from each query should match our baseline. |
