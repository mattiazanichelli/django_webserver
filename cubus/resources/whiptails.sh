#!/bin/bash


user=$(whoami)
tot_cols=$(tput cols)
tot_lines=$(tput lines)
cols=$( expr "${tot_cols}" - 10 )
lines=$( expr "${tot_lines}" - 5 )


ip_addr=$(hostname -I | awk '{print $1}')
whiptail --title "Ready!" --msgbox "Done!\n\n
The system is now ready to use.\n\n
You can access Sembo from http://${ip_addr}:8050" "${lines}" "${cols}"

rm -- "$0"

