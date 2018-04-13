from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))
# get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='ml',
    version='0.0.1',
    description='Collection of Computer Science and Machine Learning algorithms implemented in Python',
    long_description=long_description,
    packages=find_packages(exclude=['tests']),
)
