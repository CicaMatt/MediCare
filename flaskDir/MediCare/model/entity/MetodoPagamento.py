class MetodoPagamento:
    def __init__(self,CVV,PAN,titolare,beneficiario, scadenza):
        self.CVV=CVV
        self.PAN=PAN
        self.titolare=titolare
        self.beneficiario=beneficiario
        self.data_scadenza=scadenza
