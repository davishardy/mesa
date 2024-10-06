# mkutils.py
# Version 1.0.0
# 2024-10-5
# Davis Hardy

# Utilities for make scripts

# Import Modules
import os
import sys


def get_show():
    '''
    Retrieves the current show from an environment variable named "show"
    Inputs : None
    Outputs : Name of current show, path to current show
    '''
    try:
        show_name = os.getenv("show_name")
        show_root = os.getenv("show_root")
        return show_name, show_root
    except OSError:
        print("Show name or show root not found")


def get_seqs():
    '''
    Retrives the current sequences in a show
    Inputs : None
    Outputs : list of sequences in show
    '''

    show_name, show_root = get_show()
    show_folders = os.listdir(os.path.join(show_root, "show"))
    seqs = [folder for folder in show_folders if "mod" not in folder]

    return seqs


def get_input():
    '''
    Processes the input from the command line
    Inputs : None
    Outputs : list of arguments from command line
    '''
    cli_input = sys.argv
    cli_input.pop(0)

    return cli_input
