import os
import pickle
from GestioneClienti.Model.Cliente import Cliente

class ListaClienti():
    def __init__(self):
        super(ListaClienti, self).__init__()
        self.lista_clienti = []

        if os.path.isfile('GestioneClienti/Salvataggio_lista_clienti.pickle'):           #caricamento dei dati
            with open('GestioneClienti/Salvataggio_lista_clienti.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)

        #Controllo della validità di ogni abbonamento
        for cliente in self.lista_clienti:
            if cliente.abbonamento is not None and not cliente.abbonamento.verifica_validita():
                cliente.abbonamento = None

    # metodo che aggiunge il cliente che gli viene passato alla lista dei clienti
    # registrata a sistema
    def aggiungi_cliente(self, cliente, cod_abb, cod_tess):
        if cod_abb != "":
            self.rilascia_abbonamento(cod_abb, cliente)
        if cod_tess != "":
            self.rilascia_tessera(cod_tess, cliente)
        self.lista_clienti.append(cliente)

    # Metodo che assegna un nuovo abbonamento che ha come codice cod_abb (primo parametro)
    # ad un cliente (secondo parametro)
    def rilascia_abbonamento(self, cod_abb, cliente):
        cliente.assegna_abbonamento(cod_abb)

    # Metodo che assegna una nuova tessera che ha come codice cod_tess (primo parametro)
    # ad un cliente (secondo parametro)
    def rilascia_tessera(self, cod_tess, cliente):
        cliente.assegna_tessera(cod_tess)

    # metodo che elimina dal sistema il cliente che ha come codice fiscale cod_fisc (primo parametro)
    def rimuovi_cliente_by_cf(self, cod_fisc):
        for i in range(0, len(self.lista_clienti)):
            if self.lista_clienti[i].cod_fisc == cod_fisc:
                self.lista_clienti.remove(self.lista_clienti[i])
                break

    # metodo che restituisce una lista di clienti che il cui nome e cognome contengono
    # rispettivamente le due stringhe passate come parametri
    def get_cliente_by_nome(self, nome, cognome):
        lista_clien_filtrata = []
        for i in range(0, len(self.lista_clienti)):
            if nome in self.lista_clienti[i].nome and cognome in self.lista_clienti[i].cognome:
                lista_clien_filtrata.append(self.lista_clienti[i])
        return lista_clien_filtrata

    # Metodo che salva la lista dei clienti registrata a sistema
    def save_data(self):
        with open('GestioneClienti/Salvataggio_lista_clienti.pickle', 'wb') as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)
