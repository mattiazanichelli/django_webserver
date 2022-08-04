#!/bin/bash

# Variable
path=$(pwd)
json=$(ls "${path}"/customizo/resources/*.json)

# Content of script docker_setup.sh
content=(
"#!/bin/bash

# List users
currentUser=\$(getent passwd | grep bash | grep home | awk -F: '{print \$1}')

# Give currentUser Docker permission
sudo usermod -aG docker \${currentUser}
newgrp docker

# Verify that Docker Engine is installed correctly:
sudo docker run hello-world

# Add images installation script in currentUser folder and to its bash.profile
mv root/docker_images.sh /home/\${currentUser}
echo -e \"/home/\${currentUser}/docker_images.sh\" >> /home/\${currentUser}/.bashrc

# Disable firstboot.service
systemctl disable firstboot.service
rm -rf /etc/systemd/system/firstboot.service

# Self-remove script and reboot
rm -- \"\$0\" && reboot")

echo -e "${content}" > "${path}"/customizo/resources/source-files/custom/docker_setup.sh
