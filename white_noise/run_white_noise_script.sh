#!/bin/bash

# Define the directory where player.py is located
DIRECTORY="/home/pi/smart_home/sensor_experiment/temperature_sensor_experiment/white_noise"  

# Navigate to the directory
cd "$DIRECTORY" || { echo "Directory not found!"; exit 1; }

# Run the Python script
python3 player.py

