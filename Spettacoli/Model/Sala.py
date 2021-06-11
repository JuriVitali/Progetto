
from PyQt5.QtWidgets import QGridLayout

from Spettacoli.Model.Posto import Posto

class Sala():

    def __init__(self, nome, file, lunghezza_file, file_vip):
        super(Sala, self).__init__()
        self.nome = nome
        self.posti = [[Posto(i, j + 1, False) for j in range(0, lunghezza_file)] for i in file]   # crea una matrice di posti
        contatore_file = 0
        for i in file:
            vip = False
            for v in file_vip:
                if i == v:
                    vip = True               # controlla se la fila è vip
            for j in range(0, lunghezza_file):
                self.posti[contatore_file][j].premium = vip
            contatore_file += 1

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

    # Metodo che crea l'interfaccia grafica relativa alla mappa posti
    def mostra_sala(self):
        griglia_posti = QGridLayout()
        for i in range(len(self.posti)):
            for j in range(len(self.posti[i])):
                self.posti[i][j].applica_stile_check_box()
                griglia_posti.addWidget(self.posti[i][j].box, i, j)
        return griglia_posti



