from flask import Blueprint, request, render_template
from flaskDir.source.EnteFunction.EnteService import EnteService

ente_blueprint = Blueprint('ente', __name__)


@ente_blueprint.route('/creaReparto', methods=['POST'])
def creaReparto():
    """
    Gestisce la creazione di un nuovo reparto medico da parte di un ente sanitario.

    Returns:
        render_template: La pagina dell'area ente dopo la creazione del reparto.
    """
    if request.method == 'POST':
        nome = request.form.get('reparto')
        email = request.form.get('email')
        password = request.form.get('password')
        specializzazione = request.form.get('specializzazione')
        citta = request.form.get('citta')
        ente = request.form.get('ente')
        EnteService.creaReparto(nome, email, password, specializzazione, citta, ente)
        return render_template('AreaEnte.html')


@ente_blueprint.route('/deleteReparto', methods=['GET'])
def deleteReparto():
    """
    Gestisce l'eliminazione di un reparto medico da parte di un ente sanitario.

    Returns:
        render_template: La pagina dell'area ente dopo l'eliminazione del reparto.
    """
    if request.method == 'GET':
        email = request.args.get('email')
        EnteService.deleteReparto(email)
        return render_template('AreaEnte.html')
