
from PyQt5.QtWidgets import QGridLayout

from Spettacoli.Model.Posto import Posto

class Sala():

    def __init__(self, nome, file, lunghezza_file, file_premium):
        super(Sala, self).__init__()
        self.nome = nome
        self.posti = [[Posto(i, j + 1, False) for j in range(0, lunghezza_file)] for i in file]   # crea una matrice di posti
        contatore_file = 0
        for i in file:
            premium = False
            for v in file_premium:
                if i == v:
                    premium = True               # controlla se la fila è vip
            for j in range(0, lunghezza_file):
                self.posti[contatore_file][j].premium = premium
            contatore_file += 1

        self.file = file
        self.lunghezza_file = lunghezza_file

    # Metodo che consente la prenotazione di uno o più posti che devono essere passati
    # come parametro all'interno di una lista
    def prenota_posti(self, posti_da_prenotare):
        for p in posti_da_prenotare:
            posto = p.get_posto()
            for i in range(len(self.posti)):
                for j in range(len(self.posti[i])):
                    if posto["Fila"] == self.posti[i][j].fila and posto["Posizione"] == self.posti[i][j].posizione:
                        self.posti[i][j].prenota()
                    break

    def get_posti_occupati(self):
        lista_posti_occupati = []
        contatore_file = 0
        for i in self.file:
            for j in range(0, self.lunghezza_file):
                if not self.posti[contatore_file][j].disponibile:
                    lista_posti_occupati.append(self.posti[contatore_file][j])
            contatore_file += 1

        return lista_posti_occupati




