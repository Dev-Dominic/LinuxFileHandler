#!/usr/bin/env python

# Modules

import os
import sys

def get_file_extensions(folder_path):
    """Parses and returns unique list of file extensions 

    Args:
        folder_path: system path to folder to be parsed

    Return: 
        extensions: dictionary containing keys with list of values representing
        files associated with given extension(key)

    """
    extensions = {} 
    for _file in os.listdir(folder_path):
        filepath = os.path.join(folder_path, _file)

        # Ensures that only files with extensions are included 

        if not os.path.isfile(filepath): 
            continue

        ext = _file.split('.')[-1]
        if not ext in extensions: # Stops duplicate entries
            extensions[ext] = [(_file, filepath)]
        else: 
            extensions[ext].append((_file, filepath))
    return extensions

def create_ext_folders(folder_path, extensions):
    """Creates extension folder in a given folder path
    
    Args: 
        folder_path: system path to folder to be parsed
        extensions: dictionary containing keys with list of values representing

    """
    for ext_folder in extensions.keys(): 
        try: 
            os.mkdir(os.path.join(folder_path, ext_folder))
        except FileExistsError: 
            print(f'{ext_folder} already exists')

def reorganize(folder_path, extensions):
    """Reorganizes files into extension folders

    Args:
        folder_path: system path to folder to be parsed
        extensions: dictionary containing keys with list of values representing

    """
    for key,value in extensions.items():
        for _file_tuple in value:
            # Creates new filepath for specific associated files of the key
            # The _file_tuple[0] represents just the file name of a given file
            # _file_tuple[1] represents the full file path

            new_filepath = os.path.join(folder_path, key, _file_tuple[0]) 
            os.rename(_file_tuple[1], new_filepath)

if __name__ == '__main__':
    folder_path = '/home/dominic/Downloads'
    extensions = get_file_extensions(folder_path)
    create_ext_folders(folder_path, extensions)
    reorganize(folder_path, extensions)
