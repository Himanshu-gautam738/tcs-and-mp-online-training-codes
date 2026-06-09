food_items = []
def add_food_item(item_id, name, price, quantity):
    food_items.append({
        "ItemID": item_id,
        "ItemName": name,
        "Price": price,
        "Quantity": quantity
    })

def search_food_item(item_id):
    for item in food_items:
        if item["ItemID"] == item_id:
            return item
    return None

def update_food_quantity(item_id, new_quantity):
    for item in food_items:
        if item["ItemID"] == item_id:
            item["Quantity"] = new_quantity
            return True
    return False

def display_food_items():
    for item in food_items:
        print(item["ItemID"], item["ItemName"], item["Price"], item["Quantity"])

class OrderNode:
    def __init__(self, order_id, customer, item_id, quantity, date):
        self.order_id = order_id
        self.customer = customer
        self.item_id = item_id
        self.quantity = quantity
        self.date = date
        self.next = None

class OrderList:
    def __init__(self):
        self.head = None

    def place_order(self, order_id, customer, item_id, quantity, date):
        new = OrderNode(order_id, customer, item_id, quantity, date)
        new.next = self.head
        self.head = new

    def cancel_order(self, order_id):
        curr = self.head
        prev = None
        while curr:
            if curr.order_id == order_id:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def display_orders(self):
        curr = self.head
        while curr:
            print(curr.order_id, curr.customer, curr.item_id, curr.quantity, curr.date)
            curr = curr.next

add_food_item(1, "Pizza", 299.0, 10)
add_food_item(2, "Burger", 149.0, 20)
add_food_item(3, "Pasta", 199.0, 15)

update_food_quantity(2, 18)

print("Available Food Items:")
display_food_items()

orders = OrderList()

orders.place_order(101, "Rahul", 1, 2, "10-02-2026")
orders.place_order(102, "Anita", 3, 1, "10-02-2026")

orders.cancel_order(101)

print("\nCustomer Orders:")
orders.display_orders()
