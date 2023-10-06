import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Aadhar Masking"
list_of_files = [
    ".github/workflows/.gitkeep", ## keeps empty files
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "dvc.yaml",
    "param.yaml",
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb', ## notebook experiments
    'README.md',
]

for file_path in list_of_files:
    file_path = Path(file_path) ## windows uses \\ while python takes / 
    ## return windows path for a linux path type
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir != "": ## it's a directory

        os.makedirs(file_dir, exist_ok=True) ## TRUE means, creates only if doesn't exist
        logging.info(f'Creating directory {file_dir} for the file {file_name}')
    
    ## Now we need to create the file
    if(not os.path.exists(file_path) or os.path.getsize(file_path)==0):
        ## if file doens't exist or if the file doesn't have anything in it
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating an empty file {file_path}")
    else:
        logging.info(f'File {file_path} already exists')

