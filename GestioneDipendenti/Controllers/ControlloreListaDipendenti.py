
from GestioneDipendenti.Models.ListaDipendenti import ListaDipendenti
from Utilità.Controlli import Controlli

class ControlloreListaDipendenti():
    def __init__(self):
        super(ControlloreListaDipendenti, self).__init__()
        self.model = ListaDipendenti()

    # ritorna la lista completa dei dipendenti registrati a sistema
    def get_lista_completa(self):
        return self.model.lista_dipendenti

    #ritorna una lista contenente i codici di accesso dei dipendenti
    def get_codici_acc(self):
        return self.model.get_codici_acc()

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
        if Controlli.controlla_stringa_lettere(nome) == False and nome != "":
            return "Il nome inserito non è valido"
        if Controlli.controlla_stringa_lettere(cognome) == False and cognome != "":
            return "Il cognome inserito non è valido"
        return None

    # controlla che tutti i campi del dipendente che si vuole inserire a sistema siano corretti
    def controlla_campi_dipendente(self, dipendente):
        if not Controlli.controlla_stringa_lettere(dipendente.nome):
            return "Il nome inserito non è valido"
        if not Controlli.controlla_stringa_lettere(dipendente.cognome):
            return "Il cognome inserito non è valido"
        if not Controlli.controlla_cod_fisc(dipendente.cod_fisc, self.get_lista_completa()):
            return "Il codice fiscale inserito non è valido"
        if not Controlli.controlla_telefono(dipendente.telefono):
            return "Il numero di telefono inserito non è valido"
        if not Controlli.controlla_stringa_stampabile(dipendente.email):
            return "L'indirizzo email inserito non è valido"
        if dipendente.area_comp == "Biglietteria":
            if not Controlli.controlla_codice_autenticazione(dipendente.codice_autent, self.get_lista_completa()):
                return "Il codice per la futura autenticazione inserito non è valido"
        return None

    # Salva su file i dati relativi ai dipendenti registrati a sistema
    def save_data(self):
        self.model.save_data()