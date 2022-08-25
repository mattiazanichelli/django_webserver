#!/bin/bash

# Unzip sembo app if not already done
if test -f sembo.zip; then
  printf "\n\n"
  printf "%$(tput cols)s" | sed "s/ /=/g" | xargs
  echo "Installing Sembo"
  printf "%$(tput cols)s" | sed "s/ /=/g" | xargs
  printf "\n\n"

  if ! [[ $(ping -c 3 8.8.8.8 2> /dev/null) ]]; then
    whiptail --title "Warning" --msgbox "Cannot connect to the Internet.\n\nPlease connect your system to install Sembo ." 15 60
    exit 0
  fi

  unzip sembo.zip
  rm -f sembo.zip
  pip install -r sembo_app/requirements.txt --no-warn-script-location

  tot_cols=$(tput cols)
  tot_lines=$(tput lines)
  cols=$( expr "${tot_cols}" - 10 )
  lines=$( expr "${tot_lines}" - 5 )

  ip_addr=$(hostname -I | awk '{print $1}')
  whiptail --title "Done!" --msgbox "The system is now ready to use!\n\nYou can access Sembo from http://${ip_addr}:8050 after closing this message" 15 60
fi

# Show address message
ip_addr=$(hostname -I | awk '{print $1}')
echo "Sembo is running at http://${ip_addr}:8050"

# Run sembo on the background
python3 sembo_app/app.py > /dev/null &

