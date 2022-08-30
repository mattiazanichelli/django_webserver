#!/bin/bash

# Variables
path=$(pwd)
json=$(ls "${path}"/cubus/resources/*.json)
#firstName=$(cat "${json}" | jq -r .firstName)
#lastName=$(cat "${json}" | jq -r .lastName)
isoname=$(cat "${json}" | jq -r .name)


# Need these packages in order to execute scripts correctly !!!
# sudo apt install xorriso;
# sudo apt install jq;

# Execute scripts cascade
source "${path}"/cubus/resources/initiate.sh 2>> error \
&& source "${path}"/cubus/resources/write_firstboot_setup_script.sh 2>> error \
&& source "${path}"/cubus/resources/write_docker_install_script.sh 2>> error \
&& source "${path}"/cubus/resources/write_docker_images_script.sh 2>> error \
&& source "${path}"/cubus/resources/write_wait_cloud-init_script.sh 2>> error \
&& source "${path}"/cubus/resources/xorriso.sh 2>&1;

# Original with encryption script
#source "${path}"/cubus/resources/initiate.sh 2> error \
#&& source "${path}"/cubus/resources/write_encryption_script.sh 2> error \
#&& source "${path}"/cubus/resources/write_docker_install_script.sh 2> error \
#&& source "${path}"/cubus/resources/write_firstboot_setup_script.sh 2> error \
#&& source "${path}"/cubus/resources/write_docker_images_script.sh 2> error \
#&& source "${path}"/cubus/resources/write_grub_entry.sh 2> error \
#&& source "${path}"/cubus/resources/write_wait_cloud-init_script.sh 2> error \
#&& source "${path}"/cubus/resources/xorriso.sh 2>&1;

# Remove source-files directory (ISO unzipped) and json user file
rm -r "${path}"/cubus/resources/source-files/
rm -f "${path}"/cubus/resources/"${isoname}".json
