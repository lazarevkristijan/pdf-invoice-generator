import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import settings
from constants import *
import fitz
import os

def on_close(window):
    if messagebox.askokcancel('Quit', 'Do you want to quit?'):
        window.destroy()

def setNewFilePath(chosenFileLabel, generateBtn):
    newFilePath = filedialog.askopenfilename(title='Select input PDF', filetypes=[('PDF', '.pdf')]) 
    if newFilePath:
        settings.chosenFilePath = newFilePath
        chosenFileLabel.config(text=f'Chosen File: {settings.chosenFilePath.split('/')[-1]}')
        if settings.chosenTemplate.get() != 'None':
            generateBtn.config(state=tk.NORMAL)
    else:
        chosenFileLabel.config(text='No file chosen!')
        generateBtn.config(state=tk.DISABLED)

def onTemplateChange(chosenTemplateLabel, generateBtn):
    chosenTemplateLabel.config(text=f'Chosen Template: {settings.chosenTemplate.get()}')
    if(settings.chosenFilePath != ''):
        generateBtn.config(state=tk.NORMAL)
    else:
        generateBtn.config(state=tk.DISABLED)

def openGenerateMenu():
    generateWindow = tk.Tk()
    generateWindow.title('PDF Text Replacer')
    generateWindow.iconbitmap('favico.ico')
    generateWindow.resizable(False, False)

    screen_width = generateWindow.winfo_screenwidth()
    screen_height = generateWindow.winfo_screenheight()
    position_top = int(screen_height / 2 - WINDOW_SIZE / 2)
    position_right = int(screen_width / 2 - WINDOW_SIZE / 2)
    generateWindow.geometry(f'{WINDOW_SIZE}x{WINDOW_SIZE}+{position_right}+{position_top}')
    mainFrame = tk.Frame(generateWindow, padx=FRAME_PAD, pady=FRAME_PAD)
    mainFrame.configure(bg=WINDOW_BG)
    mainFrame.pack(expand=True, fill=tk.BOTH)

    settings.replacementTextBoxes = {}
    for key, placeholder in TEMPLATE_PLACEHOLDERS[settings.chosenTemplate.get()].items():
        tk.Label(mainFrame, text=key).pack()
        textBox = tk.Text(mainFrame, width=20, height=2)
        textBox.pack()

        settings.replacementTextBoxes[key] = textBox
    
    tk.Button(mainFrame, text='Generate', command=generatePDF).pack()


def generatePDF():
    doc = fitz.open(settings.chosenFilePath)

    for pageNum in range(len(doc)):
        page = doc[pageNum]

        templateValues = []
        _templateValues = TEMPLATE_PLACEHOLDERS[settings.chosenTemplate.get()].values()
        for value in _templateValues:
            templateValues.append(value)
        
        replacementValues = []
        _replacementValues = settings.replacementTextBoxes.values()
        for value in _replacementValues:
            replacementValues.append(value.get('1.0', 'end-1c'))

        for index, placeholder in enumerate(templateValues):
            textInstances = page.search_for(placeholder)
            page.add_redact_annot(textInstances[0], text=replacementValues[index], fill=(1,1,1))
            page.apply_redactions()
        
        doc.save('newFile.pdf')
        doc.close()

        os.startfile('newFile.pdf')
        

        
        # if found once, don't contineu to other pages.
        