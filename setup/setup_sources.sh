#!/bin/bash

if [ `id -u` != 0 ]
then
	echo "This script must be run as root"
	exit 1
fi

SLST=/etc/apt/sources.list
SLST_BAK=/etc/apt/sources.list.backup
ROSLST=/etc/apt/sources.list.d/ros-latest.list

if [ -f $SLST ]
then
	echo "Backing up $SLST to $SLST_BAK"
	mv $SLST $SLST_BAK
fi

echo "Copying sources.list to $SLST"
cp sources.list $SLST

echo "Copying ros-latest.list to $ROSLST"
cp ros-latest.list $ROSLST

echo "Fetching ROS keys..."
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
wget http://packages.namniart.com/repos/namniart.key -O - | sudo apt-key add -
echo "Done, now run 'sudo apt-get update' and then you will be able to install ROS"
