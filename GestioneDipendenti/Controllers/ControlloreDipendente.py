class ControlloreDipendente():
    def __init__(self, dipendente):
        self.model = dipendente

    def get_nome(self):
        return self.model.nome

    def get_cognome(self):
        return self.model.cognome

    def get_data_nascita(self):
        return self.model.data_nascita

    def get_cod_fisc(self):
        return self.model.cod_fisc

    def get_telefono(self):
        return self.model.telefono

    def get_email(self):
        return self.model.email

    def get_area_comp(self):
        return self.model.area_comp

    def get_codice_aut(self):
        return self.model.codice_autent