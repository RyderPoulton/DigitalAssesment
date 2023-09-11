
def print_list(L):
    for i in range(0, len(L)):
        output = "{} {}".format(L[i][0], L[i][1])
        print(output)


def print_order_list(L):
    for i in range(0, len(L)):
        output = "{} {} {}".format(L[i][0], L[i][1], L[i][2])
        print(output)


def print_with_index(L):
    for i in range(0, len(L)):
        output = "{}: {} {}".format(i, L[i][0], L[i][1])
        print(output)


def print_order_with_index(L):
    for i in range(0, len(L)):
        output = "{}: {} {}".format(i, L[i][0], L[i][1])
        print(output)


def add_sandwich(L, O, Z, S):
    """Add sandwich to order

    :param L: list (menu)
    :param O: list (order_list)
    :param Z: float (total cost of the order)
    :param S: int (total sandwiches ordered)
    :return: None
    """
    if S[0] == 5:
        print("5 sandwiches already ordered")
    elif S[0] < 5:
        print("{} sandwiches ordered, {} more can be ordered\n".format(S[0], 5 - S[0]))
        print_with_index(L)
        # Get sandwich ordered
        order = int(input("Enter the index number of the sandwich ordered -> "))
        sandwich = L[order]
        name = sandwich[0]
        price = sandwich[1]
        # Get amount of sandwiches ordered
        amount = int(input("Amount of sandwiches -> "))
        if amount > 5:
            print("Too many sandwiches")
        elif amount < 1:
            print("Must order 1 or more sandwiches")
            # Limit sandwiches ordered to 5
        elif S[0] + amount > 5:
            print("There is already {} sandwiches ordered. Max of 5 sandwiches can be ordered.".format(S[0]))
        else:
            # Add sandwich to order
            new_list = [amount, name, price]
            O.append(new_list)
            output = "{} {} have been added to the order".format(amount, name)
            print(output)
            total = amount * price
            new_total = Z[0] + total
            # Round total to 2dp
            rounded_total = round(new_total, 2)
            Z[0] = rounded_total
            a = S[0] + amount
            S[0] = a


def review_order(L, O, Z):
    """Review Order

    :param L: list (customer details)
    :param O: list (order_list)
    :param Z: float (total cost of the order)
    :return: None
    """
    # Check if sandwiches in order
    if len(O) >= 1:
        # Print list of sandwiches ordered with costs and quantities
        print_order_list(O)
        if len(L) == 3:
            # Print total cost of order
            print("Delivery cost: 3")
            output = "Total: {}".format(Z[0])
            print(output)
            # Print customer details
            customer_details = "Name: {}\nAddress: {}\nPhone Number: {}".format(L[0], L[1], L[2])
            print(customer_details)
        elif len(L) == 1:
            output = "Total: {}".format(Z)
            print(output)
            customer_details = "Name: {}".format(L[0])
            print(customer_details)
        elif len(L) == 0:
            print("No customer details")
        else:
            print("Error")
    elif len(O) == 0:
        print("There is nothing in the order")
    else:
        print("Error")


def delete_order(L, O, Z, S):
    """Delete order

    :param L: list (order_list)
    :param O: list (customer details)
    :param Z: float (total cost of the order)
    :param S: int (total sandwiches ordered)
    :return: None
    """
    # Clear customer details and order
    L.clear()
    O.clear()
    # Set total cost to 0
    Z[0] = 0
    # Set total sandwiches ordered to 0
    S[0] = 0


