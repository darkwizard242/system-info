# INTRODUCTION:
Cross-platform scripts developed in Python3 for fetching and providing runtime CPU, RAM, PIDs, OS and system information.

### Audience:
Quite simply, everyone. From a student to a system engineer, from a software developer to an IT enthusiast. It's developed with the thought to be easily used by anyone :wink: .

# Pre-requisites:
1. **Python3**
    * Python 3 is easily available for free to download, install and use on windows & *nix platforms. If you do not have Python 3 installed on your machine where you require the use or execution of these scripts, please feel free to use the following methods:
        
        * **Windows**: [Python3.7.0](https://www.python.org/downloads/release/python-370/) is the latest major Python release that can easily be downloaded and installed. _Note:_ Python 3.7.0 was the major release at the point of this development. Feel free to use a newer 3.x Python version if you desire.
        
        * **Ubuntu LTS OS's**:  Pre-installed on Ubuntu LTS OS's i.e. 16.04 xenial & 18.04 bionic.

2. **`psutil`** library

    * **Windows**: You can easily install psutil library using command prompt i.e. cmd. Just open cmd, and type in `pip install psutil` .
    
    * **Ubuntu LTS OS's**: Just run the [install_pre-reqs.bash](https://github.com/Tech-Overlord/system-info/blob/master/pre-reqs/install_pre-reqs.bash) script and it will take care of that for you.
    
    * **Note:** [psutil](https://github.com/giampaolo/psutil) library was developed by [Giampaolo Rodola](https://github.com/giampaolo). It is a cross platform library for system level information. Kudos to Giampaolo !!!

# Tested on:
1. Windows Operating Systems (i.e. 7, 8, 8.x & 10). Works on Windows Server editions too.

2. Ubuntu 16.04 & Ubuntu 18.04



# Usage:

Utilizing the library is pretty simple. All you need to do is execute the `main_system.py` file. Assuming that you have already downloaded either the zip/tar or cloned the project already. Following two sections will cover the execution process.

   * #### Windows:
       1. Either [Download](https://github.com/Tech-Overlord/system-info/releases/download/v1.0.0/system-info-1.0.0.zip) or clone using `git clone https://github.com/Tech-Overlord/system-info`
       2. Open a `cmd` window.
       2. Perform `cd` into the directory where the extracted archive or project is cloned in. For instance, if you have extracted or cloned into D:\ drive. Do `cd D:\system-info`
       3. Now, change directory into the `sysinfo` package i.e. `cd sysinfo`
       4. Current directory should be: **D:\system-info\sysinfo**
       5. Execute `main_system.py` with the following commands: `python main_system.py`
       6. All done. That will print a detailed output as can be seen below:
            ```batch
            D:\system-info\sysinfo>python main_system.py
            
            System & OS level details below:
            
            OS Type: Windows
            OS Release version: 10
            Processor Name: Intel64 Family 6 Model 78 Stepping 3, GenuineIntel
            Machine Name on Network is: DESKTOP-MS0CV80
            Machine Type is: AMD64
            System platform type is: win32
            
            RAM details below:
            
            Total memory is: 8481.492992 MBs
            Current available memory is: 1897.357312 MBs
            Current used memory is: 6584.13568 MBs
            Percentage of RAM being utilized currently: 77.6%
            
            Current process details below:
            {'pid': 0, 'name': 'System Idle Process', 'username': 'NT AUTHORITY\\SYSTEM'}
            {'pid': 4, 'name': 'System', 'username': 'NT AUTHORITY\\SYSTEM'}
            {'pid': 96, 'name': 'Registry', 'username': None}
            {'pid': 3268, 'name': 'SkypeHost.exe', 'username': 'DESKTOP-MS0CV80\\User'}
            {'pid': 3600, 'name': 'vmware-authd.exe', 'username': None}
            {'pid': 3672, 'name': 'svchost.exe', 'username': None}
            {'pid': 3688, 'name': 'RuntimeBroker.exe', 'username': 'DESKTOP-MS0CV80\\User'}
            {'pid': 3804, 'name': 'chrome.exe', 'username': 'DESKTOP-MS0CV80\\User'}
            {'pid': 3872, 'name': 'valWBFPolicyService.exe', 'username': None}
            {'pid': 3888, 'name': 'vmware-usbarbitrator64.exe', 'username': None}
            {'pid': 4208, 'name': 'MsMpEng.exe', 'username': None}
            {'pid': 8884, 'name': 'vmware-tray.exe', 'username': 'DESKTOP-MS0CV80\\User'}
            
            D:\system-info\sysinfo>
            ```


   * #### Ubuntu:
       1. Change to user's home directory, for e.g. by entering the following command: `cd ~`
       2. Either Download using `wget https://github.com/Tech-Overlord/system-info/releases/download/v1.0.0/system-info-1.0.0.zip` or clone using `git clone https://github.com/Tech-Overlord/system-info`
            * If cloned, simply change into the root directory of the cloned project and then into the sysinfo folder, for e.g. `cd ~/system-info/sysinfo/`
                * Do `chmod +x *`
            * If tar was downloaded using `wget`. Extract it using the commands: `tar -zxf v1.0.0.tar.gz` and then cd into extracted directory right down to *sysinfo* package, for e.g. if the extracted directory is system-info-1.0.0, then do `cd system-info-1.0.0/sysinfo`
                * Do `chmod +x *`. This will ensure that the scripts have **execute** permissions.
       5. Execute **main_system.py** file with the command: `python3 main_system.py`
       6. This will print a detailed output as shown below:
            ```shell
            vagrant@ubuntu:/vagrant/sysinfo$ python3 main_system.py
            
            System & OS level details below:
            
            OS Type: Linux
            OS Release version: 4.4.0-131-generic
            Processor Name: x86_64
            Machine Name on Network is: ubuntu
            Machine Type is: x86_64
            System platform type is: linux
            
            RAM details below:
            
            Total memory is: 1040.22016 MBs
            Current available memory is: 667.090944 MBs
            Current used memory is: 117.047296 MBs
            Percentage of RAM being utilized currently: 25.2%
            
            Current process details below:
            
            {'pid': 1, 'name': 'systemd', 'username': 'root'}
            {'pid': 2, 'name': 'kthreadd', 'username': 'root'}
            {'pid': 3, 'name': 'ksoftirqd/0', 'username': 'root'}
            {'pid': 4, 'name': 'kworker/0:0', 'username': 'root'}
            {'pid': 5, 'name': 'kworker/0:0H', 'username': 'root'}
            {'pid': 6, 'name': 'kworker/u4:0', 'username': 'root'}
            {'pid': 7, 'name': 'rcu_sched', 'username': 'root'}
            {'pid': 8, 'name': 'rcu_bh', 'username': 'root'}
            {'pid': 9, 'name': 'migration/0', 'username': 'root'}
            {'pid': 10, 'name': 'watchdog/0', 'username': 'root'}
            {'pid': 11, 'name': 'watchdog/1', 'username': 'root'}
            {'pid': 12, 'name': 'migration/1', 'username': 'root'}
            {'pid': 13, 'name': 'ksoftirqd/1', 'username': 'root'}
            {'pid': 14, 'name': 'kworker/1:0', 'username': 'root'}
            {'pid': 15, 'name': 'kworker/1:0H', 'username': 'root'}
            {'pid': 16, 'name': 'kdevtmpfs', 'username': 'root'}
            {'pid': 17, 'name': 'netns', 'username': 'root'}
            {'pid': 18, 'name': 'perf', 'username': 'root'}
            {'pid': 19, 'name': 'khungtaskd', 'username': 'root'}
            {'pid': 20, 'name': 'writeback', 'username': 'root'}
            {'pid': 21, 'name': 'ksmd', 'username': 'root'}
            {'pid': 22, 'name': 'khugepaged', 'username': 'root'}
            {'pid': 23, 'name': 'crypto', 'username': 'root'}
            {'pid': 24, 'name': 'kintegrityd', 'username': 'root'}
            {'pid': 25, 'name': 'bioset', 'username': 'root'}
            {'pid': 26, 'name': 'kblockd', 'username': 'root'}
            {'pid': 27, 'name': 'ata_sff', 'username': 'root'}
            {'pid': 28, 'name': 'md', 'username': 'root'}
            {'pid': 29, 'name': 'devfreq_wq', 'username': 'root'}
            {'pid': 30, 'name': 'kworker/u4:1', 'username': 'root'}
            {'pid': 31, 'name': 'kworker/0:1', 'username': 'root'}
            {'pid': 32, 'name': 'kworker/1:1', 'username': 'root'}
            {'pid': 34, 'name': 'kswapd0', 'username': 'root'}
            {'pid': 35, 'name': 'vmstat', 'username': 'root'}
            {'pid': 36, 'name': 'fsnotify_mark', 'username': 'root'}
            {'pid': 37, 'name': 'ecryptfs-kthrea', 'username': 'root'}
            {'pid': 53, 'name': 'kthrotld', 'username': 'root'}
            {'pid': 54, 'name': 'acpi_thermal_pm', 'username': 'root'}
            {'pid': 55, 'name': 'kworker/u4:2', 'username': 'root'}
            {'pid': 56, 'name': 'bioset', 'username': 'root'}
            {'pid': 57, 'name': 'bioset', 'username': 'root'}
            {'pid': 58, 'name': 'bioset', 'username': 'root'}
            {'pid': 59, 'name': 'bioset', 'username': 'root'}
            {'pid': 60, 'name': 'bioset', 'username': 'root'}
            {'pid': 61, 'name': 'bioset', 'username': 'root'}
            {'pid': 62, 'name': 'bioset', 'username': 'root'}
            {'pid': 63, 'name': 'bioset', 'username': 'root'}
            {'pid': 64, 'name': 'scsi_eh_0', 'username': 'root'}
            {'pid': 65, 'name': 'scsi_tmf_0', 'username': 'root'}
            {'pid': 66, 'name': 'scsi_eh_1', 'username': 'root'}
            {'pid': 67, 'name': 'scsi_tmf_1', 'username': 'root'}
            {'pid': 68, 'name': 'kworker/u4:3', 'username': 'root'}
            {'pid': 72, 'name': 'ipv6_addrconf', 'username': 'root'}
            {'pid': 85, 'name': 'deferwq', 'username': 'root'}
            {'pid': 86, 'name': 'charger_manager', 'username': 'root'}
            {'pid': 125, 'name': 'kpsmoused', 'username': 'root'}
            {'pid': 126, 'name': 'kworker/1:2', 'username': 'root'}
            {'pid': 152, 'name': 'mpt_poll_0', 'username': 'root'}
            {'pid': 153, 'name': 'mpt/0', 'username': 'root'}
            {'pid': 154, 'name': 'scsi_eh_2', 'username': 'root'}
            {'pid': 155, 'name': 'scsi_tmf_2', 'username': 'root'}
            {'pid': 156, 'name': 'bioset', 'username': 'root'}
            {'pid': 157, 'name': 'bioset', 'username': 'root'}
            {'pid': 186, 'name': 'kworker/u4:4', 'username': 'root'}
            {'pid': 259, 'name': 'raid5wq', 'username': 'root'}
            {'pid': 285, 'name': 'bioset', 'username': 'root'}
            {'pid': 315, 'name': 'jbd2/sda1-8', 'username': 'root'}
            {'pid': 316, 'name': 'ext4-rsv-conver', 'username': 'root'}
            {'pid': 372, 'name': 'kworker/1:1H', 'username': 'root'}
            {'pid': 374, 'name': 'kworker/0:2', 'username': 'root'}
            {'pid': 377, 'name': 'kworker/0:1H', 'username': 'root'}
            {'pid': 381, 'name': 'kworker/0:3', 'username': 'root'}
            {'pid': 383, 'name': 'kworker/0:4', 'username': 'root'}
            {'pid': 395, 'name': 'iscsi_eh', 'username': 'root'}
            {'pid': 401, 'name': 'systemd-journald', 'username': 'root'}
            {'pid': 404, 'name': 'ib_addr', 'username': 'root'}
            {'pid': 407, 'name': 'ib_mcast', 'username': 'root'}
            {'pid': 408, 'name': 'ib_nl_sa_wq', 'username': 'root'}
            {'pid': 409, 'name': 'ib_cm', 'username': 'root'}
            {'pid': 412, 'name': 'iw_cm_wq', 'username': 'root'}
            {'pid': 413, 'name': 'rdma_cm', 'username': 'root'}
            {'pid': 416, 'name': 'kauditd', 'username': 'root'}
            {'pid': 429, 'name': 'lvmetad', 'username': 'root'}
            {'pid': 463, 'name': 'systemd-udevd', 'username': 'root'}
            {'pid': 490, 'name': 'kworker/1:3', 'username': 'root'}
            {'pid': 550, 'name': 'iprt-VBoxWQueue', 'username': 'root'}
            {'pid': 982, 'name': 'dhclient', 'username': 'root'}
            {'pid': 1123, 'name': 'iscsid', 'username': 'root'}
            {'pid': 1124, 'name': 'iscsid', 'username': 'root'}
            {'pid': 1128, 'name': 'dbus-daemon', 'username': 'messagebus'}
            {'pid': 1130, 'name': 'atd', 'username': 'root'}
            {'pid': 1132, 'name': 'cron', 'username': 'root'}
            {'pid': 1134, 'name': 'systemd-logind', 'username': 'root'}
            {'pid': 1138, 'name': 'acpid', 'username': 'root'}
            {'pid': 1145, 'name': 'lxcfs', 'username': 'root'}
            {'pid': 1147, 'name': 'rsyslogd', 'username': 'syslog'}
            {'pid': 1158, 'name': 'dockerd', 'username': 'root'}
            {'pid': 1160, 'name': 'accounts-daemon', 'username': 'root'}
            {'pid': 1167, 'name': 'snapd', 'username': 'root'}
            {'pid': 1170, 'name': 'sshd', 'username': 'root'}
            {'pid': 1242, 'name': 'mdadm', 'username': 'root'}
            {'pid': 1252, 'name': 'agetty', 'username': 'root'}
            {'pid': 1253, 'name': 'agetty', 'username': 'root'}
            {'pid': 1262, 'name': 'irqbalance', 'username': 'root'}
            {'pid': 1278, 'name': 'VBoxService', 'username': 'root'}
            {'pid': 1287, 'name': 'polkitd', 'username': 'root'}
            {'pid': 1300, 'name': 'systemd', 'username': 'vagrant'}
            {'pid': 1304, 'name': '(sd-pam)', 'username': 'vagrant'}
            {'pid': 1544, 'name': 'dhclient', 'username': 'root'}
            {'pid': 1584, 'name': 'docker-containerd', 'username': 'root'}
            {'pid': 1982, 'name': 'sshd', 'username': 'root'}
            {'pid': 2013, 'name': 'sshd', 'username': 'vagrant'}
            {'pid': 2014, 'name': 'bash', 'username': 'vagrant'}
            {'pid': 2046, 'name': 'python3', 'username': 'vagrant'}
            ```



# Releases
[v1.0.0](https://github.com/Tech-Overlord/system-info/releases/tag/v1.0.0)

# License
Read [License](https://github.com/Tech-Overlord/system-info/blob/master/LICENSE).


<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>
</head>
<body>

<h2 style="text-align:center">About Me!</h2>

<div class="card">
  <img src="‪https://thumb.mangahub.io/mn/surviving-demon.jpg" alt="Ali" style="width:100%">
  <h1>Ali Muhammad</h1>
  <p class="title">DevOps Engineer, 1insurer</p>
  <p>University of Bedfordshire</p>
  <div style="margin: 24px 0;">
    <a href="https://www.linkedin.com/in/ali-muhammad-759791130/"><i class="fa fa-linkedin-square"></i></a>  
    <a href="mailto:am900820@gmail.com"><i class="fa fa-google"></i></a>  
    <a href="https://github.com/Tech-Overlord"><i class="fa fa-github-square"></i></a> 
 </div>
</div>

</body>
</html>

NOTE: Currently in development phase!