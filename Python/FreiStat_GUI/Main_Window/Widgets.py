"""
Sub module of the class FreiStatInterface, which implements the functionalities
of the widgets.

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

def _clickRibbonButton(self, iCommand : int) -> None:
    """
    Description
    -----------
    Method for a options in the ribbon dropdown menus.

    Parameters
    ----------
    `iCommand` : int
        Command encoded as integer
    
    """
    if (iCommand == BUTTON_LOAD):
        # Get file path
        self._strOsPath = self._openFileExplorer(BUTTON_LOAD)
        if (self._strOsPath != ""):
            self._dataHandling.import_Configuration(self._strOsPath)
        else :
            self._logger.info("No path selected, configuration not loaded.")

    elif (iCommand == BUTTON_SAVE):
        # Check if already saved
        if (self._strOsPath == ""):
            # Get custom save path
            self._strOsPath = self._openFileExplorer(BUTTON_SAVEAS)
            if (self._strOsPath != ""):
                # Save config at location
                self._dataHandling.export_Configuration(self._strOsPath)
            else :
                self._logger.info("No path selected, configuration not loaded.")
        else :
            # Save config at location
            self._dataHandling.export_Configuration(self._strOsPath)

        # Save safety backup
        self._dataHandling.export_Configuration(self._strOsPathBackup)

    elif (iCommand == BUTTON_SAVEAS):
        # Get custom save path
        self._strOsPath= self._openFileExplorer(BUTTON_SAVEAS)
        if (self._strOsPath != ""):
            # Save config at location
            self._dataHandling.export_Configuration(self._strOsPath)
        else :
            self._logger.info("No path selected, configuration not saved.")

        # Save safety backup
        self._dataHandling.export_Configuration(self._strOsPathBackup)

    elif (iCommand == BUTTON_PREFERENCES):
        # Open option menu in central frame
        self._update_CentralFrame_Options(self._fCentralFrame)

    elif (iCommand == BUTTON_HELP):
        #
        self._PopUpWindow.PopUp_Help()

    elif (iCommand == BUTTON_ABOUT):
        #
        self._PopUpWindow.PopUp_About()


def _clickButton(self, iCommand : int) -> None:
    """
    Description
    -----------
    Method for all buttons, which executs other program parts depending on
    the transmitted command.

    Parameters
    ----------
    `iCommand` : int
        Command encoded as integer
    
    """
    # Menu band commands
    if (iCommand == BUTTON_LIVEFEED):
        self._hideFrame(self._fCentralFrame)
        self._fLiveFeed.pack(fill= 'both', side= TOP, expand= TRUE, padx= 2, pady= 2)
        self._toolbarFrame.pack(fill= X, side= BOTTOM, expand= False, padx= 5)
    elif (iCommand == BUTTON_SINGLE_MODE):
        # Check if sequence mode was used before
        if (self._iNavIndex == NI_SEQ_MODE):
            # Check if experiment is running
            if (self._iSystemStatus != FS_RUNNING):
                # Clear central frame
                self._clearFrame(self._fCentralFrame)
            else :
                # Hide live feed and static plot
                self._fLiveFeed.pack_forget()
                self._toolbarFrame.pack_forget()
                self._fPlotHeadFrame


        # Update navigation index
        self._iNavIndex = NI_SINGLE_MODE

        self._update_OptionbandFrame_SingleMode(self._fOptionBand)
    elif (iCommand == BUTTON_SEQ_MODE):
        # Update navigation index
        self._iNavIndex = NI_SEQ_MODE

        # Reset sequence list
        self._SequenceList = []
        self._strFocusedFrame = None

        self._update_OptionbandFrame_SequeneceMode(self._fOptionBand)
        self._update_CentralFrame_Sequence(self._fCentralFrame)
    elif (iCommand == BUTTON_START):
        # Clear plot and terminal
        self._clearFrame(self._fPlotFrame)
        self._TextTerminal.delete(0, END)

        # Update info box with current system status
        self._iSystemStatus = FS_RUNNING
        self._strInfo.set(self._decodeSystemStatus(self._iSystemStatus))
        self._TextInfo.configure(style= "fLabelRunning.TLabel")

        # Enable live feed button
        self._ButtonLiveFeed["state"] = NORMAL

        # Experiment is running -> enable the stop button
        self._ButtonStop["state"] = NORMAL

        # Experiment is running -> disable the start button
        self._ButtonStart["state"] = DISABLED

        # Execute the experiment
        self._executeExperiment()
        
    elif (iCommand == BUTTON_STOP):
        # Update system status
        self._iSystemStatus = FS_STOP

        # Disable live feed button
        self._ButtonLiveFeed["state"] = DISABLED

        # No experiment is running -> disable the stop button
        self._ButtonStop["state"] = DISABLED

        # No experiment is running -> enable the start button
        self._ButtonStart["state"] = NORMAL

        # End experiment
        self._EcMethod._terminateExperiment()

    # Option band commands
    # Single mode
    if (iCommand == BUTTON_EC_CA):
        # Update navigation index
        self._iNavIndex = NI_SM_CA

        # Open parameter config
        self._update_CentralFrame_CA(self._fCentralFrame)

    elif (iCommand == BUTTON_EC_LSV):
        # Update navigation index
        self._iNavIndex = NI_SM_LSV

        # Open parameter config
        self._update_CentralFrame_LSV(self._fCentralFrame)

    elif (iCommand == BUTTON_EC_CV):
        # Update navigation index
        self._iNavIndex = NI_SM_CV

        # Open parameter config
        self._update_CentralFrame_CV(self._fCentralFrame)

    elif (iCommand == BUTTON_EC_NPV):
        # Update navigation index
        self._iNavIndex = NI_SM_NPV

        # Open parameter config
        self._update_CentralFrame_NPV(self._fCentralFrame)

    elif (iCommand == BUTTON_EC_DPV):
        # Update navigation index
        self._iNavIndex = NI_SM_DPV

        # Open parameter config
        self._update_CentralFrame_DPV(self._fCentralFrame)

    elif (iCommand == BUTTON_EC_SWV):
        # Update navigation index
        self._iNavIndex = NI_SM_SWV

        # Open parameter config
        self._update_CentralFrame_SWV(self._fCentralFrame)
        
    # Sequence mode
    if (iCommand == BUTTON_SM_ADD_EC_CA):
        # Add method to the sequence
        self._update_CentralFrame_Sequence_Add(CA)

        # Close the popup window
        self._fPopupEcMethod.destroy()

    elif (iCommand == BUTTON_SM_ADD_EC_LSV):
        # Add method to the sequence
        self._update_CentralFrame_Sequence_Add(LSV)

        # Close the popup window
        self._fPopupEcMethod.destroy()

    elif (iCommand == BUTTON_SM_ADD_EC_CV):
        # Add method to the sequence
        self._update_CentralFrame_Sequence_Add(CV)

        # Close the popup window
        self._fPopupEcMethod.destroy()

    elif (iCommand == BUTTON_SM_ADD_EC_NPV):
        # Add method to the sequence
        self._update_CentralFrame_Sequence_Add(NPV)

        # Close the popup window
        self._fPopupEcMethod.destroy()

    elif (iCommand == BUTTON_SM_ADD_EC_DPV):
        # Add method to the sequence
        self._update_CentralFrame_Sequence_Add(DPV)

        # Close the popup window
        self._fPopupEcMethod.destroy()

    elif (iCommand == BUTTON_SM_ADD_EC_SWV):
        # Add method to the sequence
        self._update_CentralFrame_Sequence_Add(SWV)

        # Close the popup window
        self._fPopupEcMethod.destroy()

    elif (iCommand == BUTTON_ADD):
        # Open popup window
        self._popupEcMethod()

    elif (iCommand == BUTTON_DELETE):
        # Search for the last focused sequence (Button)
        for iIndex in range(len(self._SequenceList)):
            if (self._SequenceList[iIndex][0].winfo_parent() == 
                self._strFocusedFrame):
                # Remove entry from the sequence list
                del self._SequenceList[iIndex]
                break

        # Clear window
        self._clearFrame(self._fDisplaySequence)

        # Temporary save the sequence list
        listTempSequence : list = self._SequenceList

        # Reset sequence list
        self._SequenceList = []
        self._strFocusedFrame = None
        
        # Redraw the window
        for iIndex in range(len(listTempSequence)):
            # Add method to the list
            self._update_CentralFrame_Sequence_Add(listTempSequence[iIndex][1])

            # Change text in widget to the template name
            Widget.nametowidget(self._Root, self._SequenceList[iIndex][0].
                winfo_parent() + ".!frame.!label2").configure(
                text = listTempSequence[iIndex][2])

            # Save template name of methods in sequence
            self._SequenceList[iIndex][2] = listTempSequence[iIndex][2]

            # Save experiment parameters
            self._SequenceList[iIndex][3] = listTempSequence[iIndex][3]

    elif (iCommand == BUTTON_MOVE_UP or iCommand == BUTTON_MOVE_DOWN):
        iFocusIndex : int = 0

        # Search for the last focused sequence (Button)
        for iIndex in range(len(self._SequenceList)):
            if (self._SequenceList[iIndex][0].winfo_parent() == 
                self._strFocusedFrame):
                # Save index last focus
                iFocusIndex = iIndex

                # Check which command is used
                if (iCommand == BUTTON_MOVE_UP):
                    # Check if method can't moved further up
                    if (iIndex == 0):
                        return

                    # Swtich the entries
                    self._SequenceList[iIndex - 1], self._SequenceList[iIndex] = \
                        self._SequenceList[iIndex], self._SequenceList[iIndex - 1]
                    
                    iFocusIndex -= 1
                    
                elif (iCommand == BUTTON_MOVE_DOWN):
                    # Check if method can't moved down further
                    if (iIndex == len(self._SequenceList) - 1):
                        return

                    # Swtich the entries
                    self._SequenceList[iIndex + 1], self._SequenceList[iIndex] = \
                        self._SequenceList[iIndex], self._SequenceList[iIndex + 1]                
                
                    iFocusIndex += 1
                break

        # Limit iFocusIndex
        if (iFocusIndex < 0):
            iFocusIndex = 0
        elif (iFocusIndex > len(self._SequenceList) - 1):
            iFocusIndex = len(self._SequenceList) - 1

        # Clear window
        self._clearFrame(self._fDisplaySequence)

        # Temporary save the sequence list
        listTempSequence : list = self._SequenceList

        # Reset sequence list
        self._SequenceList = []
        self._strFocusedFrame = None

        # Redraw the window
        for iIndex in range(len(listTempSequence)):
            # Add method to the list
            self._update_CentralFrame_Sequence_Add(listTempSequence[iIndex][1])

            # Check what last focused element was
            if (iFocusIndex == iIndex):
                # Update focused element
                self._strFocusedFrame = self._SequenceList[iIndex][0].winfo_parent()

                # Update color of new element
                Widget.nametowidget(self._Root, self._strFocusedFrame). \
                    configure(style= "fFocusFrame.TFrame")

            # Change text in widget to the template name
            Widget.nametowidget(self._Root, self._SequenceList[iIndex][0].
                winfo_parent() + ".!frame.!label2").configure(
                text = listTempSequence[iIndex][2])

            # Save template name of methods in sequence
            self._SequenceList[iIndex][2] = listTempSequence[iIndex][2]

            # Save experiment parameters
            self._SequenceList[iIndex][3] = listTempSequence[iIndex][3]

    # Plotband
    if (iCommand == BUTTON_TERMINAL):
        if (self._bPlotbandHidden == True):
            self._bPlotbandHidden = False
            # Show plotband
            self._fPlotBand.pack(fill= X, side= TOP, expand= False)
        self._update_PlotbandFrame_Terminal(self._fPlotBand)
        
    elif (iCommand == BUTTON_PLOTS):
        if (self._bPlotbandHidden == True):
            self._bPlotbandHidden = False
            # Show plotband
            self._fPlotBand.pack(fill= X, side= TOP, expand= False)
        self._update_PlotbandFrame_Plots(self._fPlotBand)

    # Utility functions
    # Parameter button in: Single Mode
    if (self._iNavIndex in range(NI_SINGLE_MODE, NI_SEQ_MODE)):
        if (iCommand == BUTTON_SAVE_TEMPLATE):
            # Check if an template name was given
            if (self._strTemplate.get() == ""):
                self._logger.info("No name was given for the template, " + 
                                  "templated is not saved.")
                return
            
            bTemplateFound : bool = False

            # Check if template is already used
            for iIndex in range(self._dataHandling.get_SequenceLength()):
                if (self._dataHandling.get_TemplateName() == self._strTemplate.get()):
                    bTemplateFound = True 
                    break

                # Move to the next data object
                self._dataHandling.move_next_DataObject()

            # Create instance of the data storage was not found
            if (bTemplateFound == False):
                self._dataHandling.create_DataObject()

            # Save the values which where set in the  entries
            self._saveEntries()

            # Check if experiment is running
            if (self._iSystemStatus != FS_RUNNING):
                # Enable the buttons to allow experiment start
                self._ButtonStart["state"] = NORMAL

            # Update the parameter frame
            self._update_PrameterbandFrame(self._fParameterBand)

            self._logger.info("Template saved successfully.")

        elif (iCommand == BUTTON_LOAD_TEMPLATE):
            # Update the parameter frame
            self._update_PrameterbandFrame_Template(self._fParameterBand)

        elif (iCommand == BUTTON_DELETE_TEMPLATE):
            # Delete current template
            for iIndex in range(self._dataHandling.get_SequenceLength()):
                if (self._dataHandling.get_TemplateName() == self._strTemplate.get()):
                    self._dataHandling.delete_DataObject()
                    break  

                # Move to the next data object
                self._dataHandling.move_next_DataObject()
              
    # Parameter button in: Sequence Mode
    if (self._iNavIndex == NI_SEQ_MODE):
        if (iCommand == BUTTON_SAVE_TEMPLATE):
            # Check if an template name was given
            if (self._strTemplate.get() == ""):
                self._logger.info("No name was given for the template, " + 
                                  "templated is not saved.")
                return

            bTemplateFound : bool = False

            # Search for the last focused sequence (Button)
            for iIndex in range(len(self._SequenceList)):
                if (self._SequenceList[iIndex][0].winfo_parent() == 
                    self._strFocusedFrame):

                    # Save template
                    self._SequenceList[iIndex][2] = self._strTemplate.get()

                    # Save parameter
                    self._SequenceList[iIndex][3] = self._saveEntriesInList()

                    # Change text in widget to the template name
                    Widget.nametowidget(self._Root, self._strFocusedFrame + 
                        ".!frame.!label2").configure(
                        text = self._SequenceList[iIndex][2])

            self._logger.info("Template successfully saved as parameters for the selected method.")

        elif (iCommand == BUTTON_LOAD_TEMPLATE):
            # Update the parameter frame
            self._update_PrameterbandFrame_Template(self._fParameterBand)

        elif (iCommand == BUTTON_DELETE_TEMPLATE):
            self._clickButton(BUTTON_DELETE)
            return

    # Sequence mode buttons
    if (iCommand == BUTTON_SAVE_TEMP_SEQ):
        # Check if an template name was given
        if (self._strTemplateSeq.get() == ""):
            self._logger.info("No name was given for the sequence template, " + 
                              "templated is not saved.")
            return

        # Check if the sequence cycles are given
        if (self._strCycleSeq.get() == ""):
            self._logger.info("Amount of sequence cylces is not specified, " + 
                              "templated is not saved.")
            return
            
        # Check if every method in the sequence was given a template
        for iIndex in range(len(self._SequenceList)):
            if (not self._SequenceList[iIndex][2]):
                self._logger.info("Method " + str(iIndex) + " (" + 
                    self._SequenceList[iIndex][1] + ") has no underlying " + 
                    "template. Add a template to the method and try again.")
                return     

        bTemplateFound : bool = False

        # Check if template is already used
        for iIndex in range(self._dataHandling.get_SequenceLength()):
            if (self._dataHandling.get_TemplateName() == self._strTemplateSeq.get()):
                bTemplateFound = True 
                break

            # Move to the next data object
            self._dataHandling.move_next_DataObject()

        # Create instance of the data storage was not found
        if (bTemplateFound == False):
            self._dataHandling.create_DataObject()

        # Save the values which where set in the  entries
        self._saveEntries()

        # Check if experiment is running
        if (self._iSystemStatus != FS_RUNNING):
            # Enable the buttons to allow experiment start
            self._ButtonStart["state"] = NORMAL

        # Update the parameter frame
        self._update_PrameterbandFrame(self._fParameterBand)

        self._logger.info("Sequence template saved successfully.")

    elif (iCommand == BUTTON_LOAD_TEMP_SEQ):
        # Update the parameter frame
        self._update_PrameterbandFrame_Template(self._fParameterBand)

    elif (iCommand == BUTTON_DELETE_TEMP_SEQ):
        # Delete current template
        for iIndex in range(self._dataHandling.get_SequenceLength()):
            if (self._dataHandling.get_TemplateName() == self._strTemplateSeq.get()):
                self._dataHandling.delete_DataObject()  
                break
            # Move to the next data object
            self._dataHandling.move_next_DataObject()

def _clickSequenceMethod(self, iCommand : int, button : Button) -> None:
    """
    Description
    -----------
    Click method for the different ec-methods in the sequence mode.

    Parameters
    ----------
    `iCommand` : int
        Command encoded as integer

    `button` : Button
        Id of the button which was clicked
    
    """
    # Reset color of old focused element
    if (self._strFocusedFrame is not None):
        Widget.nametowidget(self._Root, self._strFocusedFrame). \
            configure(style= "fWidgetButton.TFrame")

    # Update new focused element
    self._strFocusedFrame = button.winfo_parent()

    # Update color of new element
    Widget.nametowidget(self._Root, button.winfo_parent()). \
        configure(style= "fFocusFrame.TFrame")
    
    # Central frame
    if (iCommand == BUTTON_SM_PARA_EC_CA):
        # Open config for ec-method
        self._update_CentralFrame_CA(self._fOptionsSequence)

    elif (iCommand == BUTTON_SM_PARA_EC_LSV):
        # Add method to the sequence
        self._update_CentralFrame_LSV(self._fOptionsSequence)

    elif (iCommand == BUTTON_SM_PARA_EC_CV):
        # Open config for ec-method
        self._update_CentralFrame_CV(self._fOptionsSequence)

    elif (iCommand == BUTTON_SM_PARA_EC_NPV):
        # Open config for ec-method
        self._update_CentralFrame_NPV(self._fOptionsSequence)

    elif (iCommand == BUTTON_SM_PARA_EC_DPV):
        # Open config for ec-method
        self._update_CentralFrame_DPV(self._fOptionsSequence)

    elif (iCommand == BUTTON_SM_PARA_EC_SWV):
        # Open config for ec-method
        self._update_CentralFrame_SWV(self._fOptionsSequence)

def _clickCheckButton(self, iCommand : int) -> None:
    """
    Description
    -----------
    Method for all checkbuttons, which executs certain functions depending 
    on the transmitted command.

    Parameters
    ----------
    `iCommand` : int
        Command encoded as integer
    
    """
    if (iCommand == CHECKBUTTON_ADV_SETTING):
        if (self._iAdvancedSetting.get() == 0):
            # Hide advanced settings
            self._fAdvancedSettingContainer.pack_forget()
        else :
            # Show advanced settings
            self._createAdvancedSettingFrame(self._fCentralParameterFrame)

def _clickMinimizeButton(self, iCommand : int) -> None:
    """
    Description
    -----------
    Method for all minimize buttons, which executs certain functions depending 
    on the transmitted command.

    Parameters
    ----------
    `iCommand` : int
        Command encoded as integer
    
    """
    if (iCommand == BUTTON_MINIMIZE_PB):
        if (self._bPlotbandHidden == False):
            self._bPlotbandHidden = True
            # Hide  
            self._fPlotBand.pack_forget()
        elif (self._bPlotbandHidden == True):
            self._bPlotbandHidden = False
            # Show plotband
            self._fPlotBand.pack(fill= X, side= TOP, expand= False)
