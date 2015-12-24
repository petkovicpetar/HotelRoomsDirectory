#-------------------------------------------------------------------------------
# Name:        Rooms.py
# Purpose:     This module is for the rooms class which displays all the rooms
#              at the hotel and their given vacancies and details
#
# Author:      Petar Petkovic
#
# Created:     15/04/2015
# Copyright:   (c) Petar Petkovic 2014
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter.ttk import *
from button import button
from label import label
from NapoliWin import *

#main function for rooms
def main():
    #creates window
    win = NapoliWin("400x300", "Hotel Napoli - Rooms")
    line(win)
    #makes the window unable to be edited by the user (full screen)
    win.root.resizable(0,0)
    #labels on the rooms window
    create_labels(win)
    create_buttons(win)
    win.loopit()

def line(win):
    #dimensions of the window
    w = Canvas(master=win.root, width=400, height=300)
    w.pack()
    #separation line between smoking and non-smoking rooms
    w.create_line(200, 0, 200, 300)

def create_labels(win):
    #labels on the rooms window
    label(master=win.root, x=65, y=25, text="Economic", font=("Arial",13,"bold"))
    label(master=win.root, x=80, y=45, text="Smoking")
    label(master=win.root, x=265, y=45, text="Non-Smoking")
    label(master=win.root, x=275, y=25, text="Luxury", font=("Arial",13,"bold"))

def create_buttons(win):
    #creates a list with the details of the room, and appends it to a empty list
    b = []
    room = 1
    for i in range(20):
        infile = open("All Rooms/r" + str(room) + ".txt","r").read()
        #[""] is a palce holder for the for loop so there isn't an error
        a = infile.split() + [""]
        b.append(a)
        room += 1
    #each room takes a spot from the list and shows the ID if there is one beside the room number
    #creates the room buttons on the window using the button class
    button_one = button(master=win.root, text="1 - " + b[0][6], x=15, y=95, width=80, goto=lambda:Details("1"))
    button_two = button(master=win.root, text="2 - " + b[1][6], x=110, y=95, width=80, goto=lambda:Details("2"))
    button_three = button(master=win.root, text="3 - "+ b[2][6], x=15, y=135, width=80, goto=lambda:Details("3"))
    button_four = button(master=win.root, text="4 - "+ b[3][6], x=110, y=135, width=80, goto=lambda:Details("4"))
    button_five = button(master=win.root, text="5 - "+ b[4][6], x=15, y=175, width=80, goto=lambda:Details("5"))
    button_six = button(master=win.root, text="6 - "+ b[5][6], x=110, y=175, width=80, goto=lambda:Details("6"))
    button_seven = button(master=win.root, text="7 - "+ b[6][6], x=15, y=215, width=80, goto=lambda:Details("7"))
    button_eight = button(master=win.root, text="8 - "+ b[7][6], x=110, y=215, width=80, goto=lambda:Details("8"))
    button_nine = button(master=win.root, text="9 - "+ b[8][6], x=15, y=255, width=80, goto=lambda:Details("9"))
    button_ten = button(master=win.root, text="10 - "+ b[9][6], x=110, y=255, width=80, goto=lambda:Details("10"))
    button_eleven = button(master=win.root, text="11 - "+ b[10][6], x=215, y=95, width=80, goto=lambda:Details("11"))
    button_twelve = button(master=win.root, text="12 - "+ b[11][6], x=305, y=95, width=80, goto=lambda:Details("12"))
    button_thirteen = button(master=win.root, text="13 - "+ b[12][6], x=215, y=135, width=80, goto=lambda:Details("13"))
    button_fourteen = button(master=win.root, text="14 - "+ b[13][6], x=305, y=135, width=80, goto=lambda:Details("14"))
    button_fifteen = button(master=win.root, text="15 - "+ b[14][6], x=215, y=175, width=80, goto=lambda:Details("15"))
    button_sixteen = button(master=win.root, text="16 - "+ b[15][6], x=305, y=175, width=80, goto=lambda:Details("16"))
    button_seventeen = button(master=win.root, text="17 - "+ b[16][6], x=215, y=215, width=80, goto=lambda:Details("17"))
    button_eighteen = button(master=win.root, text="18 - "+ b[17][6], x=305, y=215, width=80, goto=lambda:Details("18"))
    button_nineteen = button(master=win.root, text="19 - "+ b[18][6], x=215, y=255, width=80, goto=lambda:Details("19"))
    button_twenty = button(master=win.root, text="20 - "+ b[19][6], x=305, y=255, width=80, goto=lambda:Details("20"))

#when button is clicked
def Details(number):
    #gets the file of whatever room number was clicked
    infile = open("All Rooms/r" + number + ".txt","r").read()
    #[""] is a palce holder for the for loop so there isn't an error
    a = infile.split()
    #creates window
    win = NapoliWin("225x175", title="Room#"+number)
    x1=15
    x2=155
    y=10
    text1=["Room number:","Number of beds:","Smoking:","Number of washrooms:","Type of room:","Cost of room:"]
    order = 0
    for i in range(6):
        label(master=win.root, x=x1, y=y, text=text1[order],font=("Arial",9))
        label(master=win.root, x=x2, y=y, text=a[order], font=("Arial",9))
        if i == 5:
            y+=13
        y+=20
        order+=1
    if len(a) == 7:
        label(master=win.root, x=15, y=142, text="ID:", font=("Arial",9))
        button(master=win.root, x=40, y=140, width=80, text=a[6], goto=lambda:win.close())
    button(master=win.root, x=135, y=140, width=80, text="Close", goto=lambda:win.close())
    win.loopit()
main()