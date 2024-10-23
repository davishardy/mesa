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
        self.template_dir = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, "templates"))
        
        # Environment variables
        self.name = os.getenv("show")
        self.root = os.getenv("show_root")
        self.show_id = self.name[0]

        # End __init__


    def _parse_template(self, template_name: str, template_type: str, ) -> list:
        """
        Parse a json file base on the element requested from it
        Input =  Template keyword
        Output = List of folder names
        """
        # Load json file
        with open(os.path.join(self.template_dir, template_name), "r") as file: # Maybe replace with a system path
            templates = json.load(file)

        if template_type in templates:
            target_template = templates[template_type]
            return target_template

        # End _parse_template


    def _create_dir(self, path: str) -> None:
        """
        Create desired paths
        Input = path of desired folder
        Output = None
        """
       # Checks if folder is present, creates if not present
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print(f"Folder exists:\n{path}\n")

        # End _create_dir


    def _create_empty(self, filepath: str) -> None:
        """
        Creates an empty file for use later in the pipeline
        Input = File path including the name
        Output = None
        """
        try:
            if os.path.exists(filepath) == False:  # Check if file exists
                with open(filepath, 'w') as file:  # Create file
                    pass
        except FileExistsError:
            # Report if file exists already
            print(f"{filepath} exists already")

        # End _create_empty


    def show(self) -> None:
        """
        Creates a show folder for assets and sequences to be populated with
        Input = Show name
        Output = None
        """

        # Creates show directory if it hasn't been created 
        if not os.path.exists(self.root):
            os.mkdir(self.root)
        else:
            print("Show folder exists")

        # Create global asset folders based on json file
        for dir in self._parse_template("base_template.json", "show"):
            self._create_dir(os.path.join(self.root, dir))

        # End show

    
    def sequence(self, seq_name: str) -> None:
        """
        Creates sequence if not present
        Input = sequence name string without any prefixes
        Output = None
        """
        # Find active sequences
        active_seqs = [seq_dir for seq_dir in os.listdir(self.root) if os.path.isdir(os.path.join(self.root, seq_dir)) and seq_dir.startswith(self.show_id)]  # Find sequences in the project

        # Adds first letter of show prefix to the sequence number
        prefixed_sequence = f"{self.show_id}{seq_name}"


        if prefixed_sequence not in active_seqs:
            # Creates sequence directory
            os.mkdir(os.path.join(self.root, prefixed_sequence))
            # Creates directories within sequence directory based off template
            for dir in self._parse_template("base_template.json", "sequence"):
                self._create_dir(os.path.join(self.root, prefixed_sequence, dir))

        else:
            print("Sequence Exists")

        # End sequence


    def shot(self, seq_name: str, shot_name: str) -> None:
        """
        Creates shot if not present
        Input = shot name string
        Output = None
        """
        # Find existing shots in folder
        prefixed_sequence = f"{self.show_id}{seq_name}"
        prefixed_shot = f"{self.show_id}{seq_name}_{shot_name}"

        active_shots = [shot for shot in os.listdir(os.path.join(self.root, prefixed_sequence)) if os.path.isdir(os.path.join(self.root, prefixed_sequence, prefixed_shot)) and prefixed_shot.startswith(self.show_id)]

        if prefixed_shot not in active_shots:
            # Creates sequence directory
            os.mkdir(os.path.join(self.root, prefixed_sequence, prefixed_shot))
            # Creates directories within sequence directory based off template
            for dir in self._parse_template("base_template.json", "shot"):
                self._create_dir(os.path.join(self.root, prefixed_sequence, prefixed_shot, dir))

        else:
            print("Shot Exists")

        # End shot
    

    def create_asset(self, asset_path, asset_name, structure):
        """
        Creates folder from a json template
        Input = path to asset, asset name, json template
        Output = None
        """

        # Create folders and iterate through contents
        if structure['type'] == 'folder':
            replaced_name = structure["name"].replace("placeholder", asset_name)
            
            folder_path = os.path.join(asset_path, replaced_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            print(f"Folder created: {folder_path}")
        
            # Recursively create contents
            for content in structure.get('contents', []):
                self.create_asset(folder_path, asset_name, content)
            
    
        # Create files
        elif structure['type'] == 'file':
            replaced_name = structure["name"].replace("placeholder", asset_name)
            file_path = os.path.join(asset_path, replaced_name)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    pass
                print(f"File created: {file_path}")
        