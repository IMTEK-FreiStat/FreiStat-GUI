"""
Module implementing a class for handling the experiment configurations defined
in the interface. The user can load these, if they were saved previously.

The class handles the following variables:

TODO
Experiment type         : `self._strElectrochemicalMethod`
Experiment parameters   : `self._listExperimentParameters`
Experiment data         : `self._listStoredData`

These are accessed by :
Experiment type         : `save_ExperimentType`      | `get_ExperimentType`
Experiment parameters   : `save_ExperimentParameters`| `get_ExperimentParameters`
Experiment data         : `append_Data`              | `get_StoredData`
                          `set_StoredData`

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

# Include dependencies

# Include internal dependencies

class DataStorage:
    """
    Descirption
    -----------
    Class in which all experiment data is stored for one electrochemical method.

    """

    def __init__(self) -> None:
        """
        Descirption
        -----------
        Constructor of class DataStorage

        """
        # Initalize class variable
        self._strTemplateName : str = ""
        self._strElectrochemicalMethod : str = ""
        self._listStoredData : list = []
        self._listExperimentParameters : list = []

    def save_TemplateName(self, strTemplateName : str) -> None:
        """
        Description
        -----------
        Save the name of the template in current data object.
        
        Parameters
        ----------
        `strTemplateName` : string
            String containing the name of the template
            
        """
        self._strTemplateName = strTemplateName

    def save_ExperimentParameters(self, listExperimentParameters: list) -> None:
        """
        Descirption
        -----------
        Save experiment parameters in the data object.
        
        Parameters
        ----------
        `listExperimentParameters` : list
            List which contains every experiment parameter required for the 
            chosen electrochemical method

        """
        self._listExperimentParameters = listExperimentParameters

    def save_ExperimentType(self, strExperimentType: str) -> None:
        """
        Descirption
        -----------
        Save experiment type in the data object.
        
        Parameters
        ----------
        `strExperimentType` : string
            String containing electrochemical method of the experiment

        """
        self._strElectrochemicalMethod = strExperimentType

    def save_SequenceCycles(self, iSeqCycle: int) -> None:
        """
        Description
        -----------
        Save amout of cycles in the sequence mode in current data object.
        
        Parameters
        ----------
        `iSeqCycle` : int
            Amout of cycles in the sequence mode

        """
        self._iSeqCycle = iSeqCycle

    # Getter methods
    def get_TemplateName(self) -> None:
        """
        Description
        -----------
        Get the name of the template in current data object.
        
        Return
        ------
        `strTemplateName` : string
            String containing the name of the template
            
        """
        return self._strTemplateName

    def get_ExperimentParameters(self) -> list:
        """
        Descirption
        -----------
        Get stored experiment parameters.
        
        Return
        ------
        `listExperimentParameters` : list
            Return list cotaining all experiment parameters

        """
        return self._listExperimentParameters 

    def get_ExperimentType(self) -> str:
        """
        Descirption
        -----------
        Get stored experiment type.
        
        Return
        ------
        `strElectrochemicalMethod` : string
            Return string containing experiment type
            
        """
        return self._strElectrochemicalMethod

    def get_SequenceCycles(self) -> None:
        """
        Description
        -----------
        Save amout of cycles in the sequence mode in current data object.
        
        Return
        ------
        `iSeqCycle` : int
            Amout of cycles in the sequence mode

        """
        return self._iSeqCycle