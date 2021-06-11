from PyQt5.QtCore import QTime

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