# -*- coding: utf-8 -*-
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='osc_python_sdk',
    version='0.9.10',
    author="Slim Kac",
    author_email="selim.kacer@outscale.com",
    description="Outscale Gateway python SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/outscale/osc_python_sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests>=2.20.0',
        'ruamel.yaml==0.15.94'
    ]
)
