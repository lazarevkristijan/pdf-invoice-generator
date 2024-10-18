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
# window.protocol('WM_DELETE_WINDOW', lambda: on_close(window))

mainFrame = tk.Frame(window, padx=FRAME_PAD, pady=FRAME_PAD)
mainFrame.pack(expand=True, fill=tk.BOTH)
mainFrame.configure(bg=WINDOW_BG)

fileLabel = tk.Label(mainFrame, text='PDF template')
fileBtn = tk.Button(mainFrame,
                    text='Choose', 
                    command=lambda: setNewFilePath(chosenFileLabel, generateBtn),
                    width=20,
                    height=2,
                    bg='#fff')
chosenFileLabel = tk.Label(mainFrame, text='No file chosen!')

settings.chosenTemplate.set(TEMPLATES_MENU[0])
templateChoosingMenu = ttk.OptionMenu(mainFrame, settings.chosenTemplate, *TEMPLATES_MENU, command=lambda x: onTemplateChange(chosenTemplateLabel, generateBtn))
chosenTemplateLabel = tk.Label(mainFrame, text=f'Chosen Template: {settings.chosenTemplate.get()}')

generateBtn = tk.Button(mainFrame, text='Generate PDF', state=tk.DISABLED, command=openGenerateMenu)

# PACK THEM BITCHEZ UP
fileLabel.pack()
fileBtn.pack()
chosenFileLabel.pack(pady=(0,10))

chosenTemplateLabel.pack()
templateChoosingMenu.pack(pady=(0,10))

generateBtn.pack()

window.mainloop()