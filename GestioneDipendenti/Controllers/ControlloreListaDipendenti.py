from GestioneDipendenti.Models.ListaDipendenti import ListaDipendenti


class ControlloreListaDipendenti():
    def __init__(self):
        super(ControlloreListaDipendenti, self).__init__()
        self.model = ListaDipendenti()

    def get_lista_completa(self):
        return self.model.lista_dipendenti

    def aggiungi_dipendente(self, dipendente):
        self.model.aggiungi_dipendente(dipendente)

    def get_dipendente_by_nome(self, nome, cognome):
        return self.model.get_dipendente_by_nome(nome, cognome)

    def elimina_dipendente_by_index(self,indice, lista_filtrata):
        dipendente_selezionato = lista_filtrata[indice]
        lista_filtrata.remove(lista_filtrata[indice])
        self.model.rimuovi_dipendente_by_cf(dipendente_selezionato.cod_fisc)

    def controlla_campi_ricerca(self, nome, cognome):
        return None

    def controlla_campi_dipendente(self, dipendente):
        return None

    def save_data(self):
        self.model.save_data()