#1.13 adds check box variable for Double Click
#1.14 adds checks for digits before converting to integers
#1.155 started to use pynput as alternative to recording mouse click outside of application
import tkinter as tk
import pyautogui
import screeninfo
import time
import keyboard
from pynput import mouse
from tkinter import messagebox

def defaultValues():
    numOfClicksEntry.insert(0, "1")
    xEntry.insert(0, "1280")
    yEntry.insert(0, "720")
    durationEntry.insert(0, ".5")
    intervalEntry.insert(0, ".5")

def clickEvent():
    startProcessButton.config(relief=tk.SUNKEN, bg="red", fg="black")
    if numOfClicksEntry.get().isdigit() and '.' not in numOfClicksEntry.get():
        numOfClicks = int(numOfClicksEntry.get())
    else:
        status.config(text='# of Clicks Value Not Valid! Insert Whole #')
        startProcessButton.config(relief=tk.RAISED, bg="green", fg="black")
        return
    if xEntry.get().isdigit():
        x = int(xEntry.get())
    else:
        status.config(text='X Value Not Valid! Insert Whole #')
        startProcessButton.config(relief=tk.RAISED, bg="green", fg="black")
        return
    if yEntry.get().isdigit():
        y = int(yEntry.get())
    else:
        status.config(text='Y Value Not Valid! Insert Whole #')
        startProcessButton.config(relief=tk.RAISED, bg="green", fg="black")
        return
    try:
        durations = float(durationEntry.get())
    except:
        status.config(text='Duration Value Not Valid! Insert #')
        startProcessButton.config(relief=tk.RAISED, bg="green", fg="black")
        return
    try:
        intervals = float(intervalEntry.get())
    except:
        status.config(text='Intervals Value Not Valid! Insert #')
        startProcessButton.config(relief=tk.RAISED, bg="green", fg="black")
        return

    if doubleClickCheckVar == 1:
        clicks = 2
    else:
        numClicks = 1
    for i in range(numOfClicks):
        pyautogui.moveTo(x, y, duration=durations)
        pos = pyautogui.position()
        pyautogui.click(clicks=numClicks, interval=intervals)
        pyautogui.moveTo(pos[0], pos[1])
        #time.sleep(1)
        if keyboard.is_pressed('esc'):
            print("Loop cancelled.")
            startProcessButton.config(relief=tk.RAISED, bg="green", fg="black")
            break
    startProcessButton.config(relief=tk.RAISED, bg="green", fg="black")
def cpcButtonPressed():
    mouseCoordinatesButton.config(relief=tk.SUNKEN, bg="yellow", fg="black")
    mouse_listener = mouse.Listener(on_click=lambda *args: logMouseClick(mouse_listener, *args))
    mouse_listener.start()
            
def logMouseClick(mouse_listener, x, y, button, pressed):
    print("x:", x)
    print("y:", y)
    print("button:", button)
    print("pressed:", pressed)
    if pressed:
        xEntry.delete(0, tk.END)
        yEntry.delete(0, tk.END)
        xEntry.insert(0, x)
        yEntry.insert(0, y)
        mouseCoordinatesButton.config(relief = tk.RAISED, bg="blue", fg="white")
        mouse_listener.stop()
        

def logEvent(event):
    print(f"Event type: {event.type}, Widget: {event.widget}")



#Creating Application Window
window = tk.Tk()
window.title("Clicker Program")

#Creates Event Log for interactions with application
window.bind_all("<Button->",logEvent)

#definitions for Menubar
#messagebox could not be called, 'tk.messagebox' instead must 'from tkinter import messagebox' then call "messagebox.command"
def onExit():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        window.destroy()
def onAbout():
    messagebox.showinfo(title="About", message="This application was created by KLJ Codes using Python\nwith dependencies on\ntkinter,\npyautogui,\nscreeninfo,\ntime,\nkeyboard,\nand pynput")

#Creating Menubar
menu=tk.Menu(window)

