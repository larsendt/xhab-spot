#!/bin/bash

BRC=~/.bashrc
BRC_BACK=~/.bashrc.backup
CURDIR=`pwd`

if [ -f BRC ]
then
	echo "Backing up $BRC to $BRC_BAK"
	mv $BRC $BRC_BAK
fi

"Linking bashrc to $BRC"
ln -s $CURDIR/bashrc $BRC
