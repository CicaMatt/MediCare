import pytest
import sqlalchemy

from flaskDir import app, db
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario
from flaskDir.MediCare.model.entity.Medici import Medico
from flaskDir.MediCare.model.entity.Paziente import Paziente
from flaskDir.MediCare.model.entity.Prenotazione import Prenotazione
from flaskDir.source.prenotazioni.services import PrenotazioneService, PazienteService, MedicoService



