#!/bin/bash

# Variables
path=$(pwd)
json=$(ls "${path}"/customizo/resources/*.json)
firstName=$(cat "${json}" | jq -r .firstName)
lastName=$(cat "${json}" | jq -r .lastName)

# Need these packages in order to execute scripts correctly
#sudo apt install xorriso;
#sudo apt install jq;

# Execute scripts cascade
source "${path}"/customizo/resources/initiate.sh 2> error \
&& source "${path}"/customizo/resources/write_encryption_script.sh 2> error \
&& source "${path}"/customizo/resources/write_docker_install_script.sh 2> error \
&& source "${path}"/customizo/resources/write_docker_setup_script.sh 2> error \
&& source "${path}"/customizo/resources/write_docker_images_script.sh 2> error \
&& source "${path}"/customizo/resources/write_grub_entry.sh 2> error \
&& source "${path}"/customizo/resources/write_wait_cloud-init_script.sh 2> error \
&& source "${path}"/customizo/resources/xorriso.sh 2>&1;

# Remove source-files directory (a.k.a ISO unzipped) and json user file
rm -r "${path}"/customizo/resources/source-files/
rm -f "${path}"/customizo/resources/"${lastName}""${firstName}".json
