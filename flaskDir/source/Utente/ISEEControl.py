from flask import Blueprint, render_template, session, request, jsonify
from flask_login import current_user, login_required


from flaskDir.source.Utente.ISEEService import ISEEService

isee_blueprint = Blueprint('isee', __name__)



@isee_blueprint.route('/isee', methods=['GET','POST'])
@login_required
def modificaISEE():
    """
    Modifica l'ISEE di un paziente.

    Returns:
    str: Pagina HTML delle informazioni personali.
    """
    if request.method == 'POST':
        paziente = request.form.get('cf')
        newISEE = request.form.get('isee')
        if paziente is not None and newISEE is not None:
            ISEEService.changeISEE(paziente,newISEE)
        return render_template("InformazioniPersonali.html")