"""
Sub module of the class FreiStatInterface, which implements the central frame.

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
from ..Data_Storage.dictionaries import *

def _create_CentralFrame(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the central frame in the middle of the interface, 
    which is used to display the plots.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the central frame is embedded
        
    """
    # Create frame for central frame 
    self._fCentralFrame = Frame(parentFrame, style="fCentralFrame.TFrame",
                                relief= SUNKEN)
    self._fCentralFrame.pack(fill= 'both', side=TOP, expand=TRUE)

def _create_UtilitybandFrame(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the utility band frame under the overview over the 
    parameters.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the utility band frame is embedded
        
    """
    # Create frames for utility buttons
    self._fUtilitybandFrame = Frame(parentFrame, style="fWidget.TFrame")
    self._fUtilitybandFrame.pack(fill= X, side= BOTTOM, expand= FALSE, padx= 5, pady= 5)

    ButtonReset = Button(self._fUtilitybandFrame, image=self._IconDelete, 
        command= lambda : self._clickButton(BUTTON_DELETE_TEMPLATE))        
    ButtonReset.pack(side= RIGHT, fill= Y, padx = 5, pady= 5)

    ButtonReset.bind("<Enter>", lambda event, 
        entry = DELETE_BUTTON : self._PopUpWindowTooltip._on_rightclick(event, entry))
    
    ButtonReset.bind("<Leave>", lambda event, 
        entry = DELETE_BUTTON  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    ButtonLoad = Button(self._fUtilitybandFrame, image=self._IconLoad, 
        command= lambda : self._clickButton(BUTTON_LOAD_TEMPLATE))        
    ButtonLoad.pack(side= RIGHT, fill= Y, padx = 5, pady= 5)

    ButtonLoad.bind("<Enter>", lambda event, 
        entry = LOAD_BUTTON : self._PopUpWindowTooltip._on_rightclick(event, entry))
    
    ButtonLoad.bind("<Leave>", lambda event, 
        entry = LOAD_BUTTON  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    ButtonSave = Button(self._fUtilitybandFrame, image=self._IconSave, 
        command= lambda : self._clickButton(BUTTON_SAVE_TEMPLATE))        
    ButtonSave.pack(side= RIGHT, fill= Y, padx = 5, pady= 5)

    ButtonSave.bind("<Enter>", lambda event, 
        entry = SAVE_BUTTON : self._PopUpWindowTooltip._on_rightclick(event, entry))
    
    ButtonSave.bind("<Leave>", lambda event, 
        entry = SAVE_BUTTON  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

def _update_CentralFrame_EntryScreen(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Helper method creating the entry frame of the central frame

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the central frame is embedded
        
    """    
    TextLogoFreiStat = Label(parentFrame, image= self._TextLogo, 
        style= "fLabelGeneralWhite.TLabel")
    TextLogoFreiStat.pack(side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextVersionInfo = Label(parentFrame, text="FreiStat GUI - Version: " + 
        __version__, style= "fLabelGeneralWhite.TLabel")
    TextVersionInfo.pack(side= TOP, expand= FALSE, padx= 5, pady= 5)

def _update_CentralFrame_Base(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Helper method creating the base frame of the central frame

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the central frame is embedded
        
    """    
    # Check if an experiment is running
    if (self._iSystemStatus != FS_RUNNING):
        # Clear present widgets
        self._clearFrame(parentFrame)
    else :
        # Hide live feed
        self._fLiveFeed.pack_forget()
        self._clearFrame(parentFrame)

    # Check if no template is available
    if (self._dataHandling.get_SequenceLength() == 0):
        # Init values of entries
        self._initEntries(self._strMethod)
    else :
        # Check if method matches interface
        if (self._dataHandling.get_ExperimentType() == self._strMethod):
            self._updateEntries(self._strMethod)
        elif (self._dataHandling.get_ExperimentType() == SEQUENCE and 
              self._iNavIndex == NI_SEQ_MODE):
            self._updateEntries(self._strMethod)
        else :
            self._initEntries(self._strMethod)

    # Create utility band
    self._create_UtilitybandFrame(parentFrame)
    
    # Create a canvas window
    canvasCentral = Canvas(parentFrame, background= "white",
        borderwidth= 0, highlightthickness= 0)
    
    # Bind resize event to canvas
    canvasCentral.bind("<Configure>", lambda event, canvas = canvasCentral: 
        self._on_resize(event, canvas))

    # Create a scrollbar
    scrollbarCentral=Scrollbar(parentFrame, orient="vertical",
        command= canvasCentral.yview)
    scrollbarCentral.pack(side= RIGHT, fill= Y)

    canvasCentral.pack(fill= "both", expand= True, side= TOP,  padx= 2, pady= 2)

    # Add scroll command to canvas
    canvasCentral.configure(yscrollcommand= scrollbarCentral.set)

    self._fCentralParameterFrame = Frame(canvasCentral, style="fCentralFrame.TFrame")
    self._fCentralParameterFrame.pack(fill= "both", side= TOP, expand= True, padx= 1)

    # Update windows to get correct size informations
    canvasCentral.create_window((0,0), window= self._fCentralParameterFrame, 
        anchor= NW, width= 1600, height= 2000)

    # Bind mousewheel scroll to frames
    self._fCentralParameterFrame.bind("<Enter>", lambda event, 
        frame = self._fCentralParameterFrame, canvas = canvasCentral : 
        self._bound_MouseWheel(event, frame, canvas))
    self._fCentralParameterFrame.bind("<Leave>", lambda event, 
        frame = canvasCentral : self._unbound_MouseWheel(event, frame))

    # Create a frame for naming the template
    fTemplate = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fTemplate.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextTemplate = Label(fTemplate, text= dic_parameters[TEMPLATE_NAME][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneralBold.TLabel")
    TextTemplate.pack(side= LEFT, padx= 5, pady= 5)

    EntryTemplate = Entry(fTemplate, textvariable= self._strTemplate, 
        width= ENTRY_WIDTH)        
    EntryTemplate.pack(side= LEFT, fill= Y, padx = 5, pady= 5)    

    EntryTemplate.bind("<Enter>", lambda event, 
        entry = TEMPLATE_NAME : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryTemplate.bind("<Leave>", lambda event, 
        entry = TEMPLATE_NAME  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Fill in spacer frame to separate parameters
    self._createSpacerFrame(self._fCentralParameterFrame, "fCentralFrame.TFrame")

def _update_CentralFrame_Options(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the central frame in the middle of the interface, 
    which is created when the user opens the option menu.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the central frame is embedded
        
    """    
    self._clearFrame(self._fCentralFrame)

    # Create base frame
    self._update_CentralFrame_Base(parentFrame)
    self._clearFrame(self._fCentralParameterFrame)

    # Create frames for every parameter
    # Low performance mode
    fGLpMode = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fGLpMode.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextGLpMode = Label(fGLpMode, text= dic_parameters[SET_GLPM][0], 
        width= TEXTBOX_WIDTH_SETTINGS, style= "fLabelGeneralBold.TLabel")
    TextGLpMode.pack(side= LEFT, padx= 5, pady= 5)

    EntryGLpMode = Checkbutton(fGLpMode, onvalue= True, offvalue= False, 
        variable= self._iGlobalLowPerformanceMode)        
    EntryGLpMode.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryGLpMode.bind("<Enter>", lambda event, 
        entry = SET_GLPM : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryGLpMode.bind("<Leave>", lambda event, 
        entry = SET_GLPM  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Low performance mode latency
    fGLpModeL = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fGLpModeL.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextGLpModeL = Label(fGLpModeL, text= dic_parameters[SET_GLPM_LATENCY][0], 
        width= TEXTBOX_WIDTH_SETTINGS, style= "fLabelGeneralBold.TLabel")
    TextGLpModeL.pack(side= LEFT, padx= 5, pady= 5)

    EntryGLpModeL = Entry(fGLpModeL, textvariable= self._strGLpmLatency, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fGLpModeL.
        register(_valdiate_ValueEntriesPositive),'%S','%d'))        
    EntryGLpModeL.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryGLpModeL.bind("<Enter>", lambda event, 
        entry = SET_GLPM_LATENCY : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryGLpModeL.bind("<Leave>", lambda event, 
        entry = SET_GLPM_LATENCY  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # WLAN mode
    fWLANMode = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fWLANMode.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextWLANMode = Label(fWLANMode, text= dic_parameters[SET_WLAN_MODE][0], 
        width= TEXTBOX_WIDTH_SETTINGS, style= "fLabelGeneralBold.TLabel")
    TextWLANMode.pack(side= LEFT, padx= 5, pady= 5)

    EntryWLANMode = Checkbutton(fWLANMode, variable= self._iWLANMode, 
        onvalue= True, offvalue= False)        
    EntryWLANMode.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryWLANMode.bind("<Enter>", lambda event, 
        entry = SET_WLAN_MODE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryWLANMode.bind("<Leave>", lambda event, 
        entry = SET_WLAN_MODE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Server IP
    fServerIP = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fServerIP.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextServerIP = Label(fServerIP, text= dic_parameters[SET_SERVER_IP][0], 
        width= TEXTBOX_WIDTH_SETTINGS, style= "fLabelGeneralBold.TLabel")
    TextServerIP.pack(side= LEFT, padx= 5, pady= 5)

    EntryServerIP = Entry(fServerIP, textvariable= self._strServerIP, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fServerIP.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryServerIP.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryServerIP.bind("<Enter>", lambda event, 
        entry = SET_SERVER_IP : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryServerIP.bind("<Leave>", lambda event, 
        entry = SET_SERVER_IP  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Server Port
    fServerPort = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fServerPort.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextServerPort = Label(fServerPort, text= dic_parameters[SET_SERVER_PORT][0], 
        width= TEXTBOX_WIDTH_SETTINGS, style= "fLabelGeneralBold.TLabel")
    TextServerPort.pack(side= LEFT, padx= 5, pady= 5)

    EntryServerPort = Entry(fServerPort, textvariable= self._strServerPort, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fServerPort.
        register(_valdiate_ValueEntriesPositive),'%S','%d'))        
    EntryServerPort.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryServerPort.bind("<Enter>", lambda event, 
        entry = SET_SERVER_PORT : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryServerPort.bind("<Leave>", lambda event, 
        entry = SET_SERVER_PORT  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Client IP
    fClientIP = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fClientIP.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextClientIP = Label(fClientIP, text= dic_parameters[SET_CLIENT_IP][0], 
        width= TEXTBOX_WIDTH_SETTINGS, style= "fLabelGeneralBold.TLabel")
    TextClientIP.pack(side= LEFT, padx= 5, pady= 5)

    EntryClientIP = Entry(fClientIP, textvariable= self._strClientIP, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fClientIP.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryClientIP.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryClientIP.bind("<Enter>", lambda event, 
        entry = SET_CLIENT_IP : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryClientIP.bind("<Leave>", lambda event, 
        entry = SET_CLIENT_IP  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Client Port
    fClientPort = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fClientPort.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextClientPort = Label(fClientPort, text= dic_parameters[SET_CLIENT_PORT][0], 
        width= TEXTBOX_WIDTH_SETTINGS, style= "fLabelGeneralBold.TLabel")
    TextClientPort.pack(side= LEFT, padx= 5, pady= 5)

    EntryClientPort = Entry(fClientPort, textvariable= self._strClientPort, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fClientPort.
        register(_valdiate_ValueEntriesPositive),'%S','%d'))        
    EntryClientPort.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryClientPort.bind("<Enter>", lambda event, 
        entry = SET_CLIENT_PORT : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryClientPort.bind("<Leave>", lambda event, 
        entry = SET_CLIENT_PORT  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Bind leave event to _fCentralParameterFrame
    self._fCentralParameterFrame.bind("<Leave>", 
        lambda event : self._savePreferences())

    # Update the preferences
    self._updatePreferences()

def _update_CentralFrame_CA(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the central frame in the middle of the interface, 
    which is created when the user wants to start a CA in single mode.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the central frame is embedded
        
    """      
    # Update class variables
    self._strMethod = CA

    # Create base frame
    self._update_CentralFrame_Base(parentFrame)

    # Create frames for every parameter
    # Potential steps
    fPotentialSteps = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fPotentialSteps.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextPotentialSteps = Label(fPotentialSteps, width= TEXTBOX_WIDTH,
        text= dic_parameters[POTENTIAL_STEPS][0], style= "fLabelGeneral.TLabel")
    TextPotentialSteps.pack(side= LEFT, padx= 5, pady= 5)

    EntryPotentialSteps = Entry(fPotentialSteps, textvariable= 
        self._strPotentialSteps, width= ENTRY_WIDTH, validate="key", 
        validatecommand= (fPotentialSteps.register(_valdiate_ArrayEntries),'%S','%d'))        
    EntryPotentialSteps.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryPotentialSteps.bind("<Enter>", lambda event, 
        entry = POTENTIAL_STEPS : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryPotentialSteps.bind("<Leave>", lambda event, 
        entry = POTENTIAL_STEPS  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Pulse lengths
    fPulseLengths = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fPulseLengths.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextPulseLengths = Label(fPulseLengths, width= TEXTBOX_WIDTH, 
        text= dic_parameters[PULSE_LENGTH][0], style= "fLabelGeneral.TLabel")
    TextPulseLengths.pack(side= LEFT, padx= 5, pady= 5)

    EntryPulseLengths = Entry(fPulseLengths, textvariable= self._strPulseLengths, 
        width= ENTRY_WIDTH, validate="key", validatecommand= 
        (fPulseLengths.register(_valdiate_ArrayEntries),'%S','%d'))        
    EntryPulseLengths.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryPulseLengths.bind("<Enter>", lambda event, 
        entry = PULSE_LENGTH : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryPulseLengths.bind("<Leave>", lambda event, 
        entry = PULSE_LENGTH  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Sampling rate
    fSamplingRate = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fSamplingRate.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextSamplingRate = Label(fSamplingRate, width= TEXTBOX_WIDTH, 
        text= dic_parameters[SAMPLING_RATE][0], style= "fLabelGeneral.TLabel")
    TextSamplingRate.pack(side= LEFT, padx= 5, pady= 5)

    EntrySamplingRate = Entry(fSamplingRate, width= ENTRY_WIDTH, 
        textvariable= self._strSamplingRate, validate="key", validatecommand= 
        (fSamplingRate.register(_valdiate_ValueEntries),'%S','%d'))        
    EntrySamplingRate.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntrySamplingRate.bind("<Enter>", lambda event, 
        entry = SAMPLING_RATE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntrySamplingRate.bind("<Leave>", lambda event, 
        entry = SAMPLING_RATE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Cycles
    fCycles = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fCycles.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCycle = Label(fCycles, text= dic_parameters[CYCLE][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextCycle.pack(side= LEFT, padx= 5, pady= 5)

    EntryCycle = Entry(fCycles, textvariable= self._strCycle, width= ENTRY_WIDTH, 
        validate="key", validatecommand= (fCycles.
        register(_valdiate_ValueEntriesPositive),'%S','%d'))        
    EntryCycle.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryCycle.bind("<Enter>", lambda event, 
        entry = CYCLE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCycle.bind("<Leave>", lambda event, 
        entry = CYCLE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # CurrentRange
    fCurrentRange = Frame(self._fCentralParameterFrame, style= "fWidget.TFrame")
    fCurrentRange.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCurrentRange = Label(fCurrentRange, width= TEXTBOX_WIDTH, 
        text= dic_parameters[LPTIA_RTIA_SIZE][0], style= "fLabelGeneral.TLabel")
    TextCurrentRange.pack(side= LEFT, padx= 5, pady= 5)

    EntryCurrentRange = Entry(fCurrentRange, textvariable= self._strCurrentrange,
        width= ENTRY_WIDTH, validate="key", validatecommand= 
        (fCurrentRange.register(_valdiate_ValueEntries),'%S','%d'))        
    EntryCurrentRange.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryCurrentRange.bind("<Enter>", lambda event, 
        entry = LPTIA_RTIA_SIZE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCurrentRange.bind("<Leave>", lambda event, 
        entry = LPTIA_RTIA_SIZE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Fill in spacer frame to separate parameters
    self._createSpacerFrame(self._fCentralParameterFrame, "fCentralFrame.TFrame")

    # Create frame to enable/ disable advanced settings
    fAdvancedSetting = Frame(self._fCentralParameterFrame, style= "fWidget.TFrame")
    fAdvancedSetting.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextAdvancedSetting = Label(fAdvancedSetting, width= TEXTBOX_WIDTH, 
        text= dic_parameters[ADVANCED_SETTING][0], style= "fLabelGeneral.TLabel")
    TextAdvancedSetting.pack(side= LEFT, padx= 5, pady= 5)

    EntryAdvancedSetting = Checkbutton(fAdvancedSetting, 
        command= lambda : self._clickCheckButton(CHECKBUTTON_ADV_SETTING), 
        variable= self._iAdvancedSetting, onvalue= True, offvalue= False)        
    EntryAdvancedSetting.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

def _update_CentralFrame_LSV(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the central frame in the middle of the interface, 
    which is created when the user wants to start a LSV in single mode.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the parameter band frame is embedded
        
    """      
    # Update class variables
    self._strMethod = LSV

    # Create base frame
    self._update_CentralFrame_Base(parentFrame)

    # Create frames for every parameter
    # StartVoltage
    fStartVoltage = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fStartVoltage.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextStartVoltage = Label(fStartVoltage, width= TEXTBOX_WIDTH, 
        text= dic_parameters[START_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextStartVoltage.pack(side= LEFT, padx= 5, pady= 5)

    EntryStartVoltage = Entry(fStartVoltage, textvariable= self._strStartVoltage, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fStartVoltage.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryStartVoltage.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryStartVoltage.bind("<Enter>", lambda event, 
        entry = START_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryStartVoltage.bind("<Leave>", lambda event, 
        entry = START_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # StopVoltage
    fStopVoltage = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fStopVoltage.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextStopVoltage = Label(fStopVoltage, width= TEXTBOX_WIDTH,
        text= dic_parameters[STOP_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextStopVoltage.pack(side= LEFT, padx= 5, pady= 5)

    EntryStopVoltage = Entry(fStopVoltage, textvariable= self._strStopVoltage, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fStopVoltage.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryStopVoltage.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryStopVoltage.bind("<Enter>", lambda event, 
        entry = STOP_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryStopVoltage.bind("<Leave>", lambda event, 
        entry = STOP_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Stepsize
    fStepsize = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fStepsize.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextStepsize = Label(fStepsize, text= dic_parameters[STEP_SIZE][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextStepsize.pack(side= LEFT, padx= 5, pady= 5)

    EntryStepsize = Entry(fStepsize, textvariable= self._strStepsize, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fStepsize.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryStepsize.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryStepsize.bind("<Enter>", lambda event, 
        entry = STEP_SIZE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryStepsize.bind("<Leave>", lambda event, 
        entry = STEP_SIZE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Scanrate
    fScanrate = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fScanrate.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextScanrate = Label(fScanrate, text= dic_parameters[SCAN_RATE][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextScanrate.pack(side= LEFT, padx= 5, pady= 5)

    EntryScanrate = Entry(fScanrate, textvariable= self._strScanrate, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fScanrate.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryScanrate.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryScanrate.bind("<Enter>", lambda event, 
        entry = SCAN_RATE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryScanrate.bind("<Leave>", lambda event, 
        entry = SCAN_RATE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Cycles
    fCycles = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fCycles.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCycle = Label(fCycles, text= dic_parameters[CYCLE][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextCycle.pack(side= LEFT, padx= 5, pady= 5)

    EntryCycle = Entry(fCycles, textvariable= self._strCycle, width= ENTRY_WIDTH, 
        validate="key", validatecommand= (fCycles.
        register(_valdiate_ValueEntriesPositive),'%S','%d'))        
    EntryCycle.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryCycle.bind("<Enter>", lambda event, 
        entry = CYCLE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCycle.bind("<Leave>", lambda event, 
        entry = CYCLE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # CurrentRange
    fCurrentRange = Frame(self._fCentralParameterFrame, style= "fWidget.TFrame")
    fCurrentRange.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCurrentRange = Label(fCurrentRange, width= TEXTBOX_WIDTH,
        text= dic_parameters[LPTIA_RTIA_SIZE][0], style= "fLabelGeneral.TLabel")
    TextCurrentRange.pack(side= LEFT, padx= 5, pady= 5)

    EntryCurrentRange = Entry(fCurrentRange, textvariable= self._strCurrentrange, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fCurrentRange.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryCurrentRange.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryCurrentRange.bind("<Enter>", lambda event, 
        entry = LPTIA_RTIA_SIZE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCurrentRange.bind("<Leave>", lambda event, 
        entry = LPTIA_RTIA_SIZE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Fill in spacer frame to separate parameters
    self._createSpacerFrame(self._fCentralParameterFrame, "fCentralFrame.TFrame")

    # Create frame to enable/ disable advanced settings
    fAdvancedSetting = Frame(self._fCentralParameterFrame, style= "fWidget.TFrame")
    fAdvancedSetting.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextAdvancedSetting = Label(fAdvancedSetting, width= TEXTBOX_WIDTH,
        text= dic_parameters[ADVANCED_SETTING][0], style= "fLabelGeneral.TLabel")
    TextAdvancedSetting.pack(side= LEFT, padx= 5, pady= 5)

    EntryAdvancedSetting = Checkbutton(fAdvancedSetting, 
        command= lambda : self._clickCheckButton(CHECKBUTTON_ADV_SETTING), 
        variable= self._iAdvancedSetting, onvalue= True, offvalue= False)        
    EntryAdvancedSetting.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

def _update_CentralFrame_CV(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the central frame in the middle of the interface, 
    which is created when the user wants to start a CV in single mode.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the parameter band frame is embedded
        
    """      
    # Update class variables
    self._strMethod = CV

    # Create base frame
    self._update_CentralFrame_Base(parentFrame)

    # Create frames for every parameter
    # StartVoltage
    fStartVoltage = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fStartVoltage.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextStartVoltage = Label(fStartVoltage, width= TEXTBOX_WIDTH, 
        text= dic_parameters[START_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextStartVoltage.pack(side= LEFT, padx= 5, pady= 5)

    EntryStartVoltage = Entry(fStartVoltage, textvariable= self._strStartVoltage, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fStartVoltage.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryStartVoltage.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryStartVoltage.bind("<Enter>", lambda event, 
        entry = START_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryStartVoltage.bind("<Leave>", lambda event, 
        entry = START_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # LowerTurningVoltage
    fLowerVoltage = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fLowerVoltage.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextLowerVoltage = Label(fLowerVoltage, width= TEXTBOX_WIDTH,
        text= dic_parameters[LOWER_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextLowerVoltage.pack(side= LEFT, padx= 5, pady= 5)

    EntryLowerVoltage = Entry(fLowerVoltage, textvariable= self._strLowerVoltage, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fLowerVoltage.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryLowerVoltage.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryLowerVoltage.bind("<Enter>", lambda event, 
        entry = LOWER_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryLowerVoltage.bind("<Leave>", lambda event, 
        entry = LOWER_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # UpperTurningVoltage
    fUpperVoltage = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fUpperVoltage.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextUpperVoltage = Label(fUpperVoltage, width= TEXTBOX_WIDTH,
        text= dic_parameters[UPPER_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextUpperVoltage.pack(side= LEFT, padx= 5, pady= 5)

    EntryUpperVoltage = Entry(fUpperVoltage, textvariable= self._strUpperVoltage, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fUpperVoltage.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryUpperVoltage.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryUpperVoltage.bind("<Enter>", lambda event, 
        entry = UPPER_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryUpperVoltage.bind("<Leave>", lambda event, 
        entry = UPPER_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Stepsize
    fStepsize = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fStepsize.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextStepsize = Label(fStepsize, text= dic_parameters[STEP_SIZE][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextStepsize.pack(side= LEFT, padx= 5, pady= 5)

    EntryStepsize = Entry(fStepsize, textvariable= self._strStepsize, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fStepsize.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryStepsize.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryStepsize.bind("<Enter>", lambda event, 
        entry = STEP_SIZE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryStepsize.bind("<Leave>", lambda event, 
        entry = STEP_SIZE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Scanrate
    fScanrate = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fScanrate.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextScanrate = Label(fScanrate, text= dic_parameters[SCAN_RATE][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextScanrate.pack(side= LEFT, padx= 5, pady= 5)

    EntryScanrate = Entry(fScanrate, textvariable= self._strScanrate, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fScanrate.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryScanrate.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryScanrate.bind("<Enter>", lambda event, 
        entry = SCAN_RATE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryScanrate.bind("<Leave>", lambda event, 
        entry = SCAN_RATE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Cycles
    fCycles = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fCycles.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCycle = Label(fCycles, text= dic_parameters[CYCLE][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextCycle.pack(side= LEFT, padx= 5, pady= 5)

    EntryCycle = Entry(fCycles, textvariable= self._strCycle, width= ENTRY_WIDTH, 
        validate="key", validatecommand= (fCycles.
        register(_valdiate_ValueEntriesPositive),'%S','%d'))        
    EntryCycle.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryCycle.bind("<Enter>", lambda event, 
        entry = CYCLE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCycle.bind("<Leave>", lambda event, 
        entry = CYCLE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # CurrentRange
    fCurrentRange = Frame(self._fCentralParameterFrame, style= "fWidget.TFrame")
    fCurrentRange.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCurrentRange = Label(fCurrentRange, width= TEXTBOX_WIDTH, 
        text= dic_parameters[LPTIA_RTIA_SIZE][0], style= "fLabelGeneral.TLabel")
    TextCurrentRange.pack(side= LEFT, padx= 5, pady= 5)

    EntryCurrentRange = Entry(fCurrentRange, textvariable= self._strCurrentrange, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fCurrentRange.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryCurrentRange.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryCurrentRange.bind("<Enter>", lambda event, 
        entry = LPTIA_RTIA_SIZE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCurrentRange.bind("<Leave>", lambda event, 
        entry = LPTIA_RTIA_SIZE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Fill in spacer frame to separate parameters
    self._createSpacerFrame(self._fCentralParameterFrame, "fCentralFrame.TFrame")

    # Create frame to enable/ disable advanced settings
    fAdvancedSetting = Frame(self._fCentralParameterFrame, style= "fWidget.TFrame")
    fAdvancedSetting.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextAdvancedSetting = Label(fAdvancedSetting, width= TEXTBOX_WIDTH, 
        text= dic_parameters[ADVANCED_SETTING][0], style= "fLabelGeneral.TLabel")
    TextAdvancedSetting.pack(side= LEFT, padx= 5, pady= 5)

    EntryAdvancedSetting = Checkbutton(fAdvancedSetting, 
        command= lambda : self._clickCheckButton(CHECKBUTTON_ADV_SETTING), 
        variable= self._iAdvancedSetting, onvalue= True, offvalue= False)        
    EntryAdvancedSetting.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

def _update_CentralFrame_NPV(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the central frame in the middle of the interface, 
    which is created when the user wants to start a NPV in single mode.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the parameter band frame is embedded
        
    """      
    # Update class variables
    self._strMethod = NPV

    # Create base frame
    self._update_CentralFrame_Base(parentFrame)

    # Create frames for every parameter
    # BaseVoltage
    fBaseVoltage = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fBaseVoltage.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextBaseVoltage = Label(fBaseVoltage, width= TEXTBOX_WIDTH,
        text= dic_parameters[BASE_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextBaseVoltage.pack(side= LEFT, padx= 5, pady= 5)

    EntryBaseVoltage = Entry(fBaseVoltage, textvariable= self._strBaseVoltage, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fBaseVoltage.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryBaseVoltage.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryBaseVoltage.bind("<Enter>", lambda event, 
        entry = BASE_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryBaseVoltage.bind("<Leave>", lambda event, 
        entry = BASE_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # StartVoltage
    fStartVoltage = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fStartVoltage.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextStartVoltage = Label(fStartVoltage, width= TEXTBOX_WIDTH,
        text= dic_parameters[START_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextStartVoltage.pack(side= LEFT, padx= 5, pady= 5)

    EntryStartVoltage = Entry(fStartVoltage, textvariable= self._strStartVoltage, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fStartVoltage.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryStartVoltage.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryStartVoltage.bind("<Enter>", lambda event, 
        entry = START_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryStartVoltage.bind("<Leave>", lambda event, 
        entry = START_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # StopVoltage
    fStopVoltage = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fStopVoltage.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextStopVoltage = Label(fStopVoltage, width= TEXTBOX_WIDTH, 
        text= dic_parameters[STOP_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextStopVoltage.pack(side= LEFT, padx= 5, pady= 5)

    EntryStopVoltage = Entry(fStopVoltage, textvariable= self._strStopVoltage, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fStopVoltage.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryStopVoltage.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryStopVoltage.bind("<Enter>", lambda event, 
        entry = STOP_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryStopVoltage.bind("<Leave>", lambda event, 
        entry = STOP_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # DeltaV staircase
    fDeltaVStaircase = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fDeltaVStaircase.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextDeltaVStaircase = Label(fDeltaVStaircase, width= TEXTBOX_WIDTH,
        text= dic_parameters[DELTA_V_STAIRCASE][0], style= "fLabelGeneral.TLabel")
    TextDeltaVStaircase.pack(side= LEFT, padx= 5, pady= 5)

    EntryDeltaVStaircase = Entry(fDeltaVStaircase, textvariable= 
        self._strDeltaVStaircase, width= ENTRY_WIDTH, validate="key", 
        validatecommand= (fDeltaVStaircase.register(_valdiate_ValueEntries),'%S','%d'))        
    EntryDeltaVStaircase.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryDeltaVStaircase.bind("<Enter>", lambda event, 
        entry = DELTA_V_STAIRCASE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryDeltaVStaircase.bind("<Leave>", lambda event, 
        entry = DELTA_V_STAIRCASE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Pulse lengths
    fPulseLengths = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fPulseLengths.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextPulseLengths = Label(fPulseLengths, width= TEXTBOX_WIDTH, 
        text= dic_parameters[PULSE_LENGTH][0], style= "fLabelGeneral.TLabel")
    TextPulseLengths.pack(side= LEFT, padx= 5, pady= 5)

    EntryPulseLengths = Entry(fPulseLengths, textvariable= self._strPulseLengths, 
        width= ENTRY_WIDTH, validate="key", validatecommand= 
        (fPulseLengths.register(_valdiate_ArrayEntries),'%S','%d'))        
    EntryPulseLengths.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryPulseLengths.bind("<Enter>", lambda event, 
        entry = PULSE_LENGTH : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryPulseLengths.bind("<Leave>", lambda event, 
        entry = PULSE_LENGTH  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Sampling duration
    fSamplingDuration = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fSamplingDuration.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextSamplingDuration = Label(fSamplingDuration, width= TEXTBOX_WIDTH, 
        text= dic_parameters[SAMPLING_DURATION][0], style= "fLabelGeneral.TLabel")
    TextSamplingDuration.pack(side= LEFT, padx= 5, pady= 5)

    EntrySamplingDuration = Entry(fSamplingDuration, width= ENTRY_WIDTH,
        textvariable= self._strSamplingDuration, validate="key", validatecommand= 
        (fSamplingDuration. register(_valdiate_ValueEntries),'%S','%d'))        
    EntrySamplingDuration.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntrySamplingDuration.bind("<Enter>", lambda event, 
        entry = SAMPLING_DURATION : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntrySamplingDuration.bind("<Leave>", lambda event, 
        entry = SAMPLING_DURATION  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Cycles
    fCycles = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fCycles.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCycle = Label(fCycles, text= dic_parameters[CYCLE][0],  
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextCycle.pack(side= LEFT, padx= 5, pady= 5)

    EntryCycle = Entry(fCycles, textvariable= self._strCycle, width= ENTRY_WIDTH, 
        validate="key", validatecommand= (fCycles.
        register(_valdiate_ValueEntriesPositive),'%S','%d'))        
    EntryCycle.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryCycle.bind("<Enter>", lambda event, 
        entry = CYCLE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCycle.bind("<Leave>", lambda event, 
        entry = CYCLE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # CurrentRange
    fCurrentRange = Frame(self._fCentralParameterFrame, style= "fWidget.TFrame")
    fCurrentRange.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCurrentRange = Label(fCurrentRange, width= TEXTBOX_WIDTH,
        text= dic_parameters[LPTIA_RTIA_SIZE][0], style= "fLabelGeneral.TLabel")
    TextCurrentRange.pack(side= LEFT, padx= 5, pady= 5)

    EntryCurrentRange = Entry(fCurrentRange, textvariable= self._strCurrentrange, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fCurrentRange.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryCurrentRange.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryCurrentRange.bind("<Enter>", lambda event, 
        entry = LPTIA_RTIA_SIZE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCurrentRange.bind("<Leave>", lambda event, 
        entry = LPTIA_RTIA_SIZE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Fill in spacer frame to separate parameters
    self._createSpacerFrame(self._fCentralParameterFrame, "fCentralFrame.TFrame")

    # Create frame to enable/ disable advanced settings
    fAdvancedSetting = Frame(self._fCentralParameterFrame, style= "fWidget.TFrame")
    fAdvancedSetting.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextAdvancedSetting = Label(fAdvancedSetting, width= TEXTBOX_WIDTH,
        text= dic_parameters[ADVANCED_SETTING][0], style= "fLabelGeneral.TLabel")
    TextAdvancedSetting.pack(side= LEFT, padx= 5, pady= 5)

    EntryAdvancedSetting = Checkbutton(fAdvancedSetting, 
        command= lambda : self._clickCheckButton(CHECKBUTTON_ADV_SETTING),
        variable= self._iAdvancedSetting, onvalue= True, offvalue= False)        
    EntryAdvancedSetting.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

def _update_CentralFrame_DPV(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the central frame in the middle of the interface, 
    which is created when the user wants to start a DPV in single mode.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the parameter band frame is embedded
        
    """      
    # Update class variables
    self._strMethod = DPV

    # Create base frame
    self._update_CentralFrame_Base(parentFrame)

    # Create frames for every parameter
    # StartVoltage
    fStartVoltage = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fStartVoltage.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextStartVoltage = Label(fStartVoltage, width= TEXTBOX_WIDTH,
        text= dic_parameters[START_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextStartVoltage.pack(side= LEFT, padx= 5, pady= 5)

    EntryStartVoltage = Entry(fStartVoltage, textvariable= self._strStartVoltage, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fStartVoltage.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryStartVoltage.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryStartVoltage.bind("<Enter>", lambda event, 
        entry = START_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryStartVoltage.bind("<Leave>", lambda event, 
        entry = START_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # StopVoltage
    fStopVoltage = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fStopVoltage.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextStopVoltage = Label(fStopVoltage, width= TEXTBOX_WIDTH,
        text= dic_parameters[STOP_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextStopVoltage.pack(side= LEFT, padx= 5, pady= 5)

    EntryStopVoltage = Entry(fStopVoltage, textvariable= self._strStopVoltage, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fStopVoltage.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryStopVoltage.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryStopVoltage.bind("<Enter>", lambda event, 
        entry = STOP_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryStopVoltage.bind("<Leave>", lambda event, 
        entry = STOP_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # DeltaV staircase
    fDeltaVStaircase = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fDeltaVStaircase.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextDeltaVStaircase = Label(fDeltaVStaircase, width= TEXTBOX_WIDTH,
        text= dic_parameters[DELTA_V_STAIRCASE][0], style= "fLabelGeneral.TLabel")
    TextDeltaVStaircase.pack(side= LEFT, padx= 5, pady= 5)

    EntryDeltaVStaircase = Entry(fDeltaVStaircase, width= ENTRY_WIDTH, 
        textvariable= self._strDeltaVStaircase,  validate="key", validatecommand= 
        (fDeltaVStaircase.register(_valdiate_ValueEntries),'%S','%d'))        
    EntryDeltaVStaircase.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryDeltaVStaircase.bind("<Enter>", lambda event, 
        entry = DELTA_V_STAIRCASE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryDeltaVStaircase.bind("<Leave>", lambda event, 
        entry = DELTA_V_STAIRCASE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # DeltaV peak
    fDeltaVPeak = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fDeltaVPeak.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextDeltaVPeak= Label(fDeltaVPeak, text= dic_parameters[DELTA_V_PEAK][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextDeltaVPeak.pack(side= LEFT, padx= 5, pady= 5)

    EntryDeltaVPeak = Entry(fDeltaVPeak, textvariable= self._strDeltaVPeak, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fDeltaVPeak.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryDeltaVPeak.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryDeltaVPeak.bind("<Enter>", lambda event, 
        entry = DELTA_V_PEAK : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryDeltaVPeak.bind("<Leave>", lambda event, 
        entry = DELTA_V_PEAK  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Pulse lengths
    fPulseLengths = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fPulseLengths.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextPulseLengths = Label(fPulseLengths, width= TEXTBOX_WIDTH,
        text= dic_parameters[PULSE_LENGTH][0], style= "fLabelGeneral.TLabel")
    TextPulseLengths.pack(side= LEFT, padx= 5, pady= 5)

    EntryPulseLengths = Entry(fPulseLengths, textvariable= self._strPulseLengths, 
        width= ENTRY_WIDTH, validate="key", validatecommand= 
        (fPulseLengths.register(_valdiate_ArrayEntries),'%S','%d'))        
    EntryPulseLengths.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryPulseLengths.bind("<Enter>", lambda event, 
        entry = PULSE_LENGTH : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryPulseLengths.bind("<Leave>", lambda event, 
        entry = PULSE_LENGTH  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Sampling duration
    fSamplingDuration = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fSamplingDuration.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextSamplingDuration = Label(fSamplingDuration, width= TEXTBOX_WIDTH,
        text= dic_parameters[SAMPLING_DURATION][0], style= "fLabelGeneral.TLabel")
    TextSamplingDuration.pack(side= LEFT, padx= 5, pady= 5)

    EntrySamplingDuration = Entry(fSamplingDuration, width= ENTRY_WIDTH, 
        textvariable= self._strSamplingDuration, validate="key", validatecommand= 
        (fSamplingDuration.register(_valdiate_ValueEntries),'%S','%d'))        
    EntrySamplingDuration.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntrySamplingDuration.bind("<Enter>", lambda event, 
        entry = SAMPLING_DURATION : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntrySamplingDuration.bind("<Leave>", lambda event, 
        entry = SAMPLING_DURATION  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Cycles
    fCycles = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fCycles.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCycle = Label(fCycles, text= dic_parameters[CYCLE][0],  
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextCycle.pack(side= LEFT, padx= 5, pady= 5)

    EntryCycle = Entry(fCycles, textvariable= self._strCycle, width= ENTRY_WIDTH, 
        validate="key", validatecommand= (fCycles.
        register(_valdiate_ValueEntriesPositive),'%S','%d'))        
    EntryCycle.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryCycle.bind("<Enter>", lambda event, 
        entry = CYCLE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCycle.bind("<Leave>", lambda event, 
        entry = CYCLE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # CurrentRange
    fCurrentRange = Frame(self._fCentralParameterFrame, style= "fWidget.TFrame")
    fCurrentRange.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCurrentRange = Label(fCurrentRange, width= TEXTBOX_WIDTH,
        text= dic_parameters[LPTIA_RTIA_SIZE][0], style= "fLabelGeneral.TLabel")
    TextCurrentRange.pack(side= LEFT, padx= 5, pady= 5)

    EntryCurrentRange = Entry(fCurrentRange, textvariable= self._strCurrentrange, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fCurrentRange.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryCurrentRange.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryCurrentRange.bind("<Enter>", lambda event, 
        entry = LPTIA_RTIA_SIZE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCurrentRange.bind("<Leave>", lambda event, 
        entry = LPTIA_RTIA_SIZE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Fill in spacer frame to separate parameters
    self._createSpacerFrame(self._fCentralParameterFrame, "fCentralFrame.TFrame")

    # Create frame to enable/ disable advanced settings
    fAdvancedSetting = Frame(self._fCentralParameterFrame, style= "fWidget.TFrame")
    fAdvancedSetting.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextAdvancedSetting = Label(fAdvancedSetting, width= TEXTBOX_WIDTH,
        text= dic_parameters[ADVANCED_SETTING][0], style= "fLabelGeneral.TLabel")
    TextAdvancedSetting.pack(side= LEFT, padx= 5, pady= 5)

    EntryAdvancedSetting = Checkbutton(fAdvancedSetting, 
        command= lambda : self._clickCheckButton(CHECKBUTTON_ADV_SETTING),
        variable= self._iAdvancedSetting, onvalue= True, offvalue= False)        
    EntryAdvancedSetting.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

def _update_CentralFrame_SWV(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the central frame in the middle of the interface, 
    which is created when the user wants to start a SWV in single mode.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the parameter band frame is embedded
        
    """      
    # Update class variables
    self._strMethod = SWV

    # Create base frame
    self._update_CentralFrame_Base(parentFrame)

    # Create frames for every parameter
    # StartVoltage
    fStartVoltage = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fStartVoltage.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextStartVoltage = Label(fStartVoltage, width= TEXTBOX_WIDTH, 
        text= dic_parameters[START_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextStartVoltage.pack(side= LEFT, padx= 5, pady= 5)

    EntryStartVoltage = Entry(fStartVoltage, textvariable= self._strStartVoltage, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fStartVoltage.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryStartVoltage.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryStartVoltage.bind("<Enter>", lambda event, 
        entry = START_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryStartVoltage.bind("<Leave>", lambda event, 
        entry = START_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # StopVoltage
    fStopVoltage = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fStopVoltage.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextStopVoltage = Label(fStopVoltage, width= TEXTBOX_WIDTH, 
        text= dic_parameters[STOP_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextStopVoltage.pack(side= LEFT, padx= 5, pady= 5)

    EntryStopVoltage = Entry(fStopVoltage, textvariable= self._strStopVoltage, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fStopVoltage.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryStopVoltage.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryStopVoltage.bind("<Enter>", lambda event, 
        entry = STOP_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryStopVoltage.bind("<Leave>", lambda event, 
        entry = STOP_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # DeltaV staircase
    fDeltaVStaircase = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fDeltaVStaircase.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextDeltaVStaircase = Label(fDeltaVStaircase, width= TEXTBOX_WIDTH,
        text= dic_parameters[DELTA_V_STAIRCASE][0], style= "fLabelGeneral.TLabel")
    TextDeltaVStaircase.pack(side= LEFT, padx= 5, pady= 5)

    EntryDeltaVStaircase = Entry(fDeltaVStaircase, width= ENTRY_WIDTH, 
        textvariable= self._strDeltaVStaircase, validate="key", validatecommand= 
        (fDeltaVStaircase.register(_valdiate_ValueEntries),'%S','%d'))        
    EntryDeltaVStaircase.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryDeltaVStaircase.bind("<Enter>", lambda event, 
        entry = DELTA_V_STAIRCASE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryDeltaVStaircase.bind("<Leave>", lambda event, 
        entry = DELTA_V_STAIRCASE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # DeltaV peak
    fDeltaVPeak = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fDeltaVPeak.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextDeltaVPeak= Label(fDeltaVPeak, text= dic_parameters[DELTA_V_PEAK][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextDeltaVPeak.pack(side= LEFT, padx= 5, pady= 5)

    EntryDeltaVPeak = Entry(fDeltaVPeak, textvariable= self._strDeltaVPeak, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fDeltaVPeak.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryDeltaVPeak.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryDeltaVPeak.bind("<Enter>", lambda event, 
        entry = DELTA_V_PEAK : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryDeltaVPeak.bind("<Leave>", lambda event, 
        entry = DELTA_V_PEAK  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Duty cycle
    fPulseLengths = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fPulseLengths.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextPulseLengths = Label(fPulseLengths, text= dic_parameters[DUTY_CYCLE][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextPulseLengths.pack(side= LEFT, padx= 5, pady= 5)

    EntryPulseLengths = Entry(fPulseLengths, textvariable= self._strDutyCycle, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fPulseLengths.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryPulseLengths.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryPulseLengths.bind("<Enter>", lambda event, 
        entry = DUTY_CYCLE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryPulseLengths.bind("<Leave>", lambda event, 
        entry = DUTY_CYCLE : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Sampling duration
    fSamplingDuration = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fSamplingDuration.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextSamplingDuration = Label(fSamplingDuration, width= TEXTBOX_WIDTH, 
        text= dic_parameters[SAMPLING_DURATION][0], style= "fLabelGeneral.TLabel")
    TextSamplingDuration.pack(side= LEFT, padx= 5, pady= 5)

    EntrySamplingDuration = Entry(fSamplingDuration, width= ENTRY_WIDTH, 
        textvariable= self._strSamplingDuration, validate="key", validatecommand= 
        (fSamplingDuration.register(_valdiate_ValueEntries),'%S','%d'))        
    EntrySamplingDuration.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntrySamplingDuration.bind("<Enter>", lambda event, 
        entry = SAMPLING_DURATION : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntrySamplingDuration.bind("<Leave>", lambda event, 
        entry = SAMPLING_DURATION : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Cycles
    fCycles = Frame(self._fCentralParameterFrame, style="fWidget.TFrame")
    fCycles.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCycle = Label(fCycles, text= dic_parameters[CYCLE][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextCycle.pack(side= LEFT, padx= 5, pady= 5)

    EntryCycle = Entry(fCycles, textvariable= self._strCycle, width= ENTRY_WIDTH, 
        validate="key", validatecommand= (fCycles.
        register(_valdiate_ValueEntriesPositive),'%S','%d'))        
    EntryCycle.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryCycle.bind("<Enter>", lambda event, 
        entry = LPTIA_RTIA_SIZE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCycle.bind("<Leave>", lambda event, 
        entry = LPTIA_RTIA_SIZE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # CurrentRange
    fCurrentRange = Frame(self._fCentralParameterFrame, style= "fWidget.TFrame")
    fCurrentRange.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCurrentRange = Label(fCurrentRange, width= TEXTBOX_WIDTH, 
        text= dic_parameters[LPTIA_RTIA_SIZE][0], style= "fLabelGeneral.TLabel")
    TextCurrentRange.pack(side= LEFT, padx= 5, pady= 5)

    EntryCurrentRange = Entry(fCurrentRange, textvariable= self._strCurrentrange, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fCurrentRange.
        register(_valdiate_ValueEntries),'%S','%d'))        
    EntryCurrentRange.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryCurrentRange.bind("<Enter>", lambda event, 
        entry = LPTIA_RTIA_SIZE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCurrentRange.bind("<Leave>", lambda event, 
        entry = LPTIA_RTIA_SIZE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Fill in spacer frame to separate parameters
    self._createSpacerFrame(self._fCentralParameterFrame, "fCentralFrame.TFrame")

    # Create frame to enable/ disable advanced settings
    fAdvancedSetting = Frame(self._fCentralParameterFrame, style= "fWidget.TFrame")
    fAdvancedSetting.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextAdvancedSetting = Label(fAdvancedSetting, width= TEXTBOX_WIDTH, 
        text= dic_parameters[ADVANCED_SETTING][0], style= "fLabelGeneral.TLabel")
    TextAdvancedSetting.pack(side= LEFT, padx= 5, pady= 5)

    EntryAdvancedSetting = Checkbutton(fAdvancedSetting, 
        command= lambda : self._clickCheckButton(CHECKBUTTON_ADV_SETTING),
        variable= self._iAdvancedSetting, onvalue= True, offvalue= False)        
    EntryAdvancedSetting.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

def _createAdvancedSettingFrame(self, parentFrame : Frame) -> None:
    """
    Description
    -----------
    Method for creating a frame for the advanced settings.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the parameter band frame is embedded
        
    """    
    # Create frame to house advanced settings
    self._fAdvancedSettingContainer = Frame(parentFrame, 
                                            style= "fCentralFrame.TFrame",)
    self._fAdvancedSettingContainer.pack(fill= X, side= TOP, expand= FALSE, padx=10)

    # Fixed working electrode potential
    fFixedWEPotential = Frame(self._fAdvancedSettingContainer, 
                              style="fWidget.TFrame")
    fFixedWEPotential.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextFixedWEPotential = Label(fFixedWEPotential, width= TEXTBOX_WIDTH,
        text= dic_parameters[FIXED_WE_POTENTIAL][0], style= "fLabelGeneral.TLabel")
    TextFixedWEPotential.pack(side= LEFT, padx= 5, pady= 5)

    EntryFixedWEPotential = Checkbutton(fFixedWEPotential, 
        variable= self._iFixedWEPotential, onvalue= True, offvalue= False)        
    EntryFixedWEPotential.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryFixedWEPotential.bind("<Enter>", lambda event, 
        entry = FIXED_WE_POTENTIAL : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryFixedWEPotential.bind("<Leave>", lambda event, 
        entry = FIXED_WE_POTENTIAL  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Mains filter
    fMainsFilter = Frame(self._fAdvancedSettingContainer, style="fWidget.TFrame")
    fMainsFilter.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextMainsFilter = Label(fMainsFilter, text= dic_parameters[MAINS_FILTER][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextMainsFilter.pack(side= LEFT, padx= 5, pady= 5)

    EntryMainsFilter = Checkbutton(fMainsFilter, variable= self._iMainsFilter, 
        onvalue= True, offvalue= False)        
    EntryMainsFilter.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryMainsFilter.bind("<Enter>", lambda event, 
        entry = MAINS_FILTER : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryMainsFilter.bind("<Leave>", lambda event, 
        entry = MAINS_FILTER  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Sinc 2 oversampling rate
    fOsrSinc2 = Frame(self._fAdvancedSettingContainer, style="fWidget.TFrame")
    fOsrSinc2.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextOsrSinc2 = Label(fOsrSinc2, text= dic_parameters[SINC2_OVERSAMPLING][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextOsrSinc2.pack(side= LEFT, padx= 5, pady= 5)

    EntryOsrSinc2 = Entry(fOsrSinc2, textvariable= self._strOsrSinc2, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fOsrSinc2.
        register(_valdiate_ValueEntriesPositive),'%S','%d'))        
    EntryOsrSinc2.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryOsrSinc2.bind("<Enter>", lambda event, 
        entry = SINC2_OVERSAMPLING : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryOsrSinc2.bind("<Leave>", lambda event, 
        entry = SINC2_OVERSAMPLING  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Sinc 3 oversmapling rate
    fOsrSinc3 = Frame(self._fAdvancedSettingContainer, style="fWidget.TFrame")
    fOsrSinc3.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextOsrSinc3 = Label(fOsrSinc3, text= dic_parameters[SINC3_OVERSAMPLING][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextOsrSinc3.pack(side= LEFT, padx= 5, pady= 5)

    EntryOsrSinc3 = Entry(fOsrSinc3, textvariable= self._strOsrSinc3, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fOsrSinc3.
        register(_valdiate_ValueEntriesPositive),'%S','%d'))        
    EntryOsrSinc3.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryOsrSinc3.bind("<Enter>", lambda event, 
        entry = SINC3_OVERSAMPLING : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryOsrSinc3.bind("<Leave>", lambda event, 
        entry = SINC3_OVERSAMPLING  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Enable optimizer
    fOptimizer = Frame(self._fAdvancedSettingContainer, style="fWidget.TFrame")
    fOptimizer.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextOptimizer = Label(fOptimizer, text= dic_parameters[ENABLE_OPTIMIZER][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextOptimizer.pack(side= LEFT, padx= 5, pady= 5)

    EntryOptimizer = Checkbutton(fOptimizer, variable= self._iEnableOptimizer, 
                                 onvalue= True, offvalue= False)        
    EntryOptimizer.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryOptimizer.bind("<Enter>", lambda event, 
        entry = ENABLE_OPTIMIZER : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryOptimizer.bind("<Leave>", lambda event, 
        entry = ENABLE_OPTIMIZER  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Low performance mode
    fLpMode = Frame(self._fAdvancedSettingContainer, style="fWidget.TFrame")
    fLpMode.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextLpMode = Label(fLpMode, text= dic_parameters[LOW_PERFORMANCE_MODE][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextLpMode.pack(side= LEFT, padx= 5, pady= 5)

    EntryLpMode = Checkbutton(fLpMode, variable= self._iLowPerformanceMode, 
        onvalue= True, offvalue= False)        
    EntryLpMode.pack(side= LEFT, fill= Y, padx = 5, pady= 5)

    EntryLpMode.bind("<Enter>", lambda event, 
        entry = LOW_PERFORMANCE_MODE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryLpMode.bind("<Leave>", lambda event, 
        entry = LOW_PERFORMANCE_MODE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

def _update_CentralFrame_Sequence(self, parentFrame : Frame) -> None:
    """
    Description
    -----------
    Method for creating the base structure of the central frame for the 
    sequence mode.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the parameter band frame is embedded
        
    """   
    # Update class variables
    self._strMethod = SEQUENCE

    # Check if an experiment is running
    if (self._iSystemStatus != FS_RUNNING):
        # Clear present widgets
        self._clearFrame(parentFrame)
    else :
        # Hide live feed
        self._hideFrame(parentFrame)

    # Create frame for main window
    fMainSequenceFrame = Frame(parentFrame, style="fCentralFrame.TFrame")
    fMainSequenceFrame.pack(fill= 'both', side= TOP, expand= True, padx= 3, pady= 3)

    # Create a left (display sequence) and a right (parameters) frame
    fWindowLeft = Frame(fMainSequenceFrame, style="fCentralFrame.TFrame")
    fWindowLeft.pack(fill= 'both', expand= True, side= LEFT)

    self._fOptionsSequence = Frame(fMainSequenceFrame, style="fCentralFrame.TFrame")
    self._fOptionsSequence.pack(fill= 'both', expand= True, side= RIGHT)

    # Add frame for sequence template name
    fTemplate = Frame(fWindowLeft, style="fWidget.TFrame")
    fTemplate.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextTemplate = Label(fTemplate, text= dic_parameters[TEMPLATE_NAME_SEQUENCE][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneralBold.TLabel")
    TextTemplate.pack(side= LEFT, padx= 5, pady= 5)

    EntryTemplate = Entry(fTemplate, textvariable= self._strTemplateSeq, 
        width= ENTRY_WIDTH)        
    EntryTemplate.pack(side= LEFT, fill= Y, padx = 5, pady= 5)   

    EntryTemplate.bind("<Enter>", lambda event, 
        entry = TEMPLATE_NAME_SEQUENCE : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryTemplate.bind("<Leave>", lambda event, 
        entry = TEMPLATE_NAME_SEQUENCE  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Add frame for sequence cycles
    fCycles = Frame(fWindowLeft, style="fWidget.TFrame")
    fCycles.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextCycle = Label(fCycles, text= dic_parameters[SEQUENCE_CYCLES][0], 
        width= TEXTBOX_WIDTH, style= "fLabelGeneral.TLabel")
    TextCycle.pack(side= LEFT, padx= 5, pady= 5)

    EntryCycle= Entry(fCycles, textvariable= self._strCycleSeq, 
        width= ENTRY_WIDTH, validate="key", validatecommand= (fCycles.
        register(_valdiate_ValueEntriesPositive),'%S','%d'))        
    EntryCycle.pack(side= LEFT, fill= Y, padx = 5, pady= 5) 

    EntryCycle.bind("<Enter>", lambda event, 
        entry = SEQUENCE_CYCLES : self._PopUpWindowTooltip._on_rightclick(event, entry))
    EntryCycle.bind("<Leave>", lambda event, 
        entry = SEQUENCE_CYCLES  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    # Create a canvas for the left and right window
    canvasWindowLeft = Canvas(fWindowLeft, background= "white",
        borderwidth= 0, highlightthickness= 0)
    canvasWindowLeft.pack(fill= 'both', expand= True, side= LEFT,  padx= 1)

    # Create scrollbars for both windows
    scrollbarWindowLeft=Scrollbar(fWindowLeft,orient="vertical",
        command= canvasWindowLeft.yview)
    scrollbarWindowLeft.pack(side= RIGHT, fill= Y)

    # Add scroll command to canvas
    canvasWindowLeft.configure(yscrollcommand= scrollbarWindowLeft.set)

    # Create the both actual frames
    self._fDisplaySequence = Frame(canvasWindowLeft, style="fCentralFrameSequence.TFrame")
    self._fDisplaySequence.pack(fill= 'both', side= TOP, expand= True, padx= 1)

    # Put frames into canvas
    canvasWindowLeft.create_window((0,0), window= self._fDisplaySequence, 
        anchor= NW, width= 1600, height= 2000)

    # Bind mousewheel scroll to frames
    self._fDisplaySequence.bind("<Enter>", lambda event, frame = 
        self._fDisplaySequence, canvas = canvasWindowLeft : 
        self._bound_MouseWheel(event, frame, canvas))
    self._fDisplaySequence.bind("<Leave>", lambda event, 
        frame = canvasWindowLeft : self._unbound_MouseWheel(event, frame))

    # Create frames for utility buttons
    fUtility = Frame(parentFrame, style="fWidget.TFrame")
    fUtility.pack(fill= X, side= BOTTOM, expand= FALSE, padx= 5, pady= 5)

    ButtonDelete = Button(fUtility, image=self._IconDeleteSequence, 
        command= lambda : self._clickButton(BUTTON_DELETE_TEMP_SEQ))        
    ButtonDelete.pack(side= RIGHT, fill= Y, padx = 5, pady= 5)

    ButtonDelete.bind("<Enter>", lambda event, 
        entry = DELETE_SEQUENCE_BUTTON : self._PopUpWindowTooltip._on_rightclick(event, entry))
    
    ButtonDelete.bind("<Leave>", lambda event, 
        entry = DELETE_SEQUENCE_BUTTON  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    ButtonLoad = Button(fUtility, image=self._IconLoadSequence, 
        command= lambda : self._clickButton(BUTTON_LOAD_TEMP_SEQ))        
    ButtonLoad.pack(side= RIGHT, fill= Y, padx = 5, pady= 5)

    ButtonLoad.bind("<Enter>", lambda event, 
        entry = LOAD_SEQUENCE_BUTTON : self._PopUpWindowTooltip._on_rightclick(event, entry))
    
    ButtonLoad.bind("<Leave>", lambda event, 
        entry = LOAD_SEQUENCE_BUTTON  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

    ButtonSave = Button(fUtility, image=self._IconSaveSequence, 
        command= lambda : self._clickButton(BUTTON_SAVE_TEMP_SEQ))        
    ButtonSave.pack(side= RIGHT, fill= Y, padx = 5, pady= 5)

    ButtonSave.bind("<Enter>", lambda event, 
        entry = SAVE_SEQUENCE_BUTTON : self._PopUpWindowTooltip._on_rightclick(event, entry))
    
    ButtonSave.bind("<Leave>", lambda event, 
        entry = SAVE_SEQUENCE_BUTTON  : self._PopUpWindowTooltip._on_rightclick_release(event, entry))

def _update_CentralFrame_Sequence_Add(self, strMethod : str) -> None:
    """
    Description
    -----------
    Method for creating the base structure of the central frame for the 
    sequence mode.

    Parameters
    ----------
    `strMethod` : string
        Method which should be added to the sequence
        
    """   
    # Check if max sequnece length is reached
    if (len(self._SequenceList) == FREISTAT_SEQUENCE_LENGTH):
        return

    # Check if link arrow should be added
    if (len(self._SequenceList) > 0):
        canvas = Canvas(self._fDisplaySequence, width= 44, height= 28)
        canvas.pack(side= TOP, anchor= NW)
        canvas.create_image(22, 0, image=self._SequenceLink, anchor=NW)

    # Create base frame
    fBaseFrame = Frame(self._fDisplaySequence, style="fWidgetButton.TFrame")
    fBaseFrame.pack(side= TOP, padx= 5, pady= 5, anchor= W)

    # Check which method should be added
    if (strMethod == CA):
        ButtonCA = Button(fBaseFrame, image=self._IconCA, command= lambda : 
            self._clickSequenceMethod(BUTTON_SM_PARA_EC_CA, ButtonCA))        
        ButtonCA.pack(side= LEFT, fill= Y, padx = 5, pady= 5)
        self._SequenceList.append([ButtonCA, CA,[],[]])

        TextCA = Label(fBaseFrame, text= "CA config", 
            style= "fLabelGeneralBold.TLabel", width= TEXTBOX_WIDTH_SEQ)
        TextCA.pack(side= LEFT, padx= 5, pady= 5)

    elif (strMethod == LSV):
        ButtonLSV = Button(fBaseFrame, image=self._IconLSV, command= lambda : 
            self._clickSequenceMethod(BUTTON_SM_PARA_EC_LSV, ButtonLSV))        
        ButtonLSV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)
        self._SequenceList.append([ButtonLSV, LSV,[],[]])

        TextLSV = Label(fBaseFrame, text= "LSV config", 
            style= "fLabelGeneralBold.TLabel", width= TEXTBOX_WIDTH_SEQ)
        TextLSV.pack(side= LEFT, padx= 5, pady= 5)

    elif (strMethod == CV):
        ButtonCV = Button(fBaseFrame, image=self._IconCV, command= lambda : 
            self._clickSequenceMethod(BUTTON_SM_PARA_EC_CV, ButtonCV))        
        ButtonCV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)
        self._SequenceList.append([ButtonCV, CV,[],[]])

        TextCV = Label(fBaseFrame, text= "CV config", 
            style= "fLabelGeneralBold.TLabel", width= TEXTBOX_WIDTH_SEQ)
        TextCV.pack(side= LEFT, padx= 5, pady= 5)

    elif (strMethod == NPV):
        ButtonNPV = Button(fBaseFrame, image=self._IconNPV, command= lambda : 
            self._clickSequenceMethod(BUTTON_SM_PARA_EC_NPV, ButtonNPV))        
        ButtonNPV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)
        self._SequenceList.append([ButtonNPV, NPV,[],[]])

        TextNPV = Label(fBaseFrame, text= "NPV config", 
            style= "fLabelGeneralBold.TLabel", width= TEXTBOX_WIDTH_SEQ)
        TextNPV.pack(side= LEFT, padx= 5, pady= 5)

    elif (strMethod == DPV):
        ButtonDPV = Button(fBaseFrame, image=self._IconDPV, command= lambda : 
            self._clickSequenceMethod(BUTTON_SM_PARA_EC_DPV, ButtonDPV))        
        ButtonDPV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)
        self._SequenceList.append([ButtonDPV, DPV,[],[]])

        TextDPV = Label(fBaseFrame, text= "DPV config", 
            style= "fLabelGeneralBold.TLabel", width= TEXTBOX_WIDTH_SEQ)
        TextDPV.pack(side= LEFT, padx= 5, pady= 5)

    elif (strMethod == SWV):
        ButtonSWV = Button(fBaseFrame, image=self._IconSWV, command= lambda : 
            self._clickSequenceMethod(BUTTON_SM_PARA_EC_SWV, ButtonSWV))        
        ButtonSWV.pack(side= LEFT, fill= Y, padx = 5, pady= 5)
        self._SequenceList.append([ButtonSWV, SWV,[],[]])
        
        TextSWV = Label(fBaseFrame, text= "SWV config", 
            style= "fLabelGeneralBold.TLabel")
        TextSWV.pack(side= LEFT, padx= 5, pady= 5)

    # Add frame displaying the used template
    fUsedTemplate = Frame(fBaseFrame, style="fWidgetButton.TFrame")
    fUsedTemplate.pack(side= TOP, padx= 5, pady= 5, anchor= W)

    TextTemplate = Label(fUsedTemplate, text= "Template :", 
        style= "fLabelGeneralBold.TLabel", width= TEXTBOX_WIDTH_SEQ_NAME)
    TextTemplate.pack(side= TOP, padx= 5)

    TextTemplate = Label(fUsedTemplate, text= "Undefined", 
        style= "fLabelGeneral.TLabel", width= TEXTBOX_WIDTH_SEQ_NAME)
    TextTemplate.pack(side= TOP, padx= 5)

def _update_CentralFrame_Sequence_Load(self) -> None:
    """
    Description
    -----------
    Method for recreating the sequence based on the loaded sequence 
    configuration.
        
    """   
    # Reset sequence list
    self._SequenceList = []
    self._strFocusedFrame = None

    # Temporary save experiment parameters
    listExperimentParameters : list = self._dataHandling.get_ExperimentParameters()

    # Update template name
    self._strTemplateSeq.set(self._dataHandling.get_TemplateName())

    # Update sequence cycle
    self._strCycleSeq.set(self._dataHandling.get_SequenceCycles())

    # Loop over all experiments in the sequence
    for iIndex in range(len(listExperimentParameters)):
        # Add method to the list
        self._update_CentralFrame_Sequence_Add(listExperimentParameters[iIndex][0])
        
        # Change text in widget to the template name
        Widget.nametowidget(self._Root, self._SequenceList[iIndex][0].
            winfo_parent() + ".!frame.!label2").configure(
            text = listExperimentParameters[iIndex][1])
        
        # Save template name of methods in sequence
        self._SequenceList[iIndex][2] = listExperimentParameters[iIndex][1]

        # Save experiment parameters
        self._SequenceList[iIndex][3] = listExperimentParameters[iIndex][2]

def _valdiate_ArrayEntries(strInput : str, acttyp) -> bool:
    """
    Description
    -----------
    Helper method used for validation of entry widgets which require an array
    as input.

    Parameters
    ----------
    `strInput` : string
        Input string which should be validated

    Return
    ------
    `bValidateResult` : bool
        Result of the validation encoded as integer

    """
    if (acttyp == '1'):
        if (strInput != "," and strInput != "." and strInput != " " and 
            strInput != "+" and strInput != "-" and strInput != "e" and 
            not strInput.isdigit()):
            return False

    return True

def _valdiate_ValueEntries(strInput : str, acttyp) -> bool:
    """
    Description
    -----------
    Helper method used for validation of entry widgets with only one parameter

    Parameters
    ----------
    `strInput` : string
        Input string which should be validated

    Return
    ------
    `bValidateResult` : bool
        Result of the validation encoded as integer

    """
    if (acttyp == '1'):
        if (strInput != "." and strInput != "+" and strInput != "-" and 
            strInput != "e" and not strInput.isdigit()):
            return False

    return True

def _valdiate_ValueEntriesPositive(strInput : str, acttyp) -> bool:
    """
    Description
    -----------
    Helper method used for validation of entry widgets with only one positive
    parameter.

    Parameters
    ----------
    `strInput` : string
        Input string which should be validated

    Return
    ------
    `bValidateResult` : bool
        Result of the validation encoded as integer

    """
    if (acttyp == '1'):
        if (not strInput.isdigit()):
            return False

    return True