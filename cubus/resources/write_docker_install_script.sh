#!/bin/bash

# Variable
path=$(pwd)
json=$(ls "${path}"/cubus/resources/*.json)

# Content of script docker_install.sh
content=(
"#!/bin/bash

sudo apt-get update
sudo apt-get upgrade -y

# Add Docker’s official GPG key:
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \\
  \"deb [arch=\$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \\
  \$(lsb_release -cs) stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine:
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose

# Self-remove script
rm -- \"\$0\"")

echo -e "${content}" > "${path}"/cubus/resources/source-files/custom/docker_install.sh

# Write firstboot.service
service=(
"[Unit]
Description=One time boot script
[Service]
Type=simple
Restart=no
User=root
ExecStart=/root/firstboot_setup.sh
[Install]
WantedBy=multi-user.target")

echo -e "${service}" > "${path}"/cubus/resources/source-files/custom/firstboot.service
