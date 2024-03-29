from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT='-e .'
# return type of the this function is list and  this file returns the list of the requirments

def get_requirements(path)->List[str]:
    
    # get the files from the requirement.txt and install it
    with open("requirements.txt",'r') as f:
        requirements=f.readlines()
        
    # removing the line changer from the requirements 
    requirements=[req.replace('/n','') for req in requirements]
    
    # if the files read the -e . remove that 
    if '-e .' in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements
    
    




setup(
    name='ml_project',
    version='0.0.1',
    author="khuma pokharel",
    author_email='khumapokharel2076@gmail.com',
    packages=find_packages(),
    
    # it is hard to give the all the package name so we will take it from the requirements.txt file
    install_requires= get_requirements('requirements.txt'),
)