import os
import pickle

class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.lista_dipendenti = []

        if os.path.isfile('GestioneDipendenti/Salvataggio_lista_dipendenti.pickle'):
            with open('GestioneDipendenti/Salvataggio_lista_dipendenti.pickle', 'rb') as f:
                self.lista_dipendenti = pickle.load(f)

    # aggiunge un dipendente alla lista dei dipendenti registrati a sistema
    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    # elimina il dipendente nella lista che ha codice fiscale uguale a quello passato come paramentro
    def rimuovi_dipendente_by_cf(self, cod_fisc):
        for i in range(0, len(self.lista_dipendenti)):
            if self.lista_dipendenti[i].cod_fisc == cod_fisc:
                self.lista_dipendenti.remove(self.lista_dipendenti[i])
                break

    # ritorna una lista contenente i dipendenti registrati a sistema che contengono nel loro nome e cognome
    # rispettivamente l nome ed il cognome passati come parametro
    def get_dipendente_by_nome(self, nome, cognome):
        lista_dip_filtrata = []
        for i in range(0, len(self.lista_dipendenti)):
            if nome in self.lista_dipendenti[i].nome and cognome in self.lista_dipendenti[i].cognome :
                lista_dip_filtrata.append(self.lista_dipendenti[i])
        return lista_dip_filtrata

    # Salva su file i dati relativi ai dipendenti registrati a sistema
    def save_data(self):
        with open('GestioneDipendenti/Salvataggio_lista_dipendenti.pickle', 'wb') as handle:
            pickle.dump(self.lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)