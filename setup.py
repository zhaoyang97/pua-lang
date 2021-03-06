
from setuptools import setup, find_packages

setup(
    name='pua-lang',
    summary='PUA Programming Language written in Python.',
    version='0.1.4',
    author='zy',
    author_email='',
    install_requires = ["setuptools"],
    include_package_data = True,
    packages=find_packages(exclude=['test']),
    license='MIT license',
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
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
