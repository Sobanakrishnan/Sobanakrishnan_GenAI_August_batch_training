

print("--- Part A ---")


def add_item_buggy(item, cart=[]):
    cart.append(item)
    return cart


print(add_item_buggy("apple"))
print(add_item_buggy("banana"))
print(add_item_buggy("milk", cart=["bread"]))
print(add_item_buggy("eggs"))



def add_item(item, cart=None):
    
    if cart is None:
        cart = []
    cart.append(item)
    return cart


print("\n--- Part B ---")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))


def create_cart(owner, discount=0):

    return {"owner": owner, "items": [], "discount": discount}


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})


def update_price(price_tuple, new_price):
   
    try:
        price_tuple[0] = new_price
        return price_tuple
    except TypeError as e:
        print(f"TypeError caught: {e}")
        return price_tuple


def calculate_total(cart):
    subtotal = 0
    for item in cart["items"]:
        subtotal += item["price"] * item["qty"]
    discount_amount = subtotal * (cart["discount"] / 100)
    final_total = subtotal - discount_amount
    return round(final_total, 2)


def main():
    print("\n--- Part C ---")

 
    cart1 = create_cart("Alice", discount=10)
    cart2 = create_cart("Bob")  

    add_to_cart(cart1, "Laptop", 50000, qty=1)
    add_to_cart(cart1, "Mouse", 500, qty=2)

    add_to_cart(cart2, "Keyboard", 1200, qty=1)

    print("Cart 1 (Alice):", cart1)
    print("Cart 2 (Bob):  ", cart2)

    
    print("\nCart 1 items id:", id(cart1["items"]))
    print("Cart 2 items id:", id(cart2["items"]))
    print("Are item lists the same object?", cart1["items"] is cart2["items"])

    print("\nAlice's total:", calculate_total(cart1))
    print("Bob's total:  ", calculate_total(cart2))

   
    price_record = ("Laptop", 50000)
    print("\nAttempting to modify a tuple element...")
    update_price(list(price_record), 48000)  
    update_price(price_record, 48000)        


if __name__ == "__main__":
    main()



# 1. Why is discount=0 safe but cart=[] dangerous?
#    `0` is an immutable int. Default arguments are evaluated once at
#    function definition time and stored on the function object, but
#    since ints can't be mutated in place, every call that relies on
#    the default just gets the same value 0 rebound locally — nothing
#    persists between calls. `[]`, however, is a mutable list. That
#    SAME list object is reused across every call that doesn't pass
#    its own cart, and because list methods like append() mutate the
#    object in place, changes from one call leak into the next call.
#
# 2. What is the difference between rebinding and mutating?
#    - Rebinding means pointing a variable name at a different object,
#      e.g. `x = x + 1` or `discount = 5` — the original object is
#      untouched; the name now refers to a new object.
#    - Mutating means changing the contents of an object in place
#      while the variable still points to the SAME object in memory.
# 3. Which of these are mutable? — list, tuple, dict, set, str, int
#    - list  -> mutable
#    - tuple -> immutable
#    - dict  -> mutable
#    - set   -> mutable
#    - str   -> immutable
#    - int   -> immutable
#
# 4. When you pass a list into a function and modify it, do changes
#    reflect outside? Why?
#    Yes. Python passes object references by value — the function
#    parameter becomes a new local name, but it refers to the exact
#    same list object the caller has. If the function mutates that
#    object in place (append, remove, sort, item assignment, etc.),
#    the change is visible outside the function too, because there is
#    only ever one underlying list object. This would NOT happen if
#    the function instead rebinds the parameter to a brand-new list
