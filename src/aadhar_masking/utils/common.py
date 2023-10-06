import os
from box.exceptions import BoxValueError
import yaml
from aadhar_masking import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

def decode_image(img, file):
    img_data = base64.b64decode(img)
    with open(file,'wb') as f:
        f.write(img_data)
        f.close()

def encode_image(img):
    with open(img, 'rb') as f:
        return base64.b16encode(f.read())
    

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'Yaml File at {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml File is Empty!!")
    except Exception as excp:
        return excp
    

@ensure_annotations
def create_directories(path_to_dirs : list, verbose = True):
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Created directory at {path}')


@ensure_annotations
def save_json(path : Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f'JSON File saved at {path}')