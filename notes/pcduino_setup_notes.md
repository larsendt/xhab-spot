# XHAB PCDuino Setup Notes

## Create the xhab user and make admin

    sudo adduser xhab
    sudo adduser xhab sudo

Set the password to xhab

## Change hostname

    sudo vim /etc/hostname

Set it to spot-x where x is the number on the back of the board

## Add an option to autoconnect to UCB Wireless

Edit /etc/network/interfaces

    auto wlan{3,4}
    iface wlan{3,4} inet dhcp
    wireless-essid UCB Wireless

The wlanX number can be found by running `ifconfig`

## Partition the SD card

* 1GB for /var (mmcblk0p1)
* 2GB for /usr (mmcblk0p2)
* the rest for /home (mmcblk0p3)

    fdisk /dev/mmcblk0

create the filesystems

    mkfs.ext4 /dev/mmcblk0p1
    mkfs.ext4 /dev/mmcblk0p2
    mkfs.ext4 /dev/mmcblk0p3

## Mount folders

    sudo vim /etc/fstab

add the following lines to the fstab (insert between 1st and second line)

/dev/mmcblk0p1  /var    ext4    defaults,noatime    0   0
/dev/mmcblk0p2  /usr    ext4    defaults,noatime    0   0
/dev/mmcblk0p3  /home   ext4    defaults,noatime    0   0

## Fix /etc/apt/sources.list

In the above file, change each url from

    http://ports.ubuntu.com/ubuntu-ports/

to

    http://ports.ubuntu.com

## Run updates

    sudo apt-get update
    sudo apt-get upgrade

## Generate ssh keys as the xhab user

    ssh-keygen

## Things to install

*git
*vim
*ros-groovy-ros-base

## Things done so far
spot-1 2/15/2014:
    partitions on SD card created
    migrated /var /usr and /home
    created xhab user
    added xhab user to sudo group
    set hostname to spot-1
    fixed /etc/apt/sources.list
    updated system
    installed ROS
    installed git + vim
    generated ssh key and uploaded to github (under Dane's account)
    cloned xhab-spot repository
    set wireless to autoconnect to UCB Wireless
    done for now

spot-2 2/15/2014:
    created xhab user
    added xhab user to sudo group
    set hostname to spot-2
    fixed /etc/apt/sources.list
    updated system
    made partitions + migrated /usr /var /home
    installed git+vim+ROS
    generated ssh key and uploaded to github under Dane's account
    cloned xhab-spot repository
    set wireless to autoconnect to UCB Wireless
    done for now

spot-3 2/15/2014:
    reinstalled ubuntu
    set hostname to spot-3
    created xhab user and added to sudo group
    creating partitions
    updated system

spot-4 2/15/2014:
    installed git+vim
    fixed /etc/apt/sources.list
    autoconnect to UCB Wireless
    set hostname to spot-4
    installed git+vim
