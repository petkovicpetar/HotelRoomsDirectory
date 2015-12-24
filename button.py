#-------------------------------------------------------------------------------
# Name:        button.py
# Purpose:     This module is for the button class which uses the pre-defined
#              tkinter 'Button' widget
#
# Author:      Petar Petkovic
#
# Created:     12/04/2015
# Copyright:   (c) Petar Petkovic 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter.ttk import *

class button:
    def __init__(self, master, text, x, y, width, goto):

        """ Creates a rectangular modern OS based button
        (thanks to the tkinter.ttk module) using tkinter.

        master - the frame the button is placed on
        text   - the text that the button will contain
        x      - the x position of the top-left corner of the button in pixels
        y      - the y position of the top-left corner of the button in pixels
        width  - the width of the button in pixels
        goto   - the function that is called when the button is clicked """

        button = Button(master=master, text=text, command=goto)
        button.pack()
        button.place(x=x, y=y, width=width)
