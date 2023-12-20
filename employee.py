class Employee:
    def __init__(self, ID_employee, fio, data_rozh, pol, pasport, email, phone):
        self.ID_employee = ID_employee
        self.fio = fio
        self.data_rozh = data_rozh
        self.pol = pol
        self.pasport = pasport
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.ID_employee}, {self.fio}, {self.data_rozh}, {self.pol}, {self.pasport}, {self.email}, {self.phone}"
