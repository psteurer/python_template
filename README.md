# Python 3 Template

Simple template for python 3 main to start your application.

It supports remote debugging and logging that can be enabled using command line arguments. The source code is documented with docstrings in reStructured text.

## Copy Sources to Raspberry Pi

You can use rsync to synchronize your project with the Raspberry Pi, and then run it from there.

```bash
# synchronize local project folder with remote folder on Raspberry Pi
rsync -av --no-perms --omit-dir-times --progress --exclude=__*__ --exclude=.* ../python_template pi@icpi:~/

# connect to Raspberry Pi
ssh pi@icpi

# run the scripts as you desire
python3 ~/python_template/main.py
```

If desired, you can add the secure copy command as a task to your Visual Studio Code and assign a keyboard shortcut.

## References

[1] [Python Tutorial, w3schools](https://www.w3schools.com/python/)

[2] [Getting Started with Python, Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial) 

[3] [Documenting Python Code: A Complete Guide, realpython](https://realpython.com/documenting-python-code/) 

[4] [Logging in Python, realpython](https://realpython.com/python-logging/) 

[5] [Getting Started With Testing in Python, realpython](https://realpython.com/python-testing/) 