from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str = 'requirements.txt')->List[str]:
    """
    This function returns the list of requirements 
    """
    with open(file_path) as f :
        requirements = f.readlines()
        req_list = [requirement.replace("\n"," ") for requirement in requirements ]
    if HYPEN_E_DOT in requirements: 
        req_list.remove(HYPEN_E_DOT)
    return req_list
setup(
    name = 'ml_project',
    version = '0.0.1',
    author='JMAL Yessine',
    author_email='yessinejmal.prepa@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),
) 