fileMenu = tk.Menu(menu, tearoff=False)
fileMenu.add_command(label="Exit", command=onExit)

helpMenu = tk.Menu(menu, tearoff=False)
helpMenu.add_command(label="Support")
helpMenu.add_command(label="About", command=onAbout)

menu.add_cascade(label="File", menu=fileMenu)
menu.add_cascade(label="About", menu=helpMenu)

window.config(menu=menu)

#Filling in Application
introFrame = tk.Frame()
intro = tk.Label(master=introFrame, text="Mouse Clicker Settings")
introFrame.pack(anchor=tk.W)
intro.pack(side=tk.LEFT, anchor=tk.W)

numOfClicksFrame = tk.Frame()
numOfClicksLabel = tk.Label(master=numOfClicksFrame, text="# of Clicks")
numOfClicksEntry = tk.Entry(master=numOfClicksFrame)
numOfClicksFrame.pack(anchor=tk.W)
numOfClicksLabel.pack(side=tk.LEFT)
numOfClicksEntry.pack(side=tk.RIGHT)


xFrame = tk.Frame(master=window)
xLabel = tk.Label(master=xFrame, text="X Coordiante")
xEntry = tk.Entry(master=xFrame,)
xFrame.pack(anchor=tk.W)
xLabel.pack(side=tk.LEFT, anchor=tk.W)
xEntry.pack(side=tk.LEFT, anchor=tk.E)


yFrame = tk.Frame()
yLabel = tk.Label(master=yFrame, text="Y Coordiante")
yEntry = tk.Entry(master=yFrame,)
yFrame.pack(anchor=tk.W)
yLabel.pack(side=tk.LEFT, anchor=tk.W)
yEntry.pack(side=tk.LEFT, anchor=tk.E)

durationFrame = tk.Frame()
durationLabel = tk.Label(master=durationFrame, text="Duration")
durationEntry = tk.Entry(master=durationFrame,)
durationFrame.pack(anchor=tk.W)
durationLabel.pack(side=tk.LEFT, anchor=tk.W)
durationEntry.pack(side=tk.LEFT, anchor=tk.E)

intervalFrame = tk.Frame()
intervalLabel = tk.Label(master=intervalFrame, text="Interval")
intervalEntry = tk.Entry(master=intervalFrame,)
intervalFrame.pack(anchor=tk.W)
intervalLabel.pack(side=tk.LEFT, anchor=tk.W)
intervalEntry.pack(side=tk.LEFT, anchor=tk.E)

doubleClickFrame = tk.Frame()
doubleClickLabel = tk.Label(master=doubleClickFrame , text="Double Click")

doubleClickCheckVar = tk.IntVar()
doubleClickCheckButton = tk.Checkbutton(doubleClickFrame, variable=doubleClickCheckVar)
doubleClickFrame.pack(anchor=tk.W)
doubleClickLabel.pack(side=tk.LEFT, anchor=tk.W)
doubleClickCheckButton.pack(side=tk.LEFT, anchor=tk.E)

buttonFrame = tk.Frame()
buttonFrame.pack(anchor=tk.W)

startProcessButton = tk.Button(
    buttonFrame,
    text="Start Process",
    relief="raised",
    width=14,
    height=2,
    bg="green",
    fg="black",
    command=clickEvent
)
startProcessButton.pack(side=tk.LEFT, anchor=tk.W)

mouseCoordinatesButton = tk.Button(
    buttonFrame,
    text="Capture Mouse\nCoordinates",
    relief="raised",
    width= 14,
    height=2,
    bg="blue",
    fg="white",
    command=cpcButtonPressed,
    takefocus=0
)
mouseCoordinatesButton.pack(side=tk.RIGHT, anchor=tk.E)

statusFrame = tk.Frame()
status = tk.Label(master=statusFrame, text="Application Ready")
statusFrame.pack(anchor=tk.W)
status.pack(side=tk.LEFT, anchor=tk.W)

#inserting defaultValues in entry fields 
defaultValues()

window.mainloop()
