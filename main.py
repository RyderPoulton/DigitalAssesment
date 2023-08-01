
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
        output = "{}: {} Amount:{}".format(i, L[i][1], L[i][0])
        print(output)


def print_order_with_index(L):
    for i in range(0, len(L)):
        output = "{}: {} {}".format(i, L[i][0], L[i][1])
        print(output)


def receipt(L, O, Z):
    print_order_list(L)
    print(Z)
    print(O)


def add_sandwich(L, O, Z):
    print_with_index(L)
    order = int(input("Enter the index number of the sandwich ordered -> "))
    if order in L:
        print("There are {} {} in the order".format(L[0], L[1]))
    else:
        sandwich = L[order]
        name = sandwich[0]
        price = sandwich[1]
        amount = int(input("Amount of sandwiches -> "))
        if amount > 5:
            print("Too many sandwiches")
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
    print_order_list(O)
    print(Z)
    if len(L) == 3:
        customer_details = "Name: {}\nAddress: {}\nPhone Number: {}".format(L[0], L[1], L[2])
        print(customer_details)
    elif len(L) == 1:
        customer_details = "Name: {}".format(L[0])
        print(customer_details)
    elif len(L) == 0:
        print("No customer details")
    else:
        print("Error")


def delete_order(L, O):
    L.clear()
    O.clear()


def edit_order(L):
    print_order_with_index(L)
    index = int(input("What would you like to edit -> "))
    item = L[index]
    change = int(input("How many would you like to add/remove (use +/-) -> "))
    sandwich_amount = item[0] + change
    output = "{} {} have been ordered".format(sandwich_amount, item[1])
    print(output)


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


def complete_order(L, O):
    if len(L) >= 1:
        if len(O) >= 1:
            print("Order Complete")
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
    A: Print Menu
    B: Add Sandwich
    C: Review Order
    D: Delete Order
    E: Edit Order
    F: Pick Up or Delivery
    G: Complete Order
    Q: Quit
    '''
    run = True
    while run == True:
        print(my_menu)
        choice = input("Enter choice -> ").upper()
        if choice == "A":
            print_list(my_list)
        elif choice == "B":
            add_sandwich(my_list, order_list, total)
        elif choice == "C":
            review_order(delivery_list, order_list, total)
        elif choice == "D":
            delete_order(order_list, delivery_list)
            print("Order deleted\n"
                  "Start new order:")
        elif choice == "E":
            edit_order(order_list)
        elif choice == "F":
            delivery_option(delivery_list, total)
        elif choice == "G":
            complete_order(order_list, delivery_list)
            receipt(order_list, delivery_list, total)
        elif choice == "Q":
            print("Program Ended")
            run = False
        else:
            print("Error")


menu()
