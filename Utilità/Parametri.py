from PyQt5.QtCore import QTime


class Parametri():
    eta_minima = ["Adatto a tutti", "Sconsigliato ai minori di 6 anni", "Vietato ai minori di 14 anni",
                  "Vietato ai minori di 18 anni"]               #lista dei vincoli sull'età per la visione di un film
    aree_di_competenza = ["Biglietteria", "Bar", "Pulizie"]     #lista delle aree di competenza del personale
    sale = ["Sala 1", "Sala 2", "Sala 3", "Sala 4"]      #lista dei nomi delle sale del cinema
    orario_di_apertura = QTime(14, 0)
    orario_di_chiusura = QTime(1, 0)


    # Parametri rigurdanti le sale
    file_sala_1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    lunghezza_file_sala_1 = 12
    file_vip_sala_1 = ["L", "M"]

    file_sala_2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    lunghezza_file_sala_2 = 11
    file_vip_sala_2 = ["L", "M"]

    file_sala_3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    lunghezza_file_sala_3 = 13
    file_vip_sala_3 = ["L"]

    file_sala_4 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    lunghezza_file_sala_4 = 10
    file_vip_sala_4 = ["K", "L"]