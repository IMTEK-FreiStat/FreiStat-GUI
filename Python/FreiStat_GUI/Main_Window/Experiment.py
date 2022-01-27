"""
Sub module of the class FreiStatInterface, which implements all functions which
are used to execute the experiments.

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
from FreiStat.Methods.run_electrochemical_method import Run_Electrochemical_Method
from FreiStat.Methods.run_chronoamperometry import Run_CA
from FreiStat.Methods.run_linear_sweep_voltammetry import Run_LSV
from FreiStat.Methods.run_cyclic_voltammetry import Run_CV
from FreiStat.Methods.run_normal_pulse_voltammetry import Run_NPV
from FreiStat.Methods.run_differential_pulse_voltammetry import Run_DPV
from FreiStat.Methods.run_square_wave_voltammetry import Run_SWV
from FreiStat.Methods.run_sequence import Run_Sequence

from matplotlib import pyplot as plt
from matplotlib.figure import SubplotParams
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import matplotlib
matplotlib.use('TkAgg')

# Import internal dependencies
from ..Data_Storage.constants import *

def _executeExperiment(self) -> None:
    """
    Description
    -----------
    Method which starts the different facades of the Python library with
    the chosen experiment parameters
    
    """
    # Clear central frame
    self._clearFrame(self._fCentralFrame)

    if (self._dataHandling.get_ExperimentType() == SEQUENCE):
        # Execute the sequence
        self._executeSequence()
    else :
        # Execute in single mode
        self._executeSingleMethod()

def _executeSingleMethod(self) -> None:
    """
    Description
    -----------
    Method which starts the single mode of the Python library with the chosen 
    experiment parameters
    
    """
    # Initialize variables
    iCommunicationMode : int

    listExperimentParameters : list = []

    if (self._iWLANMode.get() == True):
        iCommunicationMode = FREISTAT_WLAN
    else :
        iCommunicationMode = FREISTAT_SERIAL

    RunEcMethod : Run_Electrochemical_Method = None

    # Check which experiment should be executed
    if (self._dataHandling.get_ExperimentType() == CA):
        # Temporary store experiment paramters
        listExperimentParameters = self._dataHandling.get_ExperimentParameters()

        # Save low performance mode
        self._bLowPerformanceMode = listExperimentParameters[9][1]

        # Run chronoamperometry on FreiStat
        RunEcMethod = Run_CA(logger= self._logger, mode= FREISTAT_BACKEND, 
                             commnicationMode= iCommunicationMode, 
                             wlanSetting=[self._strServerIP.get(),
                                          int(self._strServerPort.get()),
                                          self._strClientIP.get(),
                                          int(self._strClientPort.get())])
        self._EcMethod = RunEcMethod
        
        RunEcMethod.start(Potential_Steps= listExperimentParameters[0][1], 
                          Pulse_Lengths= listExperimentParameters[1][1],
                          Sampling_Rate= listExperimentParameters[2][1],
                          Cycle= listExperimentParameters[3][1],
                          CurrentRange= listExperimentParameters[4][1],
                          MainsFilter = listExperimentParameters[5][1],
                          Sinc2_Oversampling = listExperimentParameters[6][1],
                          Sinc3_Oversampling = listExperimentParameters[7][1],
                          EnableOptimizer= listExperimentParameters[8][1],
                          LowPerformanceMode= listExperimentParameters[9][1])

        if (listExperimentParameters[8][1] == True):
            self._dataHandling.save_ExperimentParmeters(
                self._decodeOptimizerParameters(
                    RunEcMethod._listExperimentParameters))
            self._update_PrameterbandFrame(self._fParameterBand)

    elif (self._dataHandling.get_ExperimentType() == LSV):
        # Temporary store experiment paramters
        listExperimentParameters = self._dataHandling.get_ExperimentParameters()

        # Save low performance mode
        self._bLowPerformanceMode = listExperimentParameters[11][1]

        # Run linear sweep voltammetry on FreiStat
        RunEcMethod = Run_LSV(logger= self._logger, mode= FREISTAT_BACKEND, 
                              commnicationMode= iCommunicationMode, 
                              wlanSetting=[self._strServerIP.get(),
                                           int(self._strServerPort.get()),
                                           self._strClientIP.get(),
                                           int(self._strClientPort.get())])
        self._EcMethod = RunEcMethod

        RunEcMethod.start(StartVoltage= listExperimentParameters[0][1], 
                          StopVoltage= listExperimentParameters[1][1],
                          Stepsize= listExperimentParameters[2][1],
                          Scanrate= listExperimentParameters[3][1],
                          Cycle= listExperimentParameters[4][1],
                          CurrentRange= listExperimentParameters[5][1],
                          FixedWEPotential= listExperimentParameters[6][1],
                          MainsFilter = listExperimentParameters[7][1],
                          Sinc2_Oversampling = listExperimentParameters[8][1],
                          Sinc3_Oversampling = listExperimentParameters[9][1],
                          EnableOptimizer= listExperimentParameters[10][1],
                          LowPerformanceMode= listExperimentParameters[11][1])

        if (listExperimentParameters[10][1] == True):
            self._dataHandling.save_ExperimentParmeters(
                self._decodeOptimizerParameters(
                    RunEcMethod._listExperimentParameters))
            self._update_PrameterbandFrame(self._fParameterBand)

    elif (self._dataHandling.get_ExperimentType() == CV):
        # Temporary store experiment paramters
        listExperimentParameters = self._dataHandling.get_ExperimentParameters()

        # Save low performance mode
        self._bLowPerformanceMode = listExperimentParameters[12][1]

        # Run cyclic voltammetry on FreiStat
        RunEcMethod = Run_CV(logger= self._logger, mode= FREISTAT_BACKEND, 
                             commnicationMode= iCommunicationMode, 
                             wlanSetting=[self._strServerIP.get(),
                                          int(self._strServerPort.get()),
                                          self._strClientIP.get(),
                                          int(self._strClientPort.get())])
        self._EcMethod = RunEcMethod

        RunEcMethod.start(StartVoltage= listExperimentParameters[0][1], 
                          SecondVertex= listExperimentParameters[1][1],
                          FirstVertex= listExperimentParameters[2][1],
                          Stepsize= listExperimentParameters[3][1],
                          Scanrate= listExperimentParameters[4][1],
                          Cycle= listExperimentParameters[5][1],
                          CurrentRange= listExperimentParameters[6][1],
                          FixedWEPotential= listExperimentParameters[7][1],
                          MainsFilter = listExperimentParameters[8][1],
                          Sinc2_Oversampling = listExperimentParameters[9][1],
                          Sinc3_Oversampling = listExperimentParameters[10][1],
                          EnableOptimizer= listExperimentParameters[11][1],
                          LowPerformanceMode= listExperimentParameters[12][1])

        if (listExperimentParameters[11][1] == True):
            self._dataHandling.save_ExperimentParmeters(
                self._decodeOptimizerParameters(
                    RunEcMethod._listExperimentParameters))
            self._update_PrameterbandFrame(self._fParameterBand)

    elif (self._dataHandling.get_ExperimentType() == NPV):
        # Temporary store experiment paramters
        listExperimentParameters = self._dataHandling.get_ExperimentParameters()

        # Save low performance mode
        self._bLowPerformanceMode = listExperimentParameters[13][1]

        # Run normal pulse voltammetry on FreiStat
        RunEcMethod = Run_NPV(logger= self._logger, mode= FREISTAT_BACKEND, 
                              commnicationMode= iCommunicationMode, 
                              wlanSetting=[self._strServerIP.get(),
                                           int(self._strServerPort.get()),
                                           self._strClientIP.get(),
                                           int(self._strClientPort.get())])
        self._EcMethod = RunEcMethod
        
        RunEcMethod.start(BaseVoltage= listExperimentParameters[0][1],
                          StartVoltage= listExperimentParameters[1][1], 
                          StopVoltage= listExperimentParameters[2][1],
                          DeltaV_Staircase= listExperimentParameters[3][1],
                          Pulse_Lengths= listExperimentParameters[4][1],
                          Sampling_Duration= listExperimentParameters[5][1],
                          Cycle= listExperimentParameters[6][1],
                          CurrentRange= listExperimentParameters[7][1],
                          FixedWEPotential= listExperimentParameters[8][1],
                          MainsFilter = listExperimentParameters[9][1],
                          Sinc2_Oversampling = listExperimentParameters[10][1],
                          Sinc3_Oversampling = listExperimentParameters[11][1],
                          EnableOptimizer= listExperimentParameters[12][1],
                          LowPerformanceMode= listExperimentParameters[13][1])

        if (listExperimentParameters[12][1] == True):
            self._dataHandling.save_ExperimentParmeters(
                self._decodeOptimizerParameters(
                    RunEcMethod._listExperimentParameters))
            self._update_PrameterbandFrame(self._fParameterBand)

    elif (self._dataHandling.get_ExperimentType() == DPV):
        # Temporary store experiment paramters
        listExperimentParameters = self._dataHandling.get_ExperimentParameters()

        # Save low performance mode
        self._bLowPerformanceMode = listExperimentParameters[13][1]

        # Run differential pulse voltammetry on FreiStat
        RunEcMethod = Run_DPV(logger= self._logger, mode= FREISTAT_BACKEND, 
                              commnicationMode= iCommunicationMode, 
                              wlanSetting=[self._strServerIP.get(),
                                           int(self._strServerPort.get()),
                                           self._strClientIP.get(),
                                           int(self._strClientPort.get())])
        self._EcMethod = RunEcMethod
        
        RunEcMethod.start(StartVoltage= listExperimentParameters[0][1], 
                          StopVoltage= listExperimentParameters[1][1],
                          DeltaV_Staircase= listExperimentParameters[2][1],
                          DeltaV_Peak= listExperimentParameters[3][1],
                          Pulse_Lengths= listExperimentParameters[4][1],
                          Sampling_Duration= listExperimentParameters[5][1],
                          Cycle= listExperimentParameters[6][1],
                          CurrentRange= listExperimentParameters[7][1],
                          FixedWEPotential= listExperimentParameters[8][1],
                          MainsFilter = listExperimentParameters[9][1],
                          Sinc2_Oversampling = listExperimentParameters[10][1],
                          Sinc3_Oversampling = listExperimentParameters[11][1],
                          EnableOptimizer= listExperimentParameters[12][1],
                          LowPerformanceMode= listExperimentParameters[13][1])

        if (listExperimentParameters[12][1] == True):
            self._dataHandling.save_ExperimentParmeters(
                self._decodeOptimizerParameters(
                    RunEcMethod._listExperimentParameters))
            self._update_PrameterbandFrame(self._fParameterBand)

    elif (self._dataHandling.get_ExperimentType() == SWV):
        # Temporary store experiment paramters
        listExperimentParameters = self._dataHandling.get_ExperimentParameters()

        # Save low performance mode
        self._bLowPerformanceMode = listExperimentParameters[13][1]

        # Run square wave voltammetry on FreiStat
        RunEcMethod = Run_SWV(logger= self._logger, mode= FREISTAT_BACKEND, 
                              commnicationMode= iCommunicationMode, 
                              wlanSetting=[self._strServerIP.get(),
                                           int(self._strServerPort.get()),
                                           self._strClientIP.get(),
                                           int(self._strClientPort.get())])
        self._EcMethod = RunEcMethod

        RunEcMethod.start(StartVoltage= listExperimentParameters[0][1], 
                          StopVoltage= listExperimentParameters[1][1],
                          DeltaV_Staircase= listExperimentParameters[2][1],
                          DeltaV_Peak= listExperimentParameters[3][1],
                          DutyCycle= listExperimentParameters[4][1],
                          Sampling_Duration= listExperimentParameters[5][1],
                          Cycle= listExperimentParameters[6][1],
                          CurrentRange= listExperimentParameters[7][1],
                          FixedWEPotential= listExperimentParameters[8][1],
                          MainsFilter = listExperimentParameters[9][1],
                          Sinc2_Oversampling = listExperimentParameters[10][1],
                          Sinc3_Oversampling = listExperimentParameters[11][1],
                          EnableOptimizer= listExperimentParameters[12][1],
                          LowPerformanceMode= listExperimentParameters[13][1])

        if (listExperimentParameters[12][1] == True):
            self._dataHandling.save_ExperimentParmeters(
                self._decodeOptimizerParameters(
                RunEcMethod._listExperimentParameters))
            self._update_PrameterbandFrame(self._fParameterBand)

    # Save reference of the plotter
    self._plotter = RunEcMethod.get_plotter()

    # Save reference of the process
    self._process = RunEcMethod.get_process()

    # Save reference of the figure to prevent garbage collection
    self._fig = self._plotter.get_figure()

    # Save reference of the data queue to prevent garbage collection
    self._dataQueue = RunEcMethod.get_dataQueue()
    
    # Resize figure
    iDpi = self._fCentralFrame.winfo_fpixels('3c')
    self._fig.set_size_inches(self._fCentralFrame.winfo_width() / iDpi, 
                                self._fCentralFrame.winfo_height()/ iDpi, 
                                forward=True)

    # Draw frame of the figure
    self._fLiveFeed = Frame(self._fCentralFrame, style="fCentralFrame.TFrame")
    self._fLiveFeed.pack(fill= 'both', side=TOP, expand=TRUE, padx= 2, pady= 2)
    self._canvas = FigureCanvasTkAgg(self._fig, master= self._fLiveFeed)
    self._canvas.get_tk_widget().pack(side= TOP, expand= TRUE)
    self._canvas.draw()

    # Create the toolbar
    self._toolbarFrame = Frame(master= self._fLiveFeed)
    self._toolbarFrame.pack(fill= X, side= BOTTOM, expand= False, padx= 5)
    toolbar = Toolbar(self._canvas, self._toolbarFrame)
    toolbar.config(background= "white")
    toolbar._message_label.config(background= "white", font= "Arial 10 bold")

    self._plotter.set_listBox(self._TextTerminal)
    self._plotter.set_progressBar(self._ProgressBar)
    
    # Call animate function of plotter
    if (self._bLowPerformanceMode == False):
        self._plotter.T_Animate(self._dataQueue)
        self._animate = self._plotter.get_animate()
        self._canvas.draw()
    else :
        self._plotter.T_Print(self._strGLpmLatency.get(), self._dataQueue)
        self._animate = self._plotter.get_animate()

    # Update frame
    self._fLiveFeed.update()

def _executeSequence(self) -> None:
    """
    Description
    -----------
    Method which starts the squence mode of the Python library with the chosen 
    experiment parameters
    
    """
    # Initialize variabels
    bEnableOptimizer : bool = False
    bLowPerformanceMode : bool = False
    iCommunicationMode : int
    self._listCanvas = []
    
    if (self._iWLANMode.get() == True):
        iCommunicationMode = FREISTAT_WLAN
    else :
        iCommunicationMode = FREISTAT_SERIAL


    # Temporary store experiment paramters
    listExperimentParameters = self._dataHandling.get_ExperimentParameters()

    # Check if the optimizer and the low performance mode should be enabled
    # Loop over the experiment parameter list
    for iIndex in range(len(listExperimentParameters)):
        # Loop over the experiment parameters in each method
        for iParameter in range(len(listExperimentParameters[iIndex][2])):
            if (listExperimentParameters[iIndex][2][iParameter][0] ==
                ENABLE_OPTIMIZER):
                
                # Check if the optimizer of one method is enabled
                if (listExperimentParameters[iIndex][2][iParameter][1] == True):
                    bEnableOptimizer = True

            if (listExperimentParameters[iIndex][2][iParameter][0] ==
                LOW_PERFORMANCE_MODE):
                
                # Check if the optimizer of one method is enabled
                if (listExperimentParameters[iIndex][2][iParameter][1] == True):
                    bLowPerformanceMode = True

    # Create a sequence object
    RunEcMethod2 = Run_Sequence(EnableOptimizer= bEnableOptimizer, 
                               logger=self._logger, mode= FREISTAT_BACKEND, 
                               commnicationMode= iCommunicationMode, 
                               wlanSetting=[self._strServerIP.get(),
                                            int(self._strServerPort.get()),
                                            self._strClientIP.get(),
                                            int(self._strClientPort.get())])
    self._EcMethod = RunEcMethod2

    # Add methods to the sequence
    for iMethod in range(len(listExperimentParameters)):
        if (listExperimentParameters[iMethod][0] == CA):
            RunEcMethod2.add_CA(
                Potential_Steps= listExperimentParameters[iMethod][2][0][1], 
                Pulse_Lengths= listExperimentParameters[iMethod][2][1][1],
                Sampling_Rate= listExperimentParameters[iMethod][2][2][1],
                Cycle= listExperimentParameters[iMethod][2][3][1],
                CurrentRange= listExperimentParameters[iMethod][2][4][1],
                MainsFilter = listExperimentParameters[iMethod][2][5][1],
                Sinc2_Oversampling = listExperimentParameters[iMethod][2][6][1],
                Sinc3_Oversampling = listExperimentParameters[iMethod][2][7][1])

        elif (listExperimentParameters[iMethod][0] == LSV):
            RunEcMethod2.add_LSV(
                StartVoltage= listExperimentParameters[iMethod][2][0][1], 
                StopVoltage= listExperimentParameters[iMethod][2][1][1],
                Stepsize= listExperimentParameters[iMethod][2][2][1],
                Scanrate= listExperimentParameters[iMethod][2][3][1],
                Cycle= listExperimentParameters[iMethod][2][4][1],
                CurrentRange= listExperimentParameters[iMethod][2][5][1],
                FixedWEPotential= listExperimentParameters[iMethod][2][6][1],
                MainsFilter = listExperimentParameters[iMethod][2][7][1],
                Sinc2_Oversampling = listExperimentParameters[iMethod][2][8][1],
                Sinc3_Oversampling = listExperimentParameters[iMethod][2][9][1])

        elif (listExperimentParameters[iMethod][0] == CV):
            RunEcMethod2.add_CV(
                StartVoltage= listExperimentParameters[iMethod][2][0][1], 
                SecondVertex= listExperimentParameters[iMethod][2][1][1],
                FirstVertex= listExperimentParameters[iMethod][2][2][1],
                Stepsize= listExperimentParameters[iMethod][2][3][1],
                Scanrate= listExperimentParameters[iMethod][2][4][1],
                Cycle= listExperimentParameters[iMethod][2][5][1],
                CurrentRange= listExperimentParameters[iMethod][2][6][1],
                FixedWEPotential= listExperimentParameters[iMethod][2][7][1],
                MainsFilter = listExperimentParameters[iMethod][2][8][1],
                Sinc2_Oversampling = listExperimentParameters[iMethod][2][9][1],
                Sinc3_Oversampling = listExperimentParameters[iMethod][2][10][1])

        elif (listExperimentParameters[iMethod][0] == NPV):
            RunEcMethod2.add_NPV(
                BaseVoltage= listExperimentParameters[iMethod][2][0][1],
                StartVoltage= listExperimentParameters[iMethod][2][1][1], 
                StopVoltage= listExperimentParameters[iMethod][2][2][1],
                DeltaV_Staircase= listExperimentParameters[iMethod][2][3][1],
                Pulse_Lengths= listExperimentParameters[iMethod][2][4][1],
                Sampling_Duration= listExperimentParameters[iMethod][2][5][1],
                Cycle= listExperimentParameters[iMethod][2][6][1],
                CurrentRange= listExperimentParameters[iMethod][2][7][1],
                FixedWEPotential= listExperimentParameters[iMethod][2][8][1],
                MainsFilter = listExperimentParameters[iMethod][2][9][1],
                Sinc2_Oversampling = listExperimentParameters[iMethod][2][10][1],
                Sinc3_Oversampling = listExperimentParameters[iMethod][2][11][1])

        elif (listExperimentParameters[iMethod][0] == DPV):
            RunEcMethod2.add_DPV(
                StartVoltage= listExperimentParameters[iMethod][2][0][1], 
                StopVoltage= listExperimentParameters[iMethod][2][1][1],
                DeltaV_Staircase= listExperimentParameters[iMethod][2][2][1],
                DeltaV_Peak= listExperimentParameters[iMethod][2][3][1],
                Pulse_Lengths= listExperimentParameters[iMethod][2][4][1],
                Sampling_Duration= listExperimentParameters[iMethod][2][5][1],
                Cycle= listExperimentParameters[iMethod][2][6][1],
                CurrentRange= listExperimentParameters[iMethod][2][7][1],
                FixedWEPotential= listExperimentParameters[iMethod][2][8][1],
                MainsFilter = listExperimentParameters[iMethod][2][9][1],
                Sinc2_Oversampling = listExperimentParameters[iMethod][2][10][1],
                Sinc3_Oversampling = listExperimentParameters[iMethod][2][11][1])

        elif (listExperimentParameters[iMethod][0] == SWV):
            RunEcMethod2.add_SWV(
                StartVoltage= listExperimentParameters[iMethod][2][0][1], 
                StopVoltage= listExperimentParameters[iMethod][2][1][1],
                DeltaV_Staircase= listExperimentParameters[iMethod][2][2][1],
                DeltaV_Peak= listExperimentParameters[iMethod][2][3][1],
                DutyCycle= listExperimentParameters[iMethod][2][4][1],
                Sampling_Duration= listExperimentParameters[iMethod][2][5][1],
                Cycle= listExperimentParameters[iMethod][2][6][1],
                CurrentRange= listExperimentParameters[iMethod][2][7][1],
                FixedWEPotential= listExperimentParameters[iMethod][2][8][1],
                MainsFilter = listExperimentParameters[iMethod][2][9][1],
                Sinc2_Oversampling = listExperimentParameters[iMethod][2][10][1],
                Sinc3_Oversampling = listExperimentParameters[iMethod][2][11][1])

    # Start the sequence
    RunEcMethod2.start(SequenceCycles= self._dataHandling.get_SequenceCycles(),
                      LowPerformanceMode= bLowPerformanceMode)

    # Save reference of the plotter
    self._plotter = RunEcMethod2.get_plotter()

    # Save reference of the process
    self._process = RunEcMethod2.get_process()

    # Save reference of the figure to prevent garbage collection
    self._fig = self._plotter.get_figure()

    # Save reference of the list of figures to prevent garbage collection
    self._listFigures = self._plotter.get_listfigures()

    # Save reference of the data queue to prevent garbage collection
    self._dataQueue = RunEcMethod2.get_dataQueue()

    # Resize figure
    iDpi = self._fCentralFrame.winfo_fpixels('3c')
    self._fig.set_size_inches(self._fCentralFrame.winfo_width() / iDpi, 
                              self._fCentralFrame.winfo_height() / iDpi, 
                              forward=True)

    # Draw frame of the figure
    self._fLiveFeed = Frame(self._fCentralFrame, style="fCentralFrame.TFrame")
    self._fLiveFeed.pack(fill= 'both', side=TOP, expand=TRUE, padx= 2, pady= 2)
    self._canvas = FigureCanvasTkAgg(self._fig, master= self._fLiveFeed)
    self._canvas.get_tk_widget().pack(side= TOP, expand= TRUE)
    self._canvas.draw()

    # Create the toolbar
    self._toolbarFrame = Frame(master= self._fLiveFeed)
    self._toolbarFrame.pack(fill= X, side= BOTTOM, expand= False, padx= 5)
    toolbar = Toolbar(self._canvas, self._toolbarFrame)
    toolbar.config(background= "white")
    toolbar._message_label.config(background= "white", font= "Arial 10 bold")

    # Draw frame of the figure
    self._fStaticPlot = Frame(self._fCentralFrame, style="fCentralFrame.TFrame")
    self._fStaticPlot.pack(fill= 'both', side=TOP, expand=TRUE, padx= 2, pady= 2)

    # Create canvas for each plot
    for iIndex in range(len(self._listFigures)):
        # Resize figure
        iDpi = self._fPlotFrame.winfo_fpixels('3c')

        self._listFigures[iIndex].set_size_inches(
            self._fPlotFrameHeight / iDpi * 1.2, 
            self._fPlotFrameHeight / iDpi, forward=True)

        # Draw frame of the figure
        self._listCanvas.append(FigureCanvasTkAgg(self._listFigures[iIndex], 
                                                  master= self._fPlotFrame))
        self._listCanvas[iIndex].get_tk_widget().pack(side= LEFT, 
            anchor= N, padx = 5)
        self._listCanvas[iIndex].mpl_connect("button_press_event", lambda event, 
            iPlotID = iIndex: self._on_mouse_press(event, iPlotID))
        self._listCanvas[iIndex].draw()

    # Create one central plot
    subplotParams = SubplotParams(top= 0.95, right= 0.75)
    self._figureStatic, (self._axesStatic) = plt.subplots(1, 1,
                                        subplotpars= subplotParams)
    self._figureStatic.set_size_inches(self._fCentralFrame.winfo_width() / iDpi, 
                                       self._fCentralFrame.winfo_height()/ iDpi, 
                                       forward=True)
    self._axesStatic.grid()

    self._canvasStatic = FigureCanvasTkAgg(self._figureStatic, 
                                            master= self._fStaticPlot)
    self._canvasStatic.get_tk_widget().pack(side= TOP, expand= TRUE)
    self._canvasStatic.draw()


    # Create the toolbar
    self._toolbarFrameStatic = Frame(master= self._fStaticPlot)
    toolbarStatic = Toolbar(self._canvasStatic, self._toolbarFrameStatic)
    toolbarStatic.config(background= "white")
    toolbarStatic._message_label.config(background= "white", font= "Arial 10 bold")

    self._fStaticPlot.pack_forget()

    self._plotter.set_listBox(self._TextTerminal)
    self._plotter.set_progressBar(self._ProgressBar)

    # Call animate function of plotter
    self._plotter.T_Animate(self._dataQueue)
    self._animate = self._plotter.get_animate()
    self._canvas.draw()

    # Update frame
    self._fLiveFeed.update()

class Toolbar(NavigationToolbar2Tk): 
    """
    Description
    -----------
    Custom class overwriting the default matplotlib plot toolbar.
    
    """
    def __init__(self, plotCanvas, frame):
        # Create the default toolbar
        NavigationToolbar2Tk.__init__(self, plotCanvas, frame)

        # Remove the button to reconfig the subplots
        self.children['!button4'].pack_forget() 