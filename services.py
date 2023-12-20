class Services:
    def __init__(self, ID_Services, naimenovanie, opisanie, vremia_na_vipoln, stoim):
        self.ID_Services = ID_Services
        self.naimenovanie = naimenovanie
        self.opisanie = opisanie
        self.vremia_na_vipoln = vremia_na_vipoln
        self.stoim = stoim

    def __str__(self):
        return f"{self.ID_Services}, {self.naimenovanie}, {self.opisanie}, {self.vremia_na_vipoln}, {self.stoim}"
