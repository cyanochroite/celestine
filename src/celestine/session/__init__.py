"""Celestine Image Viewer"""
"""Load and save user settings from a file."""

import sys
import configparser


from celestine.core import load





from celestine.session.configuration import Configuration
from celestine.session.parser import Parser


class Session():
    def __init__(self, directory):
        self.directory = directory

#        self.configuration = Configuration(directory)

        self.config = Configuration(directory)
        self.configuration = self.config.load(directory)

        try:
            self.application = sys.argv[1]
        except IndexError:
            print("hack and bad default?")
            sys.argv.append("tkinter")
            self.application = sys.argv[1]

        self.window = load.module("window", "main")



    def figtree(self, configuration, application):
        """Build up the configuration file."""
        module = load.module("application", application)
        configuration.configuration.add_section(application)
        configuration = module.configuration(configuration)
        configuration.configuration.set(application, "task", "main")
        return configuration
    
    
        
    
    def main(self):
        root = load.module("application")
        module = load.module("application", self.application)

        argument = root.argument()
        self.argument = module.argument(argument)

        configuration = root.Configuration(self.directory)
        self.configuration = configuration.load()
        
        default = root.configuration(self.directory)
        default = self.figtree(default, "terminal")
        default = self.figtree(default, self.application)
        self.default = default
        
        self.parser = Parser()

        temargument = self.parser.parse(self)

        self.module = load.module("application", self.application, self.task)
        return self.module.main(self)

