from flaskDir import test

class VisualizzaFarmaco(test.Model):
    Farmaco = test.Column(test.Integer, test.ForeignKey('farmaco.ID'), primary_key=True)
    Paziente = test.Column(test.String(16), test.ForeignKey('paziente.CF'), primary_key=True)