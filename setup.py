import os
from setuptools import setup, find_packages

# Get the directory where setup.py is located
current_directory = os.path.abspath(os.path.dirname(__file__))

# Use that directory to construct the absolute path to README.rst
with open(os.path.join(current_directory, 'README.rst'), 'r') as f:
    long_description = f.read()

setup(
    name = 'cobamp',
    version = '0.2.0',
    package_dir = {'':'src'},
    packages = find_packages('src'),
    install_requires = ["numpy",
                        "scipy",
                        "pandas",
                        "optlang",
                        "matplotlib",
                        "pathos",
                        "boolean.py"],

    author = 'Vítor Vieira',
    author_email = 'vvieira@ceb.uminho.pt',
    description = 'cobamp - pathway analysis methods for genome-scale metabolic models',
    license = 'GNU General Public License v3.0',
    keywords = 'pathway analysis metabolic model',
    url = 'https://github.com/BioSystemsUM/cobamp',
    long_description = long_description,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
