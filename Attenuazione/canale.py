
from math import *

class Canale:
    def __init__(self, tipo = 0, hertz = 0, dato1 = 0, dato2 = 0, dato3 = 0, dato4 = 0):
        """
        Classe per il calcolo delle attenuazioni acustiche
        dovute alle canalizzazioni degli impianti
        """
        # attributi
        self.hertz_dict = {63:0,125:1,250:2,500:3,1000:4,2000:5,4000:6,8000:7}
        
        self.atten = 0.0
        self.tipo = tipo
        self.hertz = hertz
        if self.tipo == 'canale':
            self.larghezza = dato1
            self.altezza = dato2
            self.lunghezza = dato3
            self.portata = dato4
        
        elif self.tipo == 'curva':
            self.larghezza = dato1
            self.altezza = dato2
            self.raggio_curva = dato3
            
        elif self.tipo == 'deviatore':
            self.residua = dato1
            self.totale = dato2
            
        elif self.tipo == 'cilindrico':
            self.diametro = dato1
            self.lunghezza = dato2
            
        elif self.tipo == 'sonodec':
            self.diametro = dato1
            self.lunghezza = dato2
            
        else:
            self.tipo = ''
            
        
            
        # metodi
    def attenuazione(self):
        if self.tipo == 'canale':
            return self.per_tutte_frequenze_canali()
        
        elif self.tipo == 'curva':
            return self.calcolo_attenuazione_curve()
            
        elif self.tipo == 'deviatore':
            return self.calcolo_attenuazione_deviatori()
            
        elif self.tipo == 'cilindrico':
            return self.per_tutte_frequenze_canali()
            
        elif self.tipo == 'sonodec':
            return self.calcolo_attenuazione_sonodec()
            
        else:
            print('Errore nei dati inseriti!')
            
    # calcolo dei canali        
    def calcolo_coeff_dimensione(self):
        if self.tipo == 'canale':
            perimetro = self.larghezza*2/1000 + self.altezza*2/1000
            area = self.larghezza/1000*self.altezza/1000
        elif self.tipo == 'cilindrico':
            perimetro = self.diametro/1000*pi
            area = (self.diametro/2000)**2*pi
        coefficiente = perimetro/area
        return coefficiente
            
    def calcolo_attenuazione_canali(self):
        rf = self.riduzione_per_frequenza()
        coefficiente = self.calcolo_coeff_dimensione()
        if coefficiente <= 5:
            attenuazione = rf[0]*self.lunghezza/1000
        elif coefficiente >= 12:
            attenuazione = rf[2]*self.lunghezza/1000
        else:
            attenuazione = rf[1]*self.lunghezza/1000
        return attenuazione    
            
    def riduzione_per_frequenza(self):
        if self.hertz <= 63:
            attenuazione = [0.3, 0.9, 0.0]
        elif self.hertz >= 250:
            attenuazione = [0.3, 0.3, 0.3]    
        else:
            attenuazione = [0.3, 0.3, 0.9]
        return attenuazione
        
    def per_tutte_frequenze_canali(self):
        attenuazione = []
        for i in (63, 125, 250, 500, 1000, 2000, 4000, 8000):
            self.hertz = i
            attenuazione.append(round(self.calcolo_attenuazione_canali(), 2))
        return attenuazione
            
    # calcolo curve
    def attenuazione_curva(self):
        attenuazione = [0, 0, 0, 0, 0, 0, 0, 0]
        hz = self.hertz
        if self.raggio_curva <150:
            atten = [0, 0, 0, 0, 0, 0, 0, 0]
            attenuazione = atten[self.hertz_dict[hz]]
        elif self.raggio_curva <= 299:
            atten = [0, 0, 0, 0, 1, 2, 3, 3]
            attenuazione = atten[self.hertz_dict[hz]]
        elif self.raggio_curva <= 599:
            atten = [0, 0, 0, 1, 2, 3, 3, 3]
            attenuazione = atten[self.hertz_dict[hz]]
        elif self.raggio_curva <= 1200:
            atten = [0, 0, 1, 2, 3, 3, 3, 3]
            attenuazione = atten[self.hertz_dict[hz]]
        return attenuazione
            
    def calcolo_attenuazione_curve(self):
        attenuazione = [0, 0, 0, 0, 0, 0, 0, 0]
        if self.raggio_curva <150:
            attenuazione = [0, 0, 0, 0, 0, 0, 0, 0]
        elif self.raggio_curva <= 299:
            attenuazione = [0, 0, 0, 0, 1, 2, 3, 3]
        elif self.raggio_curva <= 599:
            attenuazione = [0, 0, 0, 1, 2, 3, 3, 3]
        elif self.raggio_curva <= 1200:
            attenuazione = [0, 0, 1, 2, 3, 3, 3, 3]
        return attenuazione

    # calcolo deviatori
    def attenuazione_deviatore(self):
        attenuazione = -10*log10(self.totale/self.residua)
        return round(attenuazione, 2)
        
    def calcolo_attenuazione_deviatori(self):
        attenuazione = []
        att = -10*log10(self.totale/self.residua)
        for i in range(8):
            attenuazione.append(round(att, 2))
        return attenuazione
            
        
    
    # calcolo sonodec
    def calcolo_attenuazione_sonodec(self):
        pass
        
        
        
if __name__ == '__main__':
     can1 = Canale('cilindrico', 100, 200, 300, 500)
     #verifica = can1.per_tutte_frequenze_canali()
     #print(verifica)
     prova = can1.attenuazione()
     print(prova)


