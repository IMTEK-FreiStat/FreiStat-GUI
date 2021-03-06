"""
Module containing the dictionaries for the text inside the GUI

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

# Import dependencies
from FreiStat.Data_storage.constants import *

# Import internal dependencies
from ..Data_Storage.constants import *

dic_parameters = {
    SET_GLPM            : ["Low performance mode:", 
                           "Disables the visualization of the measurement results in the plot to increase the performance."],
    SET_GLPM_LATENCY    : ["Low performance mode latency (ms):", 
                           "Defines the time interval in which the plot is updated."],
    SET_WLAN_MODE       : ["WLAN mode:", 
                           "Disable serial communication and enable connection via WiFi."],
    SET_SERVER_IP       : ["Server IP:", 
                           "Ip address of the system running the GUI. Format: xxx.xxx.xxx.xxx"],
    SET_SERVER_PORT     : ["Server Port:", 
                           "Port of the system running the GUI which should be used for communication."],
    SET_CLIENT_IP       : ["Client IP:", 
                           "IP address of the system running the GUI. Format: xxx.xxx.xxx.xxx"],
    SET_CLIENT_PORT     : ["Client Port:", 
                           "Port of the FreiStat which should be used for communication."],
    TEMPLATE_NAME       : ["Template name:", 
                           "Name under which the settings should be saved."],
    TEMPLATE_NAME_SEQUENCE : ["Sequence template name:",
                           "Name under which the settings for the sequence should be saved."],
    ADVANCED_SETTING    : ["Show advanced settings:", 
                           "Show/ hide the advanced settings"],
    ENABLE_OPTIMIZER    : ["Enable optimizer:", 
                           "Disabling not recommended. Optimizes: Stepsize, Filter settings"],
    LOW_PERFORMANCE_MODE: ["Low performance mode:", 
                           "Disables the visualization of the measurement results in the plot to increase the performance."],
    SEQUENCE_CYCLES     : ["Sequence cycles:", 
                           "Amount of times the whole sequence should be repeated."],
    BASE_POTENTIAL      : ["Base potential (V):", 
                           "Potential the cell is polarized to inbetween steps."],
    START_POTENTIAL     : ["Starting potential (V):", 
                           "Potential at which the measurement starts."],
    STOP_POTENTIAL      : ["Stop potential (V):", 
                           "Potential at which the measurement stops."],
    LOWER_POTENTIAL     : ["Second vertex potential (V):", 
                           "If second vertex is higher than first vertex, CV sweeps down first."],
    UPPER_POTENTIAL     : ["First vertex potential (V):", 
                           "If first vertex is higher than second vertex, CV sweeps up first."],
    POTENTIAL_STEPS     : ["Potential steps (V):", 
                           "List of potential steps which are applied to the cell. Format: x.xx, x.xx"],
    PULSE_LENGTH        : ["Pulse lengths (s):", 
                           "List of pulse lengths (requires same number of entries as potential steps). Format: x.xx, x.xx"],
    DUTY_CYCLE          : ["Duty cycle (s):", 
                           "Duty cycle which should be applied. In SWV: Duty cycle / 2 = time for each half potential."],
    SAMPLING_RATE       : ["Sampling rate (s):", 
                           "Time interval, in which values should be sampled. Required > 3 ms"],
    SAMPLING_DURATION   : ["Sampling duration (s):", 
                           "Sampling interval at the end of a potential step. Required > 3 ms"],
    STEP_SIZE           : ["Step size (V):", 
                           "Voltage increment with every step. Can be tuned by the optimizer."],
    SCAN_RATE           : ["Scan rate (V/s):", 
                           "Voltage change per second."],
    DELTA_V_STAIRCASE   : ["Delta V staircase (V):", 
                           "Voltage increment of the underlying staircase potential per measurement step."],
    DELTA_V_PEAK        : ["Delta V peak (V):", 
                           "Peak potential applied to the underlying staircase potential."],
    CYCLE               : ["Cycles:", 
                           "Amount of cycles the method should be repeated."],
    LPTIA_RTIA_SIZE     : ["Current range (A):", 
                           "Maximum current measurable, to large values reduce the resolution of 1 LSB."],
    FIXED_WE_POTENTIAL  : ["Fixed WE potential:", 
                           "Disabling allows the system to vary the potential on circuit level. Disable if cell potential exceeds 2.0 V."],
    MAINS_FILTER        : ["Mains filter:", 
                           "Enable/ disable the 50/60 Hz mains filter."],
    SINC2_OVERSAMPLING  : ["Sinc2 Oversampling rate:", 
                           "Possible value range: 0 - 1333"],
    SINC3_OVERSAMPLING  : ["Sinc3 Oversampling rate:", 
                           "Possible values: 0, 2, 4, 5"],
    LOAD_BUTTON         : ["Load Button",
                           "Load template"],
    SAVE_BUTTON         : ["Save Button",
                           "Save template"],
    DELETE_BUTTON       : ["Delete Button",
                           "Delete current template"],
    LOAD_SEQUENCE_BUTTON: ["Load Seqeuence Button",
                           "Load seqeuence template"],
    SAVE_SEQUENCE_BUTTON: ["Save Seqeuence Button",
                           "Save sequence template"],
    DELETE_SEQUENCE_BUTTON: ["Delete Seqeuence Button",
                           "Delete focussed electrochemical method from sequence"]                         
}

dic_helpText = {
    GENERAL             : ["Online Wiki",
                           "Visit IMTEK-FreiStat on GitHub for furhter information and help"],
    SINGLE_MODE         : ["1. Press \"Single Mode\" in the header",
                           "2. Select electrochemical method in the left menu",
                           "3. Adjust experiment parameters",
                           "4. Save template by pressing the save icon",
                           "5. Press \"Start\" in the header"],
    SEQUENCE_MODE       : ["1. Press \"Seqeunce Mode\" in the header",
                           "2. Add electrochemical methods of choice by pressing \"Add\" in the left menu",
                           "3. Adjust experiment parameters for every electrochemical method",
                           "4. Save every method in the sequnece (save icon without \"S\" indicator)",
                           "5. Save sequence template by pressing the save icon with the \"S\" indicator",
                           "6. Press \"Start\" in the header"],
    TEMPLATES           : ["Create template:",
                           "- If a method is saved, a template is saved using the \"Template Name\"",
                           "Load template:",
                           "- Press the load icon in \"Single mode\" or \"Sequence mode\"",
                           "- Select template which should be loaded in the right menu"],
    DATA_EXPORT         : ["Data export location:",
                           "- FreiStat creates 2 folders (\"Persistent_Data_Objects\" and \"Measurements\")",
                           "- These folders are located in the same location as the executing Python file",
                           "- Structure inside these folders: \"\\YY_MM_DD\\HH_MM_SS\\\"",
                           "- Stores experiment parameters and measurement results"]
}