#!/bin/bash
# Script launches desired commands 
# based on the specified arguments on the command line.

# Informs about missing arguments and displays help
function PrintArgumentsHelp {
    echo "Running script $0 failed."
    echo "No or invalid arguments supplied. Valid arguments are:"
    echo "  info:       show current hardware and operating system"
    echo "  python:     install python"
    echo "  sync:       synchronize workspace files with remote machine"
    echo "  debug:      launch main python process through ptvsd for remote debugging"
    echo "  sync2debug: sync and then launch debug through ssh from host"
}

# Print OS info such as if script is running on an ARM processor and Linux
function PrintOSInfo {
    echo "Checking machine hardware name, operating system and release"
    CURRENT_MACHINE_HW_NAME=$(uname -m)
    CURRENT_OS_NAME=$(uname -s)
    CURRENT_RELEASE=$(uname -r)
    echo "Running $CURRENT_OS_NAME on $CURRENT_MACHINE_HW_NAME release $CURRENT_RELEASE"
}

# Print OS info such as if script is running on an ARM processor and Linux
function ExitIfNotRunningOnArmAndLinux {
    if [[ $CURRENT_MACHINE_HW_NAME == "arm"* ]] && [ $CURRENT_OS_NAME == "Linux" ]; then
        echo "Running on ARM and Linux"
    else
        echo "Not running on ARM and Linux -> scripts exits immediately"
        exit
    fi
}

# Install Python 3
function InstallPython {
    # install python 3
    sudo apt-get -y install python3
    # install python package index (should be included by default)
    sudo apt-get -y install python3-pip
}

# Sync local workspace files with Raspberry Pi
function SyncWorkspace {
    echo "Synchronizing local workspace files with Raspberry Pi..."
    rsync -av --no-perms --omit-dir-times --progress --exclude=__*__ --exclude=.* ../python_template pi@icpi:~/
}

# Launch main python process through ptvsd for remote debugging
function LaunchMainWithDebugger {
    echo "Launching main python process through ptvsd for remote debugging..."
    cd ~/python_template/source
    python3 -m ptvsd --host icpi.local --port 3000 -m main --debug
}

# Sync and then launch debug through ssh from host
function Sync2Debug {
    echo "Sync2Debug..."
    SyncWorkspace
    ssh pi@icpi.local python_template/scripts/launch.sh debug
    echo "End of remote debugging session."
}

# Check if an argument was provided
if [ -z "$1" ]; then
    PrintArgumentsHelp
    exit
fi

# Evaluate command line arguments and run desired function
if [ $1 = "info" ]; then
    PrintOSInfo 
elif [ $1 = "python" ]; then 
    PrintOSInfo
    InstallPython
elif [ $1 = "sync" ]; then 
    PrintOSInfo
    SyncWorkspace
elif [ $1 = "debug" ]; then 
    PrintOSInfo
    LaunchMainWithDebugger
elif [ $1 = "sync2debug" ]; then 
    PrintOSInfo
    Sync2Debug
else
    PrintArgumentsHelp
    exit
fi
