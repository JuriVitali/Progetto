from PyQt5.QtCore import QTime

from Spettacoli.Model.Sala import Sala
from Utilità.Parametri import Parametri


class Spettacolo():
    def __init__(self, film, data, ora_inizio, sala):
        super(Spettacolo, self).__init__()
        self.id = film.titolo + sala.nome + str(data.day()) + str(data.month()) + str(ora_inizio.hour())
        self.film = film
        self.data = data
        self.ora_inizio = ora_inizio

        #si tiene conto della pubblicità iniziale (20 minuti), della durata del film e della pausa(5 minuti)
        self.ora_fine = QTime(ora_inizio).addSecs((20 * 60) + (int(self.film.durata) * 60) + (5 * 60))
        self.sala = sala

        #Creazione di una lista che conterrà oggetti Cliente corrispondenti alle persone presenti allo spettacolo
        self.lista_presenze = []

    # Metodo che aggiunge tutti gli oggetti di tipo Cliente passatigli in una lista (lista_spettatori) alla
    # lista delle presenze
    def aggiungi_spettatori(self, lista_spettatori):
        for spettatore in lista_spettatori:
            self.lista_presenze.append(spettatore)

    # Metodo che costruisce un oggetto di tipo sala a partire dal suo nome e dai posti occupati.
    # Viene utilizzato quando si deve caricare la lista degli spettacoli dal file perchè non
    # è possibile salvare oggetti di tipo Sala
    def ricostruisci_sala(self, sala):
        if sala["Sala"] == Parametri.sale[0]:
            self.sala = Sala(Parametri.sale[0], Parametri.file_sala_1, Parametri.lunghezza_file_sala_1,
                        Parametri.file_vip_sala_1)
        elif sala["Sala"] == Parametri.sale[1]:
            self.sala = Sala(Parametri.sale[1], Parametri.file_sala_2, Parametri.lunghezza_file_sala_2,
                        Parametri.file_vip_sala_2)
        elif sala["Sala"] == Parametri.sale[2]:
            self.sala = Sala(Parametri.sale[2], Parametri.file_sala_3, Parametri.lunghezza_file_sala_3,
                        Parametri.file_vip_sala_3)
        else:
            self.sala = Sala(Parametri.sale[3], Parametri.file_sala_4, Parametri.lunghezza_file_sala_4,
                        Parametri.file_vip_sala_4)

        self.sala.prenota_posti(sala["Prenotazioni"])

    # Metodo che ritorna l'oggetto Posto corrispondente alla fila (primo parametro) e alla
    # posizione (secondo parametro) passategli
    def get_posto(self, nome_fila, posizione):
        for fila in self.sala.posti:
            for posto in fila:
                if posto.fila == nome_fila and posto.posizione == posizione:
                    return posto

    # metodo che dati fila(primo parametro) e colonna (secondo parametro) di un posto per lo
    # spettacolo da prenotare, prenota il posto
    def prenota_posto(self, nome_fila, posizione):
        posto_da_prenotare = self.get_posto(nome_fila, posizione)
        posto_da_prenotare.prenota()

    # Aggiorna la lista dei clienti che hanno prenotato un posto per lo spettacolo
    def aggiorna_lista_presenze(self, lista_nuovi_spettatori):
        for spettatore in lista_nuovi_spettatori:
            duplicato = False
            for presenza in self.lista_presenze:
                if spettatore.cod_fisc == presenza.cod_fisc:
                    duplicato = True

            if not duplicato:
                self.lista_presenze.append(spettatore)

