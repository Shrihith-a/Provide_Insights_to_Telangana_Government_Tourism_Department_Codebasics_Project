from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)-> List(str):
    '''
    This function will return list of requirements from requirements.txt file
    '''
    # initializing blank requirements list
    requirements = []

    # opening requirements.txt file
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        # Renove hyphen_e-Dot if present in requirements
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="Provide_Insights_to_Telangana_Government_Tourism_Department",
    version="0.0.1",
    author="Shrihith Anantharam",
    author_email="ashrihith93@gmail.com",
    description="Provide_Insights_to_Telangana_Government_Tourism_Department",
    packages = find_packages(),
    install_requires=get_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Tourism",
        "Topic :: Tourism :: Tourism Apps"
    ]

)

    