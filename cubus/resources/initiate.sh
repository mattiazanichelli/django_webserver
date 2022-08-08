#!/bin/bash

# Variables
path=$(pwd)
json=$(ls "${path}"/cubus/resources/*.json)
iso=$(ls "${path}"/cubus/resources/*.iso)
tab=(\ \ )

# Create directories, files an unzip
mkdir "${path}"/cubus/resources/source-files
7z -y x ${iso} -o"${path}"/cubus/resources/source-files
mkdir "${path}"/cubus/resources/source-files/custom
touch user-data
touch "${path}"/cubus/resources/source-files/custom/meta-data
cp "${path}"/cubus/resources/sembo.zip "${path}"/cubus/resources/source-files/custom/
cp "${path}"/cubus/resources/.run_sembo.sh "${path}"/cubus/resources/source-files/custom/

# Write user-data file
content=(
"#cloud-config
autoinstall:
${tab}version: 1
${tab}refresh-installer:  # start with an up-to-date installer
${tab}update: yes
${tab}interactive-sections:  # Install groups listed here will wait for user input
${tab}${tab}- locale
${tab}${tab}- keyboard
${tab}${tab}- network
${tab}${tab}- identity
${tab}packages:
${tab}ssh:
${tab}${tab}allow-pw: true
${tab}${tab}install-server: true
${tab}storage:
${tab}${tab}config:
${tab}${tab}- ptable: gpt
${tab}${tab}${tab}path: /dev/sda
${tab}${tab}${tab}wipe: superblock
${tab}${tab}${tab}preserve: false
${tab}${tab}${tab}name: ''
${tab}${tab}${tab}grub_device: true
${tab}${tab}${tab}type: disk
${tab}${tab}${tab}id: disk-sda
${tab}${tab}- device: disk-sda
${tab}${tab}${tab}size: 1048576
${tab}${tab}${tab}flag: bios_grub
${tab}${tab}${tab}number: 1
${tab}${tab}${tab}preserve: false
${tab}${tab}${tab}grub_device: false
${tab}${tab}${tab}type: partition
${tab}${tab}${tab}id: partition-0
${tab}${tab}- device: disk-sda
${tab}${tab}${tab}size: 600000000
${tab}${tab}${tab}wipe: superblock
${tab}${tab}${tab}flag: ''
${tab}${tab}${tab}number: 2
${tab}${tab}${tab}preserve: false
${tab}${tab}${tab}grub_device: false
${tab}${tab}${tab}type: partition
${tab}${tab}${tab}id: partition-1
${tab}${tab}- fstype: ext4
${tab}${tab}${tab}volume: partition-1
${tab}${tab}${tab}preserve: false
${tab}${tab}${tab}type: format
${tab}${tab}${tab}id: format-0
${tab}${tab}- device: disk-sda
${tab}${tab}${tab}size: -1
${tab}${tab}${tab}wipe: superblock
${tab}${tab}${tab}flag: ''
${tab}${tab}${tab}number: 3
${tab}${tab}${tab}preserve: false
${tab}${tab}${tab}grub_device: false
${tab}${tab}${tab}type: partition
${tab}${tab}${tab}id: partition-2
${tab}${tab}- volume: partition-2
${tab}${tab}${tab}key: '1234567890'
${tab}${tab}${tab}preserve: false
${tab}${tab}${tab}type: dm_crypt
${tab}${tab}${tab}id: dm_crypt-0
${tab}${tab}- name: ubuntu-vg
${tab}${tab}${tab}devices:
${tab}${tab}${tab}- dm_crypt-0
${tab}${tab}${tab}preserve: false
${tab}${tab}${tab}type: lvm_volgroup
${tab}${tab}${tab}id: lvm_volgroup-0
${tab}${tab}- name: ubuntu-lv
${tab}${tab}${tab}volgroup: lvm_volgroup-0
${tab}${tab}${tab}size: -1
${tab}${tab}${tab}wipe: superblock
${tab}${tab}${tab}preserve: false
${tab}${tab}${tab}type: lvm_partition
${tab}${tab}${tab}id: lvm_partition-0
${tab}${tab}- fstype: ext4
${tab}${tab}${tab}volume: lvm_partition-0
${tab}${tab}${tab}preserve: false
${tab}${tab}${tab}type: format
${tab}${tab}${tab}id: format-1
${tab}${tab}- path: /
${tab}${tab}${tab}device: format-1
${tab}${tab}${tab}type: mount
${tab}${tab}${tab}id: mount-1
${tab}${tab}- path: /boot
${tab}${tab}${tab}device: format-0
${tab}${tab}${tab}type: mount
${tab}${tab}${tab}id: mount-0
${tab}package_update: true
${tab}package_upgrade: true
${tab}late-commands:
${tab}${tab}- curtin in-target --target=/target -- apt-get update
${tab}${tab}- curtin in-target --target=/target -- apt-get upgrade -y
${tab}${tab}- cp /cdrom/custom/encrypt.sh /target/root
${tab}${tab}- curtin in-target --target=/target -- chmod +x /root/encrypt.sh
${tab}${tab}- curtin in-target --target=/target -- bash /root/encrypt.sh
${tab}${tab}- cp /cdrom/custom/docker_install.sh /target/root
${tab}${tab}- curtin in-target --target=/target -- chmod +x /root/docker_install.sh
${tab}${tab}- curtin in-target --target=/target -- bash /root/docker_install.sh
${tab}${tab}- cp /cdrom/custom/firstboot_setup.sh /target/root
${tab}${tab}- curtin in-target --target=/target -- chmod +x /root/firstboot_setup.sh
${tab}${tab}- cp /cdrom/custom/docker_images.sh /target/root
${tab}${tab}- curtin in-target --target=/target -- chmod +x /root/docker_images.sh
${tab}${tab}- cp /cdrom/custom/firstboot.service /target/etc/systemd/system
${tab}${tab}- curtin in-target --target=/target -- systemctl enable firstboot.service
${tab}${tab}- cp /cdrom/custom/wait_cloud-init.sh /target/root
${tab}${tab}- curtin in-target --target=/target -- chmod +x /root/wait_cloud-init.sh
${tab}${tab}- curtin in-target --target=/target -- bash /root/wait_cloud-init.sh
${tab}${tab}- cp /cdrom/custom/sembo.zip /target/root
${tab}${tab}- cp /cdrom/custom/.run_sembo.sh /target/root
${tab}${tab}- curtin in-target --target=/target -- chmod +x /root/.run_sembo.sh
${tab}${tab}- echo '===== Installation finished! ====='")
echo -e "${content}" > user-data
mv user-data "${path}"/cubus/resources/source-files/custom/

# Add packages to user-data
length=$(cat "${json}" | jq '.packages | length')
declare -a packages

for ((i=0; i<length; i++))
do
	packages+=($(cat "${json}" | jq -r .packages[$i]))
done

for ((i=0; i<length; i++)) do
	sed -i "/packages/a \ \ \ \ - ${packages[$i]}" "${path}"/cubus/resources/source-files/custom/user-data
done

# Add packages required for Docker (ca-certificate, curl, gnupg, lsb-release)
sed -i "/packages/a \ \ \ \ - lsb-release" "${path}"/cubus/resources/source-files/custom/user-data
sed -i "/packages/a \ \ \ \ - gnupg" "${path}"/cubus/resources/source-files/custom/user-data
sed -i "/packages/a \ \ \ \ - curl" "${path}"/cubus/resources/source-files/custom/user-data
sed -i "/packages/a \ \ \ \ - ca-certificates" "${path}"/cubus/resources/source-files/custom/user-data

# Add packages required for running SeMBo (net-tools, unzip, python3-pip)
sed -i "/packages/a \ \ \ \ - net-tools" "${path}"/cubus/resources/source-files/custom/user-data
sed -i "/packages/a \ \ \ \ - unzip" "${path}"/cubus/resources/source-files/custom/user-data
sed -i "/packages/a \ \ \ \ - python3-pip" "${path}"/cubus/resources/source-files/custom/user-data




