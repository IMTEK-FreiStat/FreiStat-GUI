"""
Module implementing different helper functions associated with the positioning
of objects and windows.

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

# Import dependencies
from tkinter import *
from typing import Union

# Import internal dependencies
from ..Data_Storage.constants import *

def _calculate_WindowPosition(Window : Tk) -> Union[float, float]:
    """
    Description
    -----------
    Method caluclating the rquired position parameters for displaying the window
    in the middle of a screen.
    
    Parameters
    ----------
    `Window` : Tk
        Window, whos positioning should be calculated.

    Return
    ------
    `iCenterX` : int
        Calculated center position in X-direction

    `iCenterY` : int
        Calculated center position in Y-direction


    """
    # Get screen height and width for further calculations
    iScreenWidth = Window.winfo_screenwidth()
    iScreenHeight = Window.winfo_screenheight()

    # calulate and return the center point
    iCenterX = int(iScreenWidth / 2 - MW_X_POSITION / 2)
    iCenterY = int(iScreenHeight / 2 - MW_Y_POSITION / 2)

    return [iCenterX, iCenterY]