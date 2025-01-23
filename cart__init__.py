import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


#OLD get_cart() function

# def get_cart(username: str) -> list:
#     cart_details = dao.get_cart(username)
#     if cart_details is None:
#         return []
    
#     items = []
#     for cart_detail in cart_details:
#         contents = cart_detail['contents']
#         evaluated_contents = eval(contents)
#         items.append()
#         for content in evaluated_contents:
#             items.append(content)
    
#     # items = [content for cart_detail in cart_details for content in eval(cart_detail['contents'])]

#     i2 = []
#     for i in items:
#         temp_product = products.get_product(i)
#         i2.append(temp_product)
#     return i2


# new optimized get_cart() function
def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if not cart_details:  # Handles None or empty cart_details
        return []

    # Flatten the contents of cart_details and fetch product details
    items = [
        products.get_product(item_id)
        for cart_detail in cart_details
        for item_id in eval(cart_detail['contents'])
    ]
    return items

    


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)


