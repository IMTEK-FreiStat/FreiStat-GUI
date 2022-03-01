"""
Module implementing a class for handling all data operations while running the
FreiStat interface

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

# Import dependencies
import os
import pickle
from FreiStat.Data_storage.constants import *

# Import internal dependencies
from .constants import *
from .data_storage import DataStorage

class DataHandling:
    """
    Descirption
    -----------
    Class which handles all operations regarding the stored data.

    There is only one instance of this class exisitng, regardless of the amount
    of DataStorage objects, since the data is stored in a list format, which is
    accessed in form of a ring structure from outside.

    """

    def __init__(self, strRootPath) -> None:
        """
        Description
        -----------
        Constructor of class DataHandling

        Parameters
        ----------
        ` strRootPath` : string
            Base file path of the interface

        """
        # Initialize class variables
        self._preferences : list = []
        self._listDataObject : list = []
        self._currentDataObject : int = 0
        self._strRootPath = strRootPath

    def create_DataObject(self) -> None:
        """
        Description
        -----------
        Create new data object for a electrochemical method and append it to the
        list of data storage objects. 

        Set reference to the newest object in the list.

        """
        # Create data object and append it to the list
        self._listDataObject.append(DataStorage())

        # Set reference to this new Data object
        self._currentDataObject = len(self._listDataObject) - 1

    def delete_DataObject(self) -> None:
        """
        Description
        -----------
        Delete the currently pointed to data object from the list.

        """   
        del self._listDataObject[self._currentDataObject]

    def move_first_DataObject(self) -> None:
        """
        Description
        -----------
        Move to the first stored data object in the list.

        """
        # Move to first entry in the list
        self._currentDataObject = 0

    def move_next_DataObject(self) -> None:
        """
        Description
        -----------
        Move to the next stored data object in the list. If the last object is
        reached, jump to the first entry. If the last stored object is a 
        sequence object, skip it.

        """
        # Check if list has more than 1 element
        if (len(self._listDataObject) < 1):
            return

        # Check if the second last data object is reached 
        # (Last element contains information regarding sequence and is skipped)
        if (self._currentDataObject == len(self._listDataObject) - 1):
            # Jump to first object
            self._currentDataObject = 0
        else :
            # Jump to next object
            self._currentDataObject += 1

    def move_previous_DataObject(self) -> None:
        """
        Description
        -----------
        Move to the previous stored data object in the list. If the first object 
        is reached, jump to the last entry. If the last stored object is a 
        sequence object, skip it.

        """
        # Check if first data object is reached
        if (self._currentDataObject == 0):
            # Jump to second last object (see `move_next_DataObject`)
            self._currentDataObject = len(self._listDataObject) - 1
        else :
            # Jump to previous object
            self._currentDataObject -= 1

    def export_Configuration(self, strFilePath : str) -> None:
        """
        Description
        -----------
        Export the current FreiStat configuration as an external file.     
        
        Parameters
        ----------
        `strFilePath` : string
            String containing the location where the data should be stored

        """
        with open(strFilePath, "wb") as output:
            # Write data objects as data file into the chosen directory.
            pickle.dump(self._listDataObject, output, 
                pickle.HIGHEST_PROTOCOL)

        # Change back to base directory
        os.chdir(self._strRootPath)

    def import_Configuration(self, strFilePath : str) -> None:
        """
        Description
        -----------
        Import the selected FreiStat configuration file.
        
        Parameters
        ----------
        `strFilePath` : string
            String containing the location where the data should be stored

        """
        # Load data storage object
        try:
            with open(strFilePath, "rb") as input:
                # Overrite data objects with loaded data objects
                self._listDataObject = pickle.load(input)   

            # Close input reader
            input.close      
        except:
            pass
        
    def export_Settings(self) -> None:
        """
        Description
        -----------
        Export the current settings of the FreiStat Interface.     

        """       
        with open(self._strRootPath + "\preferences", "wb") as output:
            # Write data objects as data file into the chosen directory.
            pickle.dump(self._preferences, output, 
                pickle.HIGHEST_PROTOCOL)

    def import_Settings(self) -> None:
        """
        Description
        -----------
        Import the current settings of the FreiStat Interface.     

        """
        # Check if preferences exist already
        if(os.path.exists(self._strRootPath + "\preferences") == False):
            listPreferences : list = [
                [SET_GLPM, SET_GLPM_VALUE],
                [SET_GLPM_LATENCY, SET_GLPM_LATENCY_VALUE],
                [SET_WLAN_MODE, SET_WLAN_MODE_VALUE],
                [SET_SERVER_IP, SET_SERVER_IP_VALUE],
                [SET_SERVER_PORT, SET_SERVER_PORT_VALUE],
                [SET_CLIENT_IP, SET_CLIENT_IP_VALUE],
                [SET_CLIENT_PORT, SET_CLIENT_PORT_VALUE]
            ]
            self.set_Preferences(listPreferences)
            
            return
            
        # Load data storage object
        with open(self._strRootPath + "\preferences", "rb") as input:
            # Overrite data objects with loaded data objects
            self._preferences = pickle.load(input)   

        # Close input reader
        input.close   

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
        self._listDataObject[self._currentDataObject]. \
            save_TemplateName(strTemplateName)

    def save_ExperimentParmeters(self, listExperimentParameters : list) -> None:
        """
        Description
        -----------
        Save experiment parameters in current data object.
        
        Parameters
        ----------
        `listExperimentParameters` : list
            List which contains every experiment parameter required for the 
            chosen electrochemical method
            
        """
        # Add list of experiment parameters to the current referenced data
        # object
        self._listDataObject[self._currentDataObject]. \
            save_ExperimentParameters(listExperimentParameters)

    def save_ExperimentType(self, strExperimentType: str) -> None:
        """
        Description
        -----------
        Save experiment type in current data object.
        
        Parameters
        ----------
        `strExperimentType` : string
            String containing electrochemical method of the experiment

        """
        # Save experiment type in the current referenced data object
        self._listDataObject[self._currentDataObject]. \
            save_ExperimentType(strExperimentType)

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
        # Save amout of cycles in the sequence mode in the current referenced 
        # data object
        self._listDataObject[self._currentDataObject]. \
            save_SequenceCycles(iSeqCycle)

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
        return self._listDataObject[self._currentDataObject]. \
            get_TemplateName()

    def get_ExperimentParameters(self) -> list:
        """
        Description
        -----------
        Get experiment parameters from currently referenced data object.
        
        Return
        ------
        `listExperimentParameters` : list
            List cotaining all experiment parameters

        """
        return self._listDataObject[self._currentDataObject]. \
            get_ExperimentParameters()

    def get_ExperimentType(self) -> str:
        """
        Description
        -----------
        Get experiment type from currently referenced data object.
        
        Return
        ------
        `strExperimentType` : string
            String containing experiment type

        """
        return self._listDataObject[self._currentDataObject]. \
            get_ExperimentType()

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
        # Save amout of cycles in the sequence mode in the current referenced 
        # data object
        return self._listDataObject[self._currentDataObject]. \
            get_SequenceCycles()

    def get_Preferences(self) -> list:
        """
        Description
        -----------
        Get the settings of the FreiStat interface

        Return
        ------
        `listPreferences` : list
            List containing the preferences of the interface
            
        """
        return self._preferences

    def set_Preferences(self, listPreferences : list) -> None:
        """
        Description
        -----------
        Get the settings of the FreiStat interface

        Parameters
        ----------
        `listPreferences` : list
            List containing the preferences of the interface
            
        """
        self._preferences = listPreferences

    def get_SequenceLength(self) -> int:
        """
        Description
        -----------
        Get length of the experiment sequence (amount of stored data objects).

        Return
        ------
        `LengthListDataObject` : int
            Integer containing the length of the current experiment sequence
            
        """
        return len(self._listDataObject)