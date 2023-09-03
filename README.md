# Laptop-Battery-Monitor
Python script to check battery levels &amp; NTFY for notifications

This is a python script created as a project with assistance of ChatGPT.
This script checks your battery level and lets you know if the battery gets below 20% using NTFY or terminal output when run manually.

To use the NTFY features update the Ntfy configuration variables with the URL target location and topic.

To have the script run every 5 minutes in Linux run the following:

Download the py file and move to your script location
sudo mv battery-check.py /usr/local/bin/
sudo chmod +x /usr/local/bin/battery-check.py
crontab -e
Add the following line for the script to run every 5 minutes
*/5 * * * * /usr/bin/python3 /usr/local/bin/battery-check.py
