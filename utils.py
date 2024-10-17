import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import settings
from constants import *

def on_close(window):
    if messagebox.askokcancel('Quit', 'Do you want to quit?'):
        window.destroy()

# def getInput(prompt):
#     window = tk.Tk()
#     window.withdraw()

#     input = simpledialog.askstring('Input', prompt)

#     return input

def setNewFilePath(chosenFileLabel, generateBtn):
    newFilePath = filedialog.askopenfilename(title='Select input PDF', filetypes=[('PDF', '.pdf')]) 
    if newFilePath:
        settings.chosenFilePath = newFilePath
        chosenFileLabel.config(text=f'Chosen File: {settings.chosenFilePath.split('/')[-1]}')
        generateBtn.config(state=tk.NORMAL)
    else:
        chosenFileLabel.config(text='No file chosen!')
        generateBtn.config(state=tk.DISABLED)

def onTemplateChange(chosenTemplateLabel):
    chosenTemplateLabel.config(text=settings.chosenTemplate)