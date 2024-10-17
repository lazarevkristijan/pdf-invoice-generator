import tkinter as tk
window = tk.Tk()
from tkinter import filedialog, ttk
from constants import *
from utils import *


window.title('PDF Text Replacer')
window.iconbitmap('favico.ico')
window.resizable(False, False)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_top = int(screen_height / 2 - WINDOW_SIZE / 2)
position_right = int(screen_width / 2 - WINDOW_SIZE / 2)
window.geometry(f'{WINDOW_SIZE}x{WINDOW_SIZE}+{position_right}+{position_top}')
window.protocol('WM_DELETE_WINDOW', lambda: on_close(window))

mainFrame = tk.Frame(window, padx=FRAME_PAD, pady=FRAME_PAD)
mainFrame.pack(expand=True, fill=tk.BOTH)
mainFrame.configure(bg=WINDOW_BG)

fileLabel = tk.Label(mainFrame, text='PDF template')
fileBtn = tk.Button(mainFrame, text='Choose', command=lambda: setNewFilePath(chosenFileLabel, generateBtn))
chosenFileLabel = tk.Label(mainFrame, text='No file chosen!')

settings.chosenTemplate.set(TEMPLATES_MENU[0])
templateChoosingMenu = ttk.OptionMenu(mainFrame, settings.chosenTemplate, *TEMPLATES_MENU, command=lambda x: onTemplateChange(chosenTemplateLabel))
chosenTemplateLabel = tk.Label(mainFrame, text=settings.chosenTemplate.get())

generateBtn = tk.Button(mainFrame, text='Generate PDF', state=tk.DISABLED)

# PACK THEM BITCHEZ UP
fileLabel.pack()
fileBtn.pack()
chosenFileLabel.pack()

generateBtn.pack()

templateChoosingMenu.pack()
chosenTemplateLabel.pack()

window.mainloop()

# def generate_pdf(input_pdf, output_pdf):
#     generateWindow = tk.Tk()
#     mainFrame = tk.Frame(generateWindow, padx=FRAME_PAD, pady=FRAME_PAD)
#     mainFrame.configure(bg=WINDOW_BG)
    
#     doc = fitz.open(input_pdf)

#     for page_num in range(len(doc)):
#         page = doc[page_num]

#         replaceListInput = tk.Text(mainFrame, width=20, height=2)
        
#         replaceList = replaceListInput.get('1.0', 'end-1c').split(',')
        
#         for replaceIitem in replaceList:            
#             text_instances = page.search_for(replaceIitem)
#             for inst in text_instances:
#                 page.add_redact_annot(inst, text=getInput(f'Enter input for {replaceIitem}'), fill=(1, 1, 1))
#                 page.apply_redactions()
            
#     doc.save(output_pdf)
#     doc.close()

#     os.startfile(output_pdf)

#     generateWindow.mainloop()
