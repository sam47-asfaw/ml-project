from setuptools import find_packages, setup 
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(filepath:str)-> List[str]:
    '''
    This function will return list of requirements
    '''
    requirements=[]
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [rq.replace("\n", "") for rq in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements
    



setup(
    name='mlproject',
    version='0.01',
    author ='Sam',
    author_email='sami.asfaw47@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt'),

)