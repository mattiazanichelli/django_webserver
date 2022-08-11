#!/bin/bash 

# Variable
path=$(pwd)
json=$(ls "${path}"/cubus/resources/*.json)

content=(
"#!/bin/bash

# Show final installation setup messages
source ./whiptails.sh

# Pull Docker images

# Remove docker images entry from .bashrc profile
sed -i 'N;\$!P;D' .bashrc

# Self-remove script
rm -f -- \"\$0\"")

echo -e "${content}" > "${path}"/cubus/resources/source-files/custom/docker_images.sh

# Read docker images from json file
length=$(cat "${json}" | jq '.docker_images | length')
declare -a images

for ((i=0; i<${length}; i++))
do
	images+=($(cat "${json}" | jq -r .docker_images[$i]))
done

# Search for docker images to check existence
for  ((i=0; i<${#images[@]}; i++))
do
	result=$(docker search --filter is-official=true --limit 1 "${images[$i]}" | grep OK | awk '{print $1}')
	if [ "${result}" ]
	then
		final_images[$i]+=${result}
	fi
done

# Write docker images to be pulled on first boot
for ((i=0; i<=${#final_images[@]}; i++)) do
	if [ ${final_images[$i]} ]
	then
		sed -i "/# Pull Docker images/a docker pull ${final_images[$i]}" "${path}"/cubus/resources/source-files/custom/docker_images.sh
	fi
done
