#!/bin/bash

if [ `id -u` != 0 ]
then
	echo "This script must be run as root"
	exit 1
fi

PACKAGES="vim git python-netifaces python-requests python-smbus python-setuptools libzmq-dev"

echo "Installing the following packages:"
echo $PACKAGES
echo 
echo

export DEBIAN_FRONTEND=noninteractive
apt-get -y update
apt-get -y install $PACKAGES

echo "Installing extra python packages"
easy_install pip
pip install pyzmq
