from flask import render_template, Blueprint, request, session
from flask_login import login_required, current_user

from flaskDir import app
from flaskDir.source.prenotazioni.services import PazienteService

feature_blueprint = Blueprint('feature', __name__)


@feature_blueprint.route('/moduloai',)
def moduloai():
    return render_template("ModuloAI.html")




@feature_blueprint.route('/moduloai/risultati', methods=['GET','POST'])
@login_required
def results():
    if request.method =='post' and session.get('user_role')=="medico":
        age = request.form.get("age")
        sex = request.form.get("sex")
        cp = request.form.get("cp")
        trtbps = request.form.get("trtbps")
        chol = request.form.get("chol")
        fbs = request.form.get("fbs")
        restecg = request.form.get("restecg")
        thalach = request.form.get("thalach")
        exng = request.form.get("exng")
        oldpeak = request.form.get("oldpeak")
        slp = request.form.get("slp")
        caa = request.form.get("caa")
        thall = request.form.get("thall")
        cf= request.form.get("cf")
        #Allena il modello
        PazienteService.addDocumentoSanitario("Risultati AI: malattia cardiaca", "<descrizione:risultato del modello>", cf, current_user)
        #return ...


    documentoResult = PazienteService.getmoduloAIresult(current_user)
    return  render_template('RisultatiAI.html', paziente=request.args.get('paziente'))

