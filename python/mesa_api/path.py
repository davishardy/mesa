"""Module to evaluate paths"""

import os

class Path:
    """
    Class that helps to evaluate paths
    """
    def __init__(self):
        """
        Create Path Object
        """
        self.name = os.getenv("show")
        self.root = os.getenv("show_root")
        self.show_id = self.name[0]
        self.seqs = []
        # print(f"Show name = {self.name}\nLocation = {self.root}")


    # Get seq path
    def find_sequences(self):
        """
        Finds all sequences in the project and updates the class variable "seqs"
        Input = None
        Output = None
        """

        try:
            self.seqs = [seq_dir for seq_dir in os.listdir(self.root) if os.path.isdir(os.path.join(self.root, seq_dir)) and seq_dir.startswith(self.show_id)]
        except ValueError:
            print(f"Current show directory does not exist!\nShow directory = {self.root}")

    def find_shots(self, seq):
        """
        Finds all shots in the sequence and returns them as a list
        Input = Sequence string
        Output = List of shot strings
        """
        # Create path to sequence
        sequence_dir = os.path.join(self.root, seq)
        print(sequence_dir)
        print(os.listdir(sequence_dir))
        # Get all shots within the sequence ---------------- not working
        sequence_shots = [shot_dir for shot_dir in os.listdir(sequence_dir) if os.path.isdir(os.path.join(sequence_dir, shot_dir)) and shot_dir.startswith(sequence_dir)]
        
        return sequence_shots
