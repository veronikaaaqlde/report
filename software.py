class Software:
    def __init__(self, ID_Software, naimenovanie, haracteristica, data_vipuska, stoim):
        self.ID_Software = ID_Software
        self.naimenovanie = naimenovanie
        self.haracteristica = haracteristica
        self.data_vipuska = data_vipuska
        self.stoim = stoim

    def __str__(self):
        return f"{self.ID_Software}, {self.naimenovanie}, {self.haracteristica}, {self.data_vipuska}, {self.stoim}"
