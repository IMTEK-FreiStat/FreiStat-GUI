"""
Module implementing the start of the FreiStat graphical user interface.

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

# Import internal dependencies
from FreiStat_GUI.Main_Window import FreiStatInterface

def Main():
    """
    Description
    -----------
    Example implementation of the FreiStat interface.

    """
    FreiStatInterface()

# Run main interface
if __name__ == '__main__':
    Main()