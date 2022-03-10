"""
PopUp window class of the FreiStat interface.

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
import FreiStat as FS
import FreiStat_GUI as FS_GUI
from numpy import var

# Import internal dependencies
from ..Data_Storage.constants import *
from ..Data_Storage.dictionaries import *
from ..Data_Storage.data_handling import DataHandling

class FreiStatPopUp():
    """
    Description
    -----------
    Class for implementing the PopUp windows of the FreiStat interface
    """
    from .Events import _on_rightclick
    from .Events import _on_rightclick_release

    from .Events import _bound_MouseWheel
    from .Events import _unbound_MouseWheel
    from .Events import _onMouseWheel

    from .Widgets import _clickCheckButton
    from .Widgets import _clickExport
    from .Widgets import _clickImport
    from .Widgets import _clickSelect

    def __init__(self, iCenterX : int, iCenterY : int) -> None:
        """
        Description
        -----------
        Constructor of the class FreiStatPopUp.
        
        """
        # Intialize class variables
        self._iCenterX = iCenterX
        self._iCenterY = iCenterY

        # Load image
        self._logo = PhotoImage(file= __path__[0] + 
            "./../assets/logo/FreiStat.gif")

        self._initWindow()

    def _initWindow(self) -> None:
        """
        Description
        -----------
        Intialize the actual window

        """        
        # Create root window object
        self._PopUpRoot = Toplevel()
        self._PopUpRoot.withdraw()
        self._PopUpRoot.protocol("WM_DELETE_WINDOW", self._on_Closing)
        self._PopUpRoot.resizable(FALSE, FALSE)

        # Set title of the window
        self._PopUpRoot.title("FreiStat")

        # Set logo of the window
        self._PopUpRoot.tk.call('wm', 'iconphoto', self._PopUpRoot._w, self._logo)
        self._PopUpRoot.geometry(f'{PW_X_POSITION}x{PW_Y_POSITION}+{self._iCenterX + 50}+{self._iCenterY + 50}')

    def PopUp_Help(self) -> None:
        """
        Description
        -----------
        Create a PopUp window for the help setting

        """
        # Check if window is open and just hidden
        try:
            # Unhide window
            self._PopUpRoot.geometry(f'{2*PW_X_POSITION}x{PW_Y_POSITION}+{self._iCenterX + 50}+{self._iCenterY + 50}')
            self._PopUpRoot.overrideredirect(0)
            self._PopUpRoot.deiconify()
            self._clearFrame(self._PopUpRoot)

            # Set title of the window
            self._PopUpRoot.title("Help")
        except:
            # Create new window
            self._initWindow()
            self._PopUpRoot.deiconify() 

        self._TabControl = Notebook(self._PopUpRoot)
        tab1 = Frame(self._TabControl)
        tab2 = Frame(self._TabControl)
        tab3 = Frame(self._TabControl)
        tab4 = Frame(self._TabControl)
        tab5 = Frame(self._TabControl)

        self._TabControl.add(tab1, text = "General")
        self._TabControl.add(tab2, text = "Single Mode")
        self._TabControl.add(tab3, text = "Sequence Mode")
        self._TabControl.add(tab4, text = "Templates")
        self._TabControl.add(tab5, text = "Data Export")
        self._TabControl.pack(expand = TRUE, fill ="both")

        # General
        for iIndex in range(len(dic_helpText[GENERAL])):
            helpText = Label(tab1, text= dic_helpText[GENERAL][iIndex], 
                            style= "fLabelGeneralBold.TLabel")
            helpText.pack(fill ="both", side= TOP)

        # Single Mode
        for iIndex in range(len(dic_helpText[SINGLE_MODE])):
            helpText = Label(tab2, text= dic_helpText[SINGLE_MODE][iIndex], 
                            style= "fLabelGeneralBold.TLabel")
            helpText.pack(fill ="both", side= TOP)

        # Sequence Mode
        for iIndex in range(len(dic_helpText[SEQUENCE_MODE])):
            helpText = Label(tab3, text= dic_helpText[SEQUENCE_MODE][iIndex], 
                            style= "fLabelGeneralBold.TLabel")
            helpText.pack(fill ="both", side= TOP)

        # Templates
        for iIndex in range(len(dic_helpText[TEMPLATES])):
            helpText = Label(tab4, text= dic_helpText[TEMPLATES][iIndex], 
                            style= "fLabelGeneralBold.TLabel")
            helpText.pack(fill ="both", side= TOP)

        # Data Export
        for iIndex in range(len(dic_helpText[DATA_EXPORT])):
            helpText = Label(tab5, text= dic_helpText[DATA_EXPORT][iIndex], 
                            style= "fLabelGeneralBold.TLabel")
            helpText.pack(fill ="both", side= TOP)

    def PopUp_About(self) -> None:
        """
        Description
        -----------
        Create a PopUp window for the about setting

        """
        # Check if window is open and just hidden
        try:
            # Unhide window
            self._PopUpRoot.geometry(f'{PW_X_POSITION}x{PW_Y_POSITION}+{self._iCenterX + 50}+{self._iCenterY + 50}')
            self._PopUpRoot.overrideredirect(0)
            self._PopUpRoot.deiconify()
            self._clearFrame(self._PopUpRoot)

            # Set title of the window
            self._PopUpRoot.title("About")
        except:
            # Create new window
            self._initWindow()
            self._PopUpRoot.deiconify()

        # Create frame information
        fVersionFrame = Frame(self._PopUpRoot, style="fPopUp.TFrame")
        fVersionFrame.pack(fill= 'both', side= TOP, expand= True)

        self._TextLogo = PhotoImage(file= __path__[0] + "./../assets/logo/FreiStat.png")
        self._TextLogo = self._TextLogo.subsample(4)

        TextLogoFreiStat = Label(fVersionFrame, image= self._TextLogo, 
                                style= "fLabelGeneralWhite.TLabel")
        TextLogoFreiStat.pack(side= TOP, expand= FALSE, padx= 5, pady= 5)

        # FreiStat-GUI
        TextGeneral = Label(fVersionFrame, text= FS_GUI.__name__, width= 100, 
            style= "fLabelGeneralWhiteSmallBold.TLabel")
        TextGeneral.pack(side= TOP, padx= 5, pady= 5)        

        TextVersion = Label(fVersionFrame, width= 100, 
            text= "Version: {0}".format(FS_GUI.__version__), 
            style= "fLabelGeneralWhiteSmallBold.TLabel")
        TextVersion.pack(side= TOP, padx= 5, pady= 5)

        # FreiStat-Framework
        TextGeneral = Label(fVersionFrame, text= FS.__name__, width= 100, 
            style= "fLabelGeneralWhiteSmallBold.TLabel")
        TextGeneral.pack(side= TOP, padx= 5, pady= 5)        

        TextVersion = Label(fVersionFrame, width= 100,
            text= "Version: {0}".format(FS.__version__),  
            style= "fLabelGeneralWhiteSmallBold.TLabel")
        TextVersion.pack(side= TOP, padx= 5, pady= 5)

    def PopUp_TemplateHandler(self, iCommandID, dataHandling : DataHandling, 
                              listDataStorage : list, strFilePath: str) -> None:
        """
        Description
        -----------
        Create a PopUp window for handling template import/ export management

        Parameters
        ----------
        `iCommandID` : int
            Integer indicating command (0 Import | 1 Export)

        `dataHandling` : DataHandling
            Reference to the dataHandling object
            
        `listDataStorage` : list
            List containing all loaded data storage objects

        `strFilePath` : str
            String containing the path to the import/ export location 

        """
        # Check if window is open and just hidden
        try:
            # Unhide window
            self._PopUpRoot.geometry(f'{1000}x{600}+{self._iCenterX + 50}+{self._iCenterY + 50}')
            self._PopUpRoot.overrideredirect(0)
            self._PopUpRoot.deiconify()
            self._clearFrame(self._PopUpRoot)

            # Set title of the window
            self._PopUpRoot.title("Template management")
        except:
            # Create new window
            self._initWindow()
            self._PopUpRoot.deiconify()       

        # Save reference to dataHandling object
        self._dataHandling = dataHandling

        # Save reference to imported dataStorage objects
        self._listDataStorage = listDataStorage

        # Create lists to hold IntVar references
        self._tempList : list = []
        self._templateList : list = []

        # Create list to hold template frame reference
        self._templateFrameList : list = []
        self._buttonList : list = []
        self._templateNameList : list = []

        # Save import/ export path
        self._strFilePath = strFilePath

        # Create a canvas window
        canvasFrame = Canvas(self._PopUpRoot, background= "gray95",
            borderwidth= 0, highlightthickness= 0)

        # Create a scrollbar
        scrollbarCentral=Scrollbar(self._PopUpRoot, orient="vertical",
            command= canvasFrame.yview)
        scrollbarCentral.pack(side= RIGHT, fill= Y)

        canvasFrame.pack(fill= "both", expand= True, side= TOP)

        # Add scroll command to canvas
        canvasFrame.configure(yscrollcommand= scrollbarCentral.set)

        fMainFrame = Frame(canvasFrame, style="fPopUpTemplate.TFrame")
        fMainFrame.pack(fill= "both", side= TOP, expand= True, padx= 1)

        # Update windows to get correct size informations
        canvasFrame.create_window((0,0), window= fMainFrame, 
            anchor= NW, width= 985, height= len(listDataStorage) * 500)

        # Bind mousewheel scroll to frames
        fMainFrame.bind("<Enter>", lambda event, 
            frame = fMainFrame, canvas = canvasFrame : 
            self._bound_MouseWheel(event, frame, canvas))
        fMainFrame.bind("<Leave>", lambda event, 
            frame = canvasFrame : self._unbound_MouseWheel(event, frame))

        # Loop over every data storage entry
        for iIndex in range(len(listDataStorage)):

            self._DisplayTemplate(fMainFrame, iIndex, False,
                listDataStorage[iIndex].get_TemplateName(), 
                listDataStorage[iIndex].get_ExperimentType(), 
                listDataStorage[iIndex].get_ExperimentParameters())

        fRibbonFrame = Frame(self._PopUpRoot, style="fMenuBand.TFrame",
                                relief= RAISED)
        fRibbonFrame.pack(fill= "both", side= BOTTOM)

        if (iCommandID == IMPORT_TEMPLATE):
            ButtonContinue = Button(fRibbonFrame, text= "Import templates",
                command= lambda : self._clickImport())
            ButtonContinue.pack(side= RIGHT, padx = 5, pady= 5)
        elif (iCommandID == EXPORT_TEMPLATE):
            ButtonContinue = Button(fRibbonFrame, text= "Export templates",
                command= lambda : self._clickExport())
            ButtonContinue.pack(side= RIGHT, padx = 5, pady= 5)

    def _DisplayTemplate(self, parentFrame : Frame, 
                         index : int,
                         bRecursionCall : bool,
                         templateName : str, 
                         experimentType : str, 
                         experimentParameter : list) -> None:
        """
        Description
        -----------
        Method to display template in popup window

        Parameters
        ----------
        `parentFrame` : Frame
            Reference to frame in which the template should be shown

        `index` : int
            Index indicating the position of the template in the list
            
        `bRecursionCall` : bool
            Flag indicating if the method displayed is part of a sequence

        `templateName` : str
            Name of the template

        `experimentType` : str
            Experiment type used 

        `experimentParameter` : list
            List containing the experiment parameters

        """
        fTemplateFrame = Frame(parentFrame, style="fPopUp.TFrame")
        fTemplateFrame.pack(fill= 'both', side= TOP, padx= 1, pady= 5)   

        # Create subframe for general template information
        fTemplateGeneralFrame = Frame(fTemplateFrame, style="fPopUp.TFrame")
        fTemplateGeneralFrame.pack(fill= 'both', side= TOP, padx= 1, pady= 1) 

        templateIntVar = IntVar()

        if(not bRecursionCall):
            # Checkbutton for expanding method parameters
            ButtonTemplate = Checkbutton(fTemplateGeneralFrame, onvalue= True, 
                offvalue= False, style="fCheckButtonGeneral.TCheckbutton",
                variable= templateIntVar, command= lambda index= index : 
                self._clickCheckButton(index))
            ButtonTemplate.pack(side= LEFT, fill= Y, padx = 5, pady= 5)
            self._templateList.append(templateIntVar)
        else :
            # Insert spacer element
            fSpacerFrame = Frame(fTemplateGeneralFrame, style= "fPopUp.TFrame")
            fSpacerFrame.pack(fill= Y, side= LEFT, expand= FALSE, padx= 15, pady= 5) 

        # Label for ec-method
        TextMethodName= Label(fTemplateGeneralFrame, 
            text= experimentType, 
            width= TEXTBOX_WIDTH_SMALL, style= "fLabelGeneralWhiteSmallBold.TLabel")
        TextMethodName.pack(side= LEFT, pady= 5)

        # Label for displaying the template name
        TextTemplate= Label(fTemplateGeneralFrame, 
            text= dic_parameters[TEMPLATE_NAME][0], 
            width= TEXTBOX_WIDTH_SMALL, style= "fLabelGeneralWhiteSmallBold.TLabel")
        TextTemplate.pack(side= LEFT, padx= 5, pady= 5)

        strTemplate = StringVar()
        strTemplate.set(templateName)

        EntryTemplate = Entry(fTemplateGeneralFrame, textvariable= strTemplate, 
            width= TEXTBOX_WIDTH, style= "fLabelGeneralWhiteSmallBold.TLabel")        
        EntryTemplate.pack(side= LEFT, pady= 5)   

        self._templateNameList.append(strTemplate)
        """
        TextTemplateName= Label(fTemplateGeneralFrame, 
            text= templateName, 
            width= TEXTBOX_WIDTH, style= "fLabelGeneralWhiteSmallBold.TLabel")
        TextTemplateName.pack(side= LEFT, pady= 5)
        """
        if(not bRecursionCall):
            # Border frame for button
            fBorderFrameButton = Frame(fTemplateGeneralFrame, style="fUnselectedFrame.TFrame")
            fBorderFrameButton.pack(fill= 'both', side= RIGHT, padx= 2, pady= 2)   

            ButtonShowExpPara = Button(fBorderFrameButton, text= "Unselected",
                command= lambda index= index: self._clickSelect(index))        
            ButtonShowExpPara.pack(side= RIGHT, fill= Y, padx= 3, pady= 3)
            self._buttonList.append([ButtonShowExpPara, False])
        
            # Create subframe for display of experiment setup
            fTemplateParameterFrame = Frame(fTemplateFrame, style="fWidget.TFrame")
            self._templateFrameList.append(fTemplateParameterFrame)
        else :
            fTemplateParameterFrame = Frame(fTemplateFrame, style="fWidget.TFrame")
            fTemplateParameterFrame.pack(fill= "both", side= "top", padx= 1, pady= 5)

        if (experimentType == SEQUENCE):
            # Make a recursion call for every method in the sequnece
            for iIndex in range(len(experimentParameter)):
                self._DisplayTemplate(fTemplateParameterFrame, iIndex, True,
                    experimentParameter[iIndex][1], 
                    experimentParameter[iIndex][0], 
                    experimentParameter[iIndex][2])

        else:
            # Loop over all experiment parameters
            for iIndex in range(len(experimentParameter)):
                # Create a subsubframe for an experiment parameter pair
                fParameterFrame = Frame(fTemplateParameterFrame, style="fPopUp.TFrame")
                fParameterFrame.pack(fill= 'both', side= TOP, padx= 1) 

                # Label for displaying the name of the experiment parameter
                TextParameter= Label(fParameterFrame, 
                    text= dic_parameters[experimentParameter[iIndex][0]][0], 
                    width= TEXTBOX_WIDTH, style= "fLabelGeneralWhiteSmall.TLabel")
                TextParameter.pack(side= LEFT, padx= 35, pady= 5)       

                # Create suiting representation for every parameter
                if (experimentParameter[iIndex][0] in 
                    {MAINS_FILTER, ENABLE_OPTIMIZER, LOW_PERFORMANCE_MODE}):
                    tempIntVar = IntVar()
                    tempIntVar.set(experimentParameter[iIndex][1])
                    self._tempList.append(tempIntVar)

                    EntryParameter = Checkbutton(fParameterFrame, state= DISABLED,
                        style="fCheckButtonGeneral.TCheckbutton",
                        variable= tempIntVar, onvalue= True, offvalue= False )
                    EntryParameter.pack(side= LEFT, fill= Y, padx = 5, pady= 5)              
                else :       
                    TextValue= Label(fParameterFrame, width= TEXTBOX_WIDTH, 
                        text= str(experimentParameter[iIndex][1]), 
                        style= "fLabelGeneralWhiteSmall.TLabel")
                    TextValue.pack(side= LEFT, padx= 5, pady= 5)     

    def PopUp_Tooltip(self, entry : str) -> None:
        """
        Description
        -----------
        Create a PopUp window for the tool tip for every entry

        """
        # Check if window is open and just hidden
        try:
            # Unhide window
            self._PopUpRoot.overrideredirect(0)
            self._PopUpRoot.deiconify()
            self._clearFrame(self._PopUpRoot)
        except:
            # Create new window
            self._initWindow()
            self._PopUpRoot.deiconify()

        self._PopUpRoot.overrideredirect(1)

        # Create frame information
        fTooltipFrame = Frame(self._PopUpRoot, style="fPopUp.TFrame")
        fTooltipFrame.pack(fill= 'both', side= TOP, padx= 1, pady= 1)

        TextGeneral = Label(fTooltipFrame, text= dic_parameters[entry][1], 
            width= PW_X_POSITION - 5, wraplengt= PW_X_POSITION - 5, 
            style= "fLabelGeneralWhiteSmall.TLabel")
        TextGeneral.pack(side= TOP, padx= 2, pady= 2) 

        self._PopUpRoot.geometry(f'{PW_X_POSITION}x{TextGeneral.winfo_reqheight() + 6}+{self._PopUpRoot.winfo_pointerx() + 5}+{self._PopUpRoot.winfo_pointery() + 5}')

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

    def _on_Closing(self):
        """
        Description
        -----------
        On closing event for the popup window.

        """
        self._PopUpRoot.withdraw()