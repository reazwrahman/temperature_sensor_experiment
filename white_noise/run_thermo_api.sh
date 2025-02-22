#!/bin/bash

# Define the directory where player.py is located
DIRECTORY="/home/pi/smart_home/SmartHome"

# Navigate to the directory
cd "$DIRECTORY" || { echo "Directory not found!"; exit 1; } 

# activate venv 
source ../venv/bin/activate


# Run the Python script
python3 application.py

