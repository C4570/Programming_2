from main import Product, clear_screen, load_animation, secret, text, choices
from rand_gen import generator

def menu() -> None:
    print("+------------------+")
    print("|       Menu       |")
    print("+------------------+")
    print("| 1. Add new item  |")
    print("| 2. Item search   |")
    print("| 3. Item delete   |")
    print("| 4. Stats         |")
    print("| 0. Exit          |")
    print("+------------------+")
    
if __name__ == "__main__":
    ht = generator()
    while True:
        menu()
        choice = int(input("Enter choice: "))
        # Add new item
        if choice == 1:
            clear_screen()
            while True:
                code = str(input("Enter product code: "))
                name = str(input("Enter product name: "))
                quantity = int(input("Enter the quantity of products: "))
            
                product = Product(code, name, quantity)
                ht.insert(product)
                
                # Load
                clear_screen()
                load_animation()
                clear_screen()
                
                print('The item was added without countermeasure')
                
                text('add')
                if choices() == False:
                    break
        
        # Item search        
        elif choice == 2:
            clear_screen()
            while True:
                code = str(input('Enter the code: '))
                
                # Load
                clear_screen()
                load_animation()
                clear_screen()
                
                found, index, product = ht.search(code)
                if found:
                    print(f'Item found \n\t-Index: {index}\n{str(product)}')
                else:
                    print('Item not found in:')
                    print()
                
                text('search')
                if choices() == False:
                    break

        # Delete Item
        elif choice == 3:
            clear_screen()
            while True:
                code = str(input('Enter the code: '))

                # Load
                clear_screen()
                load_animation()
                clear_screen()

                deleted = ht.delete(code)
                if deleted:
                    print(f'Item deleted')
                else:
                    print('Item not found')

                text('delete')
                if choices() == False:
                    break
        
        # Stat      
        elif choice == 4:
            clear_screen()
            print(ht)
            input()
            clear_screen()
            
        elif choice == 5:
            clear_screen()
            secret()
        
        # Exit
        elif choice == 0:
            clear_screen()
            break
        else:
            clear_screen()
            print("Invalid choice")
        print()