def edit_order(L, Z, S):
    """Edit the customer order

    :param L: list (order_list)
    :param Z: float (total cost of the order)
    :param S: int (total sandwiches ordered)
    :return: None
    """
    if len(L) > 0:
        print_order_with_index(L)
        # get item to edit
        index = int(input("What would you like to edit -> "))
        item = L[index]
        print("There are {} {} ordered".format(item[0], item[1]))
        # get quantity to remove
        change = int(input("How many would you like to add/remove (use - to remove) -> "))
        sandwich_amount = item[0] + change
        total_amount = S[0] + change
        # check cases and update where valid
        if sandwich_amount < 0:
            print("Negative amounts of sandwiches can not be ordered")
        elif sandwich_amount == 0:
            print("{} has been removed from the order".format(item[1]))
            # remove item from order
            L.pop(index)
            total = S[0] + change
            S[0] = total
            cost = Z[0] + (item[2] * change)
            # round cost to 2 decimal places
            rounded_cost = round(cost, 2)
            Z[0] = rounded_cost
        elif total_amount > 5:
            print("Max of 5 sandwiches can be ordered")
        elif change <= 5:
            output = "{} {} have been ordered".format(sandwich_amount, item[1])
            print(output)
            new_amount = item[0] + change
            S[0] = total_amount
            item[0] = new_amount
            cost = Z[0] + (item[2] * change)
            # round cost to 2 decimal places
            rounded_cost = round(cost, 2)
            Z[0] = rounded_cost
        else:
            print("Error")
    elif len(L) == 0:
        print("There is nothing in the order")
    else:
        print("Error")


def edit_customer_details(L, Z):
    """Edit customer details
    :param L: list (customer details)
    :param Z: float (total cost of the order)
    :return: None
    """
    # Check for customer details
    if len(L) > 0:
        if len(L) == 3:
            details = "Name: {}\nAddress: {}\nPhone Number: {}\nDelivery/Pickup: Delivery".format(L[0], L[1], L[2])
            print(details)
            output = "0: Name\n1: Address\n2: Phone Number\n3: Change to Pickup"
            print(output)
            # Get item to edit
            integer = int(input("Index number -> "))
            if integer == 0:
                new_name = input("Enter new name -> ")
                L[0] = new_name
            elif integer == 1:
                new_address = input("Enter new address -> ")
                L[1] = new_address
            elif integer == 2:
                new_number = input("Enter new phone number -> ")
                if len(new_number) < 7:
                    print("Phone number too short")
                elif len(new_number) > 15:
                    print("Phone number too long")
                else:
                    L[2] = new_number
            # Change delivery to pickup
            elif integer == 3:
                customer = L[0]
                L.clear()
                L.append(customer)
                total = Z[0] - 3
                Z[0] = total
            else:
                print("Error")
        elif len(L) == 1:
            # Print customer details
            customer_details = "Name: {}\nDelivery or Pickup: Pickup".format(L[0])
            print(customer_details)
            my_list = ["Name", "Change to delivery"]
            output = "0: {}\n1: {}".format(my_list[0], my_list[1])
            print(output)
            index = int(input("Enter index number -> "))
            if index == 0:
                new_name = input("Enter new name ->")
                L[0] = new_name
            # Change pickup to delivery
            elif index == 1:
                customer = L[0]
                L.clear()
                address = input("Enter address -> ")
                number = input("Enter phone number -> ")
                if len(number) < 7:
                    print("Phone number too short")
                elif len(number) > 15:
                    print("Phone number too long")
                else:
                    L.append(customer)
                    L.append(address)
                    L.append(number)
                    total = Z[0] + 3
                    Z[0] = total
        else:
            print("Error")
    elif len(L) == 0:
        print("No customer details")
    else:
        print("Error")


