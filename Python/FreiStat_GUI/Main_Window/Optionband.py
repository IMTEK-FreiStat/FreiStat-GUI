"""
Sub module of the class FreiStatInterface, which implements the optionband.

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

def _create_OptionbandFrame(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the option band at the left side of the interface, 
    which is used to display additional settings depending on the menu band.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the option band frame is embedded
        
    """       
    # Create frame for menu band 
    self._fOptionBand = Frame(parentFrame, style="fOptionBand.TFrame")
    self._fOptionBand.pack(fill=Y, side=LEFT, expand=FALSE)

def _update_OptionbandFrame_SingleMode(self, parentFarme: Frame) -> None:
    """
    Description
    -----------
    Method for creating the option band at the left side of the interface, 
    when the user has selected the single mode in the menu band.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the option band frame is embedded
        
    """    
    # Clear present widgets
    self._clearFrame(parentFarme)

    # Create CA frame
    fCA = Frame(parentFarme, style="fWidgetButton.TFrame")
    fCA.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonCA = Button(fCA, image=self._IconCA,
                        command= lambda : self._clickButton(BUTTON_EC_CA))        
    ButtonCA.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextCA = Label(fCA, text= "CA", style= "fLabelGeneralBold.TLabel")
    TextCA.pack(side= LEFT, padx= 5, pady= 5)

    # Create LSV frame
    fLSV = Frame(parentFarme, style="fWidgetButton.TFrame")
    fLSV.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonLSV = Button(fLSV, image=self._IconLSV,
                        command= lambda : self._clickButton(BUTTON_EC_LSV))        
    ButtonLSV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextLSV = Label(fLSV, text= "LSV", style= "fLabelGeneralBold.TLabel")
    TextLSV.pack(side= LEFT, padx= 5, pady= 5)

    # Create CV frame
    fCV = Frame(parentFarme, style="fWidgetButton.TFrame")
    fCV.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonCV = Button(fCV, image=self._IconCV,
                        command= lambda : self._clickButton(BUTTON_EC_CV))        
    ButtonCV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextCV = Label(fCV, text= "CV", style= "fLabelGeneralBold.TLabel")
    TextCV.pack(side= LEFT, padx= 5, pady= 5)

    # Create NPV frame
    fNPV = Frame(parentFarme, style="fWidgetButton.TFrame")
    fNPV.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonNPV = Button(fNPV, image=self._IconNPV,
                        command= lambda : self._clickButton(BUTTON_EC_NPV))        
    ButtonNPV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextNPV = Label(fNPV, text= "NPV", style= "fLabelGeneralBold.TLabel")
    TextNPV.pack(side= LEFT, padx= 5, pady= 5)

    # Create DPV frame
    fDPV = Frame(parentFarme, style="fWidgetButton.TFrame")
    fDPV.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonDPV = Button(fDPV, image=self._IconDPV,
                        command= lambda : self._clickButton(BUTTON_EC_DPV))        
    ButtonDPV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextDPV = Label(fDPV, text= "DPV", style= "fLabelGeneralBold.TLabel")
    TextDPV.pack(side= LEFT, padx= 5, pady= 5)

    # Create SWV frame
    fSWV = Frame(parentFarme, style="fWidgetButton.TFrame")
    fSWV.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonSWV = Button(fSWV, image=self._IconSWV,
                        command= lambda : self._clickButton(BUTTON_EC_SWV))        
    ButtonSWV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextSWV = Label(fSWV, text= "SWV", style= "fLabelGeneralBold.TLabel")
    TextSWV.pack(side= LEFT, padx= 5, pady= 5)

