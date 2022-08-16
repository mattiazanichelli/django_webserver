#!/bin/bash

# Unzip sembo app if not already done
if test -f sembo.zip; then
  unzip sembo.zip
  rm -f sembo.zip
  pip install -r sembo_app/requirements.txt

  tot_cols=$(tput cols)
  tot_lines=$(tput lines)
  cols=$( expr "${tot_cols}" - 10 )
  lines=$( expr "${tot_lines}" - 5 )

  ip_addr=$(hostname -I | awk '{print $1}')
  whiptail --title "Done!" --msgbox "The system is now ready to use!\n\nYou can access SeMBo from http://${ip_addr}:8050 after closing this message" 15 60
fi

# Show address message
ip_addr=$(hostname -I | awk '{print $1}')
echo "SeMBo is running at http://${ip_addr}:8050"

# Run sembo on the background
python3 sembo_app/app.py > /dev/null &

