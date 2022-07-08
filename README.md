# Server Control Utility

A Generic Server Management and Controller Utility with both CLI and GUI Interfaces 

## Information

As mentioned, this is a Generic Server Management and Controller Utility that is designed for both sysadmin general users and power users alike.

Contains both CLI and GUI Interfaces, both interfaces has features that allows for scripting capabilities.


## Setup

### Dependencies

- python
- pip
- tkinter (Temporarily while it uses tkinter as the GUI famework)
- pyinstaller (Optional; For Compiling)

### Obtaining

git clone https://github.com/hack-parthsharma/ServerControl.git

### Installing/Compiling

```
Still a WIP
```

python -m pyinstaller --one-file {options} main.py

## Documentation

### Synopsis/Syntax

python main.py {options}

### Parameters/Arguments

+ --cli : Starts in CLI Mode
+ --gui : Starts in GUI Mode
+ -c | --clean : Format Standard Output for Terminal/CLI scripting use
+ -cfg | --config <new-config-file> : Specify path to new config file
+ -h | --help : Displays this Help message
+ -v | --version : Displays the program's version and relevant information

### Usage

+ Format and start program in a mode
    - CLI Mode
        ```console
        python main.py --clean --cli
        ```
    - GUI Mode
        ```console
        python main.py --clean --gui
        ```

+ (WIP) Output to standard output and clipboard with xclip
    ```console
    echo "$(python main.py --clean --cli)" | xclip -sel clip
    ```