def _update_OptionbandFrame_SequeneceMode(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the option band at the left side of the interface, 
    when the user has selected the sequence mode in the menu band.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the option band frame is embedded
        
    """    
    # Clear present widgets
    self._clearFrame(parentFrame)

    # Create new (+) frame
    fNewMethod = Frame(parentFrame, style="fWidgetButton.TFrame")
    fNewMethod.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonAdd = Button(fNewMethod, image= self._IconAdd,
                        command= lambda : self._clickButton(BUTTON_ADD))        
    ButtonAdd.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextAdd = Label(fNewMethod, text= "Add", style= "fLabelGeneralBold.TLabel")
    TextAdd.pack(side= LEFT, padx= 5, pady= 5)

    # Create new (-) frame
    fRemoveMethod = Frame(parentFrame, style="fWidgetButton.TFrame")
    fRemoveMethod.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonRemove = Button(fRemoveMethod, image= self._IconRemove,
                        command= lambda : self._clickButton(BUTTON_DELETE))        
    ButtonRemove.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextRemove = Label(fRemoveMethod, text= "Remove", 
                       style= "fLabelGeneralBold.TLabel")
    TextRemove.pack(side= LEFT, padx= 5, pady= 5)

    # Create new (<- (up)) frame
    fMoveUpMethod = Frame(parentFrame, style="fWidgetButton.TFrame")
    fMoveUpMethod.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonMoveUp = Button(fMoveUpMethod, image= self._IconMoveUp,
                        command= lambda : self._clickButton(BUTTON_MOVE_UP))        
    ButtonMoveUp.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextMoveUp = Label(fMoveUpMethod, text= "Move up", 
                       style= "fLabelGeneralBold.TLabel")
    TextMoveUp.pack(side= LEFT, padx= 5, pady= 5)

    # Create new (-> (down)) frame
    fMoveDownMethod = Frame(parentFrame, style="fWidgetButton.TFrame")
    fMoveDownMethod.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonMoveDown = Button(fMoveDownMethod, image= self._IconMoveDown,
                        command= lambda : self._clickButton(BUTTON_MOVE_DOWN))        
    ButtonMoveDown.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextMoveDown = Label(fMoveDownMethod, text= "Move down", 
                         style= "fLabelGeneralBold.TLabel")
    TextMoveDown.pack(side= LEFT, padx= 5, pady= 5)

def _popupEcMethod(self):
    """
    Description
    -----------
    Method implementing a popup window when pressing the add button in the 
    sequence mode.

    """
    # Create a top level popup window
    self._fPopupEcMethod = Toplevel()

    # Remove header of the window
    self._fPopupEcMethod.overrideredirect(1)

    # Setup the geometry of the popup
    self._fPopupEcMethod.geometry(
        f'+{self._Root.winfo_rootx() + 95}+{self._Root.winfo_rooty() + 103}')

    # Bind focus out event to window to close it automatically
    self._fPopupEcMethod.bind("<FocusOut>", self._on_focus_out)

    # Set focus on the window
    self._fPopupEcMethod.focus_force()

    # Create CA frame
    fCA = Frame(self._fPopupEcMethod, style="fWidgetButton.TFrame")
    fCA.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonCA = Button(fCA, image=self._IconCA,
                        command= lambda : self._clickButton(BUTTON_SM_ADD_EC_CA))        
    ButtonCA.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextCA = Label(fCA, text= "CA", style= "fLabelGeneralBold.TLabel")
    TextCA.pack(side= LEFT, padx= 5, pady= 5)

    # Create LSV frame
    fLSV = Frame(self._fPopupEcMethod, style="fWidgetButton.TFrame")
    fLSV.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonLSV = Button(fLSV, image=self._IconLSV,
                        command= lambda : self._clickButton(BUTTON_SM_ADD_EC_LSV))        
    ButtonLSV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextLSV = Label(fLSV, text= "LSV", style= "fLabelGeneralBold.TLabel")
    TextLSV.pack(side= LEFT, padx= 5, pady= 5)

    # Create CV frame
    fCV = Frame(self._fPopupEcMethod, style="fWidgetButton.TFrame")
    fCV.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonCV = Button(fCV, image=self._IconCV,
                        command= lambda : self._clickButton(BUTTON_SM_ADD_EC_CV))        
    ButtonCV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextCV = Label(fCV, text= "CV", style= "fLabelGeneralBold.TLabel")
    TextCV.pack(side= LEFT, padx= 5, pady= 5)

    # Create NPV frame
    fNPV = Frame(self._fPopupEcMethod, style="fWidgetButton.TFrame")
    fNPV.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonNPV = Button(fNPV, image=self._IconNPV,
                        command= lambda : self._clickButton(BUTTON_SM_ADD_EC_NPV))        
    ButtonNPV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextNPV = Label(fNPV, text= "NPV", style= "fLabelGeneralBold.TLabel")
    TextNPV.pack(side= LEFT, padx= 5, pady= 5)

    # Create DPV frame
    fDPV = Frame(self._fPopupEcMethod, style="fWidgetButton.TFrame")
    fDPV.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonDPV = Button(fDPV, image=self._IconDPV,
                        command= lambda : self._clickButton(BUTTON_SM_ADD_EC_DPV))        
    ButtonDPV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextDPV = Label(fDPV, text= "DPV", style= "fLabelGeneralBold.TLabel")
    TextDPV.pack(side= LEFT, padx= 5, pady= 5)

    # Create SWV frame
    fSWV = Frame(self._fPopupEcMethod, style="fWidgetButton.TFrame")
    fSWV.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    ButtonSWV = Button(fSWV, image=self._IconSWV,
                        command= lambda : self._clickButton(BUTTON_SM_ADD_EC_SWV))        
    ButtonSWV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    TextSWV = Label(fSWV, text= "SWV", style= "fLabelGeneralBold.TLabel")
    TextSWV.pack(side= LEFT, padx= 5, pady= 5)
    
