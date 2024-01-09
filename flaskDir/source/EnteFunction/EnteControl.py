from flask import Blueprint, request, render_template
from flaskDir.source.EnteFunction.EnteService import EnteService

ente_blueprint=Blueprint('ente',__name__)

@ente_blueprint.route('/creaReparto', methods=['POST'])
def creaReparto():
    if request.method == 'POST':
        nome=request.form.get('reparto')
        email=request.form.get('email')
        password=request.form.get('password')
        specializzazione=request.form.get('specializzazione')
        citta=request.form.get('citta')
        ente=request.form.get('ente')
        EnteService.creaReparto(nome,email,password,specializzazione, citta,ente)
        return render_template('AreaEnte.html')