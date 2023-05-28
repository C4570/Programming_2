'''
TAD Product

__init__    : Initializes a Product object with a code, name and quantity.
__str__     : Returns the product attributes on the screen


TAD HashTable

__init__    : Initializes the hash table without an optional hash function and capacity.
hashfuntion : Calculate with the hash function the index where the product will be stored.
calculate_lf: Calculate the load factor of the hash function
insert      : Inserts an element in the hash table using a key.
search      : Searches for an element in the hash table using a key and returns the element if found.
delete      : Deletes an element from the hash table using a key.
__str__     : Returns key statistics to study performance such as the hash table load factor, the length of the longest list and the number of elements present in the table.

'''

import os
import time
import sys

#----------Animation---------- 
def load_animation():
    print("Loading:")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

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
    def __init__(self, capacity):
        self.c = capacity
        self.T = [[] for x in range(self.c)]    # For each element in the range, a list is accumulated in the list.
        
    def hashfuntion(self, code):
        key = int(''.join([str(ord(c) - ord('A') + 1) if c.isalpha() else c for c in code]))
        #                       h(k) = [c · (k · A − [k · A])]
        self.index = int((self.c *(key * 0.4570 - int((key * 0.4570)))))    
        
    
    def calculate_lf(self):
        n = sum(len(lst) for lst in self.T)
        m = self.c
        load_factor = n / m
        
        return load_factor
        
    '''def rehash(self):
        load_factor = self.calculate_lf()

        if load_factor > 0.75:
            new_c = int(self.c * 1.5)
            
        else:
            new_c = int(self.c / 1.5)
            
        new_T = [[] for x in range(new_c)]
        for lst in self.T:
            for product in lst:
                key = int(''.join([str(ord(c) - ord('A') + 1) if c.isalpha() else c for c in product.code]))
                index = int((new_c *(key * 0.4570 - int((key * 0.4570)))))
                new_T[index].append(product)
                    
            self.c = new_c
            self.T = new_T'''
            
    def insert (self, product):
        self.hashfuntion(product.code)
        self.T[self.index].append(product)
        
        '''load_factor = self.calculate_lf()
        
        if load_factor > 0.75 or load_factor < 0.6:
            self.rehash()'''
        
    def search (self, code):
        self.hashfuntion(code)
        # Search for the element in the list at the calculated index
        for product in self.T[self.index]:  
            if product.code == code:
                # If the element is found, return it
                return True, self.index, product
        # If the element is not found, return None
        return False, None, None           
                
    def delete (self, code):
        found, index, product = self.search(code)
        if found:
            self.T[index].remove(product)
            return True
        else:
            return False
    
    def __str__(self) -> str:
        # Calculate load factor and length of longest list
        load_factor = self.calculate_lf()
        max_list_length = max(len(lst) for lst in self.T)
        max_list_index = max(range(len(self.T)), key=lambda i: len(self.T[i]))

        result = f'Load factor: {load_factor}\n'
        result += f'Length of longest list: {max_list_length}\n'
        result += f'Index of longest list: {max_list_index}\n'

        print(result)
        print("Do you want to see the loaded items?\n")
        if choices() != False:
            # Iterate over all indices in the table
            for i in range(self.c):
                # If there are elements at this index
                if len(self.T[i]) > 0:
                    # Add a header for this index
                    result += f'\nIn index {i}:\n'
                    # Iterate over all products at this index
                    for j, product in enumerate(self.T[i]):
                        # Add the string representation of the product
                        result += f'{str(product)}\n'
                        # If this is not the last product at this index
                        if j < len(self.T[i]) - 1:
                            # Add a blank line between products
                            result += '\n'
            print(result)
        
        print("Do you want to see the hash table?\n")
        if choices() != False:
            print(self.T)
        
        return ''

#---------Clear-Screen---------
def clear_screen():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux (os.name is 'posix')
    else:
        os.system('clear')

#------------Secret------------
def secret():
    print(r"""
   _____                                     _           _   _                     ______         ____           _   _                     ___     ___    ___    ____  
  / ____|                                   | |         | | (_)                   |  ____|       |  _ \         (_) | |                   |__ \   / _ \  |__ \  |___ \ 
 | |        ___    _ __    _ __             | |  _   _  | |  _    __ _   _ __     | |__          | |_) |  _ __   _  | |_    ___    ___       ) | | | | |    ) |   __) |
 | |       / _ \  | '_ \  | '__|        _   | | | | | | | | | |  / _` | | '_ \    |  __|         |  _ <  | '__| | | | __|  / _ \  / __|     / /  | | | |   / /   |__ < 
 | |____  | (_) | | |_) | | |     _    | |__| | | |_| | | | | | | (_| | | | | |   | |       _    | |_) | | |    | | | |_  | (_) | \__ \    / /_  | |_| |  / /_   ___) |
  \_____|  \___/  | .__/  |_|    (_)    \____/   \__,_| |_| |_|  \__,_| |_| |_|   |_|      (_)   |____/  |_|    |_|  \__|  \___/  |___/   |____|  \___/  |____| |____/ 
                  | |                                                                                                                                                  
                  |_|                                                                                                                                                   
    """)
    input()
    clear_screen()
    
#------------Text-Choice------------
def text(var):
    print()
    print(f'Do you wish to {var} another product?')
    
def choices():
    while True:
        print("1. Yes")
        print("2. No")
        print()
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            clear_screen()
            break
        elif choice == 2:
            clear_screen()
            return False
        else:
            print("Invalid choice (* ￣︿￣)")
            input()
            clear_screen()