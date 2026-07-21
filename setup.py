'''
the setup.py file is an essential part of packaging and distributing 
python projects. it is used by setuptools to define the 
configuration of your project , such as its metadata , 
and more
'''

from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    ''''
    this function will return the list of requirements
    '''

    lines_list=[]
    try:
        with open('requirements.txt') as file:
            # read the requirements from the file and return them as a list
            lines=file.readlines()
            #process each line
            for line in lines:
                line=line.strip()
                #remove any empty lines or comments
                if line and not line.startswith("-e"):
                    lines_list.append(line)

    except FileNotFoundError:
        print("requirements.txt file not found .")    

    return lines_list           

print(get_requirements())


setup(
    name="your_package_name",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements(),
    author="sharadborde",
    author_email="bordesharad9@gamil.com"

)
