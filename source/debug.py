# Python 3 program to start your application.
# Evaluates arguments if remote debugging is specified and 
# provides startup code that enables remote debugging.

def remote_debug():
    import ptvsd

    # Allow other computers to attach to ptvsd at this IP address and port.
    ptvsd.enable_attach(address=('localhost', 3000), redirect_output=True)
    # Pause the program until a remote debugger is attached
    ptvsd.wait_for_attach()

def info():
    msg = "Hello, World!"
    print(msg)

    a = 5
    b = 6
    sum = a + b
    print("The sum of", a, "and", b, "is", sum) 
    
def main():
    import argparse

    # Check if remote debugging is specified
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="allow other computers to attach for debugging using ptvsd", action="store_true")
    args = parser.parse_args()
    if args.debug:
        print("Remote debugging enabled. Pausing until remote debugger is attached...")
        remote_debug()

    print("Launching program.")

# execute only if run as a script
main()