"""
While in the root directory run "pip install -e .".
This will install Battleship as a package, and create the models and datasets directory.
"""

from setuptools import find_packages, setup
import os

setup(name='Battleship', version='1.0', packages=find_packages())