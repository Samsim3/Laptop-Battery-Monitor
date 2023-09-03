import importlib
import subprocess

# Threshold percentage for battery level
threshold_percent = 20

# Ntfy configuration variables
ntfy_url = "URL"
ntfy_topic = "TOPIC"

# Check if psutil is installed
try:
    importlib.import_module('psutil')
except ImportError:
    print("psutil is not installed. Installing...")
    try:
        # Install psutil using pip
        subprocess.check_call(["pip", "install", "psutil"])
        print("psutil has been successfully installed.")
    except Exception as e:
        print(f"Error installing psutil: {e}")
        exit(1)

import psutil

def get_battery_status():
    """
    Get the current battery status including percentage and power source.

    Returns:
        Tuple: (battery_percent, power_plugged)
            battery_percent (int): Battery percentage (rounded to the nearest integer).
            power_plugged (bool): True if the laptop is plugged in, False if running on battery.
    """
    battery = psutil.sensors_battery()
    if battery:
        percent = round(battery.percent)  # Round off to the nearest integer
        power_plugged = battery.power_plugged
        return percent, power_plugged
    else:
        return None

battery_info = get_battery_status()

if battery_info is not None:
    percent, power_plugged = battery_info
    if power_plugged:
        print(f"Your laptop is plugged in and the battery is at {percent}%")
        if percent == 100:
            # Battery is fully charged, run the ntfy command
            ntfy_command = ["ntfy", "publish", f"{ntfy_url}/{ntfy_topic}", "The battery is fully charged. Please disconnect the charge cable."]
            subprocess.run(ntfy_command)
    else:
        if percent < threshold_percent:
            # Battery is below the threshold, run the ntfy command
            ntfy_command = ["ntfy", "publish", f"{ntfy_url}/{ntfy_topic}", f"Battery below {threshold_percent}%"]
            subprocess.run(ntfy_command)
            print(f"Your laptop is running on battery and the battery is at {percent}%")
        else:
            print(f"Your laptop is running on battery and the battery is at {percent}%")
else:
    print("Battery information is not available.")

