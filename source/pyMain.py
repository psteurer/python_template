"""
Simple template for python 3 main that can be used to start your application.

Enables remote debugging if corresponding argument is specified. 
Afterwards, calls module(s).
"""

import pyModule

def remote_debug():
    """Enable remote debugging using the Visual Studio Debugger engine provided by Microsoft."""
    import ptvsd

    # Allow other computers to attach to ptvsd at this IP address and port.
    ptvsd.enable_attach(address=('localhost', 3000), redirect_output=True)
    # Pause the program until a remote debugger is attached
    ptvsd.wait_for_attach()
        
def main():
    """Evaluate and execute command line arguments, and then call modules."""
    import argparse
  
    # Check if remote debugging was specified on the command line
    parser = argparse.ArgumentParser(description="Application does do this and that ;-)")
    parser.add_argument("-d", "--debug", help="allow other computers to attach for debugging using ptvsd", action="store_true")
    args = parser.parse_args()
    if args.debug:
        print("Remote debugging enabled. Pausing until remote debugger is attached...")
        remote_debug()

    # Add entry point for your program below
    print("Launching program.")
    pyModule.greeting()
    pyModule.greeting("Philipp")

# execute only if run as a script
main()