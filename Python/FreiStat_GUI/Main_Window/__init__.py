"""
Main window class of the FreiStat interface.

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

# Import dependencies
import logging
import os
from tkinter import *
from tkinter.ttk import *
from FreiStat.Data_storage.constants import *

# Import internal dependencies
from ..Data_Storage.constants import *
from ..Data_Storage.data_handling import DataHandling
from ..PopUp_Window import FreiStatPopUp
from ..Utility.positioning import _calculate_WindowPosition

class QueueHandler(logging.Handler):
    """
    Description
    -----------
    Class implementing custom print functionality for logging.Logger

    """

    def __init__(self, listBox):
        """
        Description
        -----------
        Overwritten logging handler constructor
        
        """
        super().__init__()
        self._listBox = listBox
        self.formatter = None

    def emit(self, record):
        """
        Description
        -----------
        Method called by the logger when a message should be printed
        
        """
        self._listBox.insert("end", record.msg)
        self._listBox.yview("end")

class FreiStatInterface():
    """
    Description
    -----------
    Class for implementing the main window of the FreiStat interface
    """

    from .CentralFrame import _create_CentralFrame
    from .CentralFrame import _create_UtilitybandFrame
    from .CentralFrame import _update_CentralFrame_EntryScreen
    from .CentralFrame import _update_CentralFrame_Base
    from .CentralFrame import _update_CentralFrame_Options
    from .CentralFrame import _update_CentralFrame_CA
    from .CentralFrame import _update_CentralFrame_LSV
    from .CentralFrame import _update_CentralFrame_CV
    from .CentralFrame import _update_CentralFrame_NPV
    from .CentralFrame import _update_CentralFrame_DPV
    from .CentralFrame import _update_CentralFrame_SWV
    from .CentralFrame import _update_CentralFrame_Sequence
    from .CentralFrame import _update_CentralFrame_Sequence_Add
    from .CentralFrame import _update_CentralFrame_Sequence_Load
    from .CentralFrame import _createAdvancedSettingFrame

    from .Events import _on_focus_out
    from .Events import _on_resize
    from .Events import _bound_MouseWheel
    from .Events import _unbound_MouseWheel
    from .Events import _onMouseWheel

    from .Experiment import _executeExperiment
    from .Experiment import _executeSequence
    from .Experiment import _executeSingleMethod

    from .Menuband import _create_MenubandFrame

    from .Optionband import _create_OptionbandFrame
    from .Optionband import _update_OptionbandFrame_SingleMode
    from .Optionband import _update_OptionbandFrame_SequeneceMode
    from .Optionband import _popupEcMethod

    from .Parameterband import _create_ParameterbandFrame
    from .Parameterband import _update_PrameterbandFrame
    from .Parameterband import _update_PrameterbandFrame_Template
    from .Parameterband import _update_PrameterbandFrame_TemplateSequence
    from .Parameterband import _onSelect

    from .Plotband import _create_PlotbandFrame
    from .Plotband import _create_PlotbandTabFrame
    from .Plotband import _update_PlotbandFrame_Plots
    from .Plotband import _update_PlotbandFrame_Terminal
    from .Plotband import _multiscroll_plotband
    
    from .Ribbon import _create_RibbonFrame

    from .Style import _LoadIcons
    from .Style import _StyleConfig

    from .Utility import _decodeExperimentParameters
    from .Utility import _decodeOptimizerParameters
    from .Utility import _decodeSystemStatus
    from .Utility import _openFileExplorer
    from .Utility import _shorten_decimals

    from .Widgets import _clickButton
    from .Widgets import _clickCheckButton
    from .Widgets import _clickMinimizeButton
    from .Widgets import _clickRibbonButton
    from .Widgets import _clickSequenceMethod
    from .Plotband import _on_mouse_press

    def __init__(self) -> None:
        """
        Description
        -----------
        Constructor of the class FreiStatInterface.
        
        """
        # Intialize class variables
        self._bAppRunning : bool= True
        self._bPlotbandHidden : bool = False

        self._iNavIndex : int = NI_SINGLE_MODE
        self._iSystemStatus : int = FS_WAITING
        self._iPlotIDprevious : int = None

        self._strMethod : str = UNDEFIEND
        self._strFocusedFrame : str = None
        self._strOsPath : str = ""
        self._strAssetPath : str = __path__[0] + './../'
        self._strOsPathBackup : str = self._strAssetPath + "./backup/backup.fst"

        self._listCanvas : list = []
        self._listCanvasPressIDs : list = []
        self._listFigures : list = []
        self._SequenceList : list = []

        self._fig  = None
        self._fStaticPlot = None

        # save current working directory of the interface
        self._strRootPath = os.getcwd()

        # Create root window object
        self._Root = Tk()
        
        # Calculate center coordinations
        iCenterX, iCenterY = _calculate_WindowPosition(self._Root)
        
        # Position window in the middle of the screen
        self._Root.geometry(f'{int(self._Root.winfo_screenwidth()*  0.8)}x{int(self._Root.winfo_screenheight()*0.8)}+{iCenterX}+{iCenterY}')

        # Add protocol to closing the main window
        self._Root.protocol("WM_DELETE_WINDOW", self._on_Closing)

        # Set title of the main window
        self._Root.title("FreiStat")

        # Set icon of the main window
        img = PhotoImage(file= self._strAssetPath + '/assets/logo/FreiStat.gif')
        self._Root.tk.call('wm', 'iconphoto', self._Root._w, img)

        # Create all styles used by the interface
        self._StyleConfig()

        # Load all icons
        self._LoadIcons()

        # Initialize entry box values
        self._iAdvancedSetting = IntVar(value= 0)
        self._iFixedWEPotential = IntVar(value= 1)
        self._iMainsFilter = IntVar(value= 0)
        self._iEnableOptimizer = IntVar(value= 1)
        self._iLowPerformanceMode = IntVar(value= 0)
        self._iGlobalLowPerformanceMode = IntVar(value= 0)
        self._iWLANMode = IntVar(value= 0)

        self._strBaseVoltage = StringVar()
        self._strStartVoltage = StringVar()
        self._strStopVoltage = StringVar()
        self._strLowerVoltage = StringVar()
        self._strUpperVoltage = StringVar()
        self._strPotentialSteps = StringVar()
        self._strPulseLengths = StringVar()
        self._strDeltaVStaircase = StringVar()
        self._strDeltaVPeak = StringVar()
        self._strStepsize = StringVar()
        self._strScanrate = StringVar()
        self._strSamplingRate = StringVar()
        self._strSamplingDuration = StringVar()
        self._strCycle = StringVar()
        self._strDutyCycle = StringVar()
        self._strCurrentrange = StringVar()
        self._strOsrSinc2 = StringVar()
        self._strOsrSinc3 = StringVar()
        self._strCycleSeq = StringVar()

        self._strGLpmLatency = StringVar()
        self._strServerIP = StringVar()
        self._strServerPort = StringVar()
        self._strClientIP = StringVar()
        self._strClientPort = StringVar()

        self._strInfo = StringVar()
        self._strTerminal = StringVar()
        self._strTemplate = StringVar()
        self._strTemplateSeq = StringVar()

        # Create instance of the data handling
        self._dataHandling = DataHandling(self._strRootPath)

        # Create base for PopUp windoes
        self._PopUpWindow = FreiStatPopUp(iCenterX, iCenterY)

        # Crfeate the different sub frames inside the main window
        # Ribbon at the most top
        self._create_RibbonFrame(self._Root)

        # Menu band at the top
        self._create_MenubandFrame(self._Root)

        # Option band at the left side
        self._create_OptionbandFrame(self._Root)
        self._update_OptionbandFrame_SingleMode(self._fOptionBand)

        # Parameter band the right side
        self._create_ParameterbandFrame(self._Root)
        self._update_PrameterbandFrame_Template(self._fParameterBand)

        # Central frame in the middle
        self._create_CentralFrame(self._Root)

        # Plot band at the bottom
        self._create_PlotbandTabFrame(self._Root)
        self._create_PlotbandFrame(self._Root)

        # Setup logger for the interface
        self._logger = logging.getLogger("FreiStat_Interface")
        self._logger.setLevel(logging.INFO)

        handler = QueueHandler(self._TextTerminal)
        handler.setLevel(logging.INFO)
        
        formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

        # Import safety backup
        self._dataHandling.set_DataStorages(
            self._dataHandling.import_Configuration(self._strOsPathBackup))

        # Import settings
        self._dataHandling.import_Settings()
        self._updatePreferences()

        # Show entry screen
        self._update_CentralFrame_EntryScreen(self._fCentralFrame)

        # Call main loop
        self.Main()

    def Main(self) -> None:
        """
        Description
        -----------
        Main loop of the interface

        """
        # Loop until window is closed
        while(self._bAppRunning):
            # Check if experiment is still running
            if (self._iSystemStatus ==  FS_RUNNING and 
                self._process.is_alive() == False):
                # Update system status
                self._iSystemStatus = FS_COMPLETED
                
                # Enable start button and disable stop / live feed button
                self._ButtonStart["state"] = NORMAL
                self._ButtonStop["state"] = DISABLED
                self._ButtonLiveFeed["state"] = DISABLED

                self._TextInfo.configure(style= "fLabelCompleted.TLabel")

            elif (self._iSystemStatus == FS_STOP):
                self._TextInfo.configure(style= "fLabelCanceled.TLabel")

            # Update info box with current system status
            self._strInfo.set(self._decodeSystemStatus(self._iSystemStatus))

            # Update interface
            self._Root.update_idletasks()
            self._Root.update()     

    def _createSpacerFrame(self, parentFrame : Frame, strStyle : str) -> None:
        """
        Description
        -----------
        Method for creating a spacer frame to visually separate different
        widgets in the interface.

        Parameters
        ----------
        `parentFrame` : Frame
            Parent frame in which the parameter band frame is embedded

        `strStyle` : string
            String encoding the style of the spacer frame.
            
        """    
        fSpacerFrame = Frame(parentFrame, style= strStyle)
        fSpacerFrame.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 10) 
  
    def _clearFrame(self, frame : Frame) -> None:
        """
        Description
        -----------
        Helper method for clearing given frame of all widgets

        Parameters
        ----------
        `frame` : Frame
            Frame which should be cleared
        
        """
        # Get list of all widgets in the Frame
        listWidget : list = frame.pack_slaves()

        # Loop over all widgets
        for widget in listWidget:
            widget.destroy()

    def _hideFrame(self, frame : Frame) -> None:
        """
        Description
        -----------
        Helper method for hiding all elements in a frame.

        Parameters
        ----------
        `frame` : Frame
            Frame whose widgets should be hidden
        
        """
        # Get list of all widgets in the Frame
        listWidget : list = frame.pack_slaves()

        # Loop over all widgets
        for widget in listWidget:
            widget.pack_forget() 

    def _showFrame(self, frame : Frame) -> None:
        """
        Description
        -----------
        Helper method for showing all elements in a frame.

        Parameters
        ----------
        `frame` : Frame
            Frame whose widgets should be hidden
        
        """
        # Get list of all widgets in the Frame
        listWidget : list = frame.pack_slaves()

        # Loop over all widgets
        for widget in listWidget:
            widget.pack() 

    def _updatePreferences(self) -> None:
        """
        Description
        -----------
        Helper method which updates displayed settings

        """
        # Read preferences
        listPreferences : list = self._dataHandling.get_Preferences()

        # Load preferences
        # Loop over all parameters
        for iIndex in range(len(listPreferences)):
            # Low performance mode
            if (listPreferences[iIndex][0] == SET_GLPM):
                self._iGlobalLowPerformanceMode.set(listPreferences[iIndex][1])
            # Low performance mode latency
            elif (listPreferences[iIndex][0] == SET_GLPM_LATENCY):
                self._strGLpmLatency.set(listPreferences[iIndex][1]) 
            # Wlan mode
            elif (listPreferences[iIndex][0] == SET_WLAN_MODE):
                self._iWLANMode.set(listPreferences[iIndex][1])         
            # Server IP
            elif (listPreferences[iIndex][0] == SET_SERVER_IP):
                self._strServerIP.set(listPreferences[iIndex][1])  
            # Server port
            elif (listPreferences[iIndex][0] == SET_SERVER_PORT):
                self._strServerPort.set(listPreferences[iIndex][1])  
            # Client IP
            elif (listPreferences[iIndex][0] == SET_CLIENT_IP):
                self._strClientIP.set(listPreferences[iIndex][1])  
            # Client port
            elif (listPreferences[iIndex][0] == SET_CLIENT_PORT):
                self._strClientPort.set(listPreferences[iIndex][1])  

    def _savePreferences(self) -> None:
        """
        Description
        -----------
        Helper method which saves the settings

        """
        listPreferences : list = [
            [SET_GLPM, self._iGlobalLowPerformanceMode.get()],
            [SET_GLPM_LATENCY, self._strGLpmLatency.get()],
            [SET_WLAN_MODE, self._iWLANMode.get()],
            [SET_SERVER_IP, self._strServerIP.get()],
            [SET_SERVER_PORT, self._strServerPort.get()],
            [SET_CLIENT_IP, self._strClientIP.get()],
            [SET_CLIENT_PORT, self._strClientPort.get()]
        ]

        # Save preferences
        self._dataHandling.set_Preferences(listPreferences)

    def _initEntries(self, strMethod : str) -> None:
        """
        Description
        -----------
        Helper method which initializes the entries of the different ec-methods,
        with their default values.

        Parameters
        ----------
        `strMethod` : string
            Electrochemical method encoded as string.

        """
        # Uncheck advanced setting button
        self._iAdvancedSetting.set(0)

        # Load global value of low performance mode
        self._iLowPerformanceMode.set(self._iGlobalLowPerformanceMode.get())

        if (strMethod == CA):
            self._strPotentialSteps.set(str(START_POTENTIAL_F) + " , " + 
                str(START_POTENTIAL_F))
            self._strPulseLengths.set(str(PULSE_LENGTH_F) + " , " + 
                str(PULSE_LENGTH_F))
            self._strSamplingRate.set(SAMPLING_RATE_F)
            self._strCycle.set(CYCLE_I)
            self._strCurrentrange.set(CURRENT_RANGE_F)
            self._strOsrSinc2.set(SINC2_OVERSAMPLING_I)
            self._strOsrSinc3.set(SINC3_OVERSAMPLING_I)

        elif (strMethod == LSV):
            self._strStartVoltage.set(START_POTENTIAL_F)
            self._strStopVoltage.set(UPPER_POTENTIAL_F)
            self._strStepsize.set(STEP_SIZE_F)
            self._strScanrate.set(SCAN_RATE_F)
            self._strCycle.set(CYCLE_I)
            self._strCurrentrange.set(CURRENT_RANGE_F)
            self._strOsrSinc2.set(SINC2_OVERSAMPLING_I)
            self._strOsrSinc3.set(SINC3_OVERSAMPLING_I)

        elif (strMethod == CV):
            self._strStartVoltage.set(START_POTENTIAL_F)
            self._strLowerVoltage.set(LOWER_POTENTIAL_F)
            self._strUpperVoltage.set(UPPER_POTENTIAL_F)
            self._strStepsize.set(STEP_SIZE_F)
            self._strScanrate.set(SCAN_RATE_F)
            self._strCycle.set(CYCLE_I)
            self._strCurrentrange.set(CURRENT_RANGE_F)
            self._strOsrSinc2.set(SINC2_OVERSAMPLING_I)
            self._strOsrSinc3.set(SINC3_OVERSAMPLING_I)

        elif (strMethod == NPV):
            self._strBaseVoltage.set(BASE_POTENTIAL_F)
            self._strStartVoltage.set(START_POTENTIAL_F)
            self._strStopVoltage.set(UPPER_POTENTIAL_F)
            self._strDeltaVStaircase.set(DELTA_V_STAIRCASE_F)
            self._strPulseLengths.set(str(PULSE_LENGTH_F) + " , " + 
                str(PULSE_LENGTH_F))
            self._strSamplingDuration.set(SAMPLING_DURATION_F)
            self._strCycle.set(CYCLE_I)
            self._strCurrentrange.set(CURRENT_RANGE_F)
            self._strOsrSinc2.set(SINC2_OVERSAMPLING_I)
            self._strOsrSinc3.set(SINC3_OVERSAMPLING_I)

        elif (strMethod == DPV):
            self._strStartVoltage.set(START_POTENTIAL_F)
            self._strStopVoltage.set(UPPER_POTENTIAL_F)
            self._strDeltaVStaircase.set(DELTA_V_STAIRCASE_F)
            self._strDeltaVPeak.set(DELTA_V_PEAK_F)
            self._strPulseLengths.set(str(PULSE_LENGTH_F) + " , " + 
                str(PULSE_LENGTH_F))
            self._strSamplingDuration.set(SAMPLING_DURATION_F)
            self._strCycle.set(CYCLE_I)
            self._strCurrentrange.set(CURRENT_RANGE_F)
            self._strOsrSinc2.set(SINC2_OVERSAMPLING_I)
            self._strOsrSinc3.set(SINC3_OVERSAMPLING_I)

        elif (strMethod == SWV):
            self._strStartVoltage.set(START_POTENTIAL_F)
            self._strStopVoltage.set(UPPER_POTENTIAL_F)
            self._strDeltaVStaircase.set(DELTA_V_STAIRCASE_F)
            self._strDeltaVPeak.set(DELTA_V_PEAK_F)
            self._strDutyCycle.set(PULSE_LENGTH_F)
            self._strSamplingDuration.set(SAMPLING_DURATION_F)
            self._strCycle.set(CYCLE_I)
            self._strCurrentrange.set(CURRENT_RANGE_F)
            self._strOsrSinc2.set(SINC2_OVERSAMPLING_I)
            self._strOsrSinc3.set(SINC3_OVERSAMPLING_I)

    def _updateEntries(self, strMethod : str) -> None:
        """
        Description
        -----------
        Helper method which updates the entries of the different ec-methods,
        with their default values.

        Parameters
        ----------
        `strMethod` : string
            Electrochemical method encoded as string.

        """
        # Initialize variables
        listExperimentParameters : list = []

        # Uncheck advanced setting button
        self._iAdvancedSetting.set(0)

        # Check which method is used
        if(self._dataHandling.get_ExperimentType() == SEQUENCE):
            for iIndex in range(len(self._SequenceList)):
                if(self._SequenceList[iIndex][0].winfo_parent() == 
                    self._strFocusedFrame):
                    listExperimentParameters = self._SequenceList[iIndex][3]
                    self._strTemplate.set(self._SequenceList[iIndex][2])

            # Check if entry was found
            if (not listExperimentParameters):
                self._initEntries(strMethod)
                return

        else :
            # Get experiment paramters
            listExperimentParameters = self._dataHandling. \
                get_ExperimentParameters()
            
            self._strTemplate.set(self._dataHandling.get_TemplateName())

        if (strMethod == CA):
            strTemp : str = ""
            for iIndex in range(len(listExperimentParameters[0][1])):
                strTemp += str(listExperimentParameters[0][1][iIndex])
                if (iIndex < len(listExperimentParameters[0][1]) - 1):
                    strTemp += " , "
            self._strPotentialSteps.set(strTemp)
            
            strTemp = ""
            for iIndex in range(len(listExperimentParameters[1][1])):
                strTemp += str(listExperimentParameters[1][1][iIndex])
                if (iIndex < len(listExperimentParameters[1][1]) - 1):
                    strTemp += " , "
            self._strPulseLengths.set(strTemp)
            self._strSamplingRate.set(self._shorten_decimals(listExperimentParameters[2][1], 3))
            self._strCycle.set(listExperimentParameters[3][1])
            self._strCurrentrange.set(self._shorten_decimals(listExperimentParameters[4][1], 6))
            self._iMainsFilter.set(listExperimentParameters[5][1])
            self._strOsrSinc2.set(listExperimentParameters[6][1])
            self._strOsrSinc3.set(listExperimentParameters[7][1])
            self._iEnableOptimizer.set(listExperimentParameters[8][1])
            self._iLowPerformanceMode.set(listExperimentParameters[9][1])

        elif (strMethod == LSV):
            self._strStartVoltage.set(self._shorten_decimals(listExperimentParameters[0][1], 3))
            self._strStopVoltage.set(self._shorten_decimals(listExperimentParameters[1][1], 3))
            self._strStepsize.set(self._shorten_decimals(listExperimentParameters[2][1], 6))
            self._strScanrate.set(self._shorten_decimals(listExperimentParameters[3][1], 3))
            self._strCycle.set(listExperimentParameters[4][1])
            self._strCurrentrange.set(self._shorten_decimals(listExperimentParameters[5][1], 6))
            self._iFixedWEPotential.set(listExperimentParameters[6][1])
            self._iMainsFilter.set(listExperimentParameters[7][1])
            self._strOsrSinc2.set(listExperimentParameters[8][1])
            self._strOsrSinc3.set(listExperimentParameters[9][1])
            self._iEnableOptimizer.set(listExperimentParameters[10][1])
            self._iLowPerformanceMode.set(listExperimentParameters[11][1])

        elif (strMethod == CV):
            self._strStartVoltage.set(self._shorten_decimals(listExperimentParameters[0][1], 3))
            self._strLowerVoltage.set(self._shorten_decimals(listExperimentParameters[1][1], 3))
            self._strUpperVoltage.set(self._shorten_decimals(listExperimentParameters[2][1], 3))
            self._strStepsize.set(self._shorten_decimals(listExperimentParameters[3][1], 6))
            self._strScanrate.set(self._shorten_decimals(listExperimentParameters[4][1], 3))
            self._strCycle.set(listExperimentParameters[5][1])
            self._strCurrentrange.set(self._shorten_decimals(listExperimentParameters[6][1], 6))
            self._iFixedWEPotential.set(listExperimentParameters[7][1])
            self._iMainsFilter.set(listExperimentParameters[8][1])
            self._strOsrSinc2.set(listExperimentParameters[9][1])
            self._strOsrSinc3.set(listExperimentParameters[10][1])
            self._iEnableOptimizer.set(listExperimentParameters[11][1])
            self._iLowPerformanceMode.set(listExperimentParameters[12][1])

        elif (strMethod == NPV):
            self._strBaseVoltage.set(self._shorten_decimals(listExperimentParameters[0][1], 3))
            self._strStartVoltage.set(self._shorten_decimals(listExperimentParameters[1][1], 3))
            self._strStopVoltage.set(self._shorten_decimals(listExperimentParameters[2][1], 3))
            self._strDeltaVStaircase.set(self._shorten_decimals(listExperimentParameters[3][1], 6))
            strTemp : str = ""
            for iIndex in range(len(listExperimentParameters[4][1])):
                strTemp += str(listExperimentParameters[4][1][iIndex])
                if (iIndex < len(listExperimentParameters[4][1]) - 1):
                    strTemp += " , "
            self._strPulseLengths.set(strTemp)
            self._strSamplingDuration.set(self._shorten_decimals(listExperimentParameters[5][1], 6))
            self._strCycle.set(listExperimentParameters[6][1])
            self._strCurrentrange.set(self._shorten_decimals(listExperimentParameters[7][1], 6))
            self._iFixedWEPotential.set(listExperimentParameters[8][1])
            self._iMainsFilter.set(listExperimentParameters[9][1])
            self._strOsrSinc2.set(listExperimentParameters[10][1])
            self._strOsrSinc3.set(listExperimentParameters[11][1])
            self._iEnableOptimizer.set(listExperimentParameters[12][1])
            self._iLowPerformanceMode.set(listExperimentParameters[13][1])

        elif (strMethod == DPV):
            self._strStartVoltage.set(self._shorten_decimals(listExperimentParameters[0][1], 3))
            self._strStopVoltage.set(self._shorten_decimals(listExperimentParameters[1][1], 3))
            self._strDeltaVStaircase.set(self._shorten_decimals(listExperimentParameters[2][1], 6))
            self._strDeltaVPeak.set(self._shorten_decimals(listExperimentParameters[3][1], 6))
            strTemp : str = ""
            for iIndex in range(len(listExperimentParameters[4][1])):
                strTemp += str(listExperimentParameters[4][1][iIndex])
                if (iIndex < len(listExperimentParameters[4][1]) - 1):
                    strTemp += " , "
            self._strPulseLengths.set(strTemp)
            self._strSamplingDuration.set(self._shorten_decimals(listExperimentParameters[5][1], 6))
            self._strCycle.set(listExperimentParameters[6][1])
            self._strCurrentrange.set(self._shorten_decimals(listExperimentParameters[7][1], 6))
            self._iFixedWEPotential.set(listExperimentParameters[8][1])
            self._iMainsFilter.set(listExperimentParameters[9][1])
            self._strOsrSinc2.set(listExperimentParameters[10][1])
            self._strOsrSinc3.set(listExperimentParameters[11][1])
            self._iEnableOptimizer.set(listExperimentParameters[12][1])
            self._iLowPerformanceMode.set(listExperimentParameters[13][1])

        elif (strMethod == SWV):
            if (type(listExperimentParameters[4][1]) == list):
                listExperimentParameters[4][1] = sum(listExperimentParameters[4][1])
            self._strStartVoltage.set(self._shorten_decimals(listExperimentParameters[0][1], 3))
            self._strStopVoltage.set(self._shorten_decimals(listExperimentParameters[1][1], 3))
            self._strDeltaVStaircase.set(self._shorten_decimals(listExperimentParameters[2][1], 6))
            self._strDeltaVPeak.set(self._shorten_decimals(listExperimentParameters[3][1], 6))
            self._strDutyCycle.set(self._shorten_decimals(listExperimentParameters[4][1], 6))
            self._strSamplingDuration.set(self._shorten_decimals(listExperimentParameters[5][1], 6))
            self._strCycle.set(listExperimentParameters[6][1])
            self._strCurrentrange.set(self._shorten_decimals(listExperimentParameters[7][1], 6))
            self._iFixedWEPotential.set(listExperimentParameters[8][1])
            self._iMainsFilter.set(listExperimentParameters[9][1])
            self._strOsrSinc2.set(listExperimentParameters[10][1])
            self._strOsrSinc3.set(listExperimentParameters[11][1])
            self._iEnableOptimizer.set(listExperimentParameters[12][1])
            self._iLowPerformanceMode.set(listExperimentParameters[13][1])

    def _saveEntries(self) -> None:
        """
        Description
        -----------
        Helper method which saves the entries of the different ec-methods.

        """
        # Check if sequence mode is used or not
        if (self._iNavIndex == NI_SEQ_MODE):
            # Save template name
            self._dataHandling.save_TemplateName(self._strTemplateSeq.get())

            # Save sequence length
            self._dataHandling.save_SequenceCycles(int(self._strCycleSeq.get()))

            # Save experiment type
            self._dataHandling.save_ExperimentType(SEQUENCE)

            # Sequence mode
            if (self._iNavIndex == NI_SEQ_MODE):
                listTempExperimentParameters = []

                for iIndex in range(len(self._SequenceList)):
                    listTempExperimentParameters.append(
                        [self._SequenceList[iIndex][1], 
                        self._SequenceList[iIndex][2], 
                        self._SequenceList[iIndex][3]])
                
                self._dataHandling.save_ExperimentParmeters(
                    listTempExperimentParameters)
        else :
            # Save template name
            self._dataHandling.save_TemplateName(self._strTemplate.get())

            # Save experiment type
            self._dataHandling.save_ExperimentType(self._strMethod)

            # Save experiment parameters
            self._dataHandling.save_ExperimentParmeters(self._saveEntriesInList())

    def _saveEntriesInList(self) -> list :
        """
        Description
        -----------
        Helper method which saves the entries of the different ec-methods in a
        list which is then returned

        Return
        ------
        `listTempExperimentParameters` : list
            List containing the experiment paramters

        """
        if (self._strMethod == CA): 
            listTempExperimentParameters = [
                [POTENTIAL_STEPS, [float(x) for x in 
                    self._strPotentialSteps.get().split(",")]],
                [PULSE_LENGTH, [float(x) for x in 
                    self._strPulseLengths.get().split(",")]],
                [SAMPLING_RATE, float(self._strSamplingRate.get())],
                [CYCLE, int(self._strCycle.get())],
                [LPTIA_RTIA_SIZE, float(self._strCurrentrange.get())],
                [MAINS_FILTER, bool(self._iMainsFilter.get())],
                [SINC2_OVERSAMPLING, int(self._strOsrSinc2.get())],
                [SINC3_OVERSAMPLING ,int(self._strOsrSinc3.get())],
                [ENABLE_OPTIMIZER, bool(self._iEnableOptimizer.get())],
                [LOW_PERFORMANCE_MODE, bool(self._iLowPerformanceMode.get())]]

        elif (self._strMethod == LSV): 
            listTempExperimentParameters = [
                [START_POTENTIAL, float(self._strStartVoltage.get())],
                [STOP_POTENTIAL, float(self._strStopVoltage.get())],
                [STEP_SIZE, float(self._strStepsize.get())],
                [SCAN_RATE, float(self._strScanrate.get())],
                [CYCLE, int(self._strCycle.get())],
                [LPTIA_RTIA_SIZE, float(self._strCurrentrange.get())],
                [FIXED_WE_POTENTIAL, bool(self._iFixedWEPotential.get())],
                [MAINS_FILTER, bool(self._iMainsFilter.get())],
                [SINC2_OVERSAMPLING, int(self._strOsrSinc2.get())],
                [SINC3_OVERSAMPLING ,int(self._strOsrSinc3.get())],
                [ENABLE_OPTIMIZER, bool(self._iEnableOptimizer.get())],
                [LOW_PERFORMANCE_MODE, bool(self._iLowPerformanceMode.get())]]

        elif (self._strMethod == CV): 
            listTempExperimentParameters = [
                [START_POTENTIAL, float(self._strStartVoltage.get())],
                [LOWER_POTENTIAL, float(self._strLowerVoltage.get())],
                [UPPER_POTENTIAL, float(self._strUpperVoltage.get())],
                [STEP_SIZE, float(self._strStepsize.get())],
                [SCAN_RATE, float(self._strScanrate.get())],
                [CYCLE, int(self._strCycle.get())],
                [LPTIA_RTIA_SIZE, float(self._strCurrentrange.get())],
                [FIXED_WE_POTENTIAL, bool(self._iFixedWEPotential.get())],
                [MAINS_FILTER, bool(self._iMainsFilter.get())],
                [SINC2_OVERSAMPLING, int(self._strOsrSinc2.get())],
                [SINC3_OVERSAMPLING ,int(self._strOsrSinc3.get())],
                [ENABLE_OPTIMIZER, bool(self._iEnableOptimizer.get())],
                [LOW_PERFORMANCE_MODE, bool(self._iLowPerformanceMode.get())]]

        elif (self._strMethod == NPV): 
            listTempExperimentParameters = [
                [BASE_POTENTIAL, float(self._strBaseVoltage.get())],
                [START_POTENTIAL, float(self._strStartVoltage.get())],
                [STOP_POTENTIAL, float(self._strStopVoltage.get())],
                [DELTA_V_STAIRCASE, float(self._strDeltaVStaircase.get())],
                [PULSE_LENGTH, [float(x) for x in 
                    self._strPulseLengths.get().split(",")]],
                [SAMPLING_DURATION, float(self._strSamplingDuration.get())],
                [CYCLE, int(self._strCycle.get())],
                [LPTIA_RTIA_SIZE, float(self._strCurrentrange.get())],
                [FIXED_WE_POTENTIAL, bool(self._iFixedWEPotential.get())],
                [MAINS_FILTER, bool(self._iMainsFilter.get())],
                [SINC2_OVERSAMPLING, int(self._strOsrSinc2.get())],
                [SINC3_OVERSAMPLING ,int(self._strOsrSinc3.get())],
                [ENABLE_OPTIMIZER, bool(self._iEnableOptimizer.get())],
                [LOW_PERFORMANCE_MODE, bool(self._iLowPerformanceMode.get())]]

        elif (self._strMethod == DPV): 
            listTempExperimentParameters = [
                [START_POTENTIAL, float(self._strStartVoltage.get())],
                [STOP_POTENTIAL, float(self._strStopVoltage.get())],
                [DELTA_V_STAIRCASE, float(self._strDeltaVStaircase.get())],
                [DELTA_V_PEAK, float(self._strDeltaVPeak.get())],
                [PULSE_LENGTH, [float(x) for x in 
                    self._strPulseLengths.get().split(",")]],
                [SAMPLING_DURATION, float(self._strSamplingDuration.get())],
                [CYCLE, int(self._strCycle.get())],
                [LPTIA_RTIA_SIZE, float(self._strCurrentrange.get())],
                [FIXED_WE_POTENTIAL, bool(self._iFixedWEPotential.get())],
                [MAINS_FILTER, bool(self._iMainsFilter.get())],
                [SINC2_OVERSAMPLING, int(self._strOsrSinc2.get())],
                [SINC3_OVERSAMPLING ,int(self._strOsrSinc3.get())],
                [ENABLE_OPTIMIZER, bool(self._iEnableOptimizer.get())],
                [LOW_PERFORMANCE_MODE, bool(self._iLowPerformanceMode.get())]]

        elif (self._strMethod == SWV): 
            listTempExperimentParameters = [
                [START_POTENTIAL, float(self._strStartVoltage.get())],
                [STOP_POTENTIAL, float(self._strStopVoltage.get())],
                [DELTA_V_STAIRCASE, float(self._strDeltaVStaircase.get())],
                [DELTA_V_PEAK, float(self._strDeltaVPeak.get())],
                [PULSE_LENGTH, float(self._strDutyCycle.get())],
                [SAMPLING_DURATION, float(self._strSamplingDuration.get())],
                [CYCLE, int(self._strCycle.get())],
                [LPTIA_RTIA_SIZE, float(self._strCurrentrange.get())],
                [FIXED_WE_POTENTIAL, bool(self._iFixedWEPotential.get())],
                [MAINS_FILTER, bool(self._iMainsFilter.get())],
                [SINC2_OVERSAMPLING, int(self._strOsrSinc2.get())],
                [SINC3_OVERSAMPLING ,int(self._strOsrSinc3.get())],
                [ENABLE_OPTIMIZER, bool(self._iEnableOptimizer.get())],
                [LOW_PERFORMANCE_MODE, bool(self._iLowPerformanceMode.get())]]

        return listTempExperimentParameters

    def _on_Closing(self):
        """
        Description
        -----------
        On closing event for the main window.

        """
        # Reset variable
        self._bAppRunning = False

        # Check if experiment is still running
        if (self._iSystemStatus == FS_RUNNING):
            # End experiment
            self._EcMethod._terminateExperiment()

        # Update the settings
        self._dataHandling.export_Settings()

        # Save safety backup
        self._dataHandling.export_Configuration(self._strOsPathBackup)

        # Close window
        self._Root.destroy()

