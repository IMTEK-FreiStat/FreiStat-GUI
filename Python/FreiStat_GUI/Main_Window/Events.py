"""
Sub module of the class FreiStatInterface, which implements different event
handling functions.

"""

__author__ = "Mark Jasper"
__contact__ = "University of Freiburg, IMTEK, Jochen Kieninger"
__credits__ = "Mark Jasper"

__version__ = "1.0.0"
__maintainer__ = "Mark Jasper"
__email__ = "mark.jasper@imtek.uni-freiburg.de, kieninger@imtek.uni-freiburg.de"

def _on_focus_out(self, event):
    """
    Description
    -----------
    Method implementing the behavior when losing the focus

    """
    # Destroy the triggering widget
    event.widget.destroy()

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
    frame.bind("<MouseWheel>", lambda event, canvas = canvas: self._onMouseWheel(event, canvas))

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
    frame.unbind("<MouseWheel>")

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

def _on_resize(self, event, canvas):
    """
    Description
    -----------
    Method implementing the behavior when resizing a canvas window

    Parameters
    ----------
    `event` : event
        Event which should be handled

    `canvas` : canvas
        Canvas which should be scrolled

    """
    # Calculate the scaling
    fscaleWidth : float = canvas.winfo_width() / \
        canvas.winfo_children()[0].winfo_width()

    # Scale the canvas
    canvas.scale("all", 0, 0, fscaleWidth, 1)
