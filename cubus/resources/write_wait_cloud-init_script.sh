#!/bin/bash

# Variable
path=$(pwd)

# Content of script wait_cloud-init.sh
script_content=(
"#!/bin/bash

# wait until cloud-init has finished before showing the login screen
mkdir -p /etc/systemd/system/getty@tty1.service.d/

content=(
\"[Unit]

After=cloud-init.target\")
echo -e \"\${content}\" > /etc/systemd/system/getty@tty1.service.d/wait_cloud-init.conf

# Self-remove script
rm -- \"\$0\"")

echo -e "${script_content}" > "${path}"/customizo/resources/source-files/custom/wait_cloud-init.sh


