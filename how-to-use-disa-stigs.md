### How to Use DISA STIGs
**Step 1.** Download and unzip the Defense Information Systems Agency (DISA) Security Technical Implementation Guide (STIG) Library.  
https://public.cyber.mil/stigs/compilations/

**Step 2.** Download and unzip the SCAP Compliance Checker (SCC) from DISA.   
https://public.cyber.mil/stigs/scap/

**Step 3.** Download and unzip STIG Viewer from DISA.   
https://cyber.mil/stigs/srg-stig-tools/

**Step 4.** Open SCC. In the "Content" pane, select the benchmarks you want to use (ex: Windows_10_STIG). In the "Scan" pane, select "Local Scan" and then, start the scan. 

**Step 6.** After the scan finishes, close SCC and verify the location of your latest scan results. They should be saved in a directory such as the one below. The filename you're interested in includes the word "XCCDF."
```bash
C:\Users\Victor\SCC\Sessions\2021-09-18_224007\Results\SCAP\XML
```

**Step 7.** Open STIG Viewer, click-on "File > Import STIG...", and select the desired .zip file (ex: MS_Windows_10_V2R2_STIG). 

**Step 8.** In STIG Viewer, ensure the benchmark you loaded is now checked. Then, click-on "Checklist > Create Checklist - Check Marked STIG(s)." You should now have two tabs open in STIG Viewer: "STIG Explorer" and "New Checklist."

**Step 9.** In STIG Viewer, click-on the "New Checklist" tab. Then, click-on "Import > XCCDF Results File..." and browse for the .xml file you confirmed existed in Step 6 (again, it should have the word "XCCDF" in its filename). Below is an example of how it may look.
```bash
WINDOWS_SCC-5.4.2_2021-09-18_224007_XCCDF-Results_Windows_10_STIG-002.002
```

**Step 10.** In STIG Viewer, click-on "File > Save Checklist As...", and save the checklist using an appropiate name (ex: win10-stig-before.ckl). Then, begin applying the fixes (from the "Fix Text" section) for each "Rule." Go from CAT I to CAT II and then, CAT III. Focus on rules based on their "Status:" Open (O), Not Reviewed (NR), Not a Finding (NF), and Not Applicable (NA). Once you've made significant progress (ex: address all CAT I findings), run another scan. 
