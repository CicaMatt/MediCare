from flask import Blueprint, render_template, session, request, jsonify
from flask_login import current_user, login_required


from flaskDir.source.Farmaci.FarmaciService import FarmaciService
from flaskDir.source.Pagamento.PagamentoService import PagamentoService

impostazioni_blueprint = Blueprint('impostazioni', __name__)


@impostazioni_blueprint.route('/pagamento',methods=['GET','POST'])
@login_required
def getMetodi():
    return render_template("Impostazioni.html",lista= PagamentoService.getMetodi(current_user.CF).all())


