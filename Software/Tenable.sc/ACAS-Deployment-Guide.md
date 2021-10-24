### Assured Compliance Assessment Solution (ACAS) Deployment Guide
### Table of Contents
* [Deploying Tenable.sc and Nessus](#deploying-tenablesc-and-nessus)
    * [Adding Your First Nessus Scanner](#adding-your-first-nessus-scanner)
    * [Configuring Your First Repository](#configuring-your-first-repository)
    * [Configuring Your First Organization](#configuring-your-first-organization)
    * [Configuring Your First Security Manager](#configuring-your-first-security-manager)
    * [Creating an Application Administrator](#creating-an-application-administrator)
    * [Creating an Security Analyst](#creating-a-security-analyst)
* [Configuring a CentOS 6.9 Virtual Machine](#granting-someone-super-user-privileges-in-centos)
    * [Granting Someone "Super-User" Privileges in CentOS](#granting-someone-super-user-privileges-in-centos)
    * [Installing VirtualBox Guest Additions in CentOS](#installing-virtualbox-guest-additions-in-centos)
    * [Changing the Hostname in CentOS](#changing-the-hostname-in-centos)
    * [Configuring a Static IP Address in CentOS](#assigning-a-static-ip-address-in-centos)
* [References](#references)

### Deploying Tenable.sc and Nessus
1. Identify a hostname for your Tenable.sc server
2. Request a Tenable.sc license (option 1: [DISA ACAS License Request Portal](https://disa.deps.mil/ext/cop/mae/netops/acas/Requests/index.aspx#/))
3. Install [CentOS](http://archive.kernel.org/centos-vault/6.9/isos/x86_64/CentOS-6.9-x86_64-LiveDVD.iso) ([change the hostname](#how-to-change-the-hostname-in-centos), [configure a static IP address](#how-to-assign-a-static-ip-address-in-centos), and specify a DNS server)
4. Download, install, and start the [Tenable.sc & Nessus Scanner](https://patches.csd.disa.mil/CollectionInfo.aspx) binaries 
    ```
    sudo mkdir /opt/downloads/
    sudo cp ./*.rpm ./*.key /opt/downloads/
    cd /opt/downloads
    sudo rpm -i ./CM-243951-SecurityCenter-5.11.0-el6.x86_64.rpm
    sudo rpm -i ./CM-253106-Nessus-8.11.0-es6.x86_64.rpm
    sudo service SecurityCenter status
    sudo service SecurityCenter start
    sudo service nessusd status
    sudo service nessusd start 
    ```
5. Browse to `https://localhost:8834` to configure the Nessus Scanner
    - Select "Managed Scanner" when prompted
    - Select "Tenable.sc" when prompted
    - Create an account when prompted
7. Browse to the Tenable.sc web interface using `https://localhost`
    - Click-on "Update License > Choose File" and select your Tenable.sc license when prompted (the key filename must match the server's hostname; ex: `hostname.key`)
    - Click-on "Activate"
    - Click-on "Next"     
8. Configure Tenable.sc
    * [Adding Your First Nessus Scanner](#adding-your-first-nessus-scanner)
    * [Configuring Your First Repository](#configuring-your-first-repository)
    * [Configuring Your First Organization](#configuring-your-first-organization)
    * [Configuring Your First Security Manager](#configuring-your-first-security-manager)
    * [Creating an Application Administrator](#creating-an-application-administrator)
    
### Adding Your First Nessus Scanner
1. Provide the following details when prompted:
    - Name: `Scanner-California-LosAngeles-T800`
    - Description: `Designated for the "User" VLAN within the city of Los Angeles, California.`
    - Host: `192.168.1.69`
    - Port: `8834`
    - Username: `skynet` (use the credentials you created previously)
    - Password: `ComeWithMeIfYouWantToLive1984` (use the credentials you created previously)
2. Click-on "Next" to start [Configuring Your First Repository](#configuring-your-first-repository)

### Configuring Your First Repository
A Repository contains all the subnets of your organization. Specifically, it is a folder with text-files that identify the individual IP addresses of the machines on your network. It also holds vulnerability data when you begin scanning. Allocate one scanner to each subnet (text-file) within your Repository (a folder containing multiple text-files). 
1. Provide the following details when prompted:
    - Name: `Repository-California`
    - Description: `"User" VLANs for all cities within the state of California.`
    - IP Ranges: `192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24`
2. Click-on "Next" to start [Configuring Your First Organization](#configuring-your-first-organization)

### Configuring Your First Organization
An Organization is a set of scanners (cybersecurity tools), users (cybersecurity personnel), and assets (machines on your network). 
1. Provide the following details when prompted:
    - Name: `Cyberdyne Systems`
    - Description: `We Are the Future`
2. Click-on "Next" and then, "Skip" to start [Configuring Your First Security Manager](#configuring-your-first-security-manager)

### Configuring Your First Security Manager
1. Provide the following details when prompted:
    - Username: `miles.dyson.sm`
    - Password: `ComeWithMeIfYouWantToLive1984`
    - Time Zone: `UTC`
    - Administrator Password: `ComeWithMeIfYouWantToLive1984`
        - **NOTE:** this is for the built-in, default administrator `admin`
2. Click-on "Next" twice
3. Click-on "Confirm"
4. Click-on "Complete Setup" 

### Creating an Application Administrator
1. Click-on "Users > Users"
2. Click-on "+ Add"
3. Provide the following details when prompted and click-on “Submit”
    - Role: `Administrator`
    - Username: `miles.dyson.aa`
    - Password: `ComeWithMeIfYouWantToLive1984`
    - Time Zone: `UTC`
4. Click-on "admin > Logout"
5. Login as the new Application Administrator 
6. Click-on "Users > Users"
7. Click-on the gear next to the `admin` account
8. Click-on "Delete"

### Creating a Security Analyst
1. Click-on "Users > Users"
2. Click-on "+ Add"
3. Provide the following details when prompted and click-on “Submit”
    - Role: `Security Analyst`
    - Username: `miles.dyson.sa`
    - Password: `ComeWithMeIfYouWantToLive1984`
    - Time Zone: `UTC`

### Granting Someone "Super-User" Privileges in CentOS
```bash
# step 1
su root
usermod -aG wheel victor # add the user to the 'wheel' group

# step 2
visudo 
    %wheel ALL=(ALL) ALL # uncommment this line
    # use ':wq!' to exit the Vim text-editor
```

### Installing VirtualBox Guest Additions in CentOS
```bash
# step 1
sudo yum install kernel kernel-devel gcc make perl
sudo reboot now

# step 2 (make sure the current kernel and downloaded one match)
uname -r 
ls /usr/src/kernels/ 

# step 3
# click-on "Insert Guest Additions CD image..." from the Devices drop-menu in VirtualBox

# step 4
cd /media/VBox_GAs_6.0.6 # change directories to where Guest Additions is mounted
sudo ./autorun.sh
sudo reboot now

# step 5
sudo usermod -aG vboxsf victor # do this to access folders shared between the host and guest
sudo reboot now # or logout the GUI shell
```

### Changing the Hostname in CentOS
```bash
# step 1
sudo vim /etc/sysconfig/network
    HOSTNAME=localhost.localdomain # remove
    HOSTNAME=foxhound # add; ex: foxhound = new hostname

# step 2
sudo reboot now
```

### Assigning a Static IP Address in CentOS
```bash
# step 1
cd /etc/sysconfig/network-scripts/
sudo vim ifcfg-eth0
    DEVICE=eth0
    ONBOOT=yes
    BOOTPROTO=none
    PREFIX=24
    IPADDR=192.168.3.69 # desired static ip
    DNS1=192.168.3.10 # local DNS server

# step 2
sudo service network restart

# step 3
ping 192.168.3.1 # ping your gateway
ping 192.168.3.10 # ping your DNS server
ping 8.8.8.8 # ping something beyond your gateway
```

### References
* [Army Naming Convention and Standards (Annex C)]( https://army.deps.mil/netcom/sites/resourcecenter/pages/cinamingconventions.aspx)
* [DISA ACAS License Request Portal](https://disa.deps.mil/ext/cop/mae/netops/acas/Requests/index.aspx#/)
* [Download CentOS 6.9](http://archive.kernel.org/centos-vault/6.9/isos/x86_64/CentOS-6.9-x86_64-LiveDVD.iso)
* [Download Tenable.sc & Nessus Scanner](https://patches.csd.disa.mil/CollectionInfo.aspx)