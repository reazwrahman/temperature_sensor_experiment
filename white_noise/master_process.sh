#!/bin/bash

# Start each script as a separate background process
/bin/bash run_thermo_ui.sh &
/bin/bash run_thermo_api.sh & 
/bin/bash run_white_noise.sh &

# Exit master script, leaving child processes running
exit 0
