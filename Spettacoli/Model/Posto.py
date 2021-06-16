
class Posto():
    def __init__(self, fila, posizione, premium):
        self.disponibile = True
        self.fila = fila
        self.posizione = posizione
        self.premium = premium          #True -> poltrona premium, False -> poltrona standard

    # Metodo che consente la prenotazione di un posto
    def prenota(self):
        self.disponibile = False








