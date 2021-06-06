from GestioneClienti.Models.ListaClienti import ListaClienti


class ControlloreListaClienti():
    def __init__(self):
        super(ControlloreListaClienti, self).__init__()
        self.model = ListaClienti()

    def get_lista_completa(self):
        return self.model.lista_clienti

    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)

    def get_cliente_by_nome(self, nome, cognome):
        return self.model.get_cliente_by_nome(nome, cognome)

    def elimina_dipendente_by_index(self, indice, lista_filtrata):
        cliente_selezionato = lista_filtrata[indice]
        lista_filtrata.remove(lista_filtrata[indice])
        self.model.rimuovi_cliente_by_cf(cliente_selezionato.cod_fisc)

    def controlla_campi_ricerca(self, nome, cognome):
        return None

    def controlla_campi_cliente(self, cliente):
        return None

    def save_data(self):
        self.model.save_data()
