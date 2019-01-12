# Python 3 Template

Simple template for python 3 main to start your application.

It supports remote debugging and logging. Both can be enabled using command line arguments. The source code is documented with docstrings in reStructured text.

## Copy sources to Raspberry Pi and run Python program

You can use rsync to synchronize your project with the Raspberry Pi, and then run it from there.

```bash
# synchronize local project folder with remote folder on Raspberry Pi
rsync -av --no-perms --omit-dir-times --progress --exclude=__*__ --exclude=.* ../python_template pi@icpi:~/

# connect to Raspberry Pi
ssh pi@icpi

# run the python programs as you desire
cd ~/python_template/source
python3 main.py
```

If desired, you can add the rsync command as a task to your Visual Studio Code and assign a keyboard shortcut.

### Using remote debugger

If you want to remotely debug your python program, you need to launch it using the following command on the Raspberry Pi.

```bash
# run the python programs as you desire
cd ~/python_template/source
python3 -m ptvsd --host icpi.local --port 3000 -m main --debug
```

Once the program is ready for the remote debugger, you can use Visual Studio Code to attached the debugger to the python program running on your Raspberry Pi. For more information, look at [remote debugging python with Visual Studio Code](https://code.visualstudio.com/docs/python/debugging#_remote-debugging).

## Script for launching commands

The above steps are also available in the script *script/launch.sh* that provides several options through command line arguments.

## References

[1] [Python Tutorial, w3schools](https://www.w3schools.com/python/)

[2] [Getting Started with Python, Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial) 

[3] [Documenting Python Code: A Complete Guide, realpython](https://realpython.com/documenting-python-code/) 

[4] [Logging in Python, realpython](https://realpython.com/python-logging/) 

[5] [Getting Started With Testing in Python, realpython](https://realpython.com/python-testing/) 