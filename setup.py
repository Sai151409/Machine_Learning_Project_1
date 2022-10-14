from xml.etree.ElementPath import find
from setuptools import setup, find_packages
from typing import List


#Declaring Variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Sai Ram"
DESCRIPTION = "This is the first fsds nov batch Machine Learning Project"
REQUIREMENTS_FILE_NAME = "requirements.txt"
 
def get_requirements_list()->List[str]:
    """
    Description :  This function is going returns the list of requirements 
    mention in the requirements.txt file
    
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove('-e .')   


setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
packages = find_packages(), #['housing']
install_requires = get_requirements_list()
)
