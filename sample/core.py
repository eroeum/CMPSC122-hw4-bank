import sys
import terminalInterface as ti

version = '0.1'

def main(arg):
    """
    Runs the core of the program
    Integrates all other python scripts/modules
    Use the core.py to run the Bank python script

    :type arg: list
    :param arg: list of arguments in terminal
    """

    # Displays terminal based application
    if('--no-gui' in arg or '-t' in arg):
        ti.displayInterface()

if __name__ == '__main__':
    main(sys.argv[1:])
