#!/bin/bash

# Variable
path=$(pwd)

# Content of script encrypt.sh
content=(
"#!/bin/bash

dd if=/dev/urandom of=/boot/keyfile bs=1024 count=4

sudo echo '1234567890' | cryptsetup -v luksAddKey /dev/sda3 /boot/keyfile

sdax=\$(lsblk | grep boot | awk '{print \$1}')

sdax=\"\${sdax:2}\"

uuid=\$(ls -l /dev/disk/by-uuid/ | grep \$sdax | awk '{print \$9}')

sed -i \"s/none/\/dev\/disk\/by-uuid\/\$uuid:\/keyfile/\" /etc/crypttab

sed -i \"s/luks/luks,keyscript=\/lib\/cryptsetup\/scripts\/passdev/\" /etc/crypttab

sudo chmod 0400 /boot/keyfile

sudo update-initramfs -u

# Self-remove script
rm -- \"\$0\"")

echo -e "${content}" > "${path}"/cubus/resources/source-files/custom/encrypt.sh