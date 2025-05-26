#!/bin/bash

interface=$1
new_mac=$2

if [ -z "$interface" ] || [ -z "$new_mac" ]; then
    echo "Usage: $0 <interface> <new_mac>"
    exit 1
fi

echo "[+] Changing MAC address for $interface to $new_mac"
ifconfig $interface down
ifconfig $interface hw ether $new_mac
ifconfig $interface up
echo "[+] MAC address changed successfully."
