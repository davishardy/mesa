"""
Module to create all elements
"""

import os
import json
import argparse

class Create:
    def __init__(self):
        """
        Initialize create object
        """
        # Create variable for the templates directory
        self.tempalte_dir = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, "templates"))
        
        # Environment variables
        self.name = os.getenv("show")
        self.root = os.getenv("show_root")


    def _parse_json(self, template):
        """
        Parse a json file base on the element requested from it
        """
        pass


    def _create_dirs(self, paths):
        """
        Create desired paths
        """
        pass


    def show(self, show_name):
        """
        Creates a show folder for assets and sequences to be populated with
        Input = show_name
        Output = None
        """

        # Creates show directory if it hasn't been created 
        if not os.path.exists(self.root):
            os.mkdir(self.root)
        else:
            print("Show folder exists")

        # Create global asset folders based on json file
    
    def sequence(self, seq_name):
        """
        Creates sequence if not present
        Input = sequence name string
        Output - None
        """
        pass

    def shot(self, shot_name):
        """
        Creates shot if not present
        Input = shot name string
        Output - None
        """
        pass



# Example of using methods within the same class - from mr.gpt
"""
class MyClass:
    def __init__(self, data):
        self.data = data

    # Public method that calls helper methods
    def process_data(self):
        cleaned_data = self._clean_data(self.data)
        transformed_data = self._transform_data(cleaned_data)
        print(f"Processed data: {transformed_data}")

    # Private helper method for cleaning data
    def _clean_data(self, data):
        # Assume data is a list, this removes any empty elements
        return [item for item in data if item]

    # Private helper method for transforming data
    def _transform_data(self, data):
        # Example transformation: converting all strings to uppercase
        return [item.upper() for item in data]

# Example usage
my_instance = MyClass(["hello", "", "world"])
my_instance.process_data()

"""