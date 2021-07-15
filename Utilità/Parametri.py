from PyQt5.QtCore import QTime


class Parametri():
    # lista dei vincoli sull'età per la visione di un film
    eta_minima = ["adatto a tutti", "sconsigliato ai minori di 6 anni", "vietato ai minori di 14 anni",
                  "vietato ai minori di 18 anni"]

    # lista delle aree di competenza del personale
    aree_di_competenza = ["Biglietteria", "Bar", "Pulizie"]

    # codice amministratore
    codice_amministratore = "A9iE2sC3"

    # lista dei nomi delle sale del cinema
    sale = ["Sala 1", "Sala 2", "Sala 3", "Sala 4"]
    orario_di_apertura = QTime(14, 0)
    orario_di_chiusura = QTime(1, 0)

    # Parametri rigurdanti le sale
    #Sala 1
    file_sala_1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    lunghezza_file_sala_1 = 10
    file_vip_sala_1 = ["J", "K"]

    # Sala 2
    file_sala_2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    lunghezza_file_sala_2 = 13
    file_vip_sala_2 = ["K", "L"]

    # Sala 3
    file_sala_3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    lunghezza_file_sala_3 = 11
    file_vip_sala_3 = ["K"]

    # Sala 4
    file_sala_4 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    lunghezza_file_sala_4 = 13
    file_vip_sala_4 = ["J"]