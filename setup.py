#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = ['bingo']
requires = ['argparse']
scripts = ['bin/make_bingo.py']

setup(
    name='Bingo',
    version='0.1',
    author='Jean-Frédéric',
    author_email='jeanfrederic.wiki@gmail.com',
    url='https://github.com.org/JeanFred/bingo',
    description='Tool to generate bingo grids.',
    license='MIT',
    packages=packages,
    install_requires=requires,
    scripts=scripts,
)
