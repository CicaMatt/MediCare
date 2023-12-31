from flask import Blueprint, request
from flaskDir.source.autenticazione import AutenticazioneService

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login_page():
    return AutenticazioneService.login_page(request)


@auth_blueprint.route('/loginente', methods=['GET', 'POST'])
def loginEnte_page():
    return AutenticazioneService.loginEnte_page(request)


@auth_blueprint.route('/registrazioneMedico', methods=['GET', 'POST'])
def registrazioneMedico():
    return AutenticazioneService.registrazione_pageMedico(request)


@auth_blueprint.route('/registrazionePaziente', methods=['GET','POST'])
def registrazionePaziente():
    return AutenticazioneService.registrazionePaziente(request)

@auth_blueprint.route('/registrazione/ente', methods=['GET','POST'])
def registrazioneEnte():
    return AutenticazioneService.registrazioneEnte(request)


@auth_blueprint.route('/logout')
def logout():
    return AutenticazioneService.logout()
