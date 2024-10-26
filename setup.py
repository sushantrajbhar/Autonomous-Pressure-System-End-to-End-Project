from setuptools import find_packages, setup
from typing import List

# the below function returns a list of strings.
def get_requirements() -> List[str]:
    requirements_list: List[str] = []
    return requirements_list

setup(
    name='Autonomous pressure system',
    version="0.0.1",
    author="Sushant",
    author_email="sushraj44@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
