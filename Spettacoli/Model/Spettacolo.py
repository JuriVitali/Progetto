from PyQt5.QtCore import QTime

from Spettacoli.Model.Sala import Sala
from Utilità.Parametri import Parametri


class Spettacolo():
    def __init__(self, film, data, ora_inizio, sala):
        super(Spettacolo, self).__init__()
        self.id = film.titolo + sala.nome + str(data.day()) + str(data.month()) + str(ora_inizio.hour())
        self.film = film
        self.data = data
        self.ora_inizio = ora_inizio

        #si tiene conto della pubblicità iniziale (20 minuti), della durata del film e della pausa(5 minuti)
        self.ora_fine = QTime(ora_inizio).addSecs((20 * 60) + (int(self.film.durata) * 60) + (5 * 60))
        self.sala = sala

        self.lista_presenze = []

    def aggiungi_spettatori(self, lista_spettatori):
        for spettatore in lista_spettatori:
            self.lista_presenze.append(spettatore)

    def ricostruisci_sala(self, sala):
        if sala["Sala"] == Parametri.sale[0]:
            self.sala = Sala(Parametri.sale[0], Parametri.file_sala_1, Parametri.lunghezza_file_sala_1,
                        Parametri.file_vip_sala_1)
        elif sala["Sala"] == Parametri.sale[1]:
            self.sala = Sala(Parametri.sale[1], Parametri.file_sala_2, Parametri.lunghezza_file_sala_2,
                        Parametri.file_vip_sala_2)
        elif sala["Sala"] == Parametri.sale[2]:
            self.sala = Sala(Parametri.sale[2], Parametri.file_sala_3, Parametri.lunghezza_file_sala_3,
                        Parametri.file_vip_sala_3)
        else:
            self.sala = Sala(Parametri.sale[3], Parametri.file_sala_4, Parametri.lunghezza_file_sala_4,
                        Parametri.file_vip_sala_4)
        self.sala.prenota_posti(sala["Prenotazioni"])

    def get_posto(self, nome_fila, posizione):
        for fila in self.sala.posti:
            for posto in fila:
                if posto.fila == nome_fila and posto.posizione == posizione:
                    return posto
