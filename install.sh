#!/bin/bash
if [[ `whoami` != 'root' ]]; then
	echo 'E: You must be root. Script needs to create a file on /usr/bin to install the script globally'
	exit 1
fi
cp main.py /usr/bin/persshistunt
chmod +x /usr/bin/persshistunt
