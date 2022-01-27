"""
Setup file used for the pip installment of the FreiStat library GUI package.

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

# Import dependencies
from setuptools import setup, find_packages
import Python.FreiStat_GUI as FS_GUI

# Open readme file
with open("README.md", "r") as readme_file:
    readme = readme_file.read()

# Intialize variables
requirements : list = ['FreiStat-Framework @ git+https://git@github.com/IMTEK-FreiStat/FreiStat-Framework.git@main#egg=FreiStat-Framework']

setup(
    name= FS_GUI.__name__,
    version= FS_GUI.__version__,
    author= FS_GUI.__author__,
    description= FS_GUI.__description__,
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/IMTEK-FreiStat/FreiStat-GUI",
    package_dir={"": "Python"},
    packages=find_packages(where="Python"),
    package_data={"": ['assets/icons/*','assets/logo/*','backup/*']},
    include_package_data= True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9.1",
    ],
)