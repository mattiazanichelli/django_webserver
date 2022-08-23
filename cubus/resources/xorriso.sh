#!/bin/bash

# Variables
path=$(pwd)
json=$(ls "${path}"/cubus/resources/*.json)
iso=$(ls "${path}"/cubus/resources/*.iso)
#first_name=$(cat "${json}" | jq -r .first_name)
#last_name=$(cat "${json}" | jq -r .last_name)
newname=$(cat "${json}" | jq -r .name)
#new_name=$(echo "${last_name}"-"${first_name}")

# Pack new ISO
xorriso -as mkisofs -r -V "Custom Ubuntu Server" -J -joliet-long -l -iso-level 3 -partition_offset 16 --grub2-mbr \
--interval:local_fs:0s-15s:zero_mbrpt,zero_gpt:"${iso}" --mbr-force-bootable \
-append_partition 2 28732ac11ff8d211ba4b00a0c93ec93b --interval:local_fs:2855516d-2864011d::"${iso}" \
-appended_part_as_gpt -c /boot.catalog -b /boot/grub/i386-pc/eltorito.img -no-emul-boot -boot-load-size 4 \
-boot-info-table --grub2-boot-info -eltorito-alt-boot -e '--interval:appended_partition_2:all::' -no-emul-boot\
 -o "${path}"/cubus/resources/"${newname}".iso "${path}"/cubus/resources/source-files/