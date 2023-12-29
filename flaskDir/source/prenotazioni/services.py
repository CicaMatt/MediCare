from flaskDir.MediCare.model.entity.DocumentoSanitario import DocumentoSanitario
from flaskDir.MediCare.model.entity.Medici import Medico


class MedicoService:
    """

    """
    #Invece di fare operazioni di input output ad ogni richiesta, memorizzo listamedici
    _listaMedici = None


    @classmethod
    def getListaMedici(cls):
        if cls._listaMedici is None:
            cls._listaMedici = Medico.query.getAll()
        return cls._listaMedici

    def filtraMedici(cls, specializzazione = None, citta = None):
        cls._listaMedici = cls.getListaMedici()

        if specializzazione is None and citta is None:
            return cls._listaMedici

        newList = []
        if specializzazione is not None and citta is not None:
            newList = [medico for medico in cls._listaMedici if medico.città == citta and specializzazione == specializzazione]

        elif citta is not None:
            newList = [medico for medico in cls._listaMedici if medico.città == citta]

        elif specializzazione is not None:
            newList = [medico for medico in cls._listaMedici if medico.specializzazione == specializzazione]

        return newList

    def filtraMediciv2(cls, specializzazione = None, citta = None):
        cls._listaMedici = cls.getListaMedici()

        if specializzazione is None and citta is None:
            return cls._listaMedici

        listaFiltrata = []
        condizioniDaVerificare = []

        if specializzazione is not None:
            condizioniDaVerificare.append(lambda medico: medico.specializzazione == specializzazione)
        if citta is not None:
            condizioniDaVerificare.append(lambda medico: medico.città == citta)

        listaFiltrata = [medico for medico in cls._listaMedici if all(condition(medico) for condition in condizioniDaVerificare)]

        return listaFiltrata






    @classmethod
    def addMedico(cls, medico):
        cls._listaMedici = cls.getListaMedici()
        cls._listaMedici.append(medico)
        Medico.query.add(medico) #add??

class UserService:

    @classmethod
    def getListaVaccini(cls, user):
        return DocumentoSanitario.query.filter_by(titolare=user.CF, tipo="vaccino")


class PrenotazioneService:

    @classmethod
    def getListaMedici(cls,specializzazione = None, citta= None):
        return MedicoService.getListaMedici(specializzazione,citta)
    @classmethod
    def getListaVaccini(cls,user):
        return UserService.getListaVaccini(user)













