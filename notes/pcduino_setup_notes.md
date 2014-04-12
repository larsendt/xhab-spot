# XHAB PCDuino Setup Notes

## Create the xhab user and make admin

Set the password to xhab

    sudo adduser xhab
    sudo adduser xhab sudo

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

The following sizes assume an 8GB SD card. If you're using a different size, you
might consider tweaking the partition sizes.

* 1GB for /var (mmcblk0p1)
* 2GB for /usr (mmcblk0p2)
* the rest (5GB ish) for /home (mmcblk0p3)

My (Dane's) reasoning for having `/var` `/usr` and `/home` on the SD card:

* /usr is already 1GB on the default install, and will grow as more things are installed
* /var is the cache for `apt`, and will need more space
* /home is where all of the sensor data for SPOT will be put

Run the `fdisk` command **THIS WILL WIPE ALL DATA ON THE SD CARD**

    fdisk /dev/mmcblk0

Input the following (not including the comments marked with #, `<enter>` means
hit the enter key) At any point, you can type `q` to quit. None of the changes
will be made until you type `w`

    d         #delete the existing partition
    n         #create a new partiton for /var
    <enter>   #make the partition type 'primary'
    <enter>   #set the partition number
    <enter>   #set the location of the first sector
    +1G       #size the first partion to 1GiB
    n         #create a new partition for /usr
    <enter>   #make the partition type 'primary'
    <enter>   #set the partition number
    <enter>   #set the location of the first sector
    +2G       #size the partition to 2GiB
    n         #create a new partition for /home
    <enter>   #make the partition type 'primary'
    <enter>   #set the partition number
    <enter>   #set the location of the first sector
    <enter>   #size the partition to all of the remaining space
    w         #write the changes to the drive


## Create the ext4 filesystems on the new partitions

    mkfs.ext4 /dev/mmcblk0p1
    mkfs.ext4 /dev/mmcblk0p2
    mkfs.ext4 /dev/mmcblk0p3


## Migrate the existing files to the new partitions

    cd                             #in root's home dir
    mkdir tmpvar tmpusr tmphome    #make some temp mountpoints
    mount /dev/mmcblk0p1 tmpvar    #mount the /var partition
    mount /dev/mmcblk0p2 tmpusr    #mount the /usr partition
    mount /dev/mmcblk0p3 tmphome   #mount the /home partition
    cp -pr /var/* tmpvar           #copy all of /var's contents to the var partition
    cp -pr /usr/* tmpusr           #copy all of /usr's contents to the usr partition
    cp -pr /usr/* tmphome          #copy all of /home's contents to the home partition


## Mount folders

    sudo vim /etc/fstab

Add the following lines to the fstab (insert between 1st and second line)

    /dev/mmcblk0p1  /var    ext4    defaults,noatime    0   0
    /dev/mmcblk0p2  /usr    ext4    defaults,noatime    0   0
    /dev/mmcblk0p3  /home   ext4    defaults,noatime    0   0

**----> REBOOT AFTER DOING THIS <----**

`/var`, `/usr`, and `/home` are now on the SD card

## Fix /etc/apt/sources.list

In the above file, change each ubuntu url from

    http://ports.ubuntu.com/ubuntu-ports/

to

    http://ports.ubuntu.com/

Also, comment out all wiimu.com lines with the # character


## Run updates

    sudo apt-get update
    sudo apt-get upgrade


## Generate ssh keys as the xhab user

    ssh-keygen


## Put the new public key on github

Instructions forthcoming. For now, email `dane.t.larsen@gmail.com`


## Clone the SPOT repository

    cd
    git clone git@github.com:larsendt/xhab-spot.git


## Add the IP reporting crontab

    crontab -e

Then add the following line (you'll need to know vim)

    * * * * * /home/xhab/xhab-spot/cron_scripts/publish_ip.py

## Load appropriate kernel modules

Look in /etc/modules, and make sure that `gpio`, `pwm`, `adc` and `sw_interrupt` are in the
file. If not, add them, one per line.

For the changes to take effect, you will need to reboot, or run

    sudo modprobe gpio
    sudo modprobe pwm
    sudo modprobe adc
    sudo modprobe sw_interrupt

## Make the interrupt device readable by all users

By default `/dev/swirq` is readable only by root. This needs to be changed so that
all users can read/write/execute it.

    sudo chmod 777 /dev/swirq

Then open /etc/rc.local and add the following line just before the last `exit 0`

    chmod 777 /dev/swirq

That's it!

## Things to install

Add more here as needed

* git
* vim
* ros-groovy-ros-base
* python-smbus
* python-netifaces
* python-requests
* python-setuptools
* python-psutil
* iTunes (just kidding! -MP)

also run these
	
    sudo easy_install pip
    sudo pip install pyzmq
    sudo pip install arrow

