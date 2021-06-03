from GestioneDipendenti.Models.ListaDipendenti import ListaDipendenti


class ControlloreListaDipendenti():
    def __init__(self):
        super(ControlloreListaDipendenti, self).__init__()
        self.model = ListaDipendenti()

    # ritorna la lista completa dei dipendenti registrati a sistema
    def get_lista_completa(self):
        return self.model.lista_dipendenti

    # aggiunge un dipendente alla lista dei dipendenti registrati a sistema
    def aggiungi_dipendente(self, dipendente):
        self.model.aggiungi_dipendente(dipendente)

    # ritorna una lista contenente i dipendenti registrati a sistema aventi il nome ed il cognome
    # passati come parametro
    def get_dipendente_by_nome(self, nome, cognome):
        return self.model.get_dipendente_by_nome(nome, cognome)

    # elimina dalla lista dei dipendenti registrati a sistema il dipendente che si trova nella posizione passata
    # come parametro della lista passata come parametro
    def elimina_dipendente_by_index(self,indice, lista_filtrata):
        dipendente_selezionato = lista_filtrata[indice]
        lista_filtrata.remove(lista_filtrata[indice])
        self.model.rimuovi_dipendente_by_cf(dipendente_selezionato.cod_fisc)

    # controlla che il nome e il cognome inseriti nella ricerca siano composti da lettere
    def controlla_campi_ricerca(self, nome, cognome):
        return None

    # controlla che tutti i campi del dipendente he si vuole inserire a sistema siano corretti
    def controlla_campi_dipendente(self, dipendente):
        return None

    # Salva su file i dati relativi ai dipendenti registrati a sistema
    def save_data(self):
        self.model.save_data()