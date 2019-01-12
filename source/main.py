"""Simple template for python 3 main to start your application.

Enables remote debugging if corresponding argument is specified.
Afterwards, calls module(s).

Requires the following python packages to be installed:
ptvsd: for remote debugging.
"""

import module


def remote_debug():
    """Enable remote debugging using Visual Studio Debugger engine."""
    import ptvsd

    # Allow other computers to attach to ptvsd at this IP address and port.
    ptvsd.enable_attach(address=('localhost', 3000), redirect_output=True)
    # Pause the program until a remote debugger is attached
    ptvsd.wait_for_attach()


def main():
    """Evaluate command line arguments, then call modules."""
    import logging
    import argparse

    log = logging.getLogger(__name__)

    # Check if remote debugging was specified on the command line
    parser = argparse.ArgumentParser(description="Application does something.")
    parser.add_argument("-d", "--debug",
                        help="enable remote debugging using ptvsd",
                        action="store_true")
    parser.add_argument("-l", "--log",
                        dest="logLevel",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help="log to stdout and set logging level.")
    args = parser.parse_args()
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    if args.logLevel:
        print("Logging to stdout enabled.")
        logging.basicConfig(level=getattr(logging, args.logLevel), format=log_format)
    if args.debug:
        print("Remote debugging enabled. Attach debugger to continue...")
        logging.basicConfig(level=logging.DEBUG, format=log_format)
        remote_debug()

    # Add entry point for your program below
    log.info("This is an info message.")
    log.debug("This is a debug message.")
    print("Launching program.")
    module.greet()
    module.greet("User")

    Greeter = module.SimpleClass("Guru")
    Greeter.say_hello("Developer")

# Main executes only if run as a script
main()
