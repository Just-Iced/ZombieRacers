import sys, os
sys.path.append(os.getcwd())
import pygame
from pygame.math import Vector2 as Vec2
import tkinter
from Engine.window import Window
from Engine.main import main
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pygame
from sys import exit
from Engine.ParticleSystem.system import System
from Engine.transform import Transform
from Game.car import Car
from Engine.ParticleSystem.systemstucture import SystemStructure

class EditorWindow:
    def __init__(self, parent, window, app):
        self.window = window
        self.parent = parent
        
        self.embed_pygame = Frame(self.parent, width=500, height=500)
        self.embed_pygame.pack(side=TOP, anchor=CENTER, padx=25, pady=25)

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

class Panel:
    def __init__(self, parent, application):
        self.parent = parent
        self.application = application
        
        self.params = SystemStructure()
        
        self.speed = NumBox("Speed Multiplier:", self.parent, 1, self.setSpeed)
        self.spawnRate = NumBox("Spawn Rate: ", self.parent, 10, self.setRate)
        self.lifeTime = NumBox("Particle Lifetime (Ms): ", self.parent, 2, self.setParticleLifetime)
        self.systemLifeTime = NumBox('System Lifetime (S): ', self.parent, 2, self.setSystemLifetime)
        self.velocity = VecBox("Velocity: ", self.parent, Vec2(0,0), self.setVel)
        self.scale = VecBox('Scale: ', self.parent, Vec2(1,1), self.setScale)
        self.scale.xBox.text['text'] = 'Min:'
        self.scale.yBox.text['text'] = 'Max:'
        
        self.sprite = FileBox('Sprite: ', self.parent, 'Sprite.png', self.setSprite)
        
        self.rSpread = CheckBox('Random Spread: ', self.parent, True, self.setRSpread)
        self.rVert = CheckBox("Random Vertical: ", self.parent, True, self.setRVert)
        
    def initPanel(self):
        self.params = self.application.system.params
        
        self.speed.clear()
        self.speed.box.insert(END, self.params.speed)
        self.spawnRate.clear()
        self.spawnRate.box.insert(END, self.params.spawnRate)
        self.lifeTime.clear()
        self.lifeTime.box.insert(END, self.params.lifetime)
        self.systemLifeTime.clear()
        self.systemLifeTime.box.insert(END, self.params.systemLifetime)
        self.velocity.clear()
        self.velocity.xBox.box.insert(END, self.params.velocity.x)
        self.velocity.yBox.box.insert(END, self.params.velocity.y)
        self.scale.clear()
        self.scale.xBox.box.insert(END, self.params.scale.x)
        self.scale.yBox.box.insert(END, self.params.scale.y)
        self.sprite.btn['text'] = self.application.system.path
        self.rSpread.value.set(self.params.randomSpread)
        self.rVert.value.set(self.params.randomVertical)
        
        
    def setSpeed(self, event):
        self.params.speed = int(self.speed.box.get())
    
    def setRate(self, event):
        self.params.spawnRate = int(self.spawnRate.box.get())
        
    def setParticleLifetime(self, event):
        self.params.lifetime = int(self.lifeTime.box.get())
    
    def setSystemLifetime(self, event):
        self.params.systemLifetime = float(self.systemLifeTime.box.get())
        
    def setVel(self, event):
        self.params.velocity = Vec2(float(self.velocity.xBox.box.get()), float(self.velocity.yBox.box.get()))
        
    def setScale(self, event):
        if float(self.scale.xBox.box.get()) > float(self.scale.yBox.box.get()):
            self.scale.xBox.clear()
            self.scale.xBox.box.insert(END, float(self.scale.yBox.box.get()))
        self.params.scale = Vec2(float(self.scale.xBox.box.get()), float(self.scale.yBox.box.get()))
        
    def setSprite(self, event=None):
        self.params.sprite = pygame.image.load(os.getcwd()+'\\Game\\'+self.sprite.value).convert_alpha()

        
    def setRSpread(self, event=None):
        self.params.randomSpread = self.rSpread.value.get()

    def setRVert(self, event=None):
        self.params.randomVertical = self.rVert.value.get()
         
