def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


def create_cart(owner, discount=0):
    return {"owner": owner, "items": [], "discount": discount}


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print(f"TypeError raised: {e}")


def calculate_total(cart):
    subtotal = 0
    for item in cart["items"]:
        subtotal += item["price"] * item["qty"]
    return subtotal - subtotal * (cart["discount"] / 100)


print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

cart1 = create_cart("Aarav", discount=10)
cart2 = create_cart("Priya")

add_to_cart(cart1, "Notebook", 50, qty=3)
add_to_cart(cart1, "Pen", 10, qty=5)
add_to_cart(cart2, "Laptop Bag", 800, qty=1)

print(cart1["items"])
print(cart2["items"])

print(calculate_total(cart1))
print(calculate_total(cart2))

price_record = (100, "USD")
update_price(price_record, 120)
