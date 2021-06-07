class Cliente():
    def __init__(self, nome, cognome, data_nascita, cod_fisc, email, cod_abb = None, cod_tess = None ):
        super(Cliente, self).__init__()
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.cod_fisc = cod_fisc
        self.email = email
        self.cod_abb = cod_abb
        self.cod_tess = cod_tess