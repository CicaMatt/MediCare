from flaskDir import test

class MetodoPagamento(test.Model):
    CVV = test.Column(test.Integer, nullable=False)
    PAN = test.Column(test.String(16), nullable=False, primary_key=True)
    nome_titolare = test.Column(test.String(255), nullable=False)
    dataScadenza = test.Column(test.String(7), nullable=False)
    beneficiario = test.Column(test.String(16), test.ForeignKey('paziente.CF'), nullable=False, primary_key=True)
