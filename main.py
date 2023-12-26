from functions import clear_screen, add_product

products = []

while(True):
    clear_screen()
    user_choice = input("Choose a option:\n1 - Add a new product\n2 - See the products\n3 - Exit\n")
    clear_screen()

    if user_choice == "1":
            add_product(products) 
            clear_screen()

    elif user_choice == "2":
        search_option = input("1 - See all products\n2 - Search a product\n")
        clear_screen()

        if search_option == "1":
            for product in products:
                print(product)
            input()
        
        elif search_option == "2":
            clear_screen()
            product_name = input("Enter the product's name:\n")
            clear_screen()

            for product in products:
                if product.name == product_name:
                    print(product)
            input()

    elif user_choice == "3":
        break
    
    else:
        print("Choose a valid option\n")
        input()

    
        

    