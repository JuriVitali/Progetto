class Film():
    def __init__(self, titolo, casa_prod, durata, genere, eta_minima):
        super(Film, self).__init__()
        self.id = str(titolo) + str(durata) + str(casa_prod)
        self.titolo = titolo
        self.casa_prod = casa_prod
        self.durata = durata
        self.genere = genere
        self.eta_minima = eta_minima
