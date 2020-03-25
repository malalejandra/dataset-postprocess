#!/usr/bin/env bash
set -eu

: ${MIN_ISO:=100}
: ${MAX_ISO:=50000}
: ${N_SAMPLES:=30}
: ${SLEEP:=60}

for dev in /sys/bus/usb/devices/*/power/control; do
	sudo bash -c "echo on > $dev"
done

if [[ ! -v TEST ]]; then
	echo "Sleeping for $SLEEP seconds"
	sleep "$SLEEP"
	xset dpms force off
fi


nikon_folder="$HOME/Projects/Datasets/Nikon-$(date +%Y-%m-%d)"

mkdir -p $nikon_folder

cd $nikon_folder


gphoto2 --set-config capturetarget=1

SUPPORTED_ISOS=$(gphoto2 --get-config /main/imgsettings/iso 2>&1 | grep '^Choice' | cut -d' ' -f 3)
for iso in $SUPPORTED_ISOS; do
	if [[ "$iso" -lt "$MIN_ISO" ]] || [[ "$iso" -gt "$MAX_ISO" ]]; then
		continue
	fi
	echo "capturing at iso=$iso"
	i=1
	while [[ "$i" -lt "$N_SAMPLES" ]]; do 
		gphoto2 --set-config /main/imgsettings/iso=$iso
		gphoto2 \
			--capture-image-and-download \
			--filename "iso-${iso}-shot-$i.NEF" \
			--force-overwrite
			--debug --debug-logfile=nikon-debug.log
		i=$(($i + 1))
	done
done
