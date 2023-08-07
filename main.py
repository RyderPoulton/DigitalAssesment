
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
    print_with_index(L)
    order = int(input("Enter the index number of the sandwich ordered -> "))
    sandwich = L[order]
    name = sandwich[0]
    price = sandwich[1]
    if name in O:
        print("There are {} {} in the order".format(L[0], L[1]))
    else:
        amount = int(input("Amount of sandwiches -> "))
        if amount > 5:
            print("Too many sandwiches")
        elif S[0] + amount > 5:
            print("There is already {} sandwiches ordered. Max of 5 sandwiches can be ordered.")
        else:
            new_list = [amount, name, price]
            O.append(new_list)
            output = "{} {} have been added to the order".format(amount, name)
            print(output)
            total = amount * price
            new_total = Z[0] + total
            rounded_total = round(new_total, 2)
            Z[0] = rounded_total


def review_order(L, O, Z):
    if len(O) >= 1:
        print_order_list(O)
        if len(L) == 3:
            print("Delivery cost: 3")
            output = "Total: {}".format(Z[0])
            print(output)
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
    # Clear customer details and order
    L.clear()
    O.clear()
    # Set total cost to 0
    Z[0] = 0
    # Set total sandwiches ordered to 0
    S[0] = 0


def edit_order(L, Z, S):
    if len(L) > 0:
        print_order_with_index(L)
        index = int(input("What would you like to edit -> "))
        item = L[index]
        change = int(input("How many would you like to add/remove (use +/-) -> "))
        sandwich_amount = item[0] + change
        if sandwich_amount == 0:
            print("{} has been removed from the order".format(item[1]))
        elif S[0] + sandwich_amount > 5:
            print("Max of 5 sandwiches can be ordered")
        elif sandwich_amount <= 5:
            output = "{} {} have been ordered".format(sandwich_amount, item[1])
            print(output)
        elif sandwich_amount > 5:
            print("Max of 5 sandwiches can be ordered")
        else:
            print("Error")
    elif len(L) == 0:
        print("There is nothing in the order")
    else:
        print("Error")


def edit_customer_details(L, Z):
    if len(L) > 0:
        if len(L) == 3:
            customer_details = "Name: {}\nAddress: {}\nPhone Number: {}\nDelivery/Pickup: Delivery".format(L[0], L[1], L[2])
            print(customer_details)
            output = "0: Name\n1: Address\n2: Phone Number\n3: Change to Pickup"
            print(output)
            integer = int(input("Index number -> "))
            if integer == 0:
                new_name = input("Enter new name -> ")
                L[0] = new_name
            elif integer == 1:
                new_address = input("Enter new address -> ")
                L[1] = new_address
            elif integer == 2:
                new_number = input("Enter new phone number -> ")
                L[2] = new_number
            elif integer == 3:
                customer = L[0]
                L.clear()
                L.append(customer)
                total = Z[0] - 3
                Z[0] = total
            else:
                print("Error")
        elif len(L) == 1:
            customer_details = "Name: {}\nDelivery or Pickup: Pickup".format(L[0])
            print(customer_details)
            my_list = ["Name", "Change to delivery"]
            output = "0: {}\n1: {}".format(my_list[0], my_list[1])
            print(output)
            index = int(input("Enter index number -> "))
            if index == 0:
                new_name = input("Enter new name ->")
                L[0] = new_name
            elif index == 1:
                customer = L[0]
                L.clear()
                address = input("Enter address -> ")
                number = input("Enter phone number -> ")
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
    option = input("Pick up: p or delivery($3 charge): d -> ").lower()
    customer = input("Customer name -> ")
    if option == "p":
        L.append(customer)
    elif option == "d":
        address = input("Enter address -> ")
        number = input("Enter phone number -> ")
        L.append(customer)
        L.append(address)
        L.append(number)
        total = Z[0] + 3
        Z[0] = total
    else:
        print("Error")


def complete_order(L, O, Z):
    if len(L) >= 1:
        if len(O) >= 1:
            review_order(L, O, Z)
            letter = input("Would you like to complete the order y/n ->").lower
            if letter == y:
                L.clear()
                O.clear()
                Z[0] = 0
                print("Order complete\nStart new order:")
            elif letter == n:
                print("Continue order")
            else:
                print("Error")
        else:
            print("No customer details")
    else:
        print("Nothing in the order")


def menu():
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
    L: Pick Up or Delivery
    F: Complete Order
    Q: Quit
    '''
    run = True
    while run == True:
        print(my_menu)
        choice = input("Enter choice -> ").upper()
        if choice == "P":
            print_list(my_list)
        elif choice == "A":
            add_sandwich(my_list, order_list, total, total_sandwiches)
        elif choice == "R":
            review_order(delivery_list, order_list, total)
        elif choice == "D":
            delete_order(order_list, delivery_list, total, total_sandwiches)
            print("Order deleted\n"
                  "Start new order:")
        elif choice == "E":
            edit_order(order_list, total, total_sandwiches)
        elif choice == "C":
            edit_customer_details(delivery_list, total)
        elif choice == "L":
            delivery_option(delivery_list, total)
        elif choice == "F":
            complete_order(order_list, delivery_list, total)
        elif choice == "Q":
            print("Program Ended")
            run = False
        else:
            print("Error")


menu()
