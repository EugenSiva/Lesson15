import threading
import time
from concurrent.futures import ThreadPoolExecutor

class ShoppingCart:
    def __init__(self):
        self.items = 0
        self.lock = threading.Lock()

    def update(self, name):
        print(f'Zakaznik-{name}: zacina nakupovat')
        self.lock.acquire()
        local_cart = self.items
        local_cart += 1
        time.sleep(1)
        self.items = local_cart
        self.lock.release()
        print(f'Zakaznik-{name}: nakupil')

print('Nakupovanie zacina')
shopping_cart = ShoppingCart()
print(f'Velkost kosika je: {shopping_cart.items}')

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(shopping_cart.update, range(3))

print(f'Velkost kosika po nakupovani je: {shopping_cart.items}')