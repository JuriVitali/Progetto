from PyQt5.QtCore import QTime

class Spettacolo():
    def __init__(self, film, data, ora_inizio, sala):
        self.id = film.titolo + sala.nome + str(data.day()) + str(data.month()) + str(ora_inizio.hour())
        self.film = film
        self.data = data
        self.ora_inizio = ora_inizio
        self.ora_fine = QTime(ora_inizio).addSecs(int(self.film.durata) * 60)
        self.sala = sala