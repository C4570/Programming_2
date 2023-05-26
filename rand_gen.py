import random
import string
from main import Product, HashTable

def generator():
    # Create a list of food names
    food_names = ['Fideos', 'Arroz', 'Pez', 'Pan', 'Leche', 'Huevos', 'Queso', 'Pollo', 'Carne', 'Verduras']

    # Create a HashTable object
    ht = HashTable()

    # Generate 10,000 unique product codes
    product_codes = set()
    while len(product_codes) < 10:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        product_codes.add(code)

    # Create and insert 10,000 Product objects with unique codes and random food names
    for code in product_codes:
        name = random.choice(food_names)
        quantity = random.randint(0, 1000)
        product = Product(code, name, quantity)
        ht.insert(product)

    return ht