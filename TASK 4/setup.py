#!/usr/bin/python3

import setuptools

import mocknet


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="Mocknet",
    version=mocknet.__version__,
    description=mocknet.__doc__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lucas Schneider",
    author_email="schneider8357@hotmail.com",
    url="https://github.com/schneider8357/mocknet",
    packages=["mocknet"],
    python_requires=">=3.8",
)
