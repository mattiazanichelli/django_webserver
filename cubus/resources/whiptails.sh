#!/bin/bash


user=$(whoami)
tot_cols=$(tput cols)
tot_lines=$(tput lines)
cols=$( expr "${tot_cols}" - 10 )
lines=$( expr "${tot_lines}" - 5 )


whiptail --title "Welcome!" --msgbox "Hello ${user}!\n\n
Welcome to your Custom Ubuntu Server.\n\n
# shellcheck disable=SC2086
Please wait until the installation is finished..." "${lines}" "${cols}"

if test -f ready; then
  ip_addr=$(hostname -I | awk '{print $1}')
  whiptail --title "Ready!" --msgbox "Done!\n\n
  The system is now ready to use.\n\n
  You can access SeMBo from http://${ip_addr}:8050" "${lines}" "${cols}"
  rm -f ready
fi

rm -- "$0"

