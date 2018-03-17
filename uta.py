from gestione_dati import InputDati

class Uta:
    """
    classe UTA per l'inserimento dei dati principali
    per il calcolo dell'abbattimento acustico delle canalizzazioni
    """
    def __init__(self):
        self.DBA = (26.2, 16.1, 8.6, 3.2, 0.0, -1.2, -1.0, 1.1)
        self.macchina = ''
        self.tipo_canale = ''
        self.portata = 0
        self.prevalenza = 0
        self.decibel = 'n'
        self.emissione = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ]
        self.schermata_input()

    # schermata di imput dati dell'uta e delle frequenze emesse
    def schermata_input(self):
        frequenze = ('63Hz', '125Hz', '250Hz', '500Hz', '1000Hz', '2000Hz', '4000Hz', '8000Hz')
        i = 0
        macchina = input('Inserire il tipo di UTA: ')
        tipo_canale = input('Mandata, Ripresa Pae, Esp: ')
        portata = input('Inserire la portata: ')
        prevalenza = input('Inserire la Prevalenza: ')
        self.macchina = 'UTA ' + macchina +' ' + tipo_canale + ' - Portata ' + portata + ' mc/h - Prevalenza ' + prevalenza + ' Pa'
        print(self.macchina)
        self.decibel = input('Inserire se le emissioni acustiche sono in dB(A) s/[n]: ')
        for i in range(8):
            self.emissione[i] = input('Inserire l\'emissione per i %s Hertz ' % frequenze[i])
            #self.scelta_decibel()
        self.scelta_decibel()

    # modifica i decibel in dB(A)   
    def scelta_decibel(self):
        if self.decibel == 's' or self.decibel == 'S':
            i = 0
            for i in range(8):
                self.emissione[i] = float(self.emissione[i]) + self.DBA[i]
        print(self.emissione)

if __name__ == '__main__':
    s = Uta()
    #s.schermata_input()
