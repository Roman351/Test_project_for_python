from User import User
from Item import Item


name = "Ivan"

Ivan = User(name, "+7 999 999 99 99", "Ivan@gmail.com")
order1 = Ivan.create_order()
order1 = Ivan.create_order()
order1 = Ivan.create_order()
order1.add_item(Item("ноутбук"))
order1.add_item(Item("наушники"))
order1.add_item(Item("Лампа"))

print(Ivan)
print(Ivan.get_orders()[0])
print(Ivan.get_orders()[0].get_items())

#order1.add_item("ноутбук")