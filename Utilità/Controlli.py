class Controlli():

    #ritorna True se la stringa è valida, cioè se la sua lunghezza è compresa tra 1 e 35 e se contiene solo
    # caratteri alfabetici, altrimenti ritorna false
    @staticmethod
    def controlla_stringa_lettere(stringa):
        s = str(stringa)
        if len(s) < 35:
            return s.isalpha()
        return False

    # ritorna True se il codice fiscale è valido è valida, cioè se la sua lunghezza è 16, contiene solo
    # caratteri alfanumerici e nessun altro elemento della lista passata ne possiede uno uguale
    @staticmethod
    def controlla_cod_fisc(cod_fisc, lista):
        cf = str(cod_fisc)
        if len(cf) == 16 and cf.isalnum():
            for persona in lista:
                if persona.cod_fisc == cf: return False
            return True
        return False

    # ritorna True se il numero di telefono è valido, cioè se la sua lunghezza è compresa tra 1 e 13 e se contiene solo
    # caratteri numerici; altrimenti ritorna false
    @staticmethod
    def controlla_telefono(telefono):
        t = str(telefono)
        if len(t) > 2 and len(t) < 13:
                return t.isdigit()
        return False

    # ritorna True se l'email è valida, cioè se la sua lunghezza è compresa tra 1 e 50 e se contiene solo
    # caratteri stampabili; altrimenti ritorna false
    @staticmethod
    def controlla_stringa_stampabile(stringa):
        s = str(stringa)
        if len(s) > 0 and len(s) < 50:
            return s.isprintable()
        return False

    # ritorna True se il codice per la futura autenticazione è valido è valida, cioè se la sua lunghezza è 8,
    # contiene solo caratteri alfanumerici e nessun altro dipendente ne possiede uno uguale
    @staticmethod
    def controlla_codice_autenticazione(codice_aut, lista_dipendenti):
        c = str(codice_aut)
        if len(c) == 8 and c.isalnum():
            for dipendente in lista_dipendenti:
                if dipendente.codice_autent == c: return False
            return True
        return False

    # ritorna True se il codice per l'abbonamento è valido , cioè se la sua lunghezza è 8,
    # contiene solo caratteri alfanumerici e nessun altro cliente ne possiede uno uguale
    @staticmethod
    def controlla_codice_abb(cod_abbon, lista_clienti):
        c = str(cod_abbon)
        if c == '': return True
        if len(c) == 8 and c.isalnum():
            for cliente in lista_clienti:
                if cliente.cod_abb == c: return False
            return True
        return False

    # ritorna True se il codice per la tessera è valido , cioè se la sua lunghezza è 8,
    # contiene solo caratteri alfanumerici e nessun altro cliente ne possiede uno uguale
    @staticmethod
    def controlla_codice_tess(cod_tessera, lista_clienti):
        c = str(cod_tessera)
        if c == '': return True
        if len(c) == 8 and c.isalnum():
            for cliente in lista_clienti:
                if cliente.cod_tess == c: return False
            return True
        return False

    # metodo statico che controlla se lo spettacolo passato come parametro si sovrappone con altri
    # spettacoli in programma.
    # lista_spettacoli è la lista contenente tutti gli spettacoli in programma
    @staticmethod
    def controlla_sovrapposizione_spettacoli(nuovo_spettacolo, lista_spettacoli):
        for spettacolo in lista_spettacoli:
            if spettacolo.data == nuovo_spettacolo.data and spettacolo.sala.nome == nuovo_spettacolo.sala.nome:
                if nuovo_spettacolo.ora_inizio < spettacolo.ora_inizio and nuovo_spettacolo.ora_fine >= spettacolo.ora_inizio:
                    return False
                if nuovo_spettacolo.ora_inizio > spettacolo.ora_inizio and nuovo_spettacolo.ora_inizio <= spettacolo.ora_fine:
                    return False
                if nuovo_spettacolo.ora_inizio == spettacolo.ora_inizio:
                    return False
        return True



