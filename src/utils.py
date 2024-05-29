"""Utils functions"""

import os

def check_and_delete_file_if_exists(file_path):
    """Helper function to check and delete and file if exists"""
    if os.path.exists(file_path):
        os.remove(file_path)
        