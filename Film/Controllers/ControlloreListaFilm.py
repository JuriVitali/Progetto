from Film.Models.ListaFilm import ListaFilm


class ControlloreListaFilm():
    def __init__(self):
        super(ControlloreListaFilm, self).__init__()
        self.model = ListaFilm()

    #ritorna la lista completa dei film registrati a sistema
    def get_lista_completa(self):
        return self.model.lista_film

    #aggiunge un film alla lista dei film registrati a sistema
    def aggiungi_film(self, film):
        self.model.aggiungi_film(film)

    #ritorna una lista contenente i film registrati a sistema aventi il titolo passato come parametro
    def get_film_by_titolo(self, titolo):
        return self.model.get_film_by_titolo(titolo)

    #elimina dalla lista dei film registrati a sistema il film che si trova nella posizione passata
    #come parametro della lista passata come parametro
    def elimina_film_by_index(self, indice, lista_filtrata):
        film_selezionato = lista_filtrata[indice]
        lista_filtrata.remove(lista_filtrata[indice])
        self.model.rimuovi_film_by_id(film_selezionato.id)

    #controlla che il titolo inserito nella ricerca abbia una lunghezza adeguata e sia composto da caratteri stampabili
    def controlla_campi_ricerca(self, titolo):
        return None

    #controlla che tutti i campi del film che si vuole inserire a sistema siano corretti
    def controlla_campi_film(self, film):
        return None

    #Salva su file i dati relativi ai film registrati a sistema
    def save_data(self):
        self.model.save_data()