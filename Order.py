import datetime
import Item

class Order:
    _id = -1
    _user = None
    _items = list()
    _cost = 0
    _datetime = datetime.datetime.now()
    _isConfirmed = False
    _isPaid = False

    _orders_amount = 0

    def __init__(self, user):
        self._id = Order._orders_amount
        Order._orders_amount += 1
        self._user = user
        self._dateTime = datetime.datetime.now()
        self._email = _isConfirmed = False
        self._isPaid = False
    def add_item(self, item):
        if type(item) == Item.Item:
            self._items.append(item)
            self._cost += item.get_cost()
        else:
            raise TypeError
    def __str__(self):
        return f"Order from user {repr(self._user)} and items {self._items} with the total cost of {self._cost}"
    def __repr__(self):
        return f"ORDER {self._id}"
    def get_items(self):
        return tuple(self._items)