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
                           "IP address of the FreiStat which should be connected. Format: xxx.xxx.xxx.xxx"],
    SET_CLIENT_PORT     : ["Client Port:", 
                           "Port of the FreiStat which should be used for communication."],
    TEMPLATE_NAME       : ["Template name:", 
                           "Name under which the settings should be saved."],
    ADVANCED_SETTING    : ["Advanced settings:", 
                           "Show/ Hide the advanced settings"],
    ENABLE_OPTIMIZER    : ["Enable optimizer:", 
                           "Optimize certain experiment parameters. See parameter overview on the right side for changes."],
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
    POTENTIAL_STEPS     : ["Potenital steps (V):", 
                           "List of potential steps which are applied to the cell. Format: x.xx, x.xx"],
    PULSE_LENGTH        : ["Pulse lenghts (s):", 
                           "List of pulse lengths (requires same amount of entries as potential steps). Format: x.xx, x.xx"],
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
                           "Amount of cycles the ec-method should be repeated."],
    LPTIA_RTIA_SIZE     : ["Current range (A):", 
                           "Maximum current measurable, to large values reduce the resolution of 1 LSB."],
    FIXED_WE_POTENTIAL  : ["Fixed WE potential:", 
                           "Disable if voltage range supasses the 2.0 V for fixed WE potential."],
    MAINS_FILTER        : ["Mains filter:", 
                           "Enable/ Disable the 50/60 Hz mains filter."],
    SINC2_OVERSAMPLING  : ["Sinc2 Oversampling rate:", 
                           "Possible value range: 0 - 1333"],
    SINC3_OVERSAMPLING  : ["Sinc3 Oversampling rate:", 
                           "Possible values: 0, 2, 4, 5"]

}