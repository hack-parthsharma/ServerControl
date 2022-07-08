"""
GUI Interface Design
"""

### Import Libraries ###

# Built-in Libraries
import os
import sys

# Dependencies
import tkinter as tk

class App():
    """
    Application class
    """
    def __init__(self):
        # Generate Application root window
        self.app = self.gen_root()

    def gen_root(self, root_params=None):
        if root_params == None:
            root = tk.Tk()
        else:
            root = tk.Tk(root_params)
        return root

    def start_app(self, app, start_params=None):
        if start_params == None:
            app.mainloop()
        else:
            app.mainloop(start_params)
