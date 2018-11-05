from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="PyBoard",
    version="1.0.0",
    author="Kevin Liu",
    description="A Python package for programming with Arduino.",
    long_description=open("README.rst").read(),
    license="GPL v3",
    url="https://github.com/kaiyu-liu/PyBoard",
    packages=find_packages(),
    classifiers=[
        "Environment :: Other Environment",
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        "Topic :: Circuits",
        "Topic :: Education",
        'Programming Language :: Python :: 3.5',
   ],
    zip_safe=False,
    install_requires=[
        'pymata_aio>=2.25',
    ]
)