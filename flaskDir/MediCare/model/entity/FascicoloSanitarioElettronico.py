class FascicoloSanitario():
    """
    La classe FascicoloSanitario rappresenta un fascicolo sanitario associato a un paziente.

    Attributi:
    - id (int): Identificatore univoco del fascicolo sanitario.
    - paziente: Paziente associato al fascicolo sanitario.
    - documents (list): Lista dei documenti sanitari presenti nel fascicolo.

    Metodi:
    - __init__(self, paziente, documenti): Costruttore della classe. Inizializza un nuovo oggetto FascicoloSanitario.

    Attributi di Classe:
    - id (int): Contatore per generare identificatori univoci per i fascicoli sanitari.

    """
    id=1
    def __init__(self,paziente,documenti):
        """
        Costruttore della classe FascicoloSanitario.

        Parametri:
        - paziente: Paziente associato al fascicolo sanitario.
        - documenti (list): Lista dei documenti sanitari presenti nel fascicolo.

        """
        self.paziente = paziente
        self.documents=documenti
        self.id=FascicoloSanitario.id
        FascicoloSanitario.id+=1

