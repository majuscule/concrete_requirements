#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='concrete-requirements',
    use_scm_version=True,
    description='setuptools compatible concrete requirement & semver tooling',
    url='https://github.com/majuscule',
    author='Dylan Lloyd',
    author_email='dylan@disinclined.org',
    packages=find_packages(),
    zip_safe=True,
    setup_requires=['setuptools_scm'],
    install_requires=[],
    extras_require={
        'dev': [
            'tox~=2.5.0',
            'pytest~=3.0.3',
            'pylint~=1.6.4',
            'pytest-pylint~=0.6.0',
        ]
    },
)
