import sys, os
sys.path.append(os.getcwd())

import pygame
import tkinter
from Engine.window import Window
from Engine.main import main

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pygame
from glob import glob

from sys import exit

from functools import partial

class GUI:
    def __init__(self, application, main):
        self.application = application
        self.main = main
        self.root = Tk()
        self.root.geometry("1280x720")
        self.root.title("Particle Editor")
        self.root.resizable(False,False)

        
        
        self.menuBar = Menu(self.root)
        
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        
        self.fileMenu.add_command(label="New", command=self.new)        
        self.fileMenu.add_separator()
    
        self.fileMenu.add_command(label="Close Without Question", command=exit)
        
        
        
        self.menuBar.add_cascade(menu = self.fileMenu, label="File")
        self.root.config(menu = self.menuBar)
        
        
        self.frame = Frame(self.root)
        
        myscrollbar=Scrollbar(self.frame,orient="vertical")
        myscrollbar.pack(side="right",fill="y")
        
        
        self.frame.pack(fill=BOTH)

        self.root.mainloop()
    
    def new(self):
        from distutils.dir_util import copy_tree

        # copy subdirectory example
        from_directory = str(os.getcwd)+'Game/ParticleSystems/testSystem.json'
        to_directory = filedialog.asksaveasfilename(initialfile="NewSystem.json", defaultextension='.json')

        if to_directory != "":
            copy_tree(from_directory, to_directory)
        
    
class Application:
    def __init__(self):
        self.main = main(Window((500,500)))
        self.gui = GUI(self, self.main)
        self.main.run()

Application()