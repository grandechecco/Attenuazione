from canale import Canale
from presentazione import Presentazione
import os

class InputDati:
    """
    Classe per la gestione dei dati di attenuazione acustica
    con input e stampa dei risultati finali su file
    """
    def __init__(self):
        self.atten = []
        self.attenuazioni = []
        self.att_canale = []
        self.schermata_input()
        

    def schermata_input(self):
        #os.system('cls')
#         macchina = input('Inserire il tipo di UTA: ')
#         tipo_canale = input('Mandata, Ripresa Pae, Esp: ')
#         portata = input('Inserire la portata: ')
#         prevalenza = input('Inserire la Prevalenza: ')
        #print('Canalizzazioni: Canale, ciliNdrico, cUrva, Deviatore, Sonodec (C-N-U-D-S), Q per uscire')
        self.inserimento_dati()

    def inserimento_dati(self):
        
        while True:
            canalizzazione = input('Inserire il tipo di canalizzazione:')
            if canalizzazione == 'Q' or canalizzazione == 'q':
                self.registra()
            elif canalizzazione == 'C' or canalizzazione == 'c':
                self.input_canale()
            elif canalizzazione == 'N' or canalizzazione == 'n':
                self.input_cilindrico()
            elif canalizzazione == 'U'or canalizzazione == 'u':
                self.input_curva()
            elif canalizzazione == 'D' or canalizzazione == 'd':
                self.input_deviatore()
            elif canalizzazione == 'S' or canalizzazione == 's':
                self.input_sonodec()
            

    def input_canale(self):
        altezza = input('Altezza canale: ')
        larghezza = input('Larghezza canale: ')
        lunghezza = input('Lunghezza canale: ')
        tratto = ('canale', 0, float(altezza), float(larghezza), float(lunghezza), 0)
        self.att_canale.append(tratto)
        #print(self.att_canale)

    def input_cilindrico(self):
        diametro = input('Diametro canale: ')
        lunghezza = input('Lunghezza canale: ')
        tratto = ('cilindrico', 0, float(diametro), float(lunghezza), 0.0, 0.0)
        self.att_canale.append(tratto)
        #print(self.att_canale)
    
    def input_curva(self):
        altezza = input('Altezza canale curva: ')
        larghezza = input('Larghezza canale curva: ')
        raggio = input('raggio curva: ')
        tratto = ('curva', 0, float(altezza), float(larghezza), float(raggio), 0.0)
        self.att_canale.append(tratto)
        #print(self.att_canale)
    
    def input_deviatore(self):
        totale = input('Portata totale: ')
        residua = input('Portata residua: ')
        tratto = ('deviatore', 0, float(totale), float(residua), 0.0, 0.0)
        self.att_canale.append(tratto)
        #print(self.att_canale)
    
    def input_sonodec(self):
        print('sonodec')


    def registra(self):
        can = Canale()
        i = 0
        for i in range(len(self.att_canale)):
            dato1, dato2, dato3, dato4, dato5, dato6 = self.att_canale[i]
            #print(self.att_canale[0])
            can = Canale(dato1, dato2, dato3, dato4, dato5, dato6)
            self.atten.append(can.attenuazione())
            #print(self.att_canale)
            presenta = Presentazione(self.att_canale[i], self.atten[i])
            stampa= presenta.formatta()
            print(stampa)
            
if __name__ == '__main__':
    s = InputDati()
    s.schermata_input()
