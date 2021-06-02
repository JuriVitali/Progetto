class ControlloreFilm():
    def __init__(self, film):
        self.model = film

    def get_id(self):
        return self.model.id

    def get_titolo(self):
        return self.model.titolo

    def get_casa_prod(self):
        return self.model.casa_prod

    def get_durata(self):
        return self.model.durata

    def get_genere(self):
        return self.model.genere

    def get_eta_minima(self):
        return self.model.eta_minima
