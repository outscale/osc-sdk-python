# -*- coding: utf-8 -*-
import setuptools
import os

def get_long_description():
    root_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root_path, 'README.md'), 'r') as fd:
        return fd.read()

def get_version():
    root_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root_path, 'osc_sdk_python', 'VERSION'), 'r') as fd:
        return fd.read().strip()

setuptools.setup(
    name='osc_sdk_python',
    version=get_version(),
    author="Outscal SAS",
    author_email="opensource@outscale.com",
    description="Outscale Gateway python SDK",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/outscale/osc_sdk_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests>=2.20.0',
        'ruamel.yaml==0.17.21'
    ]
)
