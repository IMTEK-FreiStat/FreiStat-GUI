"""
Sub module of the class FreiStatPopUp, which implements different event
handling functions.

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

# Import internal dependencies
from ..Data_Storage.dictionaries import *

def _on_rightclick(self, event, entry):
    """
    Description
    -----------
    Method implementing the behavior for right clicking any parameter window

    Parameters
    ----------
    entry : string
        String encoding the parameter (and parameter) which was clicked.

    """
    self.PopUp_Tooltip(entry)

def _on_rightclick_release(self, event, entry):
    """
    Description
    -----------
    Method implementing the behavior for releasing the rightclick after 
    clicking any parameter window

    Parameters
    ----------
    entry : string
        String encoding the parameter (and parameter) which was clicked.

    """
    self._PopUpRoot.withdraw()

