#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='drift-wip',
    version='0.1.1',
    author='Ryan Brady',
    author_email='ryan.brady@anchore.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'ipdb',
        'ipython',
        'pydantic',
    ],
    entry_points={
        'console_scripts': [
            'drift-debug = drift.commands.debug:debug',
            'drift-source = drift.commands.source_compare:compare',
            'drift-image = drift.commands.image_compare:compare',
        ],
    }
)