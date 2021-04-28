"""
Module to setup Phonic on a local machine.

"""
# Standard Imports.
from setuptools import find_packages, setup

setup(
    name="phonic",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "marshmallow",
        "flask-marshmallow",
        "marshmallow-sqlalchemy"
    ]
)
