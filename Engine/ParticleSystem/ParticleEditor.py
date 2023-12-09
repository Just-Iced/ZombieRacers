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

import threading

from sys import exit

from functools import partial

from Engine.ParticleSystem.system import System
from Engine.transform import Transform
from Game.car import Car

class GUI:
    def __init__(self, application):
        self.application = application
        self.root = Tk()
        self.root.geometry("1280x720")
        self.root.title("Particle Editor")
        self.root.resizable(False,False)

        
        
        self.menuBar = Menu(self.root)
        
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        
        self.fileMenu.add_command(label="New", command=self.new)
        self.fileMenu.add_command(label="Open", command=self.open)
        self.fileMenu.add_command(label="Close", command=self.closing)
        self.fileMenu.add_separator()
    
        self.fileMenu.add_command(label="Close Without Question", command=exit)
        
        
        
        self.menuBar.add_cascade(menu = self.fileMenu, label="File")
        self.root.config(menu = self.menuBar)
        
        
        self.frame = Frame(self.root)
        
        self.window = EditorWindow(self.frame, self.root, self)
        self.application.main = self.window.main
        
        #myscrollbar=Scrollbar(self.frame,orient="vertical")
        #myscrollbar.pack(side="right",fill="y")
        
        
        self.frame.pack(fill=BOTH)

        self.root.mainloop()
        
    def spawnSystem(self):
        self.application.system = System(self.application.main, self.application.name, Transform(pygame.math.Vector2(-65, -20), 0, pygame.math.Vector2(1,1)), 0)
        
    def closing(self):
        #creates dialogue box asking the user if they are sure they want to close the application
        if messagebox.askyesno(title ="Quit?", message="Do you really want to quit?\nAll unsaved changes will be lost!"):
            self.root.destroy()
    
    def new(self):
        #from distutils.dir_util import copy_tree
        import shutil

        # copy subdirectory example
        from_directory = 'Game/ParticleSystems/testSystem.json'
        to_directory = filedialog.asksaveasfilename(initialdir=self.application.dir, initialfile="NewSystem.json", defaultextension='.json')

        if to_directory != "":
            shutil.copy(from_directory, to_directory)
            self.application.file = to_directory
            self.application.name = os.path.basename(os.path.normpath(self.application.file))
            
    def open(self):
        self.application.file = filedialog.askopenfilename(initialdir=self.application.dir)
        self.application.name = os.path.basename(os.path.normpath(self.application.file))
        
class EditorWindow:
    def __init__(self, parent, window, app):
        self.window = window
        self.parent = parent
        
        self.embed_pygame = Frame(self.parent, width=500, height=500)
        self.embed_pygame.pack(side=TOP, anchor=CENTER, padx=25, pady=25)
        ###, anchor=SE

        os.environ['SDL_WINDOWID'] = str(self.embed_pygame.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        self.main = main(Window((500,500)))
        
        self.btn = tkinter.Button(self.parent, anchor=CENTER, font=("Arial", 24),text="Test System", command=app.spawnSystem)
        self.btn.pack(side=BOTTOM)
        
        self.update()
        
    def update(self):
        self.main.update()
        self.parent.update()
        self.embed_pygame.after(10, self.update)
        
class Application:
    def __init__(self):
        self.file = str(str(os.getcwd)+"Game/ParticleSystems/testSystem.json")
        self.dir = str(str(os.getcwd)+"Game/ParticleSystems")
        self.name = os.path.basename(os.path.normpath(self.file))
        self.main = None
        self.system = None
        self.gui = GUI(self)



Application()