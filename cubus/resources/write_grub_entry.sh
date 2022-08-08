#!/bin/bash

# Variable
path=$(pwd)
tab=(\ \ )

content=(
"menuentry \"Ubuntu Server Custom\" {
${tab}${tab}set gfxpayload=keep
${tab}${tab}linux	/casper/vmlinuz   ds=nocloud\\\\;s=/cdrom/custom/ quiet splash autoinstall ---
${tab}${tab}initrd  /casper/initrd
}")

awk -v "content=${content}" "/grub_platform/ && !x {print content; x=1} 1" "${path}"/cubus/resources/source-files/boot/grub/grub.cfg > grub.cfg
mv grub.cfg "${path}"/cubus/resources/source-files/boot/grub/grub.cfg