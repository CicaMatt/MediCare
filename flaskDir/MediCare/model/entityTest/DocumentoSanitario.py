from flaskDir import test

class DocumentoSanitario(test.Model):
    NumeroDocumento = test.Column(test.String(20), nullable=False, primary_key=True)
    tipo = test.Column(test.String(255), nullable=False)
    dataEmissione = test.Column(test.Date, nullable=False)
    descrizione = test.Column(test.Text, nullable=False)
    richiamo= test.Column(test.Date, nullable=True)
    titolare = test.Column(test.String(16), test.ForeignKey('paziente.CF'), nullable=True, primary_key=True)

