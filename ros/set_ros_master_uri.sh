#!/bin/bash

echo "Are you sourcing this script? If so, good. If not, run 'source $0 $1'"

if [[ $1 != "spot-1" && $1 != "spot-2" && $1 != "spot-3" && $1 != "spot-4" ]]
then
	echo "Error! First argument must be 'spot-[1-4]'"
	exit 1
fi

url="http://pcduino-ips.larsendt.com/$1"
ip=$(wget -qO - $url)

export ROS_MASTER_URI="http://$ip:11311"
