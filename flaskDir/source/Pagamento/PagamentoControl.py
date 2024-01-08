from flask import Blueprint, render_template, session, request, jsonify
from flask_login import current_user, login_required


from flaskDir.source.Farmaci.FarmaciService import FarmaciService
from flaskDir.source.Pagamento.PagamentoService import PagamentoService

informazionipersonali_blueprint = Blueprint('informazionipersonali', __name__)




@informazionipersonali_blueprint.route('/pagamento', methods=['GET','POST'])
@login_required
def getMetodi():
    da_elimare = request.args.get('pan')
    if da_elimare is not None:
        PagamentoService.eliminaMetodo(da_elimare)
    return render_template("InformazioniPersonali.html", lista= PagamentoService.getMetodi(current_user.CF).all())