import os
import pickle

class ListaFilm():
    def __init__(self):
        super(ListaFilm, self).__init__()
        self.lista_film = []

        if os.path.isfile('Film/Salvataggio_lista_film.pickle'):           #caricamento dei dati
            with open('Film/Salvataggio_lista_film.pickle', 'rb') as f:
                self.lista_film = pickle.load(f)

    # aggiunge un film alla lista dei film registrati a sistema
    def aggiungi_film(self, film):
        self.lista_film.append(film)

    #elimina il film nella lista che ha id uguale a quello passato come paramentro
    def rimuovi_film_by_id(self, id):
        for i in range(0, len(self.lista_film)):
            if self.lista_film[i].id == id:
                self.lista_film.remove(self.lista_film[i])
                break

    # ritorna una lista contenente i film registrati a sistema aventi il titolo passato come parametro
    def get_film_by_titolo(self, titolo):
        lista_film_filtrata = []
        for i in range(0, len(self.lista_film)):
            if titolo in self.lista_film[i].titolo:
                lista_film_filtrata.append(self.lista_film[i])
        return lista_film_filtrata

    # elimina dalla lista dei film registrati a sistema il film quello che si trova nella posizione passata
    # come parametro della lista passata come parametro
    def save_data(self):
        with open('Film/Salvataggio_lista_film.pickle', 'wb') as handle:
            pickle.dump(self.lista_film, handle, pickle.HIGHEST_PROTOCOL)