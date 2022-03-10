"""
Module containing constant naming which is used for user interface of the  
FreiStat software.

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

"""-----------------------------------------------------------------------------
| Interface: System status
|   
|   Constant              Value                     Meaning
-----------------------------------------------------------------------------"""
FS_WAITING              = 1             # FreiStat is in waiting mode
FS_RUNNING              = 2             # FreiStat experiment is running
FS_STOP                 = 3             # FreiStat experiment stopped
FS_COMPLETED            = 4             # FreiStat experiment completed

"""-----------------------------------------------------------------------------
| Interface: System status text
|   
|   Constant              Value                     Meaning
-----------------------------------------------------------------------------"""
FS_WAITING_STR          = "Waiting"     
FS_RUNNING_STR          = "Experiment\nrunning"   
FS_STOP_STR             = "Experiment\nstopped"
FS_COMPLETED_STR        = "Experiment\ncompleted"

"""-----------------------------------------------------------------------------
| Interface: Navigation indices
|   
|   Constant              Value                     Meaning
-----------------------------------------------------------------------------"""
NI_START_UP             = 0
NI_SINGLE_MODE          = 100
NI_SM_CA                = 101
NI_SM_LSV               = 102
NI_SM_CV                = 103
NI_SM_NPV               = 104
NI_SM_DPV               = 105
NI_SM_SWV               = 106
NI_SEQ_MODE             = 200


"""-----------------------------------------------------------------------------
| Main Window: Geometry
|   
|   Constant              Value                     Meaning
-----------------------------------------------------------------------------"""
MW_X_POSITION           = 1600          # Size of the main window in X direction
MW_Y_POSITION           = 900           # Size of the main window in Y direction

"""-----------------------------------------------------------------------------
| Main Window: Widget dimension
|   
|   Constant              Value                     Meaning
-----------------------------------------------------------------------------"""
TEXTBOX_WIDTH           = 25            # Width of a textbox in the interface
TEXTBOX_WIDTH_SMALL     = 15            # Width of a textbox in the interface
TEXTBOX_WIDTH_SEQ       = 10            # Width of a textbox in the sequence mode
TEXTBOX_WIDTH_SEQ_NAME  = 15            # Width of a template textbox in the sequence mode
TEXTBOX_WIDTH_SETTINGS  = 50            # Width of a textbox in the settings
ENTRY_WIDTH             = 25            # Width of a entry

"""-----------------------------------------------------------------------------
| Main Window: Button commands
|   
|   Constant              Value                     Meaning
-----------------------------------------------------------------------------"""
BUTTON_LIVEFEED         = 0             # Command for switching to the live feed
BUTTON_SINGLE_MODE      = 1             # Command for the single mode
BUTTON_SEQ_MODE         = 2             # Command for the sequence mode

BUTTON_START            = 3             # Command for starting the experiment
BUTTON_STOP             = 4             # Command for stopping the experiment

BUTTON_SAVE_TEMPLATE    = 5             # Command to save template
BUTTON_LOAD_TEMPLATE    = 6             # Command to laod template
BUTTON_DELETE_TEMPLATE  = 7             # Command to delete current template

BUTTON_SAVE_TEMP_SEQ    = 8             # Command to save sequence template
BUTTON_LOAD_TEMP_SEQ    = 9             # Command to laod sequence template
BUTTON_DELETE_TEMP_SEQ  = 10            # Command to delete sequence current template

BUTTON_ADD              = 11            # Command to add method to sequence
BUTTON_DELETE           = 12            # Command to delete method from sequence
BUTTON_MOVE_UP          = 13            # Command to move method up in sequence
BUTTON_MOVE_DOWN        = 14            # Command to move method down in sequnce

BUTTON_LOAD             = 15            # Command for loading an external saved config
BUTTON_SAVE             = 16            # Command for saving a config externally
BUTTON_SAVEAS           = 17            # Command for saving a config externally at a custom location
BUTTON_PREFERENCES      = 18            # Command for opening the option menu
BUTTON_HELP             = 19            # Command for opening the help window
BUTTON_ABOUT            = 20            # Command for opening the about window

BUTTON_TERMINAL         = 30            # Command for switching to the terminal window
BUTTON_PLOTS            = 31            # Command for switching to the plot window
BUTTON_MINIMIZE_PB      = 32            # Command for minimizing the plotband

BUTTON_EC_CA            = 100           # Command for chronoamperometry
BUTTON_EC_LSV           = 101           # Command for linear sweep voltammetry
BUTTON_EC_CV            = 102           # Command for cyclic voltammetry
BUTTON_EC_NPV           = 103           # Command for normal pulse voltammetry
BUTTON_EC_DPV           = 104           # Command for differential pulse voltammetry
BUTTON_EC_SWV           = 105           # Command for square wave voltammetry

BUTTON_SM_ADD_EC_CA     = 200           # Command for chronoamperometry
BUTTON_SM_ADD_EC_LSV    = 201           # Command for linear sweep voltammetry
BUTTON_SM_ADD_EC_CV     = 202           # Command for cyclic voltammetry
BUTTON_SM_ADD_EC_NPV    = 203           # Command for normal pulse voltammetry
BUTTON_SM_ADD_EC_DPV    = 204           # Command for differential pulse voltammetry
BUTTON_SM_ADD_EC_SWV    = 205           # Command for square wave voltammetry

BUTTON_SM_PARA_EC_CA    = 210           # Command for displaying the parameters of chronoamperometry
BUTTON_SM_PARA_EC_LSV   = 211           # Command for linear sweep voltammetry
BUTTON_SM_PARA_EC_CV    = 212           # Command for cyclic voltammetry
BUTTON_SM_PARA_EC_NPV   = 213           # Command for normal pulse voltammetry
BUTTON_SM_PARA_EC_DPV   = 214           # Command for differential pulse voltammetry
BUTTON_SM_PARA_EC_SWV   = 215           # Command for square wave voltammetry

"""-----------------------------------------------------------------------------
| Main Window: Check button commands
|   
|   Constant              Value                     Meaning
-----------------------------------------------------------------------------"""
CHECKBUTTON_ADV_SETTING = 1             # Command for enabling/ disabling advanced settings

"""-----------------------------------------------------------------------------
| PopUp Window: Geometry
|   
|   Constant              Value                     Meaning
-----------------------------------------------------------------------------"""
PW_X_POSITION           = 250           # Size of the popup window in X direction
PW_Y_POSITION           = 300           # Size of the popup window in Y direction
PW_Y_POSITION_SMALL     = 60            # Size of the popup window in Y direction

"""-----------------------------------------------------------------------------
| Configuration parameters: Settings/ Preferences
|   
|   Constant              Value
-----------------------------------------------------------------------------"""
SET_GLPM                = "pGLPM"       # Parameter for the global low performance mode
SET_GLPM_LATENCY        = "pGLPML"      # Parameter for the g.LPM latency in ms
SET_WLAN_MODE           = "pWM"         # Parameter for the wlan mode
SET_SERVER_IP           = "pSIP"        # Parameter for the server ip
SET_SERVER_PORT         = "pSPO"        # Parameter for the server port
SET_CLIENT_IP           = "pCIP"        # Parameter for the client ip
SET_CLIENT_PORT         = "pCPO"        # Parameter for the client port

"""-----------------------------------------------------------------------------
| Configuration parameters: Settings/ Preferences - Default Values
|   
|   Constant              Value
-----------------------------------------------------------------------------"""
SET_GLPM_VALUE          = 0             # Default value for the global low performance mode
SET_GLPM_LATENCY_VALUE  = "1"           # Default value for the g.LPM latency in ms
SET_WLAN_MODE_VALUE     = 0             # Default value for the wlan mode
SET_SERVER_IP_VALUE     = "192.168.1.2" # Default value for the server ip
SET_SERVER_PORT_VALUE   = "20001"       # Default value for the server port
SET_CLIENT_IP_VALUE     = "192.168.1.1" # Default value for the client ip
SET_CLIENT_PORT_VALUE   = "20000"       # Default value for the client port

"""-----------------------------------------------------------------------------
| Configuration parameters: Abbreviations
|   
|   Constant              Value                     Meaning
-----------------------------------------------------------------------------"""
TEMPLATE_NAME           = "pTN"         # Parameter template name
TEMPLATE_NAME_SEQUENCE  = "pTNS"        # Parameter template name sequence
SEQUENCE_CYCLES         = "pSC"         # Parameter sequence cycle
ADVANCED_SETTING        = "pAS"         # Parameter advanced setting
ENABLE_OPTIMIZER        = "pEO"         # Parameter enable optimizer
LOW_PERFORMANCE_MODE    = "pLPM"        # Parameter low performance mode
DUTY_CYCLE              = "pDC"         # Parameter duty cycle

"""-----------------------------------------------------------------------------
| Configuration parameters: Names
|   
|   Constant              Value
-----------------------------------------------------------------------------"""
SEQUENCE_LENGTH_U       = ""   
BASE_POTENTIAL_U        = "(V)"     
START_POTENTIAL_U       = "(V)"   
STOP_POTENTIAL_U        = "(V)"       
LOWER_POTENTIAL_U       = "(V)"        
UPPER_POTENTIAL_U       = "(V)"      
POTENTIAL_STEPS_U       = "(V)" 
PULSE_LENGTH_U          = "(s)"   
SAMPLING_RATE_U         = "(s)" 
SAMPLING_DURATION_U     = "(s)"
STEP_SIZE_U             = "(V)" 
SCAN_RATE_U             = "(V/s)"  
DELTA_V_STAIRCASE_U     = "(V)"
DELTA_V_PEAK_U          = "(V)"
CYCLE_U                 = ""      
LPTIA_RTIA_SIZE_U       = "(A)"  
FIXED_WE_POTENTIAL_U    = ""    
MAINS_FILTER_U          = ""  
SINC2_OVERSAMPLING_U    = ""       
SINC3_OVERSAMPLING_U    = ""    

"""-----------------------------------------------------------------------------
| Help Texts: Abbrebviations
|   
|   Constant              Value
-----------------------------------------------------------------------------"""
GENERAL                 = "hG"          # Abbreviation for help Text General
SINGLE_MODE             = "hSM"         # Single Mode
SEQUENCE_MODE           = "hSEM"        # Sequence Mode
TEMPLATES               = "hT"          # Templates
DATA_EXPORT             = "hDE"         # Date export
LOAD_BUTTON             = "hLB"         # Load button
SAVE_BUTTON             = "hSB"         # Save button
DELETE_BUTTON           = "hDB"         # Delete button
LOAD_SEQUENCE_BUTTON    = "hLSB"        # Load sequence button
SAVE_SEQUENCE_BUTTON    = "hSSB"        # Save seqeunce button
DELETE_SEQUENCE_BUTTON  = "hDSB"        # Delete sequence button

"""-----------------------------------------------------------------------------
| Template Management : Command ID
|   
|   Constant              Value
-----------------------------------------------------------------------------"""
IMPORT_TEMPLATE         = 1             
EXPORT_TEMPLATE         = 2