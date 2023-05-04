from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []  # Customer objects
        self.dvds = []  # DVD objects

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer, dvd = self.get_customer_and_dvd(customer_id, dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer, dvd = self.get_customer_and_dvd(customer_id, dvd_id)
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = ""
        str_customers = [str(c) for c in self.customers]
        str_dvds = [str(d) for d in self.dvds]

        result += "\n".join(str_customers) + "\n"
        result += "\n".join(str_dvds)
        return result

    def get_customer_and_dvd(self, customer_id, dvd_id):
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        return customer, dvd

