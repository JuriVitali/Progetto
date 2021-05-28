from GestioneDipendenti.Models.ListaDipendenti import ListaDipendenti


class ControlloreGestisciDipendenti():
    def __init__(self):
        super(ControlloreGestisciDipendenti, self).__init__()
        self.model = ListaDipendenti()

    def save_data(self):
        self.model.save_data()