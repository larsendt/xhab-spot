#!/bin/bash

if [ `id -u` != 0 ]
then
	echo "This script must be run as root"
	exit 1
fi

export WLAN=$(ifconfig | egrep -o "wlan[34]")

if [ -z $WLAN ]
then
	echo "No wlan found!!! THIS IS BAD"
	exit 1
fi

echo "Found wlan device at $WLAN"
sed "s/WLAN/$WLAN/g" interfaces_template > interfaces

NETIF=/etc/network/interfaces
NETIF_BAK=/etc/network/interfaces.backup
if [ -f $NETIF ]
then
	echo "Backing up $NETIF to $NETIF_BAK"
	mv $NETIF $NETIF_BAK
fi

echo "Copying interfaces file to $NETIF"
cp interfaces $NETIF
rm interfaces
