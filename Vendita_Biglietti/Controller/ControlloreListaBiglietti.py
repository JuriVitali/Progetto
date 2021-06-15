from Vendita_Biglietti.Model.ListaBiglietti import ListaBiglietti


class ControlloreListaBiglietti():
    def __init__(self):
        super(ControlloreListaBiglietti, self).__init__()
        self.model = ListaBiglietti()

    def get_lista_biglietti(self):
        return self.model.lista_biglietti

    def add_biglietto(self, biglietto):
        self.model.add_biglietto(biglietto)

    def get_cliente(self, cod_fisc):
        return self.model.get_cliente(cod_fisc)