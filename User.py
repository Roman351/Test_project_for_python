import Order

class User:
    _id = -1
    _name = ""
    _phoneNumber = ""
    _email = 0
    _money = 0
    _orders = list()

    _users_amount = 0

    def __init__(self, name="", phone_number="", email=""):
        self._id = User._users_amount
        User._users_amount += 1
        self._name = name;
        self._phoneNumber = phone_number
        self._email = email
    def create_order(self):
        self._orders.append(Order.Order(self))
        return self._orders[-1]
    def __str__(self):
        return f"User {self._name} with a balance {self._money} and orders {self._orders}"

    def __repr__(self):
        return f"USER {self._id}"

    def get_orders(self):
        return tuple(self._orders)