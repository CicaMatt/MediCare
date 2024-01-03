from flask import render_template

from flaskDir.source.Utente.AreaUtenteControl import areautente_blueprint
from flaskDir.source.prenotazioni.PrenotazioneControl import prenotazione_blueprint
from flaskDir.source.autenticazione .UserControl import auth_blueprint

from flaskDir import app

app.config.from_mapping(
    SECRET_KEY='6Js.9JsPaq324Dc', #Serve per avere le sessioni, una chiave sicura, non dovrebbe essere caricata su github
    SAML_IDP_SETTINGS={ #Per lo spid, ad esempio devo identificare Posteitaliane


    }
)

app.register_blueprint(prenotazione_blueprint, url_prefix='/prenotazione')
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(areautente_blueprint, url_prefix='/areautente')
@app.route('/')
def home():
    return render_template("HomePage.html")




@app.route('/registrazioneutente')
def registrazioneutente():
    return render_template("RegistrazionePaziente.html")




@app.route('/prenotazione')
# @login required and user is paziente
def prenotazione():
    return render_template("Prenotazione.html")


@app.route('/vaccini')
# @login required and user is paziente
def vaccini():
    return render_template("Vaccini.html")


@app.route('/farmaci')
def farmaci():
    return render_template("Farmaci.html")



@app.route('/dettagliFarmaco')
def dettagliFarmaco():
    return render_template("dettagliFarmaco.html")


@app.route('/ente')
def AreaEnte():
    return render_template("AreaEnte.html")


@app.route('/creaMedico', methods=['GET', 'POST'])
# @login_required and user is ente
def CreaMedico():
    return render_template("CreaMedico.html")


@app.route('/areaUtente')
def AreaUtente():
    return render_template('AreaUtente.html')


@app.route('/datiSanitari')
def datiSanitari():
    return render_template("DatiSanitari.html")


@app.route('/areaDiagnostica')
# @login_required and user is ente
def AreaDiagnostica():
    return render_template("AreaDiagnostica.html")


@app.route('/modificaDatiUtente')
def modificaDatiUtente():
    return render_template("ModificaDatiUtente.html")



@app.route('/listamedici')
def listamedici():
    return render_template("ListaMedici.html")

@app.route('/profilomedico')
def profilomedico():
    return render_template("ProfiloMedico.html")

@app.route('/registrazionemedico')
def registrazionemedico():
    return render_template("RegistrazioneMedico.html")

@app.route('/login')
def login():
    return render_template("Login.html")

@app.route('/loginente')
def loginente():
    return render_template("LoginEnte.html")

@app.route('/registraente')
def registraente():
    return render_template("RegistrazioneEnte.html")

@app.route('/chisiamo')
def chisiamo():
    return render_template("ChiSiamo.html")
@app.route('/aqualifunzionalitapossoaccedere')
def aqualifunzionalitapossoaccedere():
    return render_template("AQualiFunzionalitaPossoAccedere.html")

if __name__ == '__main__':
    app.run()