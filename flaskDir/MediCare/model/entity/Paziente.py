class Paziente:
    def __init__(self,CF,SPID,fse,carte,prenotazioni):
        self.__CF = CF
        self.__SPID = SPID
        self.__fascicolo = fse
        self.__carte = carte
        self.__prenotazioni =prenotazioni

    def getCF(self):
        return self.__CF

    def getSPID(self):
        return self.__SPID

    def getFascicolo(self):
        return self.__fascicolo

    def getCarte(self):
        return self.__carte

    def getPrenotazioni(self):
        return self.__prenotazioni


    def setSPID(self,SPID):
        self.__SPID = SPID

    def setFascicolo(self,fse):
        self.__fascicolo=fse

    def setCarte(self,carte):
        self.__carte = carte

    def setPrenotazioni(self,pren):
        self.__prenotazioni = pren


