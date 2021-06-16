from Utilità.Controlli import Controlli
from GestioneClienti.Model.ListaClienti import ListaClienti

class ControlloreListaClienti():
    def __init__(self):
        super(ControlloreListaClienti, self).__init__()
        self.model = ListaClienti()

    #metodo che ritorna la lista completa dei clienti registrati a sistema
    def get_lista_completa(self):
        return self.model.lista_clienti

    #metodo che aggiunge il cliente che gli viene passato alla lista dei clienti
    #registrata a sistema
    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)

    #metodo che restituisce una lista di clienti che il cui nome e cognome contengono
    #rispettivamente le due stringhe passate come parametri
    def get_cliente_by_nome(self, nome, cognome):
        return self.model.get_cliente_by_nome(nome, cognome)

    #metodo che elimina dal sistema il cliente che si trova all'indice passato (come parametro) della lista
    #di clienti passata (come parametro)
    def elimina_cliente_by_index(self, indice, lista_filtrata):
        cliente_selezionato = lista_filtrata[indice]
        lista_filtrata.remove(lista_filtrata[indice])
        self.model.rimuovi_cliente_by_cf(cliente_selezionato.cod_fisc)

    #metodo che controlla sei il nome ed il cognome passatigli sono validi.
    #Se non lo sono ritorna una stringa che descrive l'errore, mentre se sono
    #validi ritorna None
    def controlla_campi_ricerca(self, nome, cognome):
        if Controlli.controlla_stringa_lettere(nome) == False and nome != "":
            return "Il nome inserito non è valido"
        if Controlli.controlla_stringa_lettere(cognome) == False and cognome != "":
            return "Il cognome inserito non è valido"
        return None

    # Metodo che controlla la validità degli attributi del cliente passatogli come parametro.
    # Se il codice dell'abbonamento che gli viene passato non è una stringa vuota, controlla la
    # validità di tale codice e se è valido al cliente viene assegnato un Abbonamento con
    # il codice passato.
    # Il metodo procede in modo analogo con il codice della tessera.
    # Infine ritorna None se tutti i campi e i parametri sono validi, o una stringa descrivente
    # l'errore se almeno un non lo è
    def controlla_campi_cliente(self, cliente, cod_abb, cod_tess):
        if not Controlli.controlla_stringa_lettere(cliente.nome):
            return "Il nome inserito non è valido"
        if not Controlli.controlla_stringa_lettere(cliente.cognome):
            return "Il cognome inserito non è valido"
        if not Controlli.controlla_cod_fisc(cliente.cod_fisc, self.get_lista_completa()):
            return "Il codice fiscale inserito non è valido"
        if not Controlli.controlla_telefono(cliente.telefono):
            return "Il numero di telefono inserito non è valido"
        if not Controlli.controlla_stringa_stampabile(cliente.email):
           return "L'indirizzo email inserito non è valido"

        if cod_abb != "":
            avviso_abb = self.controlla_abbonamento(cod_abb, cliente)
            if avviso_abb is not None:
                return avviso_abb
            else:
                self.rilascia_abbonamento(cod_abb, cliente)

        if cod_tess != "":
            avviso_tess = self.controlla_tessera(cod_tess, cliente)
            if avviso_tess is not None:
                return avviso_tess
            else:
                self.rilascia_tessera(cod_tess, cliente)

        return None

    # Metodo che controlla che il codice dell'abbonamento passatogli come parametro sia valido, che esso
    # non sia già stato assegnato ad un altro cliente e che il cliente al quale si vuole assegnare
    # l'abbonamento (secondo parametro) abbia almeno 14 anni
    def controlla_abbonamento(self, codice_abb, cliente_selezionato):
        if not Controlli.controlla_codice_abb(codice_abb, self.get_lista_completa()) :
            return "Il codice dell'abbonamento inserito non è valido"
        if cliente_selezionato.abbonamento is not None:
            return "Il cliente è già in possesso di un abbonamento"
        if not Controlli.controlla_eta_cliente(cliente_selezionato):
            return "Il cliente non può possedere un abbonamento perchè ha meno di 14 anni"

        return None

    # Metodo che controlla che il codice della tessera passatagli come parametro sia valido, che esso
    # non sia già stata assegnato ad un altro cliente e che il cliente al quale si vuole assegnare
    # la tessera (secondo parametro) abbia almeno 14 anni
    def controlla_tessera(self, codice_tess, cliente_selezionato):
        if not Controlli.controlla_codice_tess(codice_tess, self.get_lista_completa()):
            return "Il codice della tessera inserito non è valido"
        if cliente_selezionato.tessera is not None:
            return "Il cliente è già in possesso di una tessera"
        if not Controlli.controlla_eta_cliente(cliente_selezionato):
            return "Il cliente non può possedere una tessera perchè ha meno di 14 anni"

        return None

    # Metodo che assegna un nuovo abbonamento che ha come codice cod_abb (primo parametro)
    # ad un cliente (secondo parametro)
    def rilascia_abbonamento(self, cod_abb, cliente):
        cliente.assegna_abbonamento = cod_abb

    # Metodo che assegna una nuova tessera che ha come codice cod_tess (primo parametro)
    # ad un cliente (secondo parametro)
    def rilascia_tessera(self, cod_tess, cliente):
        cliente.assegna_tessera = cod_tess

    # Metodo che salva la lista dei clienti registrata a sistema
    def save_data(self):
        self.model.save_data()
