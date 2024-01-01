from flask import Blueprint, request
from flaskDir.source.autenticazione import AutenticazioneService

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login_page():
    return AutenticazioneService.login_page(request)


@auth_blueprint.route('/loginENTE', methods=['GET', 'POST'])
def loginEnte_page():
    return AutenticazioneService.loginEnte_page(request)


@auth_blueprint.route('/registrazione', methods=['GET', 'POST'])
def registrazione_pageMedico():
    return AutenticazioneService.registrazione_pageMedico(request)




@auth_blueprint.route('/registrazione/ente', methods=['GET','POST'])
def registrazioneEnte():
    return AutenticazioneService.registrazioneEnte(request)


@auth_blueprint.route('/logout')
def logout():
    return AutenticazioneService.logout()
