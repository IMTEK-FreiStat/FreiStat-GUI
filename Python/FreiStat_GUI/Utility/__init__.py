"""
Module implementiting different utility functions

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

# Import dependencies
from FreiStat.Data_storage.constants import *
from FreiStat.Utility.decoder import _decode_LPTIA_Resistor_Size
from FreiStat.Utility.decoder import _decode_SincXOSR

def _decodeParameters(listExperimentParameters : list) -> list:
    """
    Description
    -----------
    Helper method decoding the experiment parameters returned by the optimzier
    or .csv-file back into the correct units for displaying in the interface.

    Parameters
    ----------
    `listExperimentParameters` : list
        List containing the experiment parameters returned by the optimizer

    Retrun
    ------
    `listDecExperimentParameters` : list
        List containing the decoded experiment parameters.

    """
    # Loop over the whole list
    for iIndex in range(len(listExperimentParameters)):
        if (listExperimentParameters[iIndex][0] == BASE_POTENTIAL):
            listExperimentParameters[iIndex][1] = \
                listExperimentParameters[iIndex][1] / 1000.0

        elif (listExperimentParameters[iIndex][0] == START_POTENTIAL):
            listExperimentParameters[iIndex][1] = \
                listExperimentParameters[iIndex][1] / 1000.0

        elif (listExperimentParameters[iIndex][0] == STOP_POTENTIAL):
            listExperimentParameters[iIndex][1] = \
                listExperimentParameters[iIndex][1] / 1000.0

        elif (listExperimentParameters[iIndex][0] == LOWER_POTENTIAL):
            listExperimentParameters[iIndex][1] = \
                listExperimentParameters[iIndex][1] / 1000.0

        elif (listExperimentParameters[iIndex][0] == UPPER_POTENTIAL):
            listExperimentParameters[iIndex][1] = \
                listExperimentParameters[iIndex][1] / 1000.0

        elif (listExperimentParameters[iIndex][0] == POTENTIAL_STEPS):
            listExperimentParameters[iIndex][1] = [x / 1000.0 for x in 
                listExperimentParameters[iIndex][1]]

        elif (listExperimentParameters[iIndex][0] == PULSE_LENGTH):
            listExperimentParameters[iIndex][1] = [x / 1000.0 for x in 
                listExperimentParameters[iIndex][1]]

        elif (listExperimentParameters[iIndex][0] == DELTA_V_STAIRCASE):
            listExperimentParameters[iIndex][1] = \
                listExperimentParameters[iIndex][1] / 1000.0

        elif (listExperimentParameters[iIndex][0] == DELTA_V_PEAK):
            listExperimentParameters[iIndex][1] = \
                listExperimentParameters[iIndex][1] / 1000.0

        elif (listExperimentParameters[iIndex][0] == STEP_SIZE):
            listExperimentParameters[iIndex][1] = \
                listExperimentParameters[iIndex][1] / 1000.0

        elif (listExperimentParameters[iIndex][0] == SCAN_RATE):
            listExperimentParameters[iIndex][1] = \
                listExperimentParameters[iIndex][1] / 1000.0

        elif (listExperimentParameters[iIndex][0] == SAMPLING_RATE):
            listExperimentParameters[iIndex][1] = \
                listExperimentParameters[iIndex][1] / 1000.0

        elif (listExperimentParameters[iIndex][0] == SAMPLING_DURATION):
            listExperimentParameters[iIndex][1] = \
                listExperimentParameters[iIndex][1] / 1000.0

        elif (listExperimentParameters[iIndex][0] == LPTIA_RTIA_SIZE):
            listExperimentParameters[iIndex][1] = 0.9 / \
                _decode_LPTIA_Resistor_Size(listExperimentParameters[iIndex][1])

        elif (listExperimentParameters[iIndex][0] == FIXED_WE_POTENTIAL):
            if (listExperimentParameters[iIndex][1] == 1):
                listExperimentParameters[iIndex][1] = True
            else :
                listExperimentParameters[iIndex][1] = False
        elif (listExperimentParameters[iIndex][0] == MAINS_FILTER):
            if (listExperimentParameters[iIndex][1] == 1):
                listExperimentParameters[iIndex][1] = True
            else :
                listExperimentParameters[iIndex][1] = False

        elif (listExperimentParameters[iIndex][0] == SINC2_OVERSAMPLING):
            listExperimentParameters[iIndex][1] = \
                _decode_SincXOSR(listExperimentParameters[iIndex][1], 
                SINC2_OVERSAMPLING)

        elif (listExperimentParameters[iIndex][0] == SINC3_OVERSAMPLING):
            listExperimentParameters[iIndex][1] = \
                _decode_SincXOSR(listExperimentParameters[iIndex][1], 
                SINC3_OVERSAMPLING)