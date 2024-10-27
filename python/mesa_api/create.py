"""
Module to create all elements
"""

import os
import json

class Create:
    """
    Class that helps you create shows, sequences, shots, and elements
    """
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

    def _load_template(self, template_name):
        """
        Loads a json template
        Input = name of template without the .json extension
        Output = Data structure within json file
        """
        template_file = template_name + ".json"
        template_path = os.path.join(self.template_dir, template_file)

        if os.path.exists(template_path):
            with open(template_path, 'r') as file:
                folder_structure = json.load(file)
                return folder_structure
        else:
            print("File does not exist")


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


    def show(self) -> None:
        """
        Creates a show folder for assets and sequences to be populated with
        Input = Show name
        Output = None
        """

        if not os.path.exists(self.root):
            show_template = self._load_template("show")
            self.create_asset(os.path.abspath(os.path.join(self.root, os.pardir)), "show_root", show_template)
        else:
            print("Show exists")

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
            sequence_template = self._load_template("sequence")

        else:
            print("Sequence Exists")
        '''
        pass
        # End sequence


    def shot(self, seq_name: str, shot_name: str) -> None:
        """
        Creates shot if not present
        Input = shot name string
        Output = None
        """
        '''
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
        '''
        pass
        # End shot