# Appendix D
## STRIDE Matrix 

### D-1. STRIDE
STRIDE is an acronym and helps categorize threats based on the security principle they violate. To explain, an analyst will first assess every component of their DFD using STRIDE and then add the results to a matrix. The columns of this matrix are threat categories while every DFD component is assigned a unique, individual row. If a single component is vulnerable to more than one threat, then it may have marks in multiple columns. The benefit of such a matrix is the ability to quickly prioritize risk. An example of each STRIDE threat category is listed below.
* Spoofing Identity. Illegally accessing and then using another user's authentication information, such as username and password.
* Tampering with Data. Unauthorized changes made to persistent data, such as that held in a database, and the alteration of data as it flows between two computers over an open network, such as the Internet.
* Repudiation. Users who deny performing an action without other parties having any way to prove otherwise. 
* Information Disclosure. The ability of users to read a file that they were not granted access to, or the ability of an intruder to read data in transit between two computers.
* Denial of Service. Making a web server temporarily unavailable or unusable.
* Elevation of Privilege. Situations in which an attacker has effectively penetrated all system defenses and become part of the trusted system itself.

### D-2. STRIDE Matrix Example
| Component | S   | T   | R   | I   | D   | E   |
| --------- | --- | --- | --- | --- | --- | --- |
| Directory Server | | | | | x | x |
| File Server | | x | | | | | 
