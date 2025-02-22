#!/bin/bash

# Define the directory where player.py is located
DIRECTORY="/home/pi/thermostat_ui"

# Navigate to the directory
cd "$DIRECTORY" || { echo "Directory not found!"; exit 1; }

# Run the Python script
python3 -m http.server 8000 --bind 0.0.0.0

