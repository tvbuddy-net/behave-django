#!/usr/bin/env python3
"""
Packaging setup of Django integration for behave.
"""
from os import chdir
from os.path import abspath, dirname, normpath
from setuptools import find_packages, setup

# allow setup.py to be run from any path
chdir(normpath(abspath(dirname(__file__))))

import behave_django as package  # noqa


def read_file(filename):
    with open(filename) as file:
        return file.read()


setup(
    name='behave-django',
    version=package.__version__,
    license=package.__license__,
    description=package.__doc__.strip(),
    long_description=read_file('README.rst'),
    long_description_content_type='text/x-rst',
    packages=find_packages(exclude=['test*']),
    include_package_data=True,
    url=package.__url__,
    author=package.__author__,
    author_email=package.__email__,
    maintainer=package.__maintainer__,
    maintainer_email=package.__email__,
    install_requires=read_file('requirements.txt'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Testing',
    ],
    test_suite='tests',
)
