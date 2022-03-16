"""
Sub module of the class FreiStatInterface, which implements the ribbon.

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

# Import dependencies
from tkinter import *
from tkinter.ttk import *
from FreiStat.Data_storage.constants import *

# Import internal dependencies
from ..Data_Storage.constants import *

def _create_RibbonFrame(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the ribbon at the top of the interface, which
    is used to display the different options of the interface.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the menu band frame is embedded
        
    """        
    # Create frame for ribbon band 
    self._fRibbon = Menu(parentFrame)
    parentFrame.config(menu=self._fRibbon)
    menuFile = Menu(self._fRibbon, tearoff="off")
    helpFile = Menu(self._fRibbon, tearoff="off")

    # Add file menu
    self._fRibbon.add_cascade(label="File", menu= menuFile)

    # Create load button
    menuFile.add_command(label="Load Templae", command= lambda : 
        self._clickRibbonButton(BUTTON_LOAD))

    # Create save button
    menuFile.add_command(label="Save Template", command= lambda : 
        self._clickRibbonButton(BUTTON_SAVE))

    # Create save as ... button
    menuFile.add_command(label="Save Template as", command= lambda : 
        self._clickRibbonButton(BUTTON_SAVEAS))

    menuFile.add_separator()

    # Create preferences button
    menuFile.add_command(label="Preferences", command= lambda : 
        self._clickRibbonButton(BUTTON_PREFERENCES))

    menuFile.add_separator()

    # Create exit button
    menuFile.add_command(label="Exit", command=self._on_Closing)

    # Add help menu
    self._fRibbon.add_cascade(label="Help", menu= helpFile)    

    # Create help button
    helpFile.add_command(label="Help", command= lambda : 
        self._clickRibbonButton(BUTTON_HELP))

    helpFile.add_separator()

    # Create about button
    helpFile.add_command(label="About", command= lambda : 
        self._clickRibbonButton(BUTTON_ABOUT))