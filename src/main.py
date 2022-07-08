"""
Generic System/Server Monitoring Control Utility
"""

# Import Internal Libraries
import os
import sys
import json

# Import Dependencies
import setup
import lib.gui.gui_interface as gui_interface

### Get Command Line Arguments ###
argv = sys.argv
script_name = argv[0]
argv = argv[1:] # Take all arguments past the 1st (Script)
argc = len(argv)

# Variables #
options = {
    "Config" : {
        "description" : "Specify an alternate config path",
        "arguments" : ["-cfg", "--config"],
    },
    "Clean" : {
        "description" : "Format Standard Output for Terminal/CLI scripting use",
        "arguments" : ["-c", "--clean"],
    },
    "CLI-Mode" : {
        "description" : "Start in Terminal Mode",
        "arguments" : ["--cli"],
    },
    "GUI-Mode" : {
        "description" : "Start in GUI Mode",
        "arguments" : ["--gui"],
    },
    "Help" : {
        "description" : "Displays this Help menu",
        "arguments" : ["-h", "--help"],
    },
    "Version" : {
        "description" : "Prints the version and author",
        "arguments" : ["-v", "--version"]
    }
}

to_run = {} # List of things to run
variables = {} # Variables for use

# Functions #

def run_cli():
    """
    Start in CLI Mode
    """
    if not ("Clean" in variables):
        print("Starting in CLI...")
    print("Hello World") # Print test here to simulate standard output manipulation for CLI/Terminal Scripting uses

def run_gui():
    """
    Start in GUI Mode
    """
    if not ("Clean" in variables):
        print("Starting in GUI...")
    App = gui_interface.App() 
    root = App.app
    print("Hello World") # Print test here to simulate standard output manipulation for CLI/Terminal Scripting uses
    App.start_app(root)

def help_menu():
    """
    Help Menu
    """
    for k,v in options.items():
        curr_opt_fullname = k
        curr_opt_description = v["description"]
        curr_opts = v["arguments"]

        print("{} : {}".format(curr_opt_fullname, curr_opt_description))
        print("\tOptions:")
        for i in range(len(curr_opts)):
            curr_opt = curr_opts[i]
            print("\t\t{}".format(curr_opt))

def version():
    """
    Display Version
    """
    print("Version : {}".format(PROG_SETUP.get_prog_vers()))
    print("Made by : {}".format(PROG_SETUP.get_prog_author()))

def init():
    """
    PROG_NAME = "Server Controller Utility"
    PROG_VERS = "v0.1.0" # major.minor.patch-state
    PROG_CONFIG_PATH = "~/.config/serverctrl/config.json"
    """
    global PROG_SETUP
    PROG_SETUP = setup.Settings("Server Controller Utility", "v0.2.0", "~/.config/serverctrl/config.json", "Asura (https://github.com/Thanatisia]")

def main():
    # to_run = [] # List of things to run

    # Get Functions & Variables
    if argc > 0:
        # Arguments Provided
        # for i in range(argc):
        i = 0
        while i < argc:
            # print("{} : {}".format(i, argv[i]))
            curr_arg = argv[i]

            """
            Structure:
                to_run[label] : The name of the function to run
                to_run[label]["Function"] : The Function Object
                to_run[label]["Return-Type"] : The Function Return Type
                    Options:
                        - void : No Return
                        - int : Integer return type
                        - string : String/Text return type
                        - float/real : Floating point numbers
                        - bool : Boolean True/False values
                        - blob : Image/Object type
                to_run[label]["Input" : The Argument/Parameter to pass into the function
            """
            if curr_arg == "--help" or curr_arg == "-h":
                if not ("Help" in to_run):
                    label = "Help"
                    to_run[label] = {}
                    to_run[label]["Function"] = help_menu
                    to_run[label]["Return-Type"] = "void"
                    to_run[label]["Input"] = None
            elif curr_arg == "--version" or curr_arg == "-v":
                if not ("Version" in to_run):
                    label = "version"
                    to_run[label] = {}
                    to_run[label]["Function"] = version
                    to_run[label]["Return-Type"] = "void"
                    to_run[label]["Input"] = None
            elif curr_arg == "--clean" or curr_arg == "-c":
                if not ("Clean"  in to_run):
                    variables["Clean"] = True
            elif curr_arg == "--cli":
                if not ("CLI-Mode" in to_run):
                    label = "CLI-Mode"
                    to_run[label] = {}
                    to_run[label]["Function"] = run_cli
                    to_run[label]["Return-Type"] = "void"
                    to_run[label]["Input"] = None
            elif curr_arg == "--gui":
                if not ("GUI-Mode" in to_run):
                    label = "GUI-Mode"    
                    to_run[label] = {}
                    to_run[label]["Function"] = run_gui
                    to_run[label]["Return-Type"] = "void"
                    to_run[label]["Input"] = None
            elif curr_arg == "-cfg" or curr_arg == "--config":
                # Choose Config Path
                if not ("Config" in to_run):
                    label = "Config"
                    to_run[label] = {}
                    to_run[label]["Function"] = PROG_SETUP.set_prog_config_path
                    to_run[label]["Return-Type"] = "void"

                    if not ((i+1) >= argc):
                        to_run[label]["Input"] = argv[i+1]
        
                        # Skip next argument
                        # Next argument is the input to the parameter
                        i = i+1
                    else:
                        # Reached the end, no config path specified
                        to_run[label]["Input"] = None
                        print("No Config Path specified.")
            else:
                print("Invalid Argument [{}]" .format(curr_arg))
                label = "Invalid"
                to_run[label] = {}
                to_run[label]["Function"] = help_menu
                to_run[label]["Return-Type"] = "void"
                to_run[label]["Input"] = None
                break

            # Increment by 1 after each loop
            i = i+1

    else:
        # No Arguments Provided
        # Display Help Menu
        help_menu()


    # Validation Check - Only run if valid
    if not ("Invalid" in to_run.keys()):
        # print("To Run : ")
        for label, val in to_run.items():
            # print("\t{} : {}".format(label, val))
            """
            if not ("Clean" in variables.keys()):
                print("====")
                print("{}".format(label))
                print("====")
            """

            func = val["Function"]
            u_Arg = val["Input"]
            if(not(u_Arg == None)):
                # If Argument is not empty
                func(u_Arg) 
            else:
                func()

            """
            if len(to_run) > 1:
                if not ("Clean" in variables.keys()):
                    print("")
            """

if __name__ == "__main__":
    init()
    main()

