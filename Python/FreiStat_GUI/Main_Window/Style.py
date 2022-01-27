"""
Sub module of the class FreiStatInterface, which implements the style of the
interface.

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

def _StyleConfig(self) -> None:
    """
    Description
    -----------
    Helper method for creating all styles used in the interface
    
    """
    style = Style()

    # Frames
    style.configure("fRibbon.TFrame", background= "gray80")
    style.configure("fMenuBand.TFrame", background= "gray70")
    style.configure("fOptionBand.TFrame", background= "gray60")
    style.configure("fCentralFrame.TFrame", background= "white",
                    borderwidth= 0, highlightthickness= 0)
    style.configure("fCentralFrameSequence.TFrame", background= "gray95")
    style.configure("fParameterBand.TFrame", background= "gray60")
    style.configure("fPlotBandTab.TFrame", background= "gray80",
                    borderwidth= 0, highlightthickness= 0)
    style.configure("fPlotBand.TFrame", background= "gray80")
    style.configure("fWidget.TFrame", background= "gray95")
    style.configure("fWidgetButton.TFrame", background= "gray70")
    
    style.configure("fFocusFrame.TFrame", background= "orange")

    style.configure("fPopUp.TFrame", background= "white")

    # Buttons
    style.configure("fButtonGeneral.TButton", font= "Arial 16 bold")

    # Labels
    style.configure("fLabelGeneralWhite.TLabel", font= "Arial 16 bold", 
                    background= "white")
    style.configure("fLabelGeneralWhiteSmallBold.TLabel", font= "Arial 10 bold", 
                    background= "white")
    style.configure("fLabelGeneralWhiteSmall.TLabel", font= "Arial 10", 
                    background= "white")
    style.configure("fLabelGeneralBold.TLabel", font= "Arial 10 bold")
    style.configure("fLabelGeneralBoldLarge.TLabel", font= "Arial 14 bold")
    style.configure("fLabelGeneral.TLabel", font= "Arial 10")
    style.configure("fLabelGeneralBoldGrey.TLabel", font= "Arial 10 bold", 
                    background= "gray85")

    style.configure("fLabelRunning.TLabel", font= "Arial 10 bold", 
                    background= "orange")
    style.configure("fLabelCanceled.TLabel", font= "Arial 10 bold", 
                    background= "red")
    style.configure("fLabelCompleted.TLabel", font= "Arial 10 bold", 
                    background= "#00CC00")   
    
    # Progress bar
    style.configure("LabeledProgressbar", background= "#00CC00")
    style.layout("LabeledProgressbar", 
                [("LabeledProgressbar.trough",
                    {'sticky': 'nswe', 'children': [
                        ("LabeledProgressbar.pbar", {'side': 'left', 'sticky': 'ns'}),
                        ("LabeledProgressbar.label", {'sticky': ''})
                        ]
                    }
                )])

def _LoadIcons(self) -> None:
    """
    Description
    -----------
    Helper method for loading all icons of the interface

    """
    # FreiStat logos
    self._IconLogo = PhotoImage(file= self._strAssetPath + '/assets/logo/FreiStat.gif')
    self._TextLogo = PhotoImage(file= self._strAssetPath + '/assets/logo/FreiStat.png')

    # Menu band
    self._IconLiveFeed = PhotoImage(file= self._strAssetPath + 'assets/icons/live.png')
    self._IconSequence = PhotoImage(file= self._strAssetPath + 'assets/icons/sequence.png')
    self._IconSingleMode = PhotoImage(file= self._strAssetPath + 'assets/icons/single_mode.png')

    # Central frame options
    self._IconSave  = PhotoImage(file= self._strAssetPath + 'assets/icons/Save.png')
    self._IconLoad  = PhotoImage(file= self._strAssetPath +'assets/icons/Load.png')
    self._IconDelete = PhotoImage(file= self._strAssetPath +'assets/icons/Delete.png')

    self._IconSaveSequence  = PhotoImage(file= self._strAssetPath + 'assets/icons/Save_Sequence.png')
    self._IconLoadSequence  = PhotoImage(file= self._strAssetPath +'assets/icons/Load_Sequence.png')
    self._IconDeleteSequence = PhotoImage(file= self._strAssetPath +'assets/icons/Delete_Sequence.png')    

    # EC-methods
    self._IconCA  = PhotoImage(file= self._strAssetPath + 'assets/icons/CA.png')
    self._IconLSV = PhotoImage(file= self._strAssetPath + 'assets/icons/LSV.png')
    self._IconCV  = PhotoImage(file= self._strAssetPath + 'assets/icons/CV.png')
    self._IconNPV = PhotoImage(file= self._strAssetPath + 'assets/icons/NPV.png')
    self._IconDPV = PhotoImage(file= self._strAssetPath + 'assets/icons/DPV.png')
    self._IconSWV = PhotoImage(file= self._strAssetPath + 'assets/icons/SWV.png')

    # Plotband
    self._IconMinimize = PhotoImage(file= self._strAssetPath + 'assets/icons/minimize.png')

    # Sequence mode
    self._IconAdd  = PhotoImage(file= self._strAssetPath + 'assets/icons/Add.png')
    self._IconRemove  = PhotoImage(file= self._strAssetPath + 'assets/icons/Remove.png')
    self._IconMoveUp = PhotoImage(file= self._strAssetPath + 'assets/icons/Move_up.png')
    self._IconMoveDown = PhotoImage(file= self._strAssetPath + 'assets/icons/Move_down.png')

    self._SequenceLink = PhotoImage(file= self._strAssetPath + 'assets/icons/sequence_link.png')