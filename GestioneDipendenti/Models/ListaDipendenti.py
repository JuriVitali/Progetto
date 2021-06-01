import os
import pickle

class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.lista_dipendenti = []

        if os.path.isfile('GestioneDipendenti/Salvataggio_lista_dipendenti.pickle'):
            with open('GestioneDipendenti/Salvataggio_lista_dipendenti.pickle', 'rb') as f:
                self.lista_dipendenti = pickle.load(f)

    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    def rimuovi_dipendente_by_cf(self, cod_fisc):
        for i in range(0, len(self.lista_dipendenti)):
            if self.lista_dipendenti[i].cod_fisc == cod_fisc:
                self.lista_dipendenti.remove(self.lista_dipendenti[i])
                break

    def get_dipendente_by_nome(self, nome, cognome):
        lista_dip_filtrata = []
        for i in range(0, len(self.lista_dipendenti)):
            if self.lista_dipendenti[i].nome == nome and self.lista_dipendenti[i].cognome == cognome: lista_dip_filtrata.append(self.lista_dipendenti[i])
        return lista_dip_filtrata

    def save_data(self):
        with open('GestioneDipendenti/Salvataggio_lista_dipendenti.pickle', 'wb') as handle:
            pickle.dump(self.lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)