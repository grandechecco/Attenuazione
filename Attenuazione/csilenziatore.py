"""
    Programma per il calcolo delle attenuazioni acustiche
    nelle canalizzazioni per determinare il migliore
    silenziatore del tipo Woods da applicare
"""
# files di importazione
from tkinter import *
import os

# calssi
class Silenziatore:
    ''' Classe silenziatore acustico
        per la scelta corretta senza
        dover lavorare sulle tabelle
    '''
    def __init__(self, root):
        self.root = root
        self.parametri = parametri
        self.serie, self.hz63, self.hz125, self.hz250, self.hz500,\
                    self.hz1000, self.hz2000, self.hz4000, self.hz8000,\
                    self.setti,  self.aria,  self.libera, self.lunghezza,\
                    self.base,  self.altezza,  self.modello = parametri
                    
    def stampamodello(self):
        print()
        print('Silenziatore WOODS serie ' + self.serie + ' ' + self.lunghezza +'x' + self.base + \
        'x' + self.altezza + ' modello n. ' + self.modello)
        
    def stampaattenuazione(self):
        print(' 63Hz\t125Hz\t250Hz\t500Hz\t1000Hz \t2000Hz\t4000Hz\t8000Hz')
        print('   ' + self.hz63 + '\t ' + self.hz125 + '\t  '  + self.hz250 + '\t  ' + self.hz500 + '\t   '\
        + self.hz1000 + '\t  ' + self.hz2000 + '\t  ' + self.hz4000  + '\t  ' + self.hz8000)
    
    def stampasetti(self):   
        print('setti ' + self.setti +' mm, aria ' + self.aria + 'mm, percentuale aria libera ' + self.libera + '%')
        """, 63Hz ' + self.hz63 + ' 125Hz '\
        + self.hz125 + ', 250Hz '  + self.hz250 + ', 500Hz ' + self.hz500 + ', 1000Hz '\
        + self.hz1000 + ', 2000Hz ' + self.hz2000 + ', 4000Hz ' + self.hz4000  + ', 8000Hz ' + self.hz8000)
        """
    def stampacompleta(self):
        self.stampamodello()
        self.stampaattenuazione()
        self.stampasetti()
        
# test
if __name__ == '__main__':
    root = Tk()
    Silenziatore(root)
    root.mainloop()
"""    
par1 = ['QA64', '2',' 3', '4', '5', '6', '7', '8', '9', '360', '240',  '40', '1500', '1200', '900',  '23' ]

silenziatore = Silenziatore(par1)
silenziatore.stampaattenuazione()
silenziatore.stampacompleta()
silenziator = Silenziatore()
silenziator.stampaattenuazione()
silenziator.stampacompleta()
"""
