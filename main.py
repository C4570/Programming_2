'''
class Product

__init__: Inicializa un objeto de Producto con un código, nombre y cantidad


class HashTable

__init__: Inicializa la tabla hash con una función de hash y capacidad opcionales
    -En caso de que a hashfuntion o capacity no se les pase un valor la funcion asignara un valor predeterminado a self.h y self.c. En caso de la capacity se asiganara 40.000 
     ya que el supermercado vender normalmente esta cantidad de productos.
insert  : Inserta un elemento en la tabla hash usando una clave.
delete  : Elimina un elemento de la tabla hash usando una clave.
search  : Busca un elemento en la tabla hash usando una clave y devuelve el elemento si se encuentra.
__str__ : Devuelve una representación en cadena de la tabla hash.


'''
import hashlib

#------------Product------------
class Product:
    def __init__(self, code, name, quantity):
        self.code = code
        self.name = name
        self.quantity = quantity
        
#------------HashTable------------
class HashTable:
    def __init__(self, hashfuntion=None, capacity=None):
        if hashfuntion is None:
            self.h = hashlib.md5
        else:
            self.h = hashfuntion
        if capacity is None:
            self.c = 40000
        else: 
            self.c = capacity 
        self.T = [None] * self.c
        
    
    def insert (self, key, element):
        self.T.append
    def search ( self, key):
        pass
    def delete (self, key):
        pass
    def __str__(self) -> str:
        return f'Capacidad: {self.c}\nFuncion hash: {self.T}'

#------------MENU------------
def menu() -> None:
    print("1. Modify the hash table")
    print("2. Add new item")
    print("3. Query item")
    print("4. Delete item")
    print("5. Stats")
    print("0. Exit")
    print()

if __name__ == "__main__":
    
    hs = HashTable()
    
    while True:
        menu()
        choice = int(input("Enter choice: "))
        if choice == 1:
            hashfuntion = input("Enter the Hash funtion: ")
            capacity = input("Enter capacity: ")
           
            ht = HashTable(hashfuntion, capacity)
        
        elif choice == 2:
            code = str(input("Enter product code: "))
            name = str(input("Enter product name: "))
            quantity = int(input("Enter the quantity of products: "))
            
            product = Product(code, name, quantity)
            
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 0:
            break
        else:
            print("Invalid choice")
        print()

