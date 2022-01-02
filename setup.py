
from setuptools import setup, find_packages

extra_modules = {}

setup(
    name='pua-lang',
    version='0.0.1',
    author='zy',
    author_email='consolelogi@outlook.com',
    install_requires = ["setuptools"],
    include_package_data = True,
    packages=find_packages(exclude=['test']),
    url = 'https://github.com/fivezy/pua-lang',
    entry_points = {
        'console_scripts': [
            'pua=src:commandline',
        ]
    },
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
