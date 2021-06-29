#Designed by a Russian

#to do
# 1) add minimize button
# 1.5) Make file image 
# 2) Assign customizable Path for .txt file
# 3) Make open directory button work


#imports
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import tkinter as tk
import pynput
from pynput import keyboard
from pynput.keyboard import Key, KeyCode, Listener
import pygame
from tkinter import Tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter import *
import datetime
from datetime import datetime
import time

#variables for printing indicated time on bottom right of exe
global last_bookmark
last_bookmark = False

#pygame sound for successful clip
pygame.init()
global s
global o
global c
s = pygame.mixer.Sound("C:\\Users\\svaku\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\QtDesigner\\programs\\ZeitStamp\\shutter.mp3")
o = pygame.mixer.Sound("C:\\Users\\svaku\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\QtDesigner\\programs\\ZeitStamp\\open.mp3")
c = pygame.mixer.Sound("C:\\Users\\svaku\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\QtDesigner\\programs\\ZeitStamp\\close.mp3")

current = set()
import time
from multiprocessing import Pool

#time variabes
global seconds
global minutes
global hours
global stop_timer
stop_timer = False

seconds = 0
minutes = 0
hours = 0

#defining button click commands
def clickstartsession():
    global t1
    global stop_timer
    stop_timer = True
    o = pygame.mixer.Sound("C:\\Users\\svaku\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\QtDesigner\\programs\\ZeitStamp\\open.mp3")
    o.play()
    t1 = threading.Thread(target=timerstart)
    t1.start()

def clickendsession():
    if True:
        print("Your session has ended")
        c = pygame.mixer.Sound("C:\\Users\\svaku\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\QtDesigner\\programs\\ZeitStamp\\close.mp3")
        c.play()
        global stop_timer
        stop_timer = False

def clicktimestamp():
    if True:
        global last_bookmark
        last_bookmark = True
        print((str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)), file=open("TimeStamps.txt", "a"))
        print("You're gay")
        s = pygame.mixer.Sound("C:\\Users\\svaku\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\QtDesigner\\programs\\ZeitStamp\\shutter.mp3")
        s.play()

def clicklabeltimestamps():
    if True:
        ROOT = tk.Tk()
        ROOT.withdraw()
        # the input dialog
        USER_INP = simpledialog.askstring(title="Label Your Bookmark",
                                          prompt="Event Name?")
        # check it out
        print(" ", USER_INP)
        print("Label of Event Above:", USER_INP, file=open("TimeStamps.txt", "a"))

#Scrapped button
#def testfunction():
    #print("testing 123")
    #root = Tk()
    #root.withdraw()

    #current_directory = filedialog.askdirectory()
    #file_name = "TimeStamps.txt"
    #global file_path
    #file_path = os.path.join(current_directory,file_name)
    #print(file_path)


#Code for starting the timer        
def timerstart():
    if True:
        print("jinpin xiao looks like winnie the poo")
        global seconds
        global minutes
        global hours
        global stop_timer
        seconds = 0
        minutes = 0
        hours = 0
    while True:
        seconds = seconds + 1
        print((str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)))
        time.sleep(1)
        #clock logic
        if seconds == 60:
            minutes =minutes + 1
            seconds = 0
        if minutes == 59 and seconds == 60:
            hours = hours + 1
            minutes = 0
            seconds = 0
        if stop_timer == False:
            break
        
#main window and UI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global stop_timer
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(377, 141)
        self.startsession = QtWidgets.QPushButton(MainWindow)
        self.startsession.setGeometry(QtCore.QRect(210, 30, 131, 21))
        self.startsession.setObjectName("startsession")
        self.endsession = QtWidgets.QPushButton(MainWindow)
        self.endsession.setGeometry(QtCore.QRect(210, 60, 131, 23))
        self.endsession.setObjectName("endsession")
        self.timestamp = QtWidgets.QPushButton(MainWindow)
        self.timestamp.setGeometry(QtCore.QRect(220, 90, 111, 23))
        self.timestamp.setObjectName("timestamp")
        #test button to be removed
        #self.test = QtWidgets.QPushButton(MainWindow)
        #self.test.setGeometry(QtCore.QRect(60, 10, 75, 23))
        #self.test.setObjectName("test")
        
        self.lcdNumber = QtWidgets.QLCDNumber(MainWindow)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 40, 161, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        #definition for threading the lcd to sync with the timer
        def letsstarttimer():
            t2 = threading.Thread(target=syncclock)
            t2.start()
        def syncclock():
            while True:
                self.lcdNumber.display(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
        self.labeltimestamps = QtWidgets.QPushButton(MainWindow)
        self.labeltimestamps.setGeometry(QtCore.QRect(20, 120, 101, 21))
        self.labeltimestamps.setObjectName("labeltimestamps")
        self.labellastbookmark = QtWidgets.QLabel(MainWindow)
        self.labellastbookmark.setGeometry(QtCore.QRect(284, 120, 261, 16))
        self.labellastbookmark.setObjectName("label1")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(220, 120, 261, 16))
        self.label.setObjectName("label2")
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


#BUTTON Connections to Definitions
        self.startsession.clicked.connect(clickstartsession)
                                       
        self.startsession.clicked.connect(letsstarttimer)
        
        self.endsession.clicked.connect(clickendsession)
        
        self.timestamp.clicked.connect(clicktimestamp)
        
        self.labeltimestamps.clicked.connect(clicklabeltimestamps)

        #self.test.clicked.connect(testfunction)

