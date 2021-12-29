
from setuptools import setup, find_packages

extra_modules = {}

setup(
    name='pua-lang',
    version='0.0.1',
    zip_safe=False,
    install_requires = ["setuptools"],
    include_package_data = True,
    packages=find_packages(exclude=["ez_setup", 'examples', 'apidocs', "tests"]),
    url = '',
    entry_points = {
        'console_scripts': [
            'pua=src:commandline',
        ]
    },
    classifiers = [
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
