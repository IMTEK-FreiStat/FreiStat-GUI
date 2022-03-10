"""
Sub module of the class FreiStatInterface, which implements different utiliy
functions used throughout the interface.

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

# Import dependencies
import os
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
from typing import Union
from FreiStat.Data_storage.dictionaries import *

# Import internal dependencies
from ..Data_Storage.constants import *
from ..Utility import _decodeParameters


def _openFileExplorer(self, iCommand : int) -> str :
    """
    Description
    -----------
    Method for selecting a folder or a file depending on the given command.

    Parameters
    ----------
    `iCommand` : int
        Command encoded as integer

    Return
    ------
    `strFilePath` : string
        Return selected filePath
    """
    # Initialize variables
    strFilePath : str = ""

    if (iCommand == BUTTON_LOAD):
        data = [("All Supported Files(*.fst; *.csv)","*.fst *.csv"),
                ("FreiStat Template File(*.fst)","*.fst"),
                ("CSV UTF-8(*.csv)","*.csv")]
        strFilePath = filedialog.askopenfilename(initialdir = os.getcwd(),
            filetypes= data, defaultextension= data,
            title = "Select a config file")
    elif (iCommand == BUTTON_SAVE):
        strFilePath = os.getcwd()
    elif (iCommand == BUTTON_SAVEAS):
        data = [("FreiStat Template File(*.fst)","*.fst")]
        f = filedialog.asksaveasfile(initialdir = os.getcwd(), 
                filetypes= data, defaultextension= data)
        strFilePath = f.name
       
    return strFilePath

def _shorten_decimals(self, fValue : float, iDecimals : int) -> float:
    """
    Description
    -----------
    Method for reducing the amount of decimals of a float value

    Parameters
    ----------
    `fValue` : float
        Value whose decimals should be cut

    `iDecimals` : int
        Amount of decimals

    Return
    ------
    `fValue` : float
        Value whose decimals were cut

    """
    # Initalize variabels
    iTemp = 1
    for iIndex in range(iDecimals):
        iTemp *= 10
    
    return float(int(fValue * iTemp)/ iTemp)


def _decodeExperimentParameters(self, listExperimentPair : list) \
    -> Union[str, str]:
    """
    Description
    -----------
    Method for decoding the list experiment pair back into the name of the
    parameter and the value.

    Parameters
    ----------
    `listExperimentPair` : List
        List of length 2 containing an abbreviations of an experiment parameter
        and its value.

    Return
    ------
    `strLabel` : string
        Name of the experiment parameter

    `strValue` : string
        value of the experiment parameter encoded as string

    """
    # Initialize variable
    strLabel : str = ""
    strValue : str = ""

    # Sequence mode parameters
    if (len(listExperimentPair) > 2):
        return listExperimentPair[0] , listExperimentPair[1]

    # Experiment parameters
    listParameterNames : list = [
        [SEQUENCE_LENGTH, dic_configParameters[SEQUENCE_LENGTH][0], SEQUENCE_LENGTH_U],
        [BASE_POTENTIAL, dic_configParameters[BASE_POTENTIAL][0], BASE_POTENTIAL_U],
        [START_POTENTIAL, dic_configParameters[START_POTENTIAL][0], START_POTENTIAL_U],
        [STOP_POTENTIAL, dic_configParameters[STOP_POTENTIAL][0], STOP_POTENTIAL_U],
        [LOWER_POTENTIAL, dic_configParameters[LOWER_POTENTIAL][0], LOWER_POTENTIAL_U],
        [UPPER_POTENTIAL, dic_configParameters[UPPER_POTENTIAL][0], UPPER_POTENTIAL_U],
        [POTENTIAL_STEPS, dic_configParameters[POTENTIAL_STEPS][0], POTENTIAL_STEPS_U],
        [PULSE_LENGTH, dic_configParameters[PULSE_LENGTH][0], PULSE_LENGTH_U],
        [SAMPLING_RATE, dic_configParameters[SAMPLING_RATE][0], SAMPLING_RATE_U],
        [SAMPLING_DURATION, dic_configParameters[SAMPLING_DURATION][0], SAMPLING_DURATION_U],
        [STEP_SIZE, dic_configParameters[STEP_SIZE][0], STEP_SIZE_U],
        [SCAN_RATE, dic_configParameters[SCAN_RATE][0], SCAN_RATE_U],
        [DELTA_V_STAIRCASE, dic_configParameters[DELTA_V_STAIRCASE][0], DELTA_V_STAIRCASE_U],
        [DELTA_V_PEAK, dic_configParameters[DELTA_V_PEAK][0], DELTA_V_PEAK_U],
        [CYCLE, dic_configParameters[CYCLE][0], CYCLE_U],
        [LPTIA_RTIA_SIZE, dic_configParameters[LPTIA_RTIA_SIZE][0], LPTIA_RTIA_SIZE_U],
        [FIXED_WE_POTENTIAL, dic_configParameters[FIXED_WE_POTENTIAL][0], FIXED_WE_POTENTIAL_U],
        [MAINS_FILTER, dic_configParameters[MAINS_FILTER][0], MAINS_FILTER_U],
        [SINC2_OVERSAMPLING, dic_configParameters[SINC2_OVERSAMPLING][0], SINC2_OVERSAMPLING_U],
        [SINC3_OVERSAMPLING, dic_configParameters[SINC3_OVERSAMPLING][0], SINC3_OVERSAMPLING_U]
    ]

    # Seach list of experiment parameters for entry
    for iIndex in range(len(listParameterNames)):
        if (listExperimentPair[0] == listParameterNames[iIndex][0]):
            strLabel = listParameterNames[iIndex][1] + " " + \
            listParameterNames[iIndex][2]
    
            # Covert value from int/ float to string
            strValue = str(listExperimentPair[1]) 

    return strLabel, strValue


def _decodeOptimizerParameters(self, listExperimentParameters : list) -> list:
    """
    Description
    -----------
    Helper method decoding the experiment parameters returned by the optimzier
    back into the correct units for displaying in the interface.

    Parameters
    ----------
    `listExperimentParameters` : list
        List containing the experiment parameters returned by the optimizer

    Retrun
    ------
    `listDecExperimentParameters` : list
        List containing the decoded experiment parameters.

    """
    # Decode experiment parameters
    _decodeParameters(listExperimentParameters)

    # Add parameters for optimizer and low performance mode to the list
    listExperimentParameters.append(
        [ENABLE_OPTIMIZER, bool(self._iEnableOptimizer.get())])
    listExperimentParameters.append(
        [LOW_PERFORMANCE_MODE, bool(self._iLowPerformanceMode.get())])

    return listExperimentParameters

def _decodeSystemStatus(self, iSystemStatus : int) -> str:
    """
    Description
    -----------
    Helper method decoding the system status integer into a string

    Parameters
    ----------
    `iSystemStatus` : int
        System status encoded as integer

    Return
    ------
    `strSystemStatus` : string
        System status as string

    """
    # Initialize list for comparision
    listSystemStatus : list = [
        [FS_WAITING_STR, FS_WAITING],
        [FS_RUNNING_STR, FS_RUNNING],
        [FS_STOP_STR, FS_STOP],
        [FS_COMPLETED_STR, FS_COMPLETED]
    ]

    for iIndex in range(len(listSystemStatus)):
        if (listSystemStatus[iIndex][1] == iSystemStatus):
            return listSystemStatus[iIndex][0]

