class EnteSanitario():
    def __init__(self,nome,email,password):
        self.__nome=nome
        self.__email=email
        self.__password=password
        self.__reparti=list()

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    def getReparti(self):
        return self.__reparti

    def setNome(self,nome):
        self.__nome=nome

    def setEmail(self,email):
        self.__email=email

    def setPassword(self,password):
        self.__password=password

    def setReparti(self,listaReparti):
        self.__reparti=listaReparti