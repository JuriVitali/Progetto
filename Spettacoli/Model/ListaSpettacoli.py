import os
import pickle

from PyQt5.QtCore import QDate

class ListaSpettacoli():
    def __init__(self):
        super(ListaSpettacoli, self).__init__()
        self.lista_spettacoli = []
        self.lista_film = []
        lista_sale = []

        # caricamento dei film
        if os.path.isfile('Film/Salvataggio_lista_film.pickle'):
                with open('Film/Salvataggio_lista_film.pickle', 'rb') as f:
                        self.lista_film = pickle.load(f)

        # caricamento degli spettacoli
        if os.path.isfile('Spettacoli/Salvataggio_lista_spettacoli.pickle'):
            with open('Spettacoli/Salvataggio_lista_spettacoli.pickle', 'rb') as g:
                self.lista_spettacoli = pickle.load(g)

        if os.path.isfile('Spettacoli/Salvataggio_lista_sale.pickle'):
            with open('Spettacoli/Salvataggio_lista_sale.pickle', 'rb') as h:
                lista_sale = pickle.load(h)

        # rimuove gli spettacoli avvenuti più di 14 giorni fa
        for spettacolo in self.lista_spettacoli:
            if spettacolo.data < (QDate.currentDate().addDays(-14)):
                self.lista_spettacoli.remove(spettacolo)

        # ricostruzione delle sale degli spettacoli in programma per il giorno corrente o
        # per i giorni successivi
        for spettacolo in self.lista_spettacoli:
            if spettacolo.data >= QDate.currentDate():
                for sala in lista_sale:
                    if spettacolo.id == sala["Id"]:
                        spettacolo.ricostruisci_sala(sala)
                        lista_sale.remove(sala)
                        break



    # Metodo che aggiunge uno spettacolo alla lista degli spettacoli registrati a sistema
    def aggiungi_spettacolo(self, spettacolo):
        self.lista_spettacoli.append(spettacolo)

    # Metodo che elimina lo spettacolo nella lista che ha id uguale a quello passato come paramentro
    def rimuovi_spettacolo_by_id(self, id):
        for i in range(0, len(self.lista_spettacoli)):
            if self.lista_spettacoli[i].id == id:
                self.lista_spettacoli.remove(self.lista_spettacoli[i])
                break

    # Metodo che ritorna una lista contenente gli spettacoli registrati a sistema che sono programmati per la
    # data passata come parametro
    def get_spettacolo_by_date(self, data):
        lista_spett_filtrata = []
        for i in range(0, len(self.lista_spettacoli)):
            if data == self.lista_spettacoli[i].data:
                lista_spett_filtrata.append(self.lista_spettacoli[i])
        return lista_spett_filtrata

    # Metodo che ritorna una lista contenente i film presenti nel sistema con il titolo selezionato
    def ricerca_film(self, titolo):
        lista_film_filtrata = []
        for i in range(0, len(self.lista_film)):
            if titolo in self.lista_film[i].titolo:
                lista_film_filtrata.append(self.lista_film[i])
        return lista_film_filtrata

    #Salva su file i dati relativi agli spettacoli registrati a sistema
    def save_data(self):

        # Non è possibile salvare oggetti di tipo sala, perciò per ogni sala viene salvato un dizionario
        # con le sue informazioni essenziali
        lista_sale = []
        for spettacolo in self.lista_spettacoli:
            lista_sale.append({"Sala" : spettacolo.sala.nome, "Prenotazioni" : spettacolo.sala.get_posti_occupati(), "Id" : spettacolo.id})

        with open("Spettacoli/Salvataggio_lista_sale.pickle", "wb") as handle:
            pickle.dump(lista_sale, handle, pickle.HIGHEST_PROTOCOL)

        for spettacolo in self.lista_spettacoli:
            spettacolo.sala = None

        with open("Spettacoli/Salvataggio_lista_spettacoli.pickle", "wb") as handle:
            pickle.dump(self.lista_spettacoli, handle, pickle.HIGHEST_PROTOCOL)