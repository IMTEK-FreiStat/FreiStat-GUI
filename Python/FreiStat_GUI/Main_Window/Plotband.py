"""
Sub module of the class FreiStatInterface, which implements the plotband.

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

def _create_PlotbandTabFrame(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the plot band at the bottom of the interface, which
    is used to display the plots in sequence mode and the received data.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the plot band frame is embedded

    """       
    # Create tab for terminal output and plots
    self._fTab = Frame(parentFrame, style= "fPlotBandTab.TFrame")
    self._fTab.pack(fill= X, side= TOP, expand= False)

    # Create a button for terminal and a button for plots
    self._ButtonTerminal = Button(self._fTab, text= "Terminal",
        command= lambda : self._clickButton(BUTTON_TERMINAL))        
    self._ButtonTerminal.pack(side= LEFT, fill= Y, padx = 5, pady= 1)

    self._ButtonPlots = Button(self._fTab, text= "Plots",
        command= lambda : self._clickButton(BUTTON_PLOTS))        
    self._ButtonPlots.pack(side= LEFT, fill= Y, pady= 1)

    self._MinimizePlotbandTab = Button(self._fTab, image= self._IconMinimize,
        command= lambda : self._clickMinimizeButton(BUTTON_MINIMIZE_PB))        
    self._MinimizePlotbandTab.pack(side= RIGHT, fill= Y, pady= 1)

def _create_PlotbandFrame(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for creating the plot band at the bottom of the interface, which
    is used to display the plots in sequence mode and the received data.

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the plot band frame is embedded

    """       
    # Initialize parameters
    self._fPlotFrameHeight = 250

    # Create frame for plot band 
    self._fPlotBand = Frame(parentFrame, style="fPlotBand.TFrame", 
                            height= self._fPlotFrameHeight)
    self._fPlotBand.pack(fill= X, side= TOP, expand= False)

    self._fPlotBand.pack_propagate(0)

    # Create terminal window
    self._TextTerminal = Listbox(self._fPlotBand)

    ScrollbarXTerminal = Scrollbar(self._fPlotBand, orient='horizontal', 
                                   command=self._multiscroll_plotband)
    ScrollbarYTerminal = Scrollbar(self._fPlotBand, orient='vertical', 
                                   command=self._TextTerminal.yview)
    ScrollbarYTerminal.pack(side= RIGHT, expand=False, fill=Y) 

    self._TextTerminal.config(xscrollcommand=ScrollbarXTerminal.set,
                              yscrollcommand=ScrollbarYTerminal.set)
    self._TextTerminal.pack(side= TOP, expand= True, fill= 'both', 
                            padx= 5, pady= 5)

    ScrollbarXTerminal.pack(side= BOTTOM, expand=False, fill=X)   
    
    # Create plot window
    # Create a canvas window
    self._fPlotHeadFrame = Frame(self._fPlotBand, style="fPlotBand.TFrame")
    self._fPlotHeadFrame.pack(fill= BOTH, side= TOP, expand= True, padx= 5, pady= 5)
    self._canvasPlot = Canvas(self._fPlotHeadFrame, background= "white",
                              borderwidth= 0, highlightthickness= 0)

    
    self._canvasPlot.pack(fill= 'both', expand= True, side= TOP)
    
    # Add scroll command to canvas
    self._canvasPlot.configure(xscrollcommand= ScrollbarXTerminal.set)

    self._fPlotFrame = Frame(self._canvasPlot, style="fPlotBand.TFrame")
    self._fPlotFrame.pack(fill= BOTH, side= TOP, expand= TRUE)
    
    # Update windows to get correct size informations
    self._canvasPlot.create_window((0,0), window= self._fPlotFrame, 
        anchor= NW, width= 2000, height= self._fPlotFrameHeight)

    self._fPlotHeadFrame.pack_forget() 

def _multiscroll_plotband(self, *args):
    """
    Description
    -----------
    helper method allowing for multiple scrolls with one scrollbar.
    
    """
    self._canvasPlot.xview(*args)
    self._TextTerminal.xview(*args)


def _update_PlotbandFrame_Terminal(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for displaying the terminal output of the FreiStat

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the plot band frame is embedded

    """
    # Clear the listbox widget for the plot outpu
    self._fPlotHeadFrame.pack_forget() 

    # Show the listbox widget for the terminal output
    self._TextTerminal.pack(side= TOP, fill='both', expand= True, 
                            padx= 5, pady= 5) 

def _update_PlotbandFrame_Plots(self, parentFrame: Frame) -> None:
    """
    Description
    -----------
    Method for displaying the plots of the FreiStat

    Parameters
    ----------
    `parentFrame` : Frame
        Parent frame in which the plot band frame is embedded

    """
    # Clear the listbox widget for the terminal output
    self._TextTerminal.pack_forget() 

    # Show the frame for the plots
    self._fPlotHeadFrame.pack(fill= BOTH, side= TOP, expand= True, padx= 5, pady= 5)
    """
    # Remove legend of the figure
    for iIndex in range(len(self._listFigures)):
        if (self._listFigures[iIndex].gca().get_legend() is not None):
            self._listFigures[iIndex].gca().get_legend().set_visible(False)
            self._listCanvas[iIndex].draw()
    """

def _on_mouse_press(self, event, iPlotID):
    """
    Description
    -----------
    Click event when clicking on a plot in the plot window. The plot is then
    displayed in the central frame.

    Parameters
    ----------
    `event` : event
        Event which should be handled

    `iPlotID` : int
        ID of the plot which was pressed

    """
    # Enable live feed button
    self._ButtonLiveFeed["state"] = NORMAL

    # Prevent multiple times clicking on the same image
    if (self._iPlotIDprevious == iPlotID):
        return

    # Update previously clicked image
    self._iPlotIDprevious = iPlotID

    # Hide live feed and show static plot
    self._hideFrame(self._fCentralFrame)
    self._fStaticPlot.pack(fill= 'both', side= TOP, expand= TRUE, padx= 2, pady= 2)
    self._toolbarFrameStatic.pack(fill= X, side= BOTTOM, expand= False, padx= 5)

    # Remove lines from static plot
    for iIndex in range(len(self._axesStatic.lines)):
        self._axesStatic.lines[0].remove()

    # Add new lines to static plot with the correct data
    for iIndex in range(len(self._listFigures[iPlotID].gca().lines)):
        self._axesStatic.plot(
            self._listFigures[iPlotID].gca().lines[iIndex].get_xdata(), 
            self._listFigures[iPlotID].gca().lines[iIndex].get_ydata())

    # Add labels to the plot
    for iIndex in range(len(self._axesStatic.lines)):
        self._axesStatic.lines[iIndex].set_label(
            self._listFigures[iPlotID].gca().lines[iIndex].get_label())
        
        self._axesStatic.set_xlabel(
            self._listFigures[iPlotID].gca().xaxis.get_label().get_text())
        self._axesStatic.set_ylabel(
            self._listFigures[iPlotID].gca().yaxis.get_label().get_text())

    # Update legend
    self._axesStatic.legend(title= PLOT_LEGEND_NAME, 
        bbox_to_anchor=(1.05, 1), loc='upper left')
    
    self._figureStatic.canvas.draw()

