from setuptools import setup, find_packages
from typing import List
# This is the setup file for the machine learning project.


def get_requirements(file_path:str) -> list:
    """
    This function will return the list of requirements
    """
    requirements: List[str] = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements


setup(
    name="ml project"
    ,version="0.1.0"
    ,author="Satyam Kumar",
    author_email="Satyam00043@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt'),

    
)