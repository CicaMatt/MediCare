from flask import render_template, Blueprint, request
from flask_login import login_required, current_user

from flaskDir import app
from flaskDir.source.prenotazioni.services import PazienteService

feature_blueprint = Blueprint('feature', __name__)


@feature_blueprint.route('/moduloai')
def moduloai():
    return render_template("ModuloAI.html")




@feature_blueprint.route('/moduloai/risultati', methods=['GET','POST'])
@login_required
def results():
    if request.method=='post':
        age = request.args.get("age")
        sex = request.args.get("sex")
        cp = request.args.get("cp")
        trtbps = request.args.get("trtbps")
        chol = request.args.get("chol")
        fbs = request.args.get("fbs")
        restecg = request.args.get("restecg")
        thalach = request.args.get("thalach")
        exng = request.args.get("exng")
        oldpeak = request.args.get("oldpeak")
        slp = request.args.get("slp")
        caa = request.args.get("caa")
        thall = request.args.get("thall")
        #Allena il modello
        #Users

    documentoResult = PazienteService.getmoduloAIresult(current_user)
    return  render_template('RisultatiAI.html', documento=documentoResult)

