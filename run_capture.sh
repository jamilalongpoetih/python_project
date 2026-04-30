#!/bin/bash

#1. Find the active Ethernet interface_name look for 'en' that is currently up
INTERFACE=$(ip -o link show|grep 'state UP ' | awk -F': ' '{print $2}'| grep '^en' | head -n 1)
###echo "interface is $INTERFACE"
if [ -z "$INTERFACE" ]; then 
	echo "[INFO]: No active Ethernet interface found...checking WIFI"
	INTERFACE=$(ip -o link show|grep 'state UP ' | awk -F': ' '{print $2}'| grep '^wlp1s0' | head -n 1)
	if [ -z "$INTERFACE" ]; then
		echo "[INFO]: No WIFI interface found either..."
		exit 1
	fi
fi

echo "--- Auto-detected Ethernet:$INTERFACE ---"

#2. Activate the virtual env
source venv/bin/activate

#3. Run traffic_test.py with the detected interface
#use sys.argv or argparse version of the script

if [ $# -eq 0 ]; then
	echo "No count provided, default to 10"
	COUNT=10
else
	COUNT=$1
fi
python3 traffic_test.py  -i "$INTERFACE" -c "$COUNT"
