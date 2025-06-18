menu={

'pizza':350,
'pasta':250,
'cold coffee':150,
'burger':120,    

}
print(menu)

print("welcome to ashlee's restro")
print("pizza:Rs350\npasta:Rs250\ncoldcoffee:Rs150\nburger:Rs120")
order_total=0
item_1=input("enter the name of the item you want to order:")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item{item_1}has been added to your order")
else:
    print(f"ordered item{item_1} is not available yet!")
another_order = input(f"do you want to add another item?(yes/no)")
if another_order =="yes":
    item_2=input("enter the name of second item=")
    if item_2 in menu:
    order_total+=menu[item_2]
    print(f"item{item_2} has been added to order")
else:
    print(f"ordered item{item_2} is not available!")
print(f"the total amount of items to pay is {order_total}")



     

    