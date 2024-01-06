from flask import Blueprint, render_template, session, request, jsonify
from flask_login import current_user, login_required


from flaskDir.source.Farmaci.FarmaciService import FarmaciService

farmacia_blueprint = Blueprint('farmacia', __name__)


@farmacia_blueprint.route('/farmaci')
#@login_required
def farmaci():
    return render_template("Farmaci.html",lista= FarmaciService.getFarmaci())

@farmacia_blueprint.route('/dettagliFarmaco', methods=['GET','POST'])
def dettagliFarmaco():
    id=request.args.get('id')
    categoria = request.args.get('categoria')
    return render_template("dettagliFarmaco.html",farmaco=FarmaciService.getDettagliFarmaco(id), suggeriti=FarmaciService.getSuggeriti(categoria,id))

@farmacia_blueprint.route('/filtroCatalogo', methods=['POST'])
def filtroFarmaci():
    if request.method == 'POST':
        categoria = request.form.get('categoria')
        prezzo = float(request.form.get('prezzo'))
        return render_template("Farmaci.html", lista=FarmaciService.filtraCatalogo(categoria, prezzo))

@farmacia_blueprint.route('/ricerca',methods=['POST'])
def ricerca():
    if request.method == 'POST':
        suggerimento=request.form.get('search')
        return jsonify({'result':FarmaciService.ricerca(suggerimento)})

@farmacia_blueprint.route('/ricercaNome', methods=['POST'])
def ricercaNome():
    if request.method == 'POST':
        nome=request.form.get('search')
        return render_template("Farmaci.html", lista=FarmaciService.ricercaNome(nome))