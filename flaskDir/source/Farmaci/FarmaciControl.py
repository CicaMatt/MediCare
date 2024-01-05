from flask import Blueprint, render_template, session, request
from flask_login import current_user, login_required

from flaskDir.source.prenotazioni.services import FarmaciService

farmacia_blueprint = Blueprint('farmacia', __name__)


@farmacia_blueprint.route('/farmaci')
#@login_required
def farmaci():
    return render_template("Farmaci.html",lista= FarmaciService.getFarmaci())