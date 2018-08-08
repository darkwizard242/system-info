#! /bin/bash

## This script installs pre-requisites for system-info python modules on Ubuntu's LTS version of OS machines.
## Easy to use script when initializing either of the systems with Vagrant or in isolation.

## Tested on Ubuntu 16.04 xenial & 18.04 bionic


if [ "$(grep -Ei 'ID=ubuntu|VERSION_ID="16.04"' /etc/os-release)" ];
then
	echo "OS is Ubuntu." && echo
	if [ "$(grep -Ei 'VERSION_ID="16.04"' /etc/os-release)" ];
	then
		echo "OS Version is 16.04 i.e. Ubuntu 16.04 xenial. Python 3.5.2 is available by default on the system." && echo
		echo "Beginning of pre-requistes & installation of pip3 and psutil." && echo
		echo "Performing apt-get update" && echo
		sudo apt-get update -y
		sleep 30
		echo
		echo "Printing the existing Python3's version." && echo
		python3 -V
		echo "Installing Python3's PIP and other tools." && echo
		sudo apt-get install -y python3-pip build-essential libssl-dev libffi-dev python-dev
		echo "Installing psutil library using pip" && echo
		sudo pip3 install psutil	# Installing psutil
		sleep 30
		echo
		echo "Installation of pre-reqs has been completed!" && echo
	elif [ "$(grep -Ei 'VERSION_ID="18.04"' /etc/os-release)" ];
	then
		echo "OS Version is 18.04 i.e. Ubuntu 18.04 bionic. Python 3.5.2 is available by default on the system." && echo
		echo "Beginning of pre-requistes & installation of pip3 and psutil." && echo
		echo "Performing apt-get update" && echo
		sudo apt-get update -y
		sleep 30
		echo
		echo "Printing the existing Python3's version." && echo
		python3 -V
		echo "Installing Python3's PIP and other tools." && echo
		sudo apt-get install -y python3-pip build-essential libssl-dev libffi-dev python-dev
		echo "Installing psutil library using pip" && echo
		sudo pip3 install psutil	# Installing psutil
		sleep 30
		echo
		echo "Installation of pre-reqs has been completed!" && echo
	else
		echo "OS is not one of the LTS ubuntu versions."
	fi
else
	echo "This was scripted for LTS version of Ubuntu OS's. Either the OS/Version is not Ubuntu or a LTS version of OS. Please contact Ali Muhammad (https://github.com/Tech-Overlord) to add the required Ubuntu OS version into the script."
fi

# if [ "$(grep -Ei 'ID="centos"|CENTOS_MANTISBT_PROJECT_VERSION="7"' /etc/os-release)" ];
# then
   # echo
   # echo "OS is CentOS & Version is 7 i.e. CentOS-7" && echo
   # echo "Beginning of pre-requistes & docker installation." && echo
   # echo "Performing update." && echo
   # sudo sudo yum update -y
   # sleep 30
   # echo
   # echo "Installing yum-utils" && echo
   # sudo yum install yum-utils -y
   # sleep 5
   # echo
   # echo "Installing IUS" && echo
   # sudo yum install https://centos7.iuscommunity.org/ius-release.rpm -y
   # echo "Installing Python3.6 - Latest stable version at the time of this script's development." && echo
   # sudo yum install python36u -y
   # sleep 30
   # echo
   # echo "Installing Python 3.6's pip" && echo
   # sudo yum install python36u-pip -y
   # sleep 10
   # echo "Installing psutil library using pip" && echo
   # sudo pip3.6 install psutil	# Installing psutil
   # echo "Installation of pre-reqs has been completed!" && echo
# fi