def delivery_option(L, Z):
    """Add customer details

    :param L: list (customer details)
    :param Z: float (total cost of the order)
    :return: None
    """
    if len(L) > 0:
        print("Customer Details already entered")
    elif len(L) == 0:
        # Get pickup/delivery choice
        option = input("Pick up: p or delivery($3 charge): d -> ").lower()
        # Get customer name (2 - 20 characters)
        run = True
        while run == True:
            customer = input("Customer name -> ")
            if len(customer) < 2:
                print("Name too short (2 Characters Min)")
            elif len(customer) > 20:
                print("Name too long (20 Characters Max)")
            else:
                run = False
                if option == "p":
                    L.append(customer)
                elif option == "d":
                    address = input("Enter address -> ")
                    # Get customer phone number(7 - 15 digits)
                    run = True
                    while run == True:
                        number = input("Enter phone number -> ")
                        if len(number) < 7:
                            print("Phone number too short (7 Number Min)")
                        elif len(number) > 15:
                            print("Phone number too long (15 Number Max)")
                        else:
                            run = False
                            # Append customer details to list and add $3 to total for delivery
                            L.append(customer)
                            L.append(address)
                            L.append(number)
                            total = Z[0] + 3
                            Z[0] = total
                else:
                    print("Error")


def complete_order(L, O, Z):
    """complete order

    :param L: list (order_list)
    :param O: list (customer details)
    :param Z: float (total cost of the order)
    :return: None
    """
    # Check for sandwiches in order
    if len(L) >= 1:
        # Check for customer details
        if len(O) >= 1:
            # Print order and customer details
            review_order(O, L, Z)
            # Check if ready to complete order
            letter = input("Would you like to complete the order y/n -> ").lower()
            if letter == "y":
                L.clear()
                O.clear()
                Z[0] = 0
                print("Order complete\nStart new order:")
            elif letter == "n":
                print("Continue order")
            else:
                print("Error")
        else:
            print("No customer details")
    else:
        print("Nothing in the order")


def menu():
    """Menu

    :return: None
    """
    total = [0]
    delivery_list = []
    order_list = []
    total_sandwiches = [0]
    my_list = [
        ["Halloumi and apricot jam sandwich", 15.95],
        ["Banh mi with five-spice crispy pork belly, pickled carrot, chilli, coriander and cucumber", 18.95],
        ["Roasted beetroot, carrot, spiced nuts and whipped feta", 15.95],
        ["Sausage and egg sandwich", 14.95],
        ["Smoked salmon deluxe", 15.95],
        ["Ham sandwich in a French baguette", 16.95],
        ["Kiwi & Roo’s ‘lucky beef’ steak sandwich", 18.95],
        ["Buttermilk chicken, scotch bonnet jam, pickled cabbage and crispy shallots", 18.95],
        ["Balik ekmek – griddled mackerel in a baguette with tomato, lettuce, onion, chilli and sumac", 18.95],
        ["Milanese and gremolata panini", 16.95],
        ["Fish finger sandwich with Nordic dill salsa", 15.95],
        ["Grilled cheddar and jalapeño popper sandwich", 15.95]
     ]
    my_menu = '''
    P: Print Menu
    A: Add Sandwich
    R: Review Order
    D: Delete Order
    E: Edit Order
    C: Edit Customer Details
    G: Customer Details (Pick Up/Delivery)
    F: Complete Order
    Q: Quit
    '''
    run = True
    while run == True:
        print(my_menu)
        # Get option
        choice = input("Enter choice -> ").upper()
        # Print sandwich menu
        if choice == "P":
            print_list(my_list)
            # Add sandwich to order
        elif choice == "A":
            add_sandwich(my_list, order_list, total, total_sandwiches)
            # Review order
        elif choice == "R":
            review_order(delivery_list, order_list, total)
            # Delete order
        elif choice == "D":
            delete_order(order_list, delivery_list, total, total_sandwiches)
            print("Order deleted\n"
                  "Start new order:")
            # Edit order
        elif choice == "E":
            edit_order(order_list, total, total_sandwiches)
            # Edit customer details
        elif choice == "C":
            edit_customer_details(delivery_list, total)
            # Get customer details
        elif choice == "G":
            delivery_option(delivery_list, total)
            # Complete order
        elif choice == "F":
            complete_order(order_list, delivery_list, total)
            # Quit Program
        elif choice == "Q":
            print("Program Ended")
            run = False
        else:
            print("Error")


menu()
