#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='linkedin-api',
    version=version,
    description='LinkedIn API.',
    long_description=open('README.md').read(),
    author='Praful Mathur, Alec Taylor',
    author_email='praful.mathur@gmail.com, alec.taylor6@gmail.com',
    url='http://github.com/derivatived/linkedin-api',
    packages=find_packages(),
    install_requires=['requests'],
    license='BSD',
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
    keywords=['requests', 'python-requests', 'OAuth', 'OAuth2', 'open authentication',
              'LinkedIn', 'api', 'auth', 'social networking'],
    zip_safe=False,
)
