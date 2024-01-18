from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user, login_required

from flaskDir.source.Medico.MedicoService import MedicoService

medico_blueprint = Blueprint('medico', __name__)



@medico_blueprint.route('/medico')
#@login_required
def getListaPazienti():
    dottore=request.args.get('dottore')
    return render_template("ListaPazienti.html", lista= MedicoService.getPazienti(dottore))

@medico_blueprint.route('/eliminamedico',methods=['GET','POST'])
@login_required
def eliminaMedico():
    email = current_user.email
    if email is None:
        return jsonify({"error": "Medico non trovato nella sessione"}), 400

    success = MedicoService.rimuoviMedico(email)

    if success:
        return jsonify({"message": "Paziente eliminato con successo"})
    else:
        return jsonify({"error": "Errore durante l'eliminazione del medico"}), 500