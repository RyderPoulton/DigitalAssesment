def print_list(L):
    for i in range(0, len(L)):
        output = "{} {}".format(L[i][0], L[i][1])
        print(output)


def print_with_index(L):
    for i in range(0, len(L)):
        output = "{}: {}".format(i, L[i][0])
        print(output)


def add_sandwich(L,O):
    print_with_index(L)
    order = int(input("Enter the index number of the sandwich ordered -> "))
    sandwich = L[order]
    name = sandwich[0]
    price = sandwich[1]
    amount = int(input("Amount of sandwiches -> "))
    new_list = [name, price, amount]
    O.append(new_list)
    output = "{} {} have been added to the order".format(amount, name)
    print(output)


def menu(L,O):
    order_list = []
    my_list = [
        ["Halloumi and apricot jam sandwich", 15.95],
        ["Banh mi with five-spice crispy pork belly, pickled carrot, chilli, coriander and cucumber", 18.95],
        ["Roasted beetroot, carrot, spiced nuts and whipped feta", 15.95],
        # ["Sausage and egg sandwich", 14.95]
        # ["Smoked salmon deluxe", 15.95],
        # ["Ham sandwich in a French baguette", 16.95],
         # ["Kiwi & Roo’s ‘lucky beef’ steak sandwich", 18.95],
        # ["Buttermilk chicken, scotch bonnet jam, pickled cabbage and crispy shallots", 18.95],
        # ["Balik ekmek – griddled mackerel in a baguette with tomato, lettuce, onion, chilli and sumac", 18.95],
        # ["Milanese and gremolata panini", 16.95]
        # ["Fish finger sandwich with Nordic dill salsa", 15.95],
        # ["Grilled cheddar and jalapeño popper sandwich", 15.95]
     ]
    my_menu = '''
    A: Print Menu
    B: Add Sandwich
    C: Review Order
    D: Delete Order
    D: Edit Order
    E: Pick Up or Delivery
    F: Complete Order
    Q: Quit
    '''
    run = True
    if run == True:
        print(my_menu)
        choice =  input("Enter choice -> ")
        if choice == "A":
            print_list(L)
        elif choice == "B":
            add_sandwich(L,O)
        elif choice == "Q":
            print("Program Ended")
            run = False
        else:
            print("Error")

menu(my_list, order_list)
