from flaskDir import db


class MetodoPagamento(db.Model):
    """
    Classe che rappresenta un metodo di pagamento.

    Attributi:
    - CVV (int): Valore di verifica della carta.
    - PAN (str): Numero primario del conto (numero della carta di credito, chiave primaria).
    - nome_titolare (str): Nome del titolare della carta.
    - dataScadenza (str): Data di scadenza della carta (formato: MM/YY).
    - beneficiario (str): CF (Codice Fiscale) del beneficiario (chiave esterna).

    """
    CVV = db.Column(db.Integer, nullable=False)
    PAN = db.Column(db.String(16), nullable=False, primary_key=True)
    nome_titolare = db.Column(db.String(255), nullable=False)
    dataScadenza = db.Column(db.String(7), nullable=False)
    beneficiario = db.Column(db.String(16), db.ForeignKey('paziente.CF'), nullable=False, primary_key=True)
