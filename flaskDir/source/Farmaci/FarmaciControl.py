from flask import Blueprint, render_template, request, jsonify

from flaskDir.source.Farmaci.FarmaciService import FarmaciService

farmacia_blueprint = Blueprint('farmacia', __name__)


@farmacia_blueprint.route('/farmaci')
# @login_required
def farmaci():
    """
    Restituisce la pagina del catalogo farmaci.

    Returns:
        render_template: La pagina del catalogo farmaci con la lista dei farmaci.
    """
    return render_template("Farmaci.html", lista=FarmaciService.getFarmaci())


@farmacia_blueprint.route('/dettagliFarmaco', methods=['GET', 'POST'])
def dettagliFarmaco():
    """
    Restituisce la pagina con i dettagli di un farmaco.

    Returns:
        render_template: La pagina con i dettagli del farmaco e suggerimenti correlati.
    """
    id = request.args.get('id')
    categoria = request.args.get('categoria')
    return render_template("dettagliFarmaco.html", farmaco=FarmaciService.getDettagliFarmaco(id),
                           suggeriti=FarmaciService.getSuggeriti(categoria, id))


@farmacia_blueprint.route('/filtroCatalogo', methods=['POST'])
def filtroFarmaci():
    """
    Filtra il catalogo dei farmaci in base alla categoria e al prezzo.

    Returns:
        render_template: La pagina del catalogo farmaci filtrata.
    """
    if request.method == 'POST':
        categoria = request.form.get('categoria')
        prezzo = float(request.form.get('prezzo'))
        return render_template("Farmaci.html", lista=FarmaciService.filtraCatalogo(categoria, prezzo))


@farmacia_blueprint.route('/ricerca', methods=['POST'])
def ricerca():
    """
    Gestisce la ricerca dei farmaci in base a un suggerimento.

    Returns:
        jsonify: Un oggetto JSON contenente i risultati della ricerca.
    """
    if request.method == 'POST':
        suggerimento = request.form.get('search')
        return jsonify({'result': FarmaciService.ricerca(suggerimento)})


@farmacia_blueprint.route('/ricercaNome', methods=['POST'])
def ricercaNome():
    """
    Filtra il catalogo dei farmaci in base al nome.

    Returns:
        render_template: La pagina del catalogo farmaci filtrata per nome.
    """
    if request.method == 'POST':
        nome = request.form.get('search')
        return render_template("Farmaci.html", lista=FarmaciService.ricercaNome(nome))
