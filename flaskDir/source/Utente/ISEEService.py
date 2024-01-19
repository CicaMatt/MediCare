from flaskDir import db
from flaskDir.MediCare.model.entity.Paziente import Paziente


class ISEEService:

    @classmethod
    def changeISEE(cls, cf, newIsee):
        """
        Modifica l'ISEE di un paziente.

        Args:
        cf (str): Codice fiscale del paziente.
        newIsee (float): Nuovo valore dell'ISEE.

        Returns:
        None
        """
        paziente = Paziente.query.filter_by(CF=cf).first()

        newIsee_float = float(newIsee)

        if newIsee_float < 0:
            return False

        if paziente:
            paziente.ISEE_ordinario = newIsee
            db.session.commit()
