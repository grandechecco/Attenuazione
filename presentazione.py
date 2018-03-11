from string import *

class Presentazione:
    """ Classe per la formattazione del record dati
        di attenuazione dei condotti
    """
   
    
    def __init__(self, condotto, attenuazione):
        self.tipo, self.frequenza, self.dato1, self.dato2, self.dato3, self.dato4 = condotto
        self.hz63, self.hz125, self.hz250, self.hz500, self.hz1000, self.hz2000, self.hz4000, self.hz8000 = attenuazione
        self.attenuazione = list(attenuazione)
        self.condotto = condotto
        self.lista_formattata = []
    
    
    def formatta(self):
        if self.tipo == 'canale':
            canale = 'Delta Lp %s mm di canale %sx%s' % (int(self.dato3), int(self.dato1), int(self.dato2))
            self.lista_formattata.append(canale)
            for i in range(8):
                self.lista_formattata.append(self.attenuazione[i])
            return self.lista_formattata
        elif self.tipo == 'cilindrico':
            canale = 'Delta Lp %s mm di canale diametro %s' % (int(self.dato3), int(self.dato1))
            self.lista_formattata.append(canale)
            for i in range(8):
                self.lista_formattata.append(self.attenuazione[i])
            return self.lista_formattata
        if self.tipo == 'curva':
            canale = 'Delta Lp curva %sx%s' % (int(self.dato1), int(self.dato2))
            self.lista_formattata.append(canale)
            for i in range(8):
                self.lista_formattata.append(self.attenuazione[i])
            return self.lista_formattata
        if self.tipo == 'deviatore':
            canale = 'Delta Lp deviatore'
            self.lista_formattata.append(canale)
            for i in range(8):
                self.lista_formattata.append(self.attenuazione[i])
            return self.lista_formattata
        if self.tipo == 'sonodec':
            canale = 'Delta Lp %s mm di \'Sonodec\' diametro %s' % (int(self.dato3), int(self.dato1))
            self.lista_formattata.append(canale)
            for i in range(8):
                self.lista_formattata.append(self.attenuazione[i])
            return self.lista_formattata
        
    def unisci_dati(self):
        pass
    
if __name__ == '__main__':
    condotto = ['canale', 63, 1000, 500, 2500, 8000]
    att =  [0,1,2,3,4,5,6,7]
    s = Presentazione(condotto, att)
    canale = s.formatta()
    print(canale)
    condotto = ('cilindrico', 63, 1000, 500, 2500, 8000)        
    s = Presentazione(condotto, att)
    canale = s.formatta()
    print(canale)
    condotto = ('curva', 63, 1000, 500,0,0)        
    s = Presentazione(condotto, att)
    canale = s.formatta()
    print(canale)
    condotto = ('deviatore', 63, 1000, 500,0,0)        
    s = Presentazione(condotto, att)
    canale = s.formatta()
    print(canale)
    condotto = ('sonodec', 63, 1000, 2500,0,0)        
    s = Presentazione(condotto, att)
    canale = s.formatta()
    print(canale)