#hotkeys (Note- figure out how  to make this work with LCD Timer)        

        def function_1():
            """ One of your functions to be executed by a combination """
            print ("success?")
            return letsstarttimer()
            print('Executed CTR + G')


        # Create a mapping of keys to function (use frozenset as sets/lists are not hashable - so they can't be used as keys)
        # Note the missing `()` after function_1 and function_2 as want to pass the function, not the return value of the function
        combination_to_function = {
            frozenset([Key.ctrl_l, KeyCode(vk=71)]): function_1,  # left ctrl + G
        }

        # The currently pressed keys (initially empty)
        pressed_vks = set()


        def get_vk(key):
            """
            Get the virtual key code from a key.
            These are used so case/shift modifications are ignored.
            """
            return key.vk if hasattr(key, 'vk') else key.value.vk


        def is_combination_pressed(combination):
            """ Check if a combination is satisfied using the keys pressed in pressed_vks """
            return all([get_vk(key) in pressed_vks for key in combination])


        def on_press(key):
            """ When a key is pressed """
            vk = get_vk(key)  # Get the key's vk
            pressed_vks.add(vk)  # Add it to the set of currently pressed keys

            for combination in combination_to_function:  # Loop through each combination
                if is_combination_pressed(combination):  # Check if all keys in the combination are pressed
                    combination_to_function[combination]()  # If so, execute the function


        def on_release(key):
            """ When a key is released """
            vk = get_vk(key)  # Get the key's vk
            pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys

        #Hotkey Listening Run with Multithreading        
        def listenkeyboard():
            with Listener(on_press=on_press, on_release=on_release) as listener:
                listener.join()

        t3 = threading.Thread(target=listenkeyboard)
        t3.start()

    def retranslateUi(self, MainWindow):
        global last_bookmark
        last_bookmark = True
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZeitStamp"))
        self.startsession.setText(_translate("MainWindow", "Start Session (CTR+G)"))
        self.endsession.setText(_translate("MainWindow", "End Session (CTR+H)"))
        self.timestamp.setText(_translate("MainWindow", "Time Stamp (CTR+R)"))
        self.labeltimestamps.setText(_translate("MainWindow", "Label Last Stamp"))
        #self.test.setText(_translate("MainWindow", "Test Button"))
        def livebookmark():
            global last_bookmark
            while last_bookmark == True:
                print ("its true i tell ya")
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                self.labellastbookmark.setText(_translate("MainWindow", time.strftime("%H:%M:%S", t)))
                self.labellastbookmark.setStyleSheet('color: green')
                global set_time
                set_time = current_time
                last_bookmark = False
            else:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                self.labellastbookmark.setText(_translate("MainWindow", set_time))
                time.sleep(1)
                print ("its false i tell ya")
                print (current_time)
                print (set_time)
                return livebookmark()
                        
        t4 = threading.Thread(target=livebookmark)
        t4.start()
        self.label.setText(_translate("MainWindow", "Last Save at" ))   

        
    def Start_Session(self):
        print("lol it works")
        sys.exit()

    

#hotkeys (Note- figure out how  to make this work with LCD Timer)        

def function_1():
    """ One of your functions to be executed by a combination """
    return clickstartsession()
    print('Executed CTR + G THIS IS BEING CLONED')


def function_2():
    """ Another one of your functions to be executed by a combination """
    return clickendsession()
    print('Executed CRTL + H')


def function_3():
    global s
    """ Another one of your functions to be executed by a combination """
    print('Executed CTRL + R')
    return clicktimestamp()

def function_4():
    """ Another one of your functions to be executed by a combination """
    print('Executed CTRL + L')
    return clicklabeltimestamps()

# Create a mapping of keys to function (use frozenset as sets/lists are not hashable - so they can't be used as keys)
# Note the missing `()` after function_1 and function_2 as want to pass the function, not the return value of the function
combination_to_function = {
    frozenset([Key.ctrl_l, KeyCode(vk=71)]): function_1,  # left ctrl + G
    frozenset([Key.ctrl_l, KeyCode(vk=72)]): function_2,  # left ctrl + H
    frozenset([Key.ctrl_l, KeyCode(vk=82)]): function_3,  # left crtl + R
    frozenset([Key.ctrl_l, KeyCode(vk=76)]): function_4,  # left crtl + L
}

# The currently pressed keys (initially empty)
#This is duped up on top becaues it would otherwise bet impossible to get both functions to work with the same hotkey
pressed_vks = set()


def get_vk(key):
    """
    Get the virtual key code from a key.
    These are used so case/shift modifications are ignored.
    """
    return key.vk if hasattr(key, 'vk') else key.value.vk


def is_combination_pressed(combination):
    """ Check if a combination is satisfied using the keys pressed in pressed_vks """
    return all([get_vk(key) in pressed_vks for key in combination])


def on_press(key):
    """ When a key is pressed """
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.add(vk)  # Add it to the set of currently pressed keys

    for combination in combination_to_function:  # Loop through each combination
        if is_combination_pressed(combination):  # Check if all keys in the combination are pressed
            combination_to_function[combination]()  # If so, execute the function


def on_release(key):
    """ When a key is released """
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys

#Hotkey Listening Run with Multithreading        
def listenkeyboard():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        
t3 = threading.Thread(target=listenkeyboard)
t3.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    app.setStyle('Fusion')
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

