from unittest import TestCase

from GestioneDipendenti.Models.Dipendente import Dipendente
from GestioneDipendenti.Controllers.ControlloreListaDipendenti import ControlloreListaDipendenti
from GestioneDipendenti.Models.ListaDipendenti import ListaDipendenti
from GestioneDipendenti.Views.VistaRegistraDipendente import VistaRegistraDipendente
from Utilità.Controlli import Controlli


class TestControlloreListaDipendenti(TestCase):

    # aggiustare
    def test_aggiungi_dipendente(self):
        controllore_lista_dipendenti = ControlloreListaDipendenti()
        controllore_lista_dipendenti.model.lista_dipendenti = []
        dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        dipendente2 = Dipendente(nome="Kevin", cognome="Rossi", data_nascita="2000.11.06",
                                     cod_fisc="ABC123DEF456GH78", telefono="324543664565", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="RED5654V")
        dipendente3 = Dipendente(nome="Maria", cognome="Marrone", data_nascita="1999.05.06",
                                      cod_fisc="B5N3B2JJ5I7JDH37", telefono="3345477785", email="test@email.com",
                                      area_comp="Biglietteria", codice_autent="KV8VHJSD")
        dipendente4 = Dipendente(nome="Giulia", cognome="Rossi", data_nascita="1984.10.03",
                                      cod_fisc="PALDJRN785214WAZ", telefono="3657535375", email="test@email.com",
                                      area_comp="Biglietteria", codice_autent="785W6F5V")
        # aggiungo i dipendenti alla lista dei dipendenti
        controllore_lista_dipendenti.aggiungi_dipendente(dipendente)
        controllore_lista_dipendenti.aggiungi_dipendente(dipendente2)
        controllore_lista_dipendenti.aggiungi_dipendente(dipendente3)
        controllore_lista_dipendenti.aggiungi_dipendente(dipendente4)

        #controllo che i dipenendenti sono stati inseriti nella lista
        self.assertEqual(dipendente in controllore_lista_dipendenti.get_lista_completa(), True)
        self.assertEqual(dipendente2 in controllore_lista_dipendenti.get_lista_completa(), True)
        self.assertEqual(dipendente3 in controllore_lista_dipendenti.get_lista_completa(), True)
        self.assertEqual(dipendente4 in controllore_lista_dipendenti.get_lista_completa(), True)

    # test che controlla che i campi del dipendente inserito siano validi. Test eseguito con dipendente valido
    def test_controlla_campi_dipendente(self):
        controlli = Controlli()
        lista_dipendenti = ControlloreListaDipendenti()
        dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="FREA245W")
        self.assertEqual(lista_dipendenti.controlla_campi_dipendente(dipendente), None)
        self.assertEqual(controlli.controlla_codice_autenticazione(dipendente.codice_autent, lista_dipendenti.get_lista_completa()), True)
        self.assertEqual(controlli.controlla_cod_fisc(dipendente.cod_fisc, lista_dipendenti.get_lista_completa()), True)
        self.assertEqual(controlli.controlla_telefono(dipendente.telefono), True)
        self.assertEqual(controlli.controlla_stringa_stampabile(dipendente.email), True)

    # test che controlla che i campi del dipendente inserito siano validi. Test eseguito con dipendente non valido
    def test_controlla_campi_dipendente2(self):
        controlli = Controlli()
        lista_dipendenti = ControlloreListaDipendenti()
        dipendente = Dipendente(nome="Giorgio", cognome="Mancini", data_nascita="1994.07.09",
                                     cod_fisc="ABCDEFGH1345678", telefono="", email="",
                                     area_comp="Biglietteria", codice_autent="FR45W")
        self.assertNotEqual(lista_dipendenti.controlla_campi_dipendente(dipendente), None)
        self.assertEqual(controlli.controlla_codice_autenticazione(dipendente.codice_autent, lista_dipendenti.get_lista_completa()), False)
        self.assertEqual(controlli.controlla_cod_fisc(dipendente.cod_fisc, lista_dipendenti.get_lista_completa()), False)
        self.assertEqual(controlli.controlla_telefono(dipendente.telefono), False)
        self.assertEqual(controlli.controlla_stringa_stampabile(dipendente.email), False)


    # test che controlla che l'inserimento di una stringa compresa tra 1 e 50 caratteri ritorni True
    def test_controlla_stringa_stampabile1(self):
        controlli = Controlli()
        stringa = "email@test.com"
        str49= "HdB10SIBwupXKbihPUpcid1blAqwhOFLT6os0Wamy6Ys4FvFL"
        str1 = "A"
        risp = controlli.controlla_stringa_stampabile(stringa)
        risp49 = controlli.controlla_stringa_stampabile(str49)
        risp1 = controlli.controlla_stringa_stampabile(str1)
        self.assertEqual(risp, True)
        self.assertEqual(risp49, True)
        self.assertEqual(risp1, True)


    # test che controlla che l'inserimento di una stringa vuota o superiore a 49 caratteri ritorni False
    def test_controlla_stringa_stampabile2(self):
        controlli = Controlli()
        stringa = ""
        str50 = "GKJcZW0fGTVws99h7TkXTVZuRrTqiUzVK8IRUisiLVWgiicwzb"
        str51 = "90VTpbipnhbS5zcs5uIpWQ88Payc7o5pDKoyOMHRQK97dTgyjRA"
        str70 = "91fG6lWKC1vGS7oRx6ERqqx3kpBGa74BJjfRRW2DdbuP9w8W7H1vLWCSIeajZxh5jiTjzP"
        risp = controlli.controlla_stringa_stampabile(stringa)
        risp50 = controlli.controlla_stringa_stampabile(str50)
        risp51 = controlli.controlla_stringa_stampabile(str51)
        risp70 = controlli.controlla_stringa_stampabile(str70)
        self.assertEqual(risp, False)
        self.assertEqual(risp50, False)
        self.assertEqual(risp51, False)
        self.assertEqual(risp70, False)

    # test che controlla che l'inserimento di un numero di telefono compreso tra 2 e 13 esclusi sia valido. Ritorna True se il numero è valido, altrimenti ritorna False
    def test_controlla_telefono(self):
        controlli = Controlli()
        tel3 = "123"
        tel10 = "3216751378"
        tel12 = "374555327778"
        risp3 = controlli.controlla_telefono(tel3)
        risp10 = controlli.controlla_telefono(tel10)
        risp12 = controlli.controlla_telefono(tel12)
        self.assertEqual(risp3, True)
        self.assertEqual(risp10, True)
        self.assertEqual(risp12, True)

        # test su numeri non validi
        tel_alf_num = "a53fsf94"
        tel_neg = "-344433"
        tel0 = ""
        tel1 = "1"
        tel2 = "12"
        tel13 = "2342234242424"
        tel20 = "23422342424241357943"
        risp_alf_num = controlli.controlla_telefono(tel_alf_num)
        risp_neg = controlli.controlla_telefono(tel_neg)
        risp0 = controlli.controlla_telefono(tel0)
        risp1 = controlli.controlla_telefono(tel1)
        risp2 = controlli.controlla_telefono(tel2)
        risp13 = controlli.controlla_telefono(tel13)
        risp20 = controlli.controlla_telefono(tel20)
        self.assertEqual(risp_alf_num, False)
        self.assertEqual(risp_neg, False)
        self.assertEqual(risp0, False)
        self.assertEqual(risp1, False)
        self.assertEqual(risp2, False)
        self.assertEqual(risp13, False)
        self.assertEqual(risp20, False)

    # test che controlla che l'inserimento di una stringa alfanumerico compreso tra 1 e 35 sia valido. Ritorna True se la stringa è valida, altrimenti ritorna False
    def test_controlla_stringa_lettere(self):
        controlli = Controlli()
        stringa = ""
        str1 = "A"
        str34 = "Umy6I8yR4oPXRxp7ENjCyvgRJtpwMA9vvV"
        str35 = "xC3WmigP3HBppBSa2Z9KQnc1lxbl5GXHUx6"
        str36 = "uSW5icTupr49uFK3S6nT9ajrundqrHPxDdZW"
        str50 = "GKJcZW0fGTVws99h7TkXTVZuRrTqiUzVK8IRUisiLVWgiicwzb"
        risp = controlli.controlla_stringa_stampabile(stringa)
        risp1 = controlli.controlla_stringa_stampabile(str1)
        risp34 = controlli.controlla_stringa_stampabile(str34)
        risp35 = controlli.controlla_stringa_stampabile(str35)
        risp36 = controlli.controlla_stringa_lettere(str36)
        risp50 = controlli.controlla_stringa_stampabile(str50)
        self.assertEqual(risp, False, "Dovrebbe essere non valido")
        self.assertEqual(risp1, True, "Dovrebbe essere valido")
        self.assertEqual(risp34, True, "Dovrebbe essere valido")
        self.assertEqual(risp35, True, "Dovrebbe essere valido")
        self.assertEqual(risp36, False, "Dovrebbe essere non valido")
        self.assertEqual(risp50, False, "Dovrebbe essere non valido")

    # test che controlla che l'inserimento di un codice fiscale sia valido. Ritorna True se il codice fiscale ha 16 caratteri, altrimenti ritorna False
    def test_controlla_cod_fisc(self):
        controlli =Controlli()
        lista_dipendenti = ControlloreListaDipendenti()
        cod_fisc0 = ""
        cod_fisc1 = "S"
        cod_fisc6 = "7RP22R"
        cod_fisc15 = "6KXCHO12ONP0A4G"
        cod_fisc16 = "8EVGUXC5M8VXL35N"
        cod_fisc17 = "B5JQBT3YLLCAX0EFM"
        cod_fisc30 = "U1C6NH9ED6JZQHMMBZYVSL8QSRX3UT"
        risp0 = controlli.controlla_cod_fisc(cod_fisc0, lista_dipendenti.get_lista_completa())
        risp1 = controlli.controlla_cod_fisc(cod_fisc1, lista_dipendenti.get_lista_completa())
        risp6 = controlli.controlla_cod_fisc(cod_fisc6, lista_dipendenti.get_lista_completa())
        risp15 = controlli.controlla_cod_fisc(cod_fisc15, lista_dipendenti.get_lista_completa())
        risp16 = controlli.controlla_cod_fisc(cod_fisc16, lista_dipendenti.get_lista_completa())
        risp17 = controlli.controlla_cod_fisc(cod_fisc17, lista_dipendenti.get_lista_completa())
        risp30 = controlli.controlla_cod_fisc(cod_fisc30, lista_dipendenti.get_lista_completa())
        self.assertEqual(risp0, False, "Dovrebbe essere non valido")
        self.assertEqual(risp1, False, "Dovrebbe essere non valido")
        self.assertEqual(risp6, False, "Dovrebbe essere non valido")
        self.assertEqual(risp15, False, "Dovrebbe essere non valido")
        self.assertEqual(risp16, True, "Dovrebbe essere valido")
        self.assertEqual(risp17, False, "Dovrebbe essere non valido")
        self.assertEqual(risp30, False, "Dovrebbe essere non valido")

    # test che controlla che l'inserimento del codice autentificazione sia valido. Ritorna True se il codice è di 8 caratteri alfanumerici, altrimenti ritorna False
    def test_controlla_codice_autenticazione(self):
        controlli = Controlli()
        lista_dipendenti = ControlloreListaDipendenti()
        cod_aut0 = ""
        cod_aut1 = "S"
        cod_aut7 = "7Rp22Ra"
        cod_aut8 = "S3bvt456"
        cod_aut9 = "d4rf3D4g4"
        cod_aut15 = "Lrf3c9dCYX3DAKh"
        risp0 = controlli.controlla_codice_autenticazione(cod_aut0, lista_dipendenti.get_lista_completa())
        risp1 = controlli.controlla_codice_autenticazione(cod_aut1, lista_dipendenti.get_lista_completa())
        risp7 = controlli.controlla_codice_autenticazione(cod_aut7, lista_dipendenti.get_lista_completa())
        risp8 = controlli.controlla_codice_autenticazione(cod_aut8, lista_dipendenti.get_lista_completa())
        risp9 = controlli.controlla_codice_autenticazione(cod_aut9, lista_dipendenti.get_lista_completa())
        risp15 = controlli.controlla_codice_autenticazione(cod_aut15, lista_dipendenti.get_lista_completa())
        self.assertEqual(risp0, False, "Dovrebbe essere non valido")
        self.assertEqual(risp1, False, "Dovrebbe essere non valido")
        self.assertEqual(risp7, False, "Dovrebbe essere non valido")
        self.assertEqual(risp8, True, "Dovrebbe essere non valido")
        self.assertEqual(risp9, False, "Dovrebbe essere non valido")
        self.assertEqual(risp15, False, "Dovrebbe essere non valido")

    # test che controlla che venga generato il giusto errore se il nome inserito non è valido
    def test_risposta_errore_nome(self):
        lista_dipendenti = ControlloreListaDipendenti()
        dipendente = Dipendente(nome="uSW5icTupr49uFK3S6nT9ajrundqrHPxDdZW", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        self.assertEqual(lista_dipendenti.controlla_campi_dipendente(dipendente), "Il nome inserito non è valido")

    # test che controlla che venga generato il giusto errore se il cognome inserito non è valido
    def test_risposta_errore_cognome(self):
        lista_dipendenti = ControlloreListaDipendenti()
        dipendente = Dipendente(nome="Mario", cognome="", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        self.assertEqual(lista_dipendenti.controlla_campi_dipendente(dipendente), "Il cognome inserito non è valido")

    # test che controlla che venga generato il giusto errore se il codice fiscale inserito non è valido
    def test_risposta_errore_cod_fisc(self):
        lista_dipendenti = ControlloreListaDipendenti()
        dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDFGH12345678", telefono="3214346521", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        self.assertEqual(lista_dipendenti.controlla_campi_dipendente(dipendente), "Il codice fiscale inserito non è valido")

    # test che controlla che venga generato il giusto errore se il telefono inserito non è valido
    def test_risposta_errore_telefono(self):
        lista_dipendenti = ControlloreListaDipendenti()
        dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="23422342424241357943", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        self.assertEqual(lista_dipendenti.controlla_campi_dipendente(dipendente), "Il numero di telefono inserito non è valido")

    # test che controlla che venga generato il giusto errore se l'email inserito non è valido
    def test_risposta_errore_email(self):
        lista_dipendenti = ControlloreListaDipendenti()
        dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        self.assertEqual(lista_dipendenti.controlla_campi_dipendente(dipendente), "L'indirizzo email inserito non è valido")

    # test che controlla che venga generato il giusto errore se il codice d'accesso inserito non è valido
    def test_risposta_errore_cod_accesso(self):
        lista_dipendenti = ControlloreListaDipendenti()
        dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="mario.rossi@gmail.com",
                                     area_comp="Biglietteria", codice_autent="AFD56")
        self.assertEqual(lista_dipendenti.controlla_campi_dipendente(dipendente), "Il codice per la futura autenticazione inserito non è valido")

    # test che controlla l'inserimento di nome e cognome del dipendente per la ricerca sia valido.
    def test_controlla_campi_ricerca_dipendente(self):
        lista_dipendenti = ControlloreListaDipendenti()
        r1 = lista_dipendenti.controlla_campi_ricerca("", "")
        r2 = lista_dipendenti.controlla_campi_ricerca("Mario", "Rossi")
        r3 = lista_dipendenti.controlla_campi_ricerca("Mariantonietta", "Spadoni")
        r4 = lista_dipendenti.controlla_campi_ricerca("Giorgia Maria Vittoria Laura Chiara Luisa", "Giorgia Maria Vittoria Laura Chiara Luisa")
        self.assertEqual(r1, None)
        self.assertEqual(r2, None)
        self.assertEqual(r3, None)
        self.assertNotEqual(r4, None)

        # test sui messaggi di errore
        self.assertEqual(lista_dipendenti.controlla_campi_ricerca("Giorgia Maria Vittoria Laura Chiara Luisa", "Rossi"), "Il nome inserito non è valido")
        self.assertEqual(lista_dipendenti.controlla_campi_ricerca("Fabiola", "Giorgia Maria Vittoria Laura Chiara Luisa"), "Il cognome inserito non è valido")

    # aggiustare
    def test_ricerca_dipendente(self):
        lista_dipendenti = ControlloreListaDipendenti()
        ri1 = lista_dipendenti.get_dipendente_by_nome("Carlo", "Rossi")
        ri2 = lista_dipendenti.get_dipendente_by_nome("", "")
        self.assertIsNotNone(ri1)
        self.assertIsNotNone(ri2)  # Inserimento vuoto ritorna la lista completa dei dipendenti

    # test sull'eliminazione di un dipendente dal sistema
    def test_elimina_dipendente_by_cod_fisc(self):
        controllore_lista_dipendenti = ControlloreListaDipendenti()
        controllore_lista_dipendenti.model.lista_dipendenti = []
        dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        self.assertEqual(dipendente in controllore_lista_dipendenti.get_lista_completa(), False)      # controllo che il dipendente non sia già nella lista
        controllore_lista_dipendenti.aggiungi_dipendente(dipendente)           # aggiungo il dipendente alla lista
        self.assertEqual(dipendente in controllore_lista_dipendenti.get_lista_completa(), True)       # controllo che il dipendente sia presente nella lista
        controllore_lista_dipendenti.elimina_dipendente_by_index(0,controllore_lista_dipendenti.get_lista_completa())       # elimino il dipendente dalla lista
        self.assertEqual(dipendente in controllore_lista_dipendenti.get_lista_completa(), False)      # controllo che il dipendente sia è stato eliminato dalla lista















