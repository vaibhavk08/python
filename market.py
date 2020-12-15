market = {}

print("""
1.  Add Item
2.  Remove Item
3.  Show Item
4.  List Price
0.  Exit
-----------------------------""")

option= int(input("Enter the option: "))

while option != 0:
    if option == 1:
        item = input("Name of the Item: ")
        price= float(input("Price of item: "))
        market[item]= price

    elif option == 2:
        item = input("Enter the name of Item: ")
        del(market[item])

    elif option == 3:
        for item in market:
            print(item, ":", " Rs.", market[item])

    elif option == 4:
        print("Final Total Reciept-----------------")
        for item in market:
            print(item, ":", " Rs.", market[item])

        print("------------------------------------")
        total = 0
        for item in market:
            total += market[item] 

        print("Total : Rs.",total)

    option = int(input("\n Enter the option: "))

print("Exit")               
