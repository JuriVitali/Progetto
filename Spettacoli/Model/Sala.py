from Spettacoli.Model.Posto import Posto

class Sala():

    def __init__(self, nome, file, lunghezza_file, file_premium):
        super(Sala, self).__init__()
        self.nome = nome

        #Creazione di una matrice (lista di liste) di oggetti Posto
        self.posti = [[Posto(i, j + 1, False) for j in range(0, lunghezza_file)] for i in file]   # crea una matrice di posti

        #Viene settato a True l'attributo premium dei posti che corrispondono a poltrone premium
        contatore_file = 0
        for i in file:
            premium = False
            for v in file_premium:
                if i == v:
                    premium = True               # controlla se la fila è vip
            for j in range(0, lunghezza_file):
                self.posti[contatore_file][j].premium = premium
            contatore_file += 1

        self.file = file
        self.lunghezza_file = lunghezza_file

    # Metodo che consente la prenotazione di uno o più posti che devono essere passati
    # come parametro all'interno di una lista
    def prenota_posti(self, posti_da_prenotare):
        test = 0

        for p in posti_da_prenotare:
            for i in range(len(self.posti)):
                for j in range(len(self.posti[i])):
                    if p.fila == self.posti[i][j].fila and p.posizione == self.posti[i][j].posizione:
                        self.posti[i][j].prenota()
                        test += 1
                    break
                break

        print(str(test) + " numero posti occupati")

    # Metodo che restituisce una lista di oggetti Posto che corrispondono ai posti occupati
    def get_posti_occupati(self):
        lista_posti_occupati = []
        contatore_file = 0
        for i in self.file:
            for j in range(0, self.lunghezza_file):
                if not self.posti[contatore_file][j].disponibile:
                    lista_posti_occupati.append(self.posti[contatore_file][j])
            contatore_file += 1

        return lista_posti_occupati




