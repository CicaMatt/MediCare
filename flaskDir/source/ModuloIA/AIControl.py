from flask import render_template, Blueprint, request, session, url_for, redirect
from flask_login import login_required, current_user

from flaskDir.source.Utente.FascicoloService import FascicoloService
from flaskDir.source.ModuloIA.AIService import ModuloIAService
from flaskDir.source.Utente.PazienteService import PazienteService

feature_blueprint = Blueprint('feature', __name__)


@feature_blueprint.route('/moduloai', )
def moduloai():
    return render_template("ModuloAI.html")


@feature_blueprint.route('/moduloai/risultati', methods=['GET', 'POST'])
@login_required
def results():
    if request.method == "POST" and session.get('user_role') == "paziente":
        age = int(request.form.get("age"))
        sex = int(request.form.get("sex"))
        cp = int(request.form.get("cp"))
        trtbps = int(request.form.get("trtbps"))
        chol = int(request.form.get("chol"))
        fbs = int(request.form.get("fbs"))
        restecg = int(request.form.get("restecg"))
        thalach = int(request.form.get("thalach"))
        exng = int(request.form.get("exng"))
        oldpeak = int(request.form.get("oldpeak"))
        slp = int(request.form.get("slp"))
        caa = int(request.form.get("caa"))
        thall = int(request.form.get("thall"))

        if slp is None or caa is None or thall is None:
            result = ModuloIAService.diagnosi_simple(age, sex, cp, trtbps, chol, fbs, restecg, thalach, exng, oldpeak)
            if str(result) == "[0]":
                result = "Sei fortunato! Non c'è il sospetto che tu abbia una malattia cardiaca"
            else:
                result = "Abbiamo notato dai tuoi dati una predisposizione maggiore verso il rischio di infarto. Prenditi cura della tua salute. Chiedi al tuo medico di fiducia la terapia migliore per le tue esigenze."
        else:
            result = ModuloIAService.diagnosi_accurata(age, sex, cp, trtbps, chol, fbs, restecg, thalach, exng, oldpeak,
                                                       slp, caa, thall)
            if str(result) == "[0]":
                result = "Sei fortunato! Non c'è il sospetto che tu abbia una malattia cardiaca"
            else:
                result = "Abbiamo notato dai tuoi dati una predisposizione maggiore verso il rischio di infarto. Prenditi cura della tua salute. Chiedi al tuo medico di fiducia la terapia migliore per le tue esigenze."

        FascicoloService.addDocumento("Risultati AI: malattia cardiaca", result, None, current_user.CF)
        return redirect(url_for("feature.results"))
        # return ...

    documentoResult = PazienteService.getmoduloAIresult(current_user)
    if documentoResult is None:
        return render_template('FormAI.html', paziente=request.args.get('paziente'))
    else:
        return render_template('RisultatiAI2.html', risultato=documentoResult)
