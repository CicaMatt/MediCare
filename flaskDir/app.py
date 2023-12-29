from flask import Flask, render_template

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='6Js.9JsPaq324Dc', #Serve per avere le sessioni, una chiave sicura, non dovrebbe essere caricata su github
    SAML_IDP_SETTINGS={ #Per lo spid, ad esempio devo identificare Posteitaliane


    }
)


@app.route('/')
def home():
    return render_template("HomePage.html")


@app.route('/login')
def login():
    return render_template("Login.html")


@app.route('/registrazione')
def registrazione():
    return render_template("Registrazione.html")


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


if __name__ == '__main__':
    app.run()
