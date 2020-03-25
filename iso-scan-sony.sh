#!/usr/bin/env bash
set -eu

sleep 1m
xset dpms force off

: ${MIN_ISO:=100}
: ${MAX_ISO:=500000}
: ${N_SAMPLES:=30}


sony_folder="$HOME/Projects/Datasets/Sony-$(date +%Y-%m-%d)"

mkdir -p $sony_folder

cd $sony_folder

SUPPORTED_ISOS=$(gphoto2 --get-config /main/imgsettings/iso | grep -P 'Choice: \d+ \d+$' | cut -d' ' -f 3)
for iso in $SUPPORTED_ISOS; do
	if [[ "$iso" -lt "$MIN_ISO" ]] || [[ "$iso" -gt "$MAX_ISO" ]]; then
		continue
	fi
	echo "capturing at iso=$iso"
	i=1
	while [[ "$i" -le "$N_SAMPLES" ]]; do 
		
		gphoto2 --set-config /main/imgsettings/iso=$iso
		gphoto2 --capture-image-and-download --filename "shot-$i-iso-${iso}.ARW" 
		i=$(($i + 1))
	done
done
