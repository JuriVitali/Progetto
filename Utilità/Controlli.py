class Controlli():
    eta_minima = ["Adatto a tutti", "Sconsigliato ai minori di 6 anni", "Vietato ai minori di 14 anni",
                  "Vietato ai minori di 18 anni"]
    aree_di_competenza = ["Biglietteria", "Bar", "Pulizie"]

    #ritorna True se la stringa è valida, cioè se la sua lunghezza è compresa tra 1 e 35 e se contiene solo
    # caratteri alfabetici, altrimenti ritorna false
    @staticmethod
    def controlla_stringa_lettere(stringa):
        if len(stringa) > 1 and len(stringa) < 35:
            return stringa.isaplha()
        return False

    # ritorna True se il codice fiscale è valido è valida, cioè se la sua lunghezza è 16, contiene solo
    # caratteri alfanumerici e nessun altro elemento della lista passata ne possiede uno uguale
    @staticmethod
    def controlla_cod_fisc(cod_fisc, lista):
        if len(cod_fisc) == 16 and cod_fisc.isalnum():
            for persona in lista:
                if persona.cod_fisc == cod_fisc: return False
            return True
        return False

    # ritorna True se il numero di telefono è valido, cioè se la sua lunghezza è compresa tra 1 e 13 e se contiene solo
    # caratteri numerici; altrimenti ritorna false
    @staticmethod
    def controlla_telefono(telefono):
        if len(telefono) > 1 and len(telefono) < 13:
                return telefono.isdigit()
        return False

    # ritorna True se l'email è valida, cioè se la sua lunghezza è compresa tra 1 e 50 e se contiene solo
    # caratteri stampabili; altrimenti ritorna false
    @staticmethod
    def controlla_strina_stampabile(stringa):
        if len(stringa) > 1 and len(stringa) < 50:
            return stringa.isprintable()
        return False

    # ritorna True se il codice per la futura autenticazione è valido è valida, cioè se la sua lunghezza è 8,
    # contiene solo caratteri alfanumerici e nessun altro dipendente ne possiede uno uguale
    @staticmethod
    def controlla_codice_autenticazione(codice_aut, lista_dipendenti):
        if len(codice_aut) == 8 and codice_aut.isalnum():
            for dipendente in lista_dipendenti:
                if dipendente.codice_autent == codice_aut: return False
            return True
        return False




