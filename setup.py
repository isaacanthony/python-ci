"""setup.py"""
from setuptools import setup, find_packages

setup(
    name="python-ci",
    version="0.0.1",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().strip().split("\n"),
)
