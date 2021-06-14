class ControlloreSpettacolo():
    def __init__(self, spettacolo):
        super(ControlloreSpettacolo, self).__init__()
        self.model = spettacolo

    def get_posto(self, nome_fila, posizione):
        for fila in self.model.sala.posti:
            for posto in fila:
                if posto.fila == nome_fila and posto.posizione == posizione:
                    return posto

