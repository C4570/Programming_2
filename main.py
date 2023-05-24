'''
class Product

__init__: Initializes a Product object with a code, name and quantity.


class HashTable

__init__: Initializes the hash table without an optional hash function and capacity.
    -In case capacity is not passed a value the function will assign a default value to self.c. In case capacity will be assigned 40.000 
     since the supermarket normally sells this amount of products.
insert  : Inserts an element in the hash table using a key.
delete  : Deletes an element from the hash table using a key.
search  : Searches for an element in the hash table using a key and returns the element if found.
__str__ : Returns key statistics to study performance such as the hash table load factor, the length of the longest list and the number of elements present in the table.

'''
#------------Product------------
class Product:
    def __init__(self, code, name, quantity):
        self.code = code
        self.name = name
        self.quantity = quantity
        
    def __str__(self) -> str:
        return f'\t-Name: {self.name}\n\t-Quantity: {self.quantity}\n\t-Code: {self.code}'
#------------HashTable------------
class HashTable:
    def __init__(self, capacity=None):
        if capacity is None:
            self.c = 40000
        else: 
            self.c = capacity
        self.T = [[] for x in range(self.c)]    #For each element in the range, a list is accumulated in the list.
        
    def insert (self, product):
        code = int(''.join([str(ord(c) - ord('A') + 1) if c.isalpha() else c for c in product.code]))

        index = int((self.c *(code * 0.4570 - int((code * 0.4570)))))    #h(k) = [m · (k · A − [k · A])]
        
        self.T[index].append(product)
        
    def search ( self, key):
        pass
    
    def delete (self, key):
        pass
    
    def __str__(self) -> str:
        result = f'Hash table capacity: {self.c}\n'
        for i in range(self.c):
            if len(self.T[i]) > 0:
                result += f'In index {i}:\n {str(self.T[i][0])}\n'
        return result


ht = HashTable()
product = Product('AF1574J005','Fideos', 2820)
ht.insert(product)
product = Product('AAN1235465','Arroz', 0)
ht.insert(product)
print(ht)


#------------MENU------------
def menu() -> None:
    print("1. Add new item")
    print("2. Query item")
    print("3. Delete item")
    print("4. Stats")
    print("0. Exit")
    print()
    
if __name__ == "__main__":
    hs = HashTable()
    
    while True:
        menu()
        choice = int(input("Enter choice: "))
        if choice == 1:
            code = str(input("Enter product code: "))
            name = str(input("Enter product name: "))
            quantity = int(input("Enter the quantity of products: "))
            
            product = Product(code, name, quantity)
            
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 0:
            break
        else:
            print("Invalid choice")
        print()