#-------------------------------------------------------------------------------
# Name:        input.py
# Purpose:     This module is for the input class which uses the pre-defined
#              tkinter 'Entry' widget
#
# Author:      Petar Petkovic
#
# Created:     13/04/2015
# Copyright:   (c) Petar Petkovic 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter.ttk import *

class input:
    def __init__(self, master, x, y, width, show=""):

        """ Creates a rectangular modern OS based text input field
        (thanks to the tkinter.ttk module) using tkinter.

        master - the frame the button is placed on
        x      - the x position of the top-left corner of the field in pixels
        y      - the y position of the top-left corner of the field in pixels
        width  - the width of the field in pixels
        show   - OPTIONAL parameter: useful for hiding user input with another
                 character (ex. password fields) """

        self.tvar = StringVar()
        self.input = Entry(master=master, textvariable=self.tvar, show=show)
        self.input.pack()
        self.input.place(x=x, y=y, width=width)

    def get(self):

        """ This function returns the contents of the input field """

        return self.input.get()

