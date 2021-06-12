class Cliente():
    def __init__(self, nome, cognome, data_nascita, cod_fisc, email):
        super(Cliente, self).__init__()
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.cod_fisc = cod_fisc
        self.email = email
        self.abbonamento = None
        self.tessera = None