import os
import pickle

class ListaSpettacoli():
    def __init__(self):
        super(ListaSpettacoli, self).__init__()
        self.lista_spettacoli = []
        self.lista_film = []

        if os.path.isfile('Spettacoli/Salvataggio_lista_spettacoli.pickle'):
            with open('Spettacoli/Salvataggio_lista_spettacoli.pickle', 'rb') as handle:
                self.lista_spettacoli = pickle.load(handle)

        if os.path.isfile('Film/Salvataggio_lista_film.pickle'):           #caricamento dei dati
            with open('Film/Salvataggio_lista_film.pickle', 'rb') as f:
                self.lista_film = pickle.load(f)

    # aggiunge uno spettacolo alla lista degli spettacoli registrati a sistema
    def aggiungi_spettacolo(self, spettacolo):
        self.lista_spettacoli.append(spettacolo)

    # elimina lo spettacolo nella lista che ha id uguale a quello passato come paramentro
    def rimuovi_spettacolo_by_id(self, id):
        for i in range(0, len(self.lista_spettacoli)):
            if self.lista_spettacoli[i].id == id:
                self.lista_spettacoli.remove(self.lista_spettacoli[i])
                break

    # ritorna una lista contenente gli spettacoli registrati a sistema che sono programmati per la
    #data passata come parametro
    def get_spettacolo_by_date(self, data):
        lista_spett_filtrata = []
        for i in range(0, len(self.lista_spettacoli)):
            if data == self.lista_spettacoli[i].data:
                lista_spett_filtrata.append(self.lista_spettacoli[i])
        return lista_spett_filtrata

    #Ritorna una lista contenente i film presenti nel sistema con il titolo selezionato
    def ricerca_film(self, titolo):
        lista_film_filtrata = []
        for i in range(0, len(self.lista_film)):
            if titolo in self.lista_film[i].titolo:
                lista_film_filtrata.append(self.lista_film[i])
        return lista_film_filtrata

    # Salva su file i dati relativi agli spettacoli registrati a sistema
    def save_data(self):
        with open('Spettacoli/Salvataggio_lista_spettacoli.pickle', 'wb') as handle:
            pickle.dump(self.lista_spettacoli, handle, pickle.HIGHEST_PROTOCOL)