class FileBox:
    def __init__(self, title, parent, value, valueSetter):
        self.title = title
        self.parent = parent
        self.value = value
        self.valueSetter = valueSetter
        self.frame = Frame(self.parent)


        self.text = Label(self.frame, text=self.title, font=("Arial", 18))
        self.text.pack(side=LEFT)

        self.btn = Button(self.frame, anchor=CENTER, font=('Arial', 12), text=self.value, command=self.selectFile)
        self.btn.pack(side=RIGHT, padx=15)

        self.frame.pack(side=TOP, anchor=CENTER, fill=BOTH)

    def selectFile(self):
        dir = str(os.getcwd)+"/Game"
        file = filedialog.askopenfilename(initialdir=dir)
        if file != '':
            self.folder = os.path.basename(os.path.dirname(file))
            
            if "Game" not in str(self.folder):
                self.value = str(self.folder) + "\\" + str(os.path.basename(os.path.normpath(file)))
            else:
                self.value = str(os.path.basename(os.path.normpath(file)))
            
            self.btn['text'] = self.value
            self.valueSetter()

class NumBox:
    def __init__(self, title, parent, value, valueSetter):
        self.title = title
        self.parent = parent
        self.valueSetter = valueSetter
        self.frame = Frame(self.parent)

        
        self.text = Label(self.frame, text=self.title, font=("Arial", 18))
        self.text.pack(side=LEFT)
        
        self.box = Entry(self.frame, width = 6)
        self.box.bind('<Return>', self.valueSetter)
        self.box.bind('<FocusOut>', self.valueSetter)
        self.box.insert(END, value)
        self.box.pack(side=RIGHT, padx=15)
        
        self.frame.pack(side=TOP, anchor=CENTER, fill=BOTH)
    
    def clear(self):
        self.box.delete(first=0, last=END)

class VecBox:
    def __init__(self, title, parent, value, valueSetter):
        self.title = title
        self.parent = parent
        self.value = value
        self.valueSetter = valueSetter
        
        self.frame = Frame(self.parent)
        self.f2 = Frame(self.frame)
        
        self.text = Label(self.frame, text=self.title, font=("Arial", 18))
        self.text.pack(side=LEFT)
        
        self.xBox = NumBox("X:", self.f2, self.value.x, self.valueSetter)
        self.xBox.frame.pack(side=LEFT)
        self.yBox = NumBox("Y:", self.f2, self.value.y, self.valueSetter)
        self.yBox.frame.pack(side=RIGHT)
        self.f2.pack(side=RIGHT)
        self.frame.pack(fill=BOTH)
        
    def clear(self):
        self.xBox.clear()
        self.yBox.clear()

class CheckBox:
    def __init__(self, title, parent, value, valueSetter):
        self.title = title
        self.parent = parent
        self.value = BooleanVar()
        self.value.set(value)
        self.valueSetter = valueSetter
        
        self.frame = Frame(self.parent)
        
        self.text = Label(self.frame, text=self.title, font=("Arial", 18))
        self.text.pack(side=LEFT)
        
        self.cBox = Checkbutton(self.frame, variable=self.value, onvalue=True, offvalue=False, command=self.valueSetter)
        self.cBox.pack(side=RIGHT, padx=30)
        self.frame.pack(fill=BOTH)

