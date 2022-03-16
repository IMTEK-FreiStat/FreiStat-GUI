"""
Sub module of the class FreiStatInterface, which implements the parameterband.

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

def _create_ParameterbandFrame(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the parameter band at the right side of the 
    interface, which is used to provide additional informations.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the parameter band frame is embedded
        
    """       
    # Create frame for the parameter band 
    self._fParameterBand = Frame(parentFrame, style="fParameterBand.TFrame")
    self._fParameterBand.pack(fill=Y, side=RIGHT, expand=FALSE, anchor= NE) 

def _update_PrameterbandFrame(self, parentFrame : Frame) -> None:
    """
    Description
    -----------
    Method for updating the parameter band to display the parameters of the
    experiment.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the parameter band frame is embedded

    """
    # Clear present widgets
    self._clearFrame(parentFrame)        

    # Create frame for template name and experiment type 
    fGeneralInfo = Frame(parentFrame, style="fWidget.TFrame")
    fGeneralInfo.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    TextExperimentType = Label(fGeneralInfo, text= "Template: " + 
        self._dataHandling.get_TemplateName(), width= TEXTBOX_WIDTH, 
        style= "fLabelGeneralBold.TLabel")
    TextExperimentType.pack(side= TOP, padx= 5, pady= 5)

    TextExperimentType = Label(fGeneralInfo, text= "Experiment type: " + 
        self._dataHandling.get_ExperimentType(), width= TEXTBOX_WIDTH, 
        style= "fLabelGeneralBold.TLabel")
    TextExperimentType.pack(side= TOP, padx= 5, pady= 5)

    # Check for sequence mode and display amount of cycles
    if (self._dataHandling.get_ExperimentType() == SEQUENCE):
        # Create frame
        fExperimentParameter = Frame(parentFrame, style="fWidget.TFrame")
        fExperimentParameter.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

        TextExperimentType = Label(fExperimentParameter, text= "Sequence length: " + 
                                   str(len(self._dataHandling.get_ExperimentParameters())), 
                                   width= TEXTBOX_WIDTH, 
                                   style= "fLabelGeneralBold.TLabel")
        TextExperimentType.pack(side= TOP, padx= 5, pady= 5)

        TextExperimentType = Label(fExperimentParameter, text= "Sequence cycles: " +
                                   str(self._dataHandling.get_SequenceCycles()), 
                                   width= TEXTBOX_WIDTH, 
                                   style= "fLabelGeneralBold.TLabel")
        TextExperimentType.pack(side= TOP, padx= 5, pady= 5)

    # Create frame for every experiment parameter
    fExperimentParameter = Frame(parentFrame, style="fWidget.TFrame")
    fExperimentParameter.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    for iIndex in range(len(self._dataHandling.get_ExperimentParameters())):
        # Decode experiment parameter entry back into label and value pair
        strLabel, strValue = self._decodeExperimentParameters(
            self._dataHandling.get_ExperimentParameters()[iIndex])
            
        TextExperimentType = Label(fExperimentParameter, text= strLabel, 
                                   width= TEXTBOX_WIDTH, 
                                   style= "fLabelGeneralBold.TLabel")
        TextExperimentType.pack(side= TOP, padx= 5, pady= 5)

        TextExperimentType = Label(fExperimentParameter, text= strValue, 
                                   width= TEXTBOX_WIDTH, 
                                   style= "fLabelGeneral.TLabel")
        TextExperimentType.pack(side= TOP, padx= 5, pady= 5)

def _update_PrameterbandFrame_Template(self, iCommandID : int ,
                                       parentFrame : Frame) -> None:
    """
    Description
    -----------
    Method for updating the parameter band to display all stored templates.

    Parameters
    ----------
    `iCommandID` : int
        Integer encoding a command to either show  sequence templates or method
        templates.

    `parentFrame` : Frame
        Parent frame in which the parameter band frame is embedded

    """
    # Clear present widgets
    self._clearFrame(parentFrame)   

    # Move to the first data object
    self._dataHandling.move_first_DataObject()

    # Create listbox
    self._TemplateListBox = Listbox(parentFrame, width= TEXTBOX_WIDTH, 
                                    font= "Arial 10 bold")

    # Bind select event to list box
    self._TemplateListBox.bind('<<ListboxSelect>>', self._onSelect)

    # Add scrollbars 
    ScrollbarXTerminal = Scrollbar(parentFrame, orient='horizontal', 
                                   command=self._TemplateListBox.xview)
    ScrollbarYTerminal = Scrollbar(parentFrame, orient='vertical', 
                                   command=self._TemplateListBox.yview)
    ScrollbarYTerminal.pack(side= RIGHT, expand=False, fill=Y) 
    self._TemplateListBox.config(xscrollcommand=ScrollbarXTerminal.set, 
                                 yscrollcommand=ScrollbarYTerminal.set)
    self._TemplateListBox.pack(side= TOP, expand=True, fill='both', 
                               padx= 5, pady= 5)
    ScrollbarXTerminal.pack(side= BOTTOM, expand=False, fill=X)   

    # Create frame the templates
    fTemplates = Frame(parentFrame, style= "fWidget.TFrame")
    fTemplates.pack(fill= X, side= TOP, expand= FALSE, padx= 5, pady= 5)

    # Create set based on command ID
    if (iCommandID == BUTTON_LOAD_TEMPLATE):
        # Check if currently in sequnece mode to limit method selection
        if (self._iNavIndex ==  NI_SEQ_MODE):
            tempSet = {self._strMethod}
        else : 
            tempSet = {CA, OCP, LSV, CV, NPV, DPV, SWV}
    elif (iCommandID == BUTTON_LOAD_TEMP_SEQ):
        tempSet = {SEQUENCE}
    else :
        tempSet = {}

    # Loop over all templates
    for iIndex in range(self._dataHandling.get_SequenceLength()):
        if (self._dataHandling.get_ExperimentType() in tempSet):
            self._TemplateListBox.insert(END, self._dataHandling.get_ExperimentType() + 
                " - " + self._dataHandling.get_TemplateName())

        # Move to the next data object
        self._dataHandling.move_next_DataObject()

