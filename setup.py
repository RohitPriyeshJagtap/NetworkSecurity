from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    Tis function will return lit of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt",'r') as file:
            # Read line from the file 
            lines= file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e.':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst 


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Rohit Jagtap",
    author_email="jagtaprohit005011999@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)