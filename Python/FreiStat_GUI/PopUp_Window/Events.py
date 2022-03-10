"""
Sub module of the class FreiStatPopUp, which implements different event
handling functions.

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

# Import internal dependencies
from ..Data_Storage.dictionaries import *

def _on_rightclick(self, event, entry):
    """
    Description
    -----------
    Method implementing the behavior for right clicking any parameter window

    Parameters
    ----------
    entry : string
        String encoding the parameter (and parameter) which was clicked.

    """
    self.PopUp_Tooltip(entry)

def _on_rightclick_release(self, event, entry):
    """
    Description
    -----------
    Method implementing the behavior for releasing the rightclick after 
    clicking any parameter window

    Parameters
    ----------
    entry : string
        String encoding the parameter (and parameter) which was clicked.

    """
    self._PopUpRoot.withdraw()

def _bound_MouseWheel(self, event, frame, canvas) -> None:
    """
    Description
    -----------
    Helper method which binds the mouse scroll event to a certain canvas frame.
    
    Parameters
    ----------
    `event` : event
        Event which should be handled

    `frame` : frame
        Frame at which the mouse wheel scrolling should work

    `canvas` : canvas
        Canvas which should be scrolled

    """
    frame.bind_all("<MouseWheel>", lambda event, canvas = canvas: self._onMouseWheel(event, canvas))

def _unbound_MouseWheel(self, event, frame) -> None:
    """
    Description
    -----------
    Helper method which unbinds the mouse scroll event to a certain canvas frame.
    
    Parameters
    ----------
    `event` : event
        Event which should be handled

    `frame` : frame
        Frame at which the mouse wheel scrolling should be removed

    """
    frame.unbind_all("<MouseWheel>")

def _onMouseWheel(self, event, canvas) -> None:
    """
    Description
    -----------
    Helper method which defines what happens on mouse scroll.
    
    Parameters
    ----------
    `event` : event
        Event which should be handled

    `canvas` : canvas
        Canvas which should be scrolled

    """
    canvas.yview_scroll(int(-1*(event.delta/120)),"units")
