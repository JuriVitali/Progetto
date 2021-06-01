import os
import pickle

class ListaFilm():
    def __init__(self):
        super(ListaFilm, self).__init__()
        self.lista_film = []

        if os.path.isfile('Film/Salvataggio_lista_film.pickle'):
            with open('Film/Salvataggio_lista_film.pickle', 'rb') as f:
                self.lista_film = pickle.load(f)

    def aggiungi_film(self, film):
        self.lista_film.append(film)

    def rimuovi_dipendente_by_id(self, id):
        for i in range(0, len(self.lista_film)):
            if self.lista_film[i].id == id:
                self.lista_film.remove(self.lista_film[i])
                break

    def get_film_by_titolo(self, titolo):
        lista_film_filtrata = []
        for i in range(0, len(self.lista_film)):
            if self.lista_film[i].titolo == titolo: lista_film_filtrata.append(self.lista_film[i])
        return lista_film_filtrata

    def save_data(self):
        with open('Film/Salvataggio_lista_film.pickle', 'wb') as handle:
            pickle.dump(self.lista_film, handle, pickle.HIGHEST_PROTOCOL)