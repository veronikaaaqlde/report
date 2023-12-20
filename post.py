class Post:
    def __init__(self, ID_Post, ID_employee, dolzhnnost, ZP, stazh, Obrazov):
        self.ID_Post = ID_Post
        self.ID_employee = ID_employee
        self.dolzhnnost = dolzhnnost
        self.ZP = ZP
        self.stazh = stazh
        self.Obrazov = Obrazov

    def __str__(self):
        return f"{self.ID_Post}, {self.ID_employee}, {self.dolzhnnost}, {self.ZP}, {self.stazh}, {self.Obrazov}"
