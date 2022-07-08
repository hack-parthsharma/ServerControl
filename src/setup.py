"""
Setup Script
"""

import os
import sys

class Settings():
    def __init__(self, PROG_NAME, PROG_VERS, PROG_CONFIG_PATH, PROG_AUTHOR):
        # Constructor
        self.init(PROG_NAME, PROG_VERS, PROG_CONFIG_PATH, PROG_AUTHOR)

    def init(self, PROG_NAME, PROG_VERS, PROG_CONFIG_PATH, PROG_AUTHOR):
        """
        Initialize settings
        """
        # global PROG_NAME, PROG_VERS, PROG_CONFIG_PATH
        self.PROG_NAME = PROG_NAME
        self.PROG_VERS = PROG_VERS
        self.PROG_CONFIG_PATH = PROG_CONFIG_PATH
        self.PROG_AUTHOR = PROG_AUTHOR

    def set_prog_name(self, PROG_NAME):
        self.PROG_NAME = PROG_NAME

    def get_prog_name(self):
        return self.PROG_NAME

    def set_prog_vers(self, PROG_VERS):
        self.PROG_VERS = PROG_VERS

    def get_prog_vers(self):
        return self.PROG_VERS

    def set_prog_config_path(self, PROG_CONFIG_PATH):
        self.PROG_CONFIG_PATH = PROG_CONFIG_PATH

    def get_prog_config_path(self):
        return self.PROG_CONFIG_PATH

    def set_prog_author(self, PROG_AUTHOR):
        self.PROG_AUTHOR = PROG_AUTHOR

    def get_prog_author(self):
        return self.PROG_AUTHOR
