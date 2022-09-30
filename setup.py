#!/usr/bin/env python3
# coding: utf-8

# Copyright (c) Colav.
# Distributed under the terms of the Modified BSD License.

# -----------------------------------------------------------------------------
# Minimal Python version sanity check (from IPython)
# -----------------------------------------------------------------------------

# See https://stackoverflow.com/a/26737258/2268280
# sudo pip3 install twine
# python3 setup.py sdist bdist_wheel
# twine upload dist/*
# For test purposes
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

from __future__ import print_function
from setuptools import setup, find_packages

import os
import sys


v = sys.version_info

shell = False
if os.name in ('nt', 'dos'):
    shell = True
    warning = "WARNING: Windows is not officially supported"
    print(warning, file=sys.stderr)


def main():
    setup(
        # Application name:
        name="desoper",

        # Version number (initial):
        version="0.0.3",

        # Application author details:
        author="Hinestroza",
        author_email="restrepo@udea.edu.co",

        # Packages
        packages=find_packages(exclude=['tests']),
        

        # Include additional files into the package
        include_package_data=True,

        # Details
        url="https://github.com/restrepo/DevOps",
        scripts=["bin/HPypi"],

        license="BSD",

        description="Hello World!",

        long_description=open("README.md").read(),

        long_description_content_type="text/markdown",

        # Dependent packages (distributions)
        # See: https://github.com/pypa/pipenv/issues/2171
        #install_requires=['numpy','pandas','dask','anomalies'],
        #setup_requires=["numpy >= 1.7"],
        #install_requires=["numpy >= 1.7", "scipy >= 0.13.2","dask"],
        install_requires=['numpy==1.16.5; python_version=="3.7"',
            'numpy>=1.16.5; python_version=="3.8"',
            'numpy>=1.16.5; python_version=="3.9"',
            'dask==2021.12.0; python_version=="3.7"',
            'dask==2022.2.1; python_version=="3.8"',
            'dask==2022.2.1; python_version=="3.9"',
            'anomalies==0.2.5;python_version=="3.7"',
            'anomalies==0.2.5;python_version=="3.8"',
            'anomalies==0.2.5;python_version=="3.9"',
            'pandas==1.0.0; python_version=="3.7"', 
            'pandas==1.4.2; python_version=="3.8"',
            'pandas==1.4.2; python_version=="3.9"'],
    )


if __name__ == "__main__":
    main()
