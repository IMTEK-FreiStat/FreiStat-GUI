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

# Import internal dependencies
from ..Data_Storage.constants import *
from ..Data_Storage.dictionaries import *

class FreiStatPopUp():
    """
    Description
    -----------
    Class for implementing the PopUp windows of the FreiStat interface
    """

    from .Events import _on_rightclick
    from .Events import _on_rightclick_release

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

    def PopUp_Tooltip(self, entry : str) -> None:
        """
        Description
        -----------
        Create a PopUp window for the help setting

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


        self._PopUpRoot.geometry(f'{PW_X_POSITION}x{PW_Y_POSITION_SMALL}+{self._PopUpRoot.winfo_pointerx()}+{self._PopUpRoot.winfo_pointery()}')
        self._PopUpRoot.overrideredirect(1)

        # Create frame information
        fTooltipFrame = Frame(self._PopUpRoot, style="fPopUp.TFrame")
        fTooltipFrame.pack(fill= 'both', side= TOP, expand= True, padx= 1, pady= 1)

        TextGeneral = Label(fTooltipFrame, text= dic_parameters[entry][1], 
            width= PW_X_POSITION - 5, wraplengt= PW_X_POSITION - 5, 
            style= "fLabelGeneralWhiteSmall.TLabel")
        TextGeneral.pack(side= TOP, padx= 2, pady= 2) 

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