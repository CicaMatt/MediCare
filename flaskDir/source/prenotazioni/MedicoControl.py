from flask import Blueprint, render_template, session, request, jsonify
from flask_login import current_user, login_required

from flaskDir.source.prenotazioni.MedicoService import MedicoService

medico_blueprint = Blueprint('medico', __name__)



@medico_blueprint.route('/medico')
#@login_required
def getListaPazienti():
    dottore=request.args.get('dottore')
    return render_template("ListaPazienti.html",lista= MedicoService.getPazienti(dottore))

