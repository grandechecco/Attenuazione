"""
    Programma per il calcolo delle attenuazioni acustiche
    nelle canalizzazioni per determinare il migliore
    silenziatore del tipo Woods da applicare
"""
# files di importazione
from tkinter import *
from tkinter import messagebox
import os

# costanti
PROGRAM_NAME = 'Attenuazione canali'

# calssi
class Silenziatore:
    ''' Classe silenziatore acustico
        per la scelta corretta senza
        dover lavorare sulle tabelle
    '''
    def __init__(self, root):
        self.root = root
        self.root.title(PROGRAM_NAME)
        self.root.geometry('350x300')
        self.root.content_text = Text(root, wrap = 'word')
        self.root.content_text.pack(expand = 'yes', fill = 'both')
        self.root.content_text.bind('<Control-Q>', self.onEsciMenuClicked)
        self.root.content_text.bind('<Control-q>', self.onEsciMenuClicked)

        self.initGui()


    # metodi

    # area dei menu
    def createMenu(self):
        self.menuBar = Menu(self.root)
        self.createFileMenu()
        self.createAiutoMenu()

    def createFileMenu(self):
        self.fileMenu = Menu(self.menuBar, tearoff = 0)
        self.menuBar.add_cascade(label = 'File', menu = self.fileMenu)
        self.fileMenu.add_command(label = 'Apri', command = None)
        self.fileMenu.add_command(label = 'Esci', accelerator = 'Ctrl-Q', command =  self.onEsciMenuClicked)
        self.root.config(menu = self.menuBar)
        #self.content_text.bind('<Control-Q>', self.onEsciMenuClicked)
        #self.content_text.bind('<Control-q>', self.onEsciMenuClicked)

    def createAiutoMenu(self):
        self.aiutoMenu = Menu(self.menuBar, tearoff = 0)
        self.menuBar.add_cascade(label = '?', menu = self.aiutoMenu)
        self.aiutoMenu.add_command(label = 'Aiuto', command = None)
        self.aiutoMenu.add_command(label = 'About', command =
                self.onAboutMenuClicked)

    def onAboutMenuClicked(self):
        messagebox.showinfo('Programma realizzato da:',
                'Francesco Romaro (frarom62@gmail.com) per il calcolo dell\'attenzazione \
acustica dei canali delle UTA al fine di determinare il tipo di \
silenziatore da installare')


    def onEsciMenuClicked(self):
       if messagebox.askokcancel('Esci',  'Vuoi uscire veramente?'):
        root.destroy()



    # area della top bar
    def createTopBar(self):
        pass



    # area della bottom bar
    def createBottomBar(self):
        pass



    # area del frame principale
    def createFrame(self):
        pass



    # inizializzazione della finestra
    def initGui(self):
        self.createMenu()
        self.createTopBar()
        self.createBottomBar()
        self.createFrame()



# test
if __name__ == '__main__':
    root = Tk()
    Silenziatore(root)
    root.mainloop()
