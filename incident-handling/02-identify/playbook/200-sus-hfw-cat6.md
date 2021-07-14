# 200-SUS-HFW-CAT6
Detect a Network Scan

# Objective
The first phase an attack cycle is reconnaissance. During this phase, attackers use network scans to learn about the scale and characteristics of their target environment. The host/network perimeter logs and Network Intrusion Detection Systems (NIDS) alerts generated by our security infrastructure allow us to detect this activity. This play looks for indicators of someone attempting to gather information about the network and/or the computers, applications, and users it supports in preparation of an attack.

# Detection
1. Login to Kibana
2. Click-on the Elastic icon (colorful; top-left)
3. Click-on the Discover button in the Visualize and Explore Data section (bottom-left)
4. In the Fields column (left), click-on the following field names to add them to the current view: source.ip, source.port, destination.ip, destination.port
5. Click-on the Add Filter button (top-left) and add the following filter to the current view: Field = source.ip, Operator = exists
7. Using the search bar (top), execute the queries below. Ensure to click-on the Refresh button (top-right) between queries. 
```bash
destination.port:0
```

# Analysis
* Network scans are represented within a log by consecutive one-to-many network connections in a short amount of time. Yet, keep in mind, attackers have also been known to use "low and slow" techniques to evade detection. This play looks for IP addresses sending network traffic to multiple computers. 
* The following IP addresses belong to our organization's vulnerability scanners and are known for generating false positives:
  * 10.11.12.13, 10.11.12,14, 10.11.12.15
* Once the current view is configured and the query is executed, identify the total number of logs that match our criteria. We will use this to determine how many unique source IP addresses are responsible for sending traffic to multiple destination IP addresses. 
* Pay attention to the network ID. If it matches our search criteria, but doesn't belong to our $HOME_NET (i.e. it is an external IP address), then the source can be treated as more suspicious than benign. In other words, prioritize findings where the offending address is foreign to the network. 
* Reference the Asset Inventory to confirm the identity of any internal IP address unknown to the analyst. 
* Filter by unique source IP address followed by unique destination address. Ensure to track how many logs a source IP address is responsible for out of the original total count captured above. 
  * For example, if you have 300 logs that match your search criteria, filter-out a source IP address and identify how of those 300 it is responsible for. If it is responsible for a lot of them, filter-out a random destination IP address next. This should allow you to see if the suspected IP address is sending multiple probes to multiple computers or if it is sending multiple probes to a single computer. 

# Containment

# Eradication

# Recovery

# Post-Incident Activity
```





```