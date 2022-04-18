#! /bin/sh
cp /dir/raspberry-pi-logo.jpg /dir/`date +%Y-%m-%d`.jpg
sudo chmod ugo+rwx /dir/`date +%Y-%m-%d`.jpg
python3.9 /dir/pythotev_demo_http_nasa_api_change_background.py
export DISPLAY=:0
export XAUTHORITY=/home/myuser/.Xauthority #echo XAUTHORITY to get value
export XDG_RUNTIME_DIR=/run/user/1000 #echo XDG_RUNTIME_DIR to get value
pcmanfm --set-wallpaper /dir/`date +%Y-%m-%d`.jpg
