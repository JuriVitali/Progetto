from Film.Models.ListaFilm import ListaFilm


class ControlloreListaFilm():
    def __init__(self):
        super(ControlloreListaFilm, self).__init__()
        self.model = ListaFilm()

    def get_lista_completa(self):
        return self.model.lista_film

    def aggiungi_film(self, film):
        self.model.aggiungi_film(film)

    def get_film_by_titolo(self, titolo):
        return self.model.get_film_by_titolo(titolo)

    def elimina_film_by_index(self,indice, lista_filtrata):
        film_selezionato = lista_filtrata[indice]
        lista_filtrata.remove(lista_filtrata[indice])
        self.model.rimuovi_film_by_id(film_selezionato.id)

    def controlla_campi_ricerca(self, titolo):
        return None

    def controlla_campi_film(self, film):
        return None

    def save_data(self):
        self.model.save_data()