from unittest import TestCase

from GestioneDipendenti.Models.Dipendente import Dipendente
from GestioneDipendenti.Controllers.ControlloreListaDipendenti import ControlloreListaDipendenti
from GestioneDipendenti.Models.ListaDipendenti import ListaDipendenti
from GestioneDipendenti.Views.VistaRegistraDipendente import VistaRegistraDipendente
from Utilità.Controlli import Controlli


class TestControlloreListaDipendenti(TestCase):

    def test_aggiungi_dipendente(self):
        self.lista_dipendenti = ControlloreListaDipendenti()
        self.dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        self.dipendente2 = Dipendente(nome="Kevin", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        #self.lista_dipendenti.aggiungi_dipendente(self.dipendente)
        #self.model.aggiungi_dipendente(self.dipendente)
        self.lista_dipendenti.aggiungi_dipendente(self.dipendente)
        self.lista_dipendenti.aggiungi_dipendente(self.dipendente2)
        self.lista_dipendenti.controlla_campi_dipendente(self.dipendente)
        self.lista_dipendenti.controlla_campi_dipendente(self.dipendente2)
        self.assertEqual(self.dipendenti_in_lista(self.dipendente2), True)


    # test che controlla che i campi del dipendente inserito siano validi. Test eseguito con dipendente valido
    def test_controlla_campi_dipendente(self):
        self.controlli = Controlli()
        self.lista_dipendenti = ControlloreListaDipendenti()
        self.dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="FREA245W")
        self.assertEqual(self.lista_dipendenti.controlla_campi_dipendente(self.dipendente), None)
        self.assertEqual(self.controlli.controlla_codice_autenticazione(self.dipendente.codice_autent, self.lista_dipendenti.get_lista_completa()), True)
        self.assertEqual(self.controlli.controlla_cod_fisc(self.dipendente.cod_fisc, self.lista_dipendenti.get_lista_completa()), True)
        self.assertEqual(self.controlli.controlla_telefono(self.dipendente.telefono), True)
        self.assertEqual(self.controlli.controlla_stringa_stampabile(self.dipendente.email), True)

    # test che controlla che i campi del dipendente inserito siano validi. Test eseguito con dipendente valido
    def test_controlla_campi_dipendente2(self):
        self.controlli = Controlli()
        self.lista_dipendenti = ListaDipendenti()
        self.model = ControlloreListaDipendenti()
        self.dipendente = Dipendente(nome="Giorgio", cognome="Mancini", data_nascita="1994.07.09",
                                     cod_fisc="ABCDEFGH1345678", telefono="", email="",
                                     area_comp="Biglietteria", codice_autent="FR45W")
        self.assertNotEqual(self.model.controlla_campi_dipendente(self.dipendente), None)
        self.assertEqual(self.controlli.controlla_codice_autenticazione(self.dipendente.codice_autent, self.model.get_lista_completa()), False)
        self.assertEqual(self.controlli.controlla_cod_fisc(self.dipendente.cod_fisc, self.model.get_lista_completa()), False)
        self.assertEqual(self.controlli.controlla_telefono(self.dipendente.telefono), False)
        self.assertEqual(self.controlli.controlla_stringa_stampabile(self.dipendente.email), False)


    # test che controlla che l'inserimento di una stringa compresa tra 1 e 50 caratteri ritorni True
    def test_controlla_stringa_stampabile1(self):
        self.controlli = Controlli()
        self.stringa = "email@test.com"
        self.str49= "HdB10SIBwupXKbihPUpcid1blAqwhOFLT6os0Wamy6Ys4FvFL"
        self.str1 = "A"
        self.risp = self.controlli.controlla_stringa_stampabile(self.stringa)
        self.risp49 = self.controlli.controlla_stringa_stampabile(self.str49)
        self.risp1 = self.controlli.controlla_stringa_stampabile(self.str1)
        self.assertEqual(self.risp , True , "Non valido")
        self.assertEqual(self.risp49, True, "Non valido")
        self.assertEqual(self.risp1, True, "Non valido")


    # test che controlla che l'inserimento di una stringa vuota o superiore a 49 caratteri ritorni False
    def test_controlla_stringa_stampabile2(self):
        self.controlli = Controlli()
        self.stringa = ""
        self.str50 = "GKJcZW0fGTVws99h7TkXTVZuRrTqiUzVK8IRUisiLVWgiicwzb"
        self.str51 = "90VTpbipnhbS5zcs5uIpWQ88Payc7o5pDKoyOMHRQK97dTgyjRA"
        self.str70 = "91fG6lWKC1vGS7oRx6ERqqx3kpBGa74BJjfRRW2DdbuP9w8W7H1vLWCSIeajZxh5jiTjzP"
        self.risp = self.controlli.controlla_stringa_stampabile(self.stringa)
        self.risp50 = self.controlli.controlla_stringa_stampabile(self.str50)
        self.risp51 = self.controlli.controlla_stringa_stampabile(self.str51)
        self.risp70 = self.controlli.controlla_stringa_stampabile(self.str70)
        self.assertEqual(self.risp, False)
        self.assertEqual(self.risp50, False)
        self.assertEqual(self.risp51, False)
        self.assertEqual(self.risp70, False)

    # test che controlla che l'inserimento di un numero di telefono compreso tra 2 e 13 esclusi sia valido. Ritorna True se il numero è valido, altrimenti ritorna False
    def test_controlla_telefono(self):
        self.controlli = Controlli()
        self.tel3 = "123"
        self.tel10 = "3216751378"
        self.tel12 = "374555327778"
        self.risp3 = self.controlli.controlla_telefono(self.tel3)
        self.risp10 = self.controlli.controlla_telefono(self.tel10)
        self.risp12 = self.controlli.controlla_telefono(self.tel12)
        self.assertEqual(self.risp3, True)
        self.assertEqual(self.risp10, True)
        self.assertEqual(self.risp12, True)

        # test su numeri non validi
        self.tel_alf_num = "a53fsf94"
        self.tel_neg = "-344433"
        self.tel0 = ""
        self.tel1 = "1"
        self.tel2 = "12"
        self.tel13 = "2342234242424"
        self.tel20 = "23422342424241357943"
        self.risp_alf_num = self.controlli.controlla_telefono(self.tel_alf_num)
        self.risp_neg = self.controlli.controlla_telefono(self.tel_neg)
        self.risp0 = self.controlli.controlla_telefono(self.tel0)
        self.risp1 = self.controlli.controlla_telefono(self.tel1)
        self.risp2 = self.controlli.controlla_telefono(self.tel2)
        self.risp13 = self.controlli.controlla_telefono(self.tel13)
        self.risp20 = self.controlli.controlla_telefono(self.tel20)
        self.assertEqual(self.risp_alf_num, False)
        self.assertEqual(self.risp_neg, False)
        self.assertEqual(self.risp0, False)
        self.assertEqual(self.risp1, False)
        self.assertEqual(self.risp2, False)
        self.assertEqual(self.risp13, False)
        self.assertEqual(self.risp20, False)

    # test che controlla che l'inserimento di una stringa alfanumerico compreso tra 1 e 35 sia valido. Ritorna True se la stringa è valida, altrimenti ritorna False
    def test_controlla_stringa_lettere(self):
        self.controlli = Controlli()
        self.stringa = ""
        self.str1 = "A"
        self.str34 = "Umy6I8yR4oPXRxp7ENjCyvgRJtpwMA9vvV"
        self.str35 = "xC3WmigP3HBppBSa2Z9KQnc1lxbl5GXHUx6"
        self.str36 = "uSW5icTupr49uFK3S6nT9ajrundqrHPxDdZW"
        self.str50 = "GKJcZW0fGTVws99h7TkXTVZuRrTqiUzVK8IRUisiLVWgiicwzb"
        self.risp = self.controlli.controlla_stringa_stampabile(self.stringa)
        self.risp1 = self.controlli.controlla_stringa_stampabile(self.str1)
        self.risp34 = self.controlli.controlla_stringa_stampabile(self.str34)
        self.risp35 = self.controlli.controlla_stringa_stampabile(self.str35)
        self.risp36 = self.controlli.controlla_stringa_lettere(self.str36)
        self.risp50 = self.controlli.controlla_stringa_stampabile(self.str50)
        self.assertEqual(self.risp, False, "Dovrebbe essere non valido")
        self.assertEqual(self.risp1, True, "Dovrebbe essere valido")
        self.assertEqual(self.risp34, True, "Dovrebbe essere valido")
        self.assertEqual(self.risp35, True, "Dovrebbe essere valido")
        self.assertEqual(self.risp36, False, "Dovrebbe essere non valido")
        self.assertEqual(self.risp50, False, "Dovrebbe essere non valido")

    # test che controlla che l'inserimento di un codice fiscale sia valido. Ritorna True se il codice fiscale ha 16 caratteri, altrimenti ritorna False
    def test_controlla_cod_fisc(self):
        self.controlli =Controlli()
        self.lista_dipendenti = ControlloreListaDipendenti()
        self.cod_fisc0 = ""
        self.cod_fisc1 = "S"
        self.cod_fisc6 = "7RP22R"
        self.cod_fisc15 = "6KXCHO12ONP0A4G"
        self.cod_fisc16 = "8EVGUXC5M8VXL35N"
        self.cod_fisc17 = "B5JQBT3YLLCAX0EFM"
        self.cod_fisc30 = "U1C6NH9ED6JZQHMMBZYVSL8QSRX3UT"
        self.risp0 = self.controlli.controlla_cod_fisc(self.cod_fisc0, self.lista_dipendenti.get_lista_completa())
        self.risp1 = self.controlli.controlla_cod_fisc(self.cod_fisc1, self.lista_dipendenti.get_lista_completa())
        self.risp6 = self.controlli.controlla_cod_fisc(self.cod_fisc6, self.lista_dipendenti.get_lista_completa())
        self.risp15 = self.controlli.controlla_cod_fisc(self.cod_fisc15, self.lista_dipendenti.get_lista_completa())
        self.risp16 = self.controlli.controlla_cod_fisc(self.cod_fisc16, self.lista_dipendenti.get_lista_completa())
        self.risp17 = self.controlli.controlla_cod_fisc(self.cod_fisc17, self.lista_dipendenti.get_lista_completa())
        self.risp30 = self.controlli.controlla_cod_fisc(self.cod_fisc30, self.lista_dipendenti.get_lista_completa())
        self.assertEqual(self.risp0, False, "Dovrebbe essere non valido")
        self.assertEqual(self.risp1, False, "Dovrebbe essere non valido")
        self.assertEqual(self.risp6, False, "Dovrebbe essere non valido")
        self.assertEqual(self.risp15, False, "Dovrebbe essere non valido")
        self.assertEqual(self.risp16, True, "Dovrebbe essere valido")
        self.assertEqual(self.risp17, False, "Dovrebbe essere non valido")
        self.assertEqual(self.risp30, False, "Dovrebbe essere non valido")

    # test che controlla che l'inserimento del codice autentificazione sia valido. Ritorna True se il codice è di 8 caratteri alfanumerici, altrimenti ritorna False
    def test_controlla_codice_autenticazione(self):
        self.controlli = Controlli()
        self.lista_dipendenti = ControlloreListaDipendenti()
        self.cod_aut0 = ""
        self.cod_aut1 = "S"
        self.cod_aut7 = "7Rp22Ra"
        self.cod_aut8 = "S3bvt456"
        self.cod_aut9 = "d4rf3D4g4"
        self.cod_aut15 = "Lrf3c9dCYX3DAKh"
        self.risp0 = self.controlli.controlla_codice_autenticazione(self.cod_aut0, self.lista_dipendenti.get_lista_completa())
        self.risp1 =self.controlli.controlla_codice_autenticazione(self.cod_aut1, self.lista_dipendenti.get_lista_completa())
        self.risp7 = self.controlli.controlla_codice_autenticazione(self.cod_aut7, self.lista_dipendenti.get_lista_completa())
        self.risp8 = self.controlli.controlla_codice_autenticazione(self.cod_aut8, self.lista_dipendenti.get_lista_completa())
        self.risp9 =self.controlli.controlla_codice_autenticazione(self.cod_aut9, self.lista_dipendenti.get_lista_completa())
        self.risp15 =self.controlli.controlla_codice_autenticazione(self.cod_aut15, self.lista_dipendenti.get_lista_completa())
        self.assertEqual(self.risp0, False, "Dovrebbe essere non valido")
        self.assertEqual(self.risp1, False, "Dovrebbe essere non valido")
        self.assertEqual(self.risp7, False, "Dovrebbe essere non valido")
        self.assertEqual(self.risp8, True, "Dovrebbe essere non valido")
        self.assertEqual(self.risp9, False, "Dovrebbe essere non valido")
        self.assertEqual(self.risp15, False, "Dovrebbe essere non valido")

    # test che controlla che venga generato il giusto errore se il nome inserito non è valido
    def test_risposta_errore_nome(self):
        self.lista_dipendenti = ControlloreListaDipendenti()
        self.dipendente = Dipendente(nome="uSW5icTupr49uFK3S6nT9ajrundqrHPxDdZW", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        self.assertEqual(self.lista_dipendenti.controlla_campi_dipendente(self.dipendente), "Il nome inserito non è valido")

    # test che controlla che venga generato il giusto errore se il cognome inserito non è valido
    def test_risposta_errore_cognome(self):
        self.lista_dipendenti = ControlloreListaDipendenti()
        self.dipendente = Dipendente(nome="Mario", cognome="", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        self.assertEqual(self.lista_dipendenti.controlla_campi_dipendente(self.dipendente), "Il cognome inserito non è valido")

    # test che controlla che venga generato il giusto errore se il codice fiscale inserito non è valido
    def test_risposta_errore_cod_fisc(self):
        self.lista_dipendenti = ControlloreListaDipendenti()
        self.dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDFGH12345678", telefono="3214346521", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        self.assertEqual(self.lista_dipendenti.controlla_campi_dipendente(self.dipendente), "Il codice fiscale inserito non è valido")

    # test che controlla che venga generato il giusto errore se il telefono inserito non è valido
    def test_risposta_errore_telefono(self):
        self.lista_dipendenti = ControlloreListaDipendenti()
        self.dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="23422342424241357943", email="test@email.com",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        self.assertEqual(self.lista_dipendenti.controlla_campi_dipendente(self.dipendente), "Il numero di telefono inserito non è valido")

    # test che controlla che venga generato il giusto errore se l'email inserito non è valido
    def test_risposta_errore_email(self):
        self.lista_dipendenti = ControlloreListaDipendenti()
        self.dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="",
                                     area_comp="Biglietteria", codice_autent="AFD56F5V")
        self.assertEqual(self.lista_dipendenti.controlla_campi_dipendente(self.dipendente), "L'indirizzo email inserito non è valido")

    # test che controlla che venga generato il giusto errore se il codice d'accesso inserito non è valido
    def test_risposta_errore_cod_accesso(self):
        self.lista_dipendenti = ControlloreListaDipendenti()
        self.dipendente = Dipendente(nome="Mario", cognome="Rossi", data_nascita="1979.04.06",
                                     cod_fisc="ABCDEFGH12345678", telefono="3214346521", email="mario.rossi@gmail.com",
                                     area_comp="Biglietteria", codice_autent="AFD56")
        self.assertEqual(self.lista_dipendenti.controlla_campi_dipendente(self.dipendente), "Il codice per la futura autenticazione inserito non è valido")

    # test che controlla l'inserimento di nome e cognome del dipendente per la ricerca sia valido.
    def test_controlla_campi_ricerca_dipendente(self):
        self.lista_dipendenti = ControlloreListaDipendenti()
        self.r1 = self.lista_dipendenti.controlla_campi_ricerca("", "")
        self.r2 = self.lista_dipendenti.controlla_campi_ricerca("Mario", "Rossi")
        self.r3 = self.lista_dipendenti.controlla_campi_ricerca("Mariantonietta", "Spadoni")
        self.r4 = self.lista_dipendenti.controlla_campi_ricerca("Giorgia Maria Vittoria Laura Chiara Luisa", "Giorgia Maria Vittoria Laura Chiara Luisa")
        self.assertEqual(self.r1, None)
        self.assertEqual(self.r2, None)
        self.assertEqual(self.r3, None)
        self.assertNotEqual(self.r4, None)

        # test sui messaggi di errore
        self.assertEqual(self.lista_dipendenti.controlla_campi_ricerca("Giorgia Maria Vittoria Laura Chiara Luisa", "Rossi"), "Il nome inserito non è valido")
        self.assertEqual(self.lista_dipendenti.controlla_campi_ricerca("Fabiola", "Giorgia Maria Vittoria Laura Chiara Luisa"), "Il cognome inserito non è valido")



    def dipendenti_in_lista(self, dipendente):
        self.lista_dipendenti = ControlloreListaDipendenti()
        if dipendente in self.lista_dipendenti.get_lista_completa(): return True
        return False












