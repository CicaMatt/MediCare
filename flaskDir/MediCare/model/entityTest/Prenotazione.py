from flaskDir import test

class Prenotazione(test.Model):
    ID = test.Column(test.Integer, primary_key=True, autoincrement=True)
    oraVisita = test.Column(test.Integer, nullable=False)
    dataVisita = test.Column(test.Date, nullable=False)
    tipoVisita = test.Column(test.String(255), nullable=False)
    prezzo = test.Column(test.Numeric(precision=6, scale=2), nullable=False)#cambiare salvataggio di una prenotazione nei services
    pazienteCF = test.Column(test.String(16), test.ForeignKey('paziente.CF'), nullable=True, primary_key=True)
    medico = test.Column(test.String(255), test.ForeignKey('medico.email'), nullable=True, primary_key=True)
    pagata=test.Column(test.Boolean, nullable=False, default=False)
