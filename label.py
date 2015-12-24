#-------------------------------------------------------------------------------
# Name:        label.py
# Purpose:     This module is for the label class which uses the pre-defined
#              tkinter 'Label' widget
#
# Author:      Petar Petkovic
#
# Created:     12/04/2015
# Copyright:   (c) Petar Petkovic 2014
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter.ttk import *

class label:
    def __init__(self,master, x, y, text, font=("Arial", 9, "normal")):

        """ Creates a text label for headings using tkinter.

        master - the frame the label is placed on
        text   - the text that the label will contain
        x      - the x position of the top-left corner of the label in pixels
        y      - the y position of the top-left corner of the label in pixels
        font   - OPTIONAL parameter: useful for changing the font of the
                 label """

        label = Label(master=master, text=text, font=font)
        label.pack()
        label.place(x=x, y=y)

