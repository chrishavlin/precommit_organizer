#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()


with open('requirements.txt') as reqs_file:
    requirements = reqs_file.read().strip().split("\n")


test_requirements = ['pytest>=3', ]

setup(
    author="Chris Havlin",
    author_email='chris.havlin@gmail.com',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="tired of managing precommit across repos",
    entry_points={
        'console_scripts': [
            'precommit_organizer.py=precommit_organizer.py.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='precommit_organizer.py',
    name='precommit_organizer.py',
    packages=find_packages(include=['precommit_organizer.py', 'precommit_organizer.py.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/chrishavlin/precommit_organizer',
    version='0.1.0',
    zip_safe=False,
)
