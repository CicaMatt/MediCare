from flaskDir import test

class ConsultaFarmaco(test.Model):
    Farmaco = test.Column(test.Integer, test.ForeignKey('farmaco.ID'), primary_key=True)
    Medico = test.Column(test.String(255), test.ForeignKey('medico.email'), primary_key=True)