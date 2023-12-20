from client import Client
from employee import Employee
from post import Post
from software import Software
from services import Services

class Orders:

    def __init__(self, ID_orders, ID_software, ID_client, ID_employee, ID_services):
        self.ID_orders = ID_orders
        self.ID_software = ID_software
        self.ID_client = ID_client
        self.ID_employee = ID_employee
        self.ID_services = ID_services
        self.things = []

    def __str__(self):
        return f"{orders.ID_orders}, {orders.ID_software}, {orders.ID_client}, {orders.ID_employee}, {orders.ID_services}"
    def add_client(self, client):
        self.things.append(client)
    def add_employee(self,employee):
        self.things.append(employee)
    def add_post(self, post):
        self.things.append(post)
    def add_software(self, software):
        self.things.append(software)

    def add_services(self, services):
        self.things.append(services)

with open("Orderss.txt", 'r', encoding='utf-8') as orders_file:
    line = orders_file.readline()
    ID_orders, ID_software, ID_client, ID_employee, ID_services = line.split(";")
    orders = Orders(ID_orders, ID_software, ID_client, ID_employee, ID_services)

with open("Clients.txt", 'r', encoding='utf-8') as client_file:
    for line in client_file:
        ID_client, fio, data_rozh, pol, pasport, email, phone = line.split(";")
        ID_client = int(ID_client)
        client = Client(ID_client, fio, data_rozh, pol, pasport, email, phone)
        orders.add_client(client)

with open("Employees.txt", 'r', encoding='utf-8') as employee_file:
    for line in employee_file:
        ID_employee, fio, data_rozh, pol, pasport, email, phone = line.split(";")
        ID_employee = int(ID_employee)
        employee = Employee(ID_employee, fio, data_rozh, pol, pasport, email, phone)
        orders.add_employee(employee)

with open("Posts.txt", 'r', encoding='utf-8') as post_file:
    for line in post_file:
        ID_Post, ID_employee, dolzhnnost, ZP, stazh, Obrazov = line.split(";")
        ID_Post = int(ID_Post)
        post = Post(ID_Post, ID_employee, dolzhnnost, ZP, stazh, Obrazov)
        orders.add_post(post)

with open("Softwares.txt", 'r', encoding='utf-8') as software_file:
    for line in software_file:
        ID_Software, naimenovanie, haracteristica, data_vipuska, stoim = line.split(";")
        ID_Software = int(ID_Software)
        software = Software(ID_Software, naimenovanie, haracteristica, data_vipuska, stoim)
        orders.add_software(software)

with open("Servicess.txt", 'r', encoding='utf-8') as services_file:
    for line in services_file:
        ID_Services, naimenovanie, opisanie, vremia_na_vipoln, stoim = line.split(";")
        ID_Services = int(ID_Services)
        services = Services(ID_Services, naimenovanie, opisanie, vremia_na_vipoln, stoim)
        orders.add_services(services)

print(orders)
for thing in orders.things:
    print(str(thing), end=';')