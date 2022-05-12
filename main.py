from tkinter import *
from tkinter import messagebox
import json
from os import listdir
from os import rename
from os import startfile
from os.path import isfile, join
from Save import Save
from functools import partial
import sys

window = None
changeWindow = None
activeSave = None
fo4SaveDirectories = None
savesPath = None

def initWindow():
    global window
    window = Tk()

    setWindowSettings(window)
    lbl = Label(window, text="Fallout 4 saves")
    lbl.grid(column=0, row=0)
    btn = Button(window, text="Start", command=startClicked)
    btn.grid(column=1, row=0)
    btnChange = Button(window, text="Change", command=showOtherOptions)
    btnChange.grid(column=3, row=2)
    
def setWindowSettings(window):
    w = 400
    h = 300
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.resizable(False, False)
    window.title("Fallout 4 saves launcher")

def listSaves(fo4SaveDirectories, label, active, startPos):
    global activeSave
    global window
    for i in range(0, len(fo4SaveDirectories)):
        if (fo4SaveDirectories[i].usedByFallout is active):
            lbl = Label(window, text=label + ": " + fo4SaveDirectories[i].description)
            lbl.grid(column=0, row=i+startPos)
            btnDetails = Button(window, text="Details", command=partial(showDetails, fo4SaveDirectories[i]))
            btnDetails.grid(column=2, row=i+startPos)
        if (active and fo4SaveDirectories[i].usedByFallout):
            activeSave = fo4SaveDirectories[i]
            break
    
def listInactiveSaves():
    global fo4SaveDirectories
    global changeWindow
    for i in range(0, len(fo4SaveDirectories)):
        if (not fo4SaveDirectories[i].usedByFallout):
            lbl = Label(changeWindow, text="available: " + fo4SaveDirectories[i].description)
            lbl.grid(column=0, row=i + 1)
            btnDetails = Button(changeWindow, text="Change", command=partial(changeSave, fo4SaveDirectories[i]))
            btnDetails.grid(column=1, row=i+1)

def createAvailableEntries():
    global activeSave
    global fo4SaveDirectories
    global savesPath
    jsonFile = open('config.json', mode="r", encoding="utf-8")
    jsonContent = json.load(jsonFile)
    savesPath = jsonContent['directory']
    fo4Directories = [f for f in listdir(savesPath) if not isfile(join(savesPath, f))]
    fo4SaveDirectories = []
    for i in range(0, len(fo4Directories)):
        if (isfile(join(savesPath, fo4Directories[i], "version_data.json"))):
            save = Save(join(savesPath, fo4Directories[i], "version_data.json"), fo4Directories[i])
            fo4SaveDirectories.append(save);
        
    listSaves(fo4SaveDirectories, "active", True, 2)
    listSaves(fo4SaveDirectories, "available", False, 3)
        
def startClicked():
    startfile("f4se_loader.exe");
    sys.exit()

def showDetails(fo4SaveDirectory):
    if (fo4SaveDirectory is not None):
        if (fo4SaveDirectory.additionalContents is not NONE and len(fo4SaveDirectory.additionalContents) > 0):
            additionDescription = "\n".join([str(x) for x in fo4SaveDirectory.additionalContents])
            messagebox.showinfo('Details', additionDescription)
        else:
            messagebox.showinfo('Details', 'NO DETAILS DEFINED') 
    else:
        messagebox.showinfo('Details', 'NO SAVE SET')
        
def changeSave(fo4SaveDirectory):
    global activeSave
    global savesPath
    tempDirectoryName = "TempSaves"
    directoryBaseName = "Saves"
    renameDirectory(savesPath + directoryBaseName, savesPath + tempDirectoryName)
    renameDirectory(savesPath + directoryBaseName + "_" + fo4SaveDirectory.folderName, savesPath + directoryBaseName)
    renameDirectory(savesPath + tempDirectoryName, savesPath + directoryBaseName + "_" + activeSave.folderName)
    onClosingChangeWindow()
        
def renameDirectory(sourceName, targetName):
    rename(sourceName, targetName)
    
def showOtherOptions():
    global activeSave
    global window
    global changeWindow
    window.withdraw()
    changeWindow = Tk()
    lbl = Label(changeWindow, text="Fallout 4 saves")
    lbl.grid(column=0, row=0)
    setWindowSettings(changeWindow)
    changeWindow.protocol("WM_DELETE_WINDOW", onClosingChangeWindow)
    listInactiveSaves()
    changeWindow.mainloop()
    
def onClosingChangeWindow():
    global changeWindow
    changeWindow.destroy()
    initWindowAndEntries()
    
def initWindowAndEntries():
    initWindow()
    createAvailableEntries()
    
initWindowAndEntries()

window.mainloop()
