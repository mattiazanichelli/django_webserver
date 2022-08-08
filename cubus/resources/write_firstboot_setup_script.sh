#!/bin/bash

# Variable
path=$(pwd)
json=$(ls "${path}"/cubus/resources/*.json)

# Content of script docker_setup.sh
content=(
"#!/bin/bash

# List users
currentUser=\$(getent passwd | grep bash | grep home | awk -F: '{print \$1}')

# Give currentUser Docker permission
sudo usermod -aG docker \${currentUser}
newgrp docker

# Add images installation script in currentUser folder and to its bash.profile
mv root/docker_images.sh /home/\${currentUser}
echo -e \"/home/\${currentUser}/docker_images.sh\" >> /home/\${currentUser}/.bashrc

# Move sembo zip and run script to user's home and add script execution to last line of bashrc.profile
mv /root/sembo.zip /home/\${currentUser}
mv /root/.run_sembo.sh /home/\${currentUser}
echo -e \"/home/\${currentUser}/.run_sembo.sh\" >> /home/\${currentUser}/.bashrc

# Disable firstboot.service
systemctl disable firstboot.service
rm -rf /etc/systemd/system/firstboot.service

# Self-remove script and reboot
rm -- \"\$0\" && reboot")

echo -e "${content}" > "${path}"/cubus/resources/source-files/custom/firstboot_setup.sh
