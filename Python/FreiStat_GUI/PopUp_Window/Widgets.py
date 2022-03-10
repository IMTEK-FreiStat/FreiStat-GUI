"""
Sub module of the class FreiStatPopUp, which implements the functionalities
of the widgets.

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
from ..Data_Storage.dictionaries import *

def _clickSelect(self, iIndex : int) -> None:
    """
    Description
    -----------
    Method for selecting method for import/export

    Parameters
    ----------
    `iIndex` : int
        Integer encoding the currently clicked button

    """   
    if (self._buttonList[iIndex][1]):
        # Update frame color
        Widget.nametowidget(self._PopUpRoot, self._buttonList[iIndex][0].winfo_parent()). \
        configure(style= "fUnselectedFrame.TFrame")

        # Change button text
        self._buttonList[iIndex][0].configure(text= "Unselected")

        # Change select variable
        self._buttonList[iIndex][1] = False
    else :
        # Update frame color
        Widget.nametowidget(self._PopUpRoot, self._buttonList[iIndex][0].winfo_parent()). \
        configure(style= "fSelectedFrame.TFrame")

        # Change button text
        self._buttonList[iIndex][0].configure(text= "Selected")

        # Change select variable
        self._buttonList[iIndex][1] = True

def _clickCheckButton(self, iIndex : int) -> None:
    """
    Description
    -----------
    Method callend when clicking check button in the template management

    Parameters
    ----------
    `iIndex` : int
        Integer encoding the currently clicked checkbutton

    """
    if (self._templateList[iIndex].get() == 0):
        # Hide experiment parameters
        self._templateFrameList[iIndex].pack_forget()
    else :
        # Show experiment parameters
        self._templateFrameList[iIndex].pack(fill= "both", side= "top", padx= 1, pady= 5)

def _clickImport(self) -> None:
    """
    Description
    -----------
    Method called when clicking on the import button in the template management

    """
    # Initialzie variables
    datastorageList : list = []

    # Loop over all templates
    for iIndex in range(len(self._buttonList)):
        # Check if method was selected
        if (self._buttonList[iIndex][1]):
            # Update template name
            self._listDataStorage[iIndex].save_TemplateName(self._templateNameList[iIndex].get())

            datastorageList.append(self._listDataStorage[iIndex])
            
            


    # Check if template name is already used
    for iIndex in range(self._dataHandling.get_SequenceLength()):
        for jIndex in range(len(datastorageList)):
            if (self._dataHandling.get_TemplateName() == 
                datastorageList[jIndex].get_TemplateName()):
                # Renaming of template required
                datastorageList[jIndex].save_TemplateName(
                    datastorageList[jIndex].get_TemplateName() + " Import")
        self._dataHandling.move_next_DataObject()

    # Save imported templates
    for jIndex in range(len(datastorageList)):
        self._dataHandling.import_DataObject(datastorageList[jIndex])

    # Close popup window after import
    self._on_Closing()
    
def _clickExport(self) -> None:
    """
    Description
    -----------
    Method called when clicking on the export button in the template management

    """
    # Initialzie variables
    datastorageList : list = []

    # Loop over all templates
    for iIndex in range(len(self._buttonList)):
        # Check if method was selected
        if (self._buttonList[iIndex][1]):
            datastorageList.append(self._listDataStorage[iIndex])

    # Export templates
    for jIndex in range(len(datastorageList)):
        self._dataHandling.export_Templates(self._strFilePath, datastorageList)

    # Close popup window after export
    self._on_Closing()
