from setuptools import setup, find_packages
from os.path import join, dirname

import languagebind

setup(
    name='languagebind',
    version=languagebind.__version__,
    packages=find_packages(),
)