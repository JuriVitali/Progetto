from Spettacoli.Model.ListaSpettacoli import ListaSpettacoli
from Utilità.Controlli import Controlli
from Utilità.Parametri import Parametri

class ControlloreListaSpettacoli():
    def __init__(self):
        super(ControlloreListaSpettacoli, self).__init__()
        self.model = ListaSpettacoli()

    #aggiunge uno spettacolo alla lista degli spettacoli registrati a sistema
    def aggiungi_spettacolo(self, spettacolo):
        self.model.aggiungi_spettacolo(spettacolo)

    #ritorna una lista  contenente una lista per ogni sala;
    #all'interno di ognuna di queste liste ci sono gli spettacoli programmati per il giorno
    #passato come parametro nella sala corrispondente
    def get_spettacoli_by_day_divisi(self, data):

        lista_spett_data = self.model.get_spettacolo_by_date(data)      #lista degli spettacoli programmati per il giorno scelto

        lista_spett_sala_1 = []
        lista_spett_sala_2 = []
        lista_spett_sala_3 = []
        lista_spett_sala_4 = []

        lista_spett_finale = []         #lista degli spettacoli divisi per sala

        for i in range(0, len(lista_spett_data)):
            if lista_spett_data[i].sala.nome == Parametri.sale[0]:
                lista_spett_sala_1.append(lista_spett_data[i])
            elif lista_spett_data[i].sala.nome == Parametri.sale[1]:
                lista_spett_sala_2.append(lista_spett_data[i])
            elif lista_spett_data[i].sala.nome == Parametri.sale[2]:
                lista_spett_sala_3.append(lista_spett_data[i])
            else:
                lista_spett_sala_4.append(lista_spett_data[i])

        lista_spett_finale.append(lista_spett_sala_1)
        lista_spett_finale.append(lista_spett_sala_2)
        lista_spett_finale.append(lista_spett_sala_3)
        lista_spett_finale.append(lista_spett_sala_4)

        return lista_spett_finale

    #metodo che restituisce una lista di spettacoli filtrati in base a titolo e data
    def get_spettacoli_titolo_data(self, titolo, data):
        lista_spett_data = self.model.get_spettacolo_by_date(data)      #lista degli spettacoli programmati per il giorno scelto
        lista_spett_filtrata = []

        if titolo != "":
            for spettacolo in lista_spett_data:
                if titolo in spettacolo.film.titolo:
                    lista_spett_filtrata.append(spettacolo)
        else:
            return lista_spett_data

        return lista_spett_filtrata

    #metodo che ritorna una lista di spettacoli antecedenti al giorno corrente
    def get_spettacoli_passati(self):
        return self.model.get_lista_spettacoli_passati()

    #elimina dalla lista dei film registrati a sistema il film che si trova nella posizione passata
    #come parametro della lista passata come parametro
    def elimina_spettacolo_by_index(self, indice, lista_filtrata):
        spettacolo_selezionato = lista_filtrata[indice]
        lista_filtrata.remove(lista_filtrata[indice])
        self.model.rimuovi_spettacolo_by_id(spettacolo_selezionato.id)

    #controlla che tutti i campi del film che si vuole inserire a sistema siano corretti
    def controlla_campi_spettacolo(self, spettacolo):
        if not Controlli.controlla_sovrapposizione_spettacoli(spettacolo, self.model.lista_spettacoli):
            return "Lo spettacolo si sovrappone con un altro già in programma"
        if spettacolo.ora_fine > Parametri.orario_di_chiusura and spettacolo.ora_fine < Parametri.orario_di_apertura:
            return "Lo spettacolo termina dopo l'orario di chiusura del cinema"
        return None

    # metodo che restituisce una stringa da inserire in un messaggio di errore se il titolo passato non
    # è valido
    def controlla_campi_ricerca(self, titolo):
        if Controlli.controlla_stringa_stampabile(titolo) == False:
            return "Il titolo inserito non è valido"
        return None

    # metodo che ritorna una lista contenente i film con il titolo cercato
    def ricerca_film(self, titolo):
        return self.model.ricerca_film(titolo)

    #Salva su file i dati relativi ai film registrati a sistema
    def save_data(self):
        self.model.save_data()