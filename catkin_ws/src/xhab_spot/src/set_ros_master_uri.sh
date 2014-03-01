#!/bin/bash

echo "Are you sourcing this script? If so, good. If not, run 'source $0 $1'"

if [[ $1 != "spot-1" && $1 != "spot-2" && $1 != "spot-3" && $1 != "spot-4" && $1 != "localhost" ]]
then
    echo "Error! First argument must be 'spot-[1-4]' or localhost"
    echo "This script is for informing ROS nodes where roscore is running."
else
    if [ $1 == "localhost" ] 
    then
        ip="localhost"
    else
        url="http://pcduino-ips.larsendt.com/$1"
        ip=$(wget -qO - $url)
    fi
    export ROS_MASTER_URI="http://$ip:11311"
    echo "ROS_MASTER_URI is now '$ROS_MASTER_URI'"
fi
