from PyQt5.QtCore import QDate

from Utilità.Controlli import Controlli
from GestioneClienti.Model.ListaClienti import ListaClienti

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

    def elimina_cliente_by_index(self, indice, lista_filtrata):
        cliente_selezionato = lista_filtrata[indice]
        lista_filtrata.remove(lista_filtrata[indice])
        self.model.rimuovi_cliente_by_cf(cliente_selezionato.cod_fisc)

    def controlla_campi_ricerca(self, nome, cognome):
        if Controlli.controlla_stringa_lettere(nome) == False and nome != "":
            return "Il nome inserito non è valido"
        if Controlli.controlla_stringa_lettere(cognome) == False and cognome != "":
            return "Il cognome inserito non è valido"
        return None

    def controlla_campi_cliente(self, cliente):
        if Controlli.controlla_stringa_lettere(cliente.nome) == False:
            return "Il nome inserito non è valido"
        if Controlli.controlla_stringa_lettere(cliente.cognome) == False:
            return "Il cognome inserito non è valido"
        if Controlli.controlla_cod_fisc(cliente.cod_fisc, self.get_lista_completa()) == False:
            return "Il codice fiscale inserito non è valido"
        if Controlli.controlla_stringa_stampabile(cliente.email) == False:
           return "L'indirizzo email inserito non è valido"
        if cliente.abbonamento is not None and Controlli.controlla_codice_abb(cliente.abbonamento.codice, self.get_lista_completa()) == False:
            return "Il codice abbonamento inserito non è valido"
        if cliente.tessera is not None and Controlli.controlla_codice_tess(cliente.tessera.codice, self.get_lista_completa()) == False:
            return "Il codice tessera inserito non è valido"
        if not QDate(cliente.data_nascita).isValid():
            return "La data inserita non è valida"
        return None


    def save_data(self):
        self.model.save_data()
