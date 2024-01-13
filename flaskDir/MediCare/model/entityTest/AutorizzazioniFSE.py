from flaskDir import test

class ConsultaFascicolo(test.Model):
    Medico = test.Column(test.String(255), test.ForeignKey('medico.email'), primary_key=True)
    Documento = test.Column(test.String(20), test.ForeignKey('documento_sanitario.NumeroDocumento'), primary_key=True)

