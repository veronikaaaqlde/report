class Client:
    def __init__(self, ID_client, fio, data_rozh, pol, pasport, email, phone):
        self.ID_client = ID_client
        self.fio = fio
        self.data_rozh = data_rozh
        self.pol = pol
        self.pasport = pasport
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.ID_client}, {self.fio}, {self.data_rozh}, {self.pol}, {self.pasport}, {self.email}, {self.phone}"
