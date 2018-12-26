#!/bin/bash
# Script identifies desired target, defines corresponding paths
# and deploys files to target

# Informs about missing arguments and displays help
function PrintArgumentsHelp {
    echo "Running script $0 failed."
    echo "No or invalid arguments supplied. Valid arguments are:"
    echo "  check:      show current hardware and operating system"
    echo "  python:     install python"
    echo "  app:        install app"
    echo "  all:        perform all of the above steps at once"
}

# Checks if script is running on an ARM processor and Linux
function CheckForRaspbian {
    echo "Checking machine hardware name, operating system and release"
    CURRENT_MACHINE_HW_NAME=$(uname -m)
    CURRENT_OS_NAME=$(uname -s)
    CURRENT_RELEASE=$(uname -r)
    echo "Running $CURRENT_OS_NAME on $CURRENT_MACHINE_HW_NAME release $CURRENT_RELEASE"
}

# Install app
function InstallPython {
    # install pyhton 3
    sudo apt-get -y install python3
    # install python package index (should be included by default)
    sudo apt-get -y install python3-pip
    # install pygame
    sudo apt-get -y install python3-pygame
}

# Deploy files to remote Raspberry Pi
function InstallApp {
    IP_RASPI='pi@icpi.local' # Define environment variables
    SOURCE_FILES_FOLDER='./source' # Location of source files
    TARGET_FILES_FOLDER='~/target' # Location of target files

    echo "Deploying files to Raspberry Pi..."
    rsync -av --no-perms --omit-dir-times --progress --exclude=hello.py $SOURCE_FILES_FOLDER/* $IP_RASPI:$TARGET_FILES_FOLDER 
}
 
# Check if an argument was provided
if [ -z "$1" ]
  then
    PrintArgumentsHelp
    exit
fi

# Evaluate command line arguments and run desired function
if [ $1 = "check" ]; then
    CheckForRaspbian
elif [ $1 = "python" ]; then 
    InstallPython
elif [ $1 = "app" ]; then 
    InstallApp
elif [ $1 = "all" ]; then 
    CheckForRaspbian
    InstallPython
    InstallApp
else
    PrintArgumentsHelp
    exit
fi
