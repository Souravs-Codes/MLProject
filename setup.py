from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:

    '''
    this function will return the list from requirements.txt
    '''

    E_Dot='-e.'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements] #Replacing \n with blank in requiements.txt
        if E_Dot in requirements:
            requirements.remove(E_Dot)
    return requirements

        

setup(
    name = 'MLProject',
    version='0.0.1',
    author='SAMMY',
    author_email='souravmukherjee1584@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)