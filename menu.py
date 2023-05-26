from main import Product, clear_screen, load_animation, secret
from rand_gen import generator

def menu() -> None:
    print("+------------------+")
    print("|       Menu       |")
    print("+------------------+")
    print("| 1. Add new item  |")
    print("| 2. Item search   |")
    print("| 3. Delete item   |")
    print("| 4. Stats         |")
    print("| 0. Exit          |")
    print("+------------------+")
    
if __name__ == "__main__":
    ht = generator()
    while True:
        menu()
        choice_0 = int(input("Enter choice: "))
        # Add new item
        if choice_0 == 1:
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
                
                print('Do you wish to enter another product?')
                print("1. Yes")
                print("2. No")
                print()
                choice_1 = int(input("Enter choice: "))
                
                if choice_1 == 1:
                    clear_screen()
                elif choice_1 == 2:
                    clear_screen()
                    break
                else:
                    print("Invalid choice (* ￣︿￣)")
                    input()
                    clear_screen()
        
        # Item search        
        elif choice_0 == 2:
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
                    print('Item not found')
                    print()
                print('Do you wish to search another product?')
                print("1. Yes")
                print("2. No")
                print()
                choice_1 = int(input("Enter choice: "))
                
                if choice_1 == 1:
                    clear_screen()
                elif choice_1 == 2:
                    clear_screen()
                    break
                else:
                    print("Invalid choice (* ￣︿￣)")
                    input()
                    clear_screen()

        elif choice_0 == 3:
            clear_screen()
            pass
        elif choice_0 == 4:
            clear_screen()
            pass
        elif choice_0 == 5:
            clear_screen()
            secret()
        elif choice_0 == 0:
            clear_screen()
            break
        else:
            clear_screen()
            print("Invalid choice")
        print()