def _onSelect(self, event):
    """
    Description
    -----------
    Method handling the selection of elements in the listbox for the different
    templates

    Parameters
    ----------
    `event` : event
        Event handler for selection
    
    """
    widget = event.widget

    # Check if an item can be selected
    if (len(widget.curselection()) == 0):
        return

    # get string in listbox
    strTemplateName = widget.get(int(widget.curselection()[0]))

    # Separate method from template name
    strTemplateName = strTemplateName.split(" - ")[1]

    frame : Frame = ""

    # Check if system is in single mode
    if (self._iNavIndex in range(NI_SINGLE_MODE, NI_SEQ_MODE)):
        frame = self._fCentralFrame
    # Sequence mode
    elif (self._iNavIndex == NI_SEQ_MODE):
        frame = self._fOptionsSequence               

    for iIndex in range(self._dataHandling.get_SequenceLength()):
        if (self._dataHandling.get_TemplateName() == strTemplateName):
            # Update parameter band
            self._update_PrameterbandFrame(self._fParameterBand)

            # Update central frame depending on the ec method
            if (self._dataHandling.get_ExperimentType() == CA):
                # Update navigations index
                if (self._iNavIndex != NI_SEQ_MODE):
                    self._iNavIndex = NI_SM_CA
                self._update_CentralFrame_CA(frame)
            elif (self._dataHandling.get_ExperimentType() == LSV):
                # Update navigations index
                if (self._iNavIndex != NI_SEQ_MODE):
                    self._iNavIndex = NI_SM_LSV
                self._update_CentralFrame_LSV(frame)
            elif (self._dataHandling.get_ExperimentType() == CV):
                # Update navigations index
                if (self._iNavIndex != NI_SEQ_MODE):
                    self._iNavIndex = NI_SM_CV
                self._update_CentralFrame_CV(frame)
            elif (self._dataHandling.get_ExperimentType() == NPV):
                # Update navigations index
                if (self._iNavIndex != NI_SEQ_MODE):
                    self._iNavIndex = NI_SM_NPV
                self._update_CentralFrame_NPV(frame)
            elif (self._dataHandling.get_ExperimentType() == DPV):
                # Update navigations index
                if (self._iNavIndex != NI_SEQ_MODE):
                    self._iNavIndex = NI_SM_DPV
                self._update_CentralFrame_DPV(frame)
            elif (self._dataHandling.get_ExperimentType() == SWV):
                # Update navigations index
                if (self._iNavIndex != NI_SEQ_MODE):
                    self._iNavIndex = NI_SM_SWV
                self._update_CentralFrame_SWV(frame)
            elif (self._dataHandling.get_ExperimentType() == SEQUENCE):
                # Update navigations index
                self._iNavIndex = NI_SEQ_MODE
                self._update_OptionbandFrame_SequeneceMode(self._fOptionBand)
                self._update_CentralFrame_Sequence(self._fCentralFrame)

                # Reconstruct the sequence
                self._update_CentralFrame_Sequence_Load()
            break
        # Move to the next data object
        self._dataHandling.move_next_DataObject()

    if (self._iNavIndex == NI_SEQ_MODE):
        frame = self._fOptionsSequence

        if (self._dataHandling.get_ExperimentType() != SEQUENCE):
            # Move back to the sequence object
            for iIndex in range(self._dataHandling.get_SequenceLength()):
                if (self._dataHandling.get_TemplateName() == self._strTemplateSeq.get()):
                    # Update parameter band
                    self._update_PrameterbandFrame(self._fParameterBand)
                    return
                # Move to the next data object
                self._dataHandling.move_next_DataObject() 