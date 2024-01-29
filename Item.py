class Item:
    _name = ""
    _cost = 0
    _description = ""

    def __init__(self, name):
        self._name = name
    def get_cost(self):
        return self._cost
    def __str__(self):
        return f"Item {self._name}"

    def __repr__(self):
        return f" ORDER {self._name}"