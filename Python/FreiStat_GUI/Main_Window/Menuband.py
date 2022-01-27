"""
Sub module of the class FreiStatInterface, which implements the Menuband.

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

def _create_MenubandFrame(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the Menu band at the top of the interface, which
    is used to display the different options of the interface.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the Menu band frame is embedded
        
    """           
    # Create frame for Menu band 
    self._fMenuBand = Frame(parentFrame, style="fMenuBand.TFrame", 
                             relief= RAISED)
    self._fMenuBand.pack(fill= X, side= TOP, expand= FALSE)

    # Create live feed frame
    fLiveFeed = Frame(self._fMenuBand, style="fWidgetButton.TFrame")
    fLiveFeed.pack(fill= Y, side= LEFT, expand= FALSE, padx= 5, pady= 5)

    self._ButtonLiveFeed = Button(fLiveFeed, image=self._IconLiveFeed, 
        state= DISABLED, command= lambda : self._clickButton(BUTTON_LIVEFEED))        
    self._ButtonLiveFeed.pack(side= TOP, fill= Y, padx = 5, pady= 5)

    TextLiveFeed = Label(fLiveFeed, text= "Live feed", 
                           style= "fLabelGeneralBold.TLabel")
    TextLiveFeed.pack(side= BOTTOM, padx= 5, pady= 5)

    # Create single mode frame
    fSingleMode = Frame(self._fMenuBand, style="fWidgetButton.TFrame")
    fSingleMode.pack(fill= Y, side= LEFT, expand= FALSE, padx= 5, pady= 5)

    ButtonSingleMode = Button(fSingleMode, image=self._IconSingleMode,
                            command= lambda : self._clickButton(BUTTON_SINGLE_MODE))        
    ButtonSingleMode.pack(side= TOP, fill= Y, padx = 5, pady= 5)

    TextSingleMode = Label(fSingleMode, text= "Single mode", 
                           style= "fLabelGeneralBold.TLabel")
    TextSingleMode.pack(side= BOTTOM, padx= 5, pady= 5)

    # Create sequence frame
    fSequenceMode = Frame(self._fMenuBand, style="fWidgetButton.TFrame")
    fSequenceMode.pack(fill= Y, side= LEFT, expand= FALSE, padx= 5, pady= 5)

    ButtonSequence = Button(fSequenceMode, image=self._IconSequence,
                            command= lambda : self._clickButton(BUTTON_SEQ_MODE))        
    ButtonSequence.pack(side= TOP, fill= Y, padx = 5, pady= 5)

    TextSequence = Label(fSequenceMode, text= "Sequence mode", 
                         style= "fLabelGeneralBold.TLabel")
    TextSequence.pack(side= BOTTOM, padx= 5, pady= 5)

    # Create info box
    fInfo = Frame(self._fMenuBand, style= "fWidget.TFrame", relief= RAISED)
    fInfo.pack(fill= Y, side= RIGHT, expand= FALSE, padx= 5, pady= 5)

    self._TextInfo = Label(fInfo, text= "INFO",  textvariable= self._strInfo,
                     style= "fLabelGeneralBoldGrey.TLabel", width= TEXTBOX_WIDTH,
                     relief= SUNKEN)
    self._TextInfo.pack(side= TOP, padx= 5, pady= 5)

    self._ProgressBar = Progressbar(fInfo, orient= "horizontal", length= 180,
                                    mode= "determinate", style="LabeledProgressbar")
    self._ProgressBar.pack(side= BOTTOM, padx= 5, pady= 5)    

    # Create start/ stop frame
    fStartStopFrame = Frame(self._fMenuBand, style= "fWidget.TFrame", relief= RAISED)
    fStartStopFrame.pack(fill= Y, side= RIGHT, expand= FALSE, padx= 5, pady= 5)

    self._ButtonStart = Button(fStartStopFrame, text= "Start", state= DISABLED, 
                               style="fButtonGeneral.TButton",
                               command= lambda : self._clickButton(BUTTON_START))        
    self._ButtonStart.pack(side= TOP, expand= TRUE, fill= 'both', padx = 5, pady= 5)

    self._ButtonStop = Button(fStartStopFrame, text= "Stop", state= DISABLED, 
                              style="fButtonGeneral.TButton",
                              command= lambda : self._clickButton(BUTTON_STOP))        
    self._ButtonStop.pack(side= BOTTOM, expand= TRUE, fill= 'both', padx = 5, pady= 5)