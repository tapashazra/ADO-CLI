# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# ---------------------------------------------------------

from setuptools import setup, find_packages

NAME = 'vsts-cli-common'
VERSION = '0.1.3'

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    'keyring~=13.2.1',
    'knack==0.4.1',
    'python-dateutil==2.7.3',
    'azure-devops~=4.0.0.dev'
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

setup(
    name=NAME,
    version=VERSION,
    license='MIT',
    description="VSTS Command Line Common",
    author="Microsoft Corporation",
    author_email="vstscli@microsoft.com",
    url="https://github.com/Microsoft/vsts-cli",
    keywords=["Microsoft", "VSTS", "Team Services", "SDK", "AzureTfs", "CLI"],
    install_requires=REQUIRES,
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)