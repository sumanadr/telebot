import os
import yaml as _yaml


def get_config():
    
    with open('./config.yml') as config_file:
        return _yaml.load(config_file)