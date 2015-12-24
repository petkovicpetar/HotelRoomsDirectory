#-------------------------------------------------------------------------------
# Name:        NapoliWin.py
# Purpose:     This module creates the GUIs for the entire software
#
# Author:      Petar Petkovic
#
# Created:     09/04/2015
# Copyright:   (c) Petar Petkovic 2014
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter.ttk import *
from winsound import MessageBeep

class NapoliWin:
    def __init__(self, size="200x200", title="title"):

        """ Creates a modern OS based graphical window
        (thanks to the tkinter.ttk module) using tkinter.

        size  - string value for the length and width of the window
                (ex. "200x300")
        title - the title of the window placed on the title bar
        """

        self.size = size
        self.title = title
        self.root = Tk()
        self.root.geometry(self.size)
        self.root.resizable(0,0)
        self.root.wm_title(self.title)

    def loopit(self):

        """ This is a mandatory method used by tkinter to loop over
        and over again to run the graphical window. """

        self.root.mainloop()

    def setTitle(self, title):

        """ This method allows the user to set a different window
        title then the one initially assigned. """

        self.title = title
        self.root.wm_title(self.title)

    def close(self):

        """This method allows the user to close the window. """

        self.root.destroy()

class MessageDialog(NapoliWin):
    def __init__(self, size="260x95", title="title", message="message"):

        """ This class inherits attributes from the 'NapoliWin' class
        and makes a default size for all message dialogs in the software.


        """

        NapoliWin.__init__(self, size, title)
        a = Label(master=self.root, text=message)
        # play 'alert' sound
        MessageBeep()
        a.pack(expand=True)
        b = Button(master=self.root, text="Close", command=self.root.destroy)
        b.pack(expand=True)
        self.root.mainloop()