class GUI:
    def __init__(self, application):

        self.application = application
        self.root = Tk()
        self.root.geometry("1000x720")
        self.root.title("Particle Editor")
        self.root.resizable(False,False)
        
        self.menuBar = Menu(self.root)
        
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        
        self.fileMenu.add_command(label="New", command=self.new)
        self.fileMenu.add_command(label="Open", command=self.open)
        self.fileMenu.add_command(label="Save", command=self.save)
        self.fileMenu.add_command(label="Save As", command=self.saveAs)
        self.fileMenu.add_command(label="Close", command=self.closing)
        self.fileMenu.add_separator()
    
        self.fileMenu.add_command(label="Close Without Question", command=exit)
        
        
        self.menuBar.add_cascade(menu = self.fileMenu, label="File")
        self.root.config(menu = self.menuBar)

        self.root.bind('<Control-s>', func=self.save)
        self.root.bind('<Control-a>', func=self.saveAs)
        self.root.bind('<Control-o>', func=self.open)
        self.root.bind('<Control-n>', func=self.new)
        
        self.frame = Frame(self.root)
        
        self.window = EditorWindow(self.frame, self.root, self)
        self.application.main = self.window.main
        
        self.frame.pack(side=LEFT)
        
        self.edit= Frame(self.root)
        self.panel = Panel(self.edit, self.application)
        self.edit.pack(anchor=CENTER, padx=25, pady=150)
        self.vcmd = (self.edit.register(self.callback))
 
        self.root.bind_all("<Button-1>", lambda event: event.widget.focus_set())
        
        self.open()
        self.spawnSystem()
        self.panel.initPanel()
        
        self.root.mainloop()
        
    def callback(self, P):
        if str.isdigit(P) or "-" in P or str(P) == "":
            return True
        else:
            return False
        
    def spawnSystem(self):
        self.application.system = System(self.application.main, self.application.name, Transform(pygame.math.Vector2(-60, -18), 0, pygame.math.Vector2(1,1)), 0)
        if self.panel.params != SystemStructure():
            self.application.system.params = self.panel.params
            
    def closing(self):
        #creates dialogue box asking the user if they are sure they want to close the application
        if messagebox.askyesno(title ="Quit?", message="Do you really want to quit?\nAll unsaved changes will be lost!"):
            self.root.destroy()
    
    def new(self, event=None):
        #from distutils.dir_util import copy_tree
        import shutil

        # copy subdirectory example
        from_directory = 'Game/ParticleSystems/testSystem.json'
        to_directory = filedialog.asksaveasfilename(initialdir=self.application.dir, initialfile="NewSystem.json", defaultextension='.json')

        if to_directory != "":
            shutil.copy(from_directory, to_directory)
            self.application.file = to_directory
            self.application.name = os.path.basename(os.path.normpath(self.application.file))
            self.panel.params = SystemStructure()
            self.spawnSystem()
            self.panel.initPanel()
            
    def open(self, event=None):
        self.application.file = filedialog.askopenfilename(initialdir=self.application.dir)
        self.application.name = os.path.basename(os.path.normpath(self.application.file))
        self.panel.params = SystemStructure()
        self.spawnSystem()
        self.panel.initPanel()
        
    def save(self, event=None):
        import json
        p = self.panel.params
        self.application.system.path = self.panel.sprite.value
        dictionary = {
            "speed": p.speed,
            "spawnRate": p.spawnRate,
            "sprite": self.application.system.path,
            "lifetime": p.lifetime,
            "systemlifetime": p.systemLifetime,
            "velocity": [p.velocity.x,p.velocity.y],
            "scale": [p.scale.x,p.scale.y],
            "randomSpread": p.randomSpread,
            "randomVertical": p.randomVertical            
        }
        
        f = str(self.application.file)
        with open(f, "w") as outfile:
            json.dump(dictionary, outfile)
            
    def saveAs(self, event=None):
        import json
        p = self.panel.params
        self.application.system.path = self.panel.sprite.value
        dictionary = {
            "speed": p.speed,
            "spawnRate": p.spawnRate,
            "sprite": self.application.system.path,
            "lifetime": p.lifetime,
            "systemlifetime": p.systemLifetime,
            "velocity": [p.velocity.x,p.velocity.y],
            "scale": [p.scale.x,p.scale.y],
            "randomSpread": p.randomSpread,
            "randomVertical": p.randomVertical            
        }
        
        f = filedialog.asksaveasfilename(initialdir=self.application.dir, initialfile=self.application.name, defaultextension='.json')
        if f != '':
            with open(f, "w") as outfile:
                json.dump(dictionary, outfile)
                
            self.application.file = f
            self.application.name = os.path.basename(os.path.normpath(self.application.file))
            self.panel.params = SystemStructure()
            self.spawnSystem()
            self.panel.initPanel()


class Application:
    def __init__(self):
        self.file = str(str(os.getcwd)+"Game/ParticleSystems/testSystem.json")
        self.dir = str(str(os.getcwd)+"Game/ParticleSystems")
        self.name = os.path.basename(os.path.normpath(self.file))
        self.main = None
        self.system = None
        self.gui = GUI(self)

Application()