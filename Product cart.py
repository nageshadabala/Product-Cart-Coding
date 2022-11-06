final_products = [
    {"price": 2000, "name": "cycle", "period": 178},
    {"price": 8000, "name": "realme7", "period": 256},
    {"price": 6000, "name": "realme6", "period": 198}
]


def function():
    pricelow = int(input("enter price low value :"))
    pricehigh = int(input("enter price hign value : "))
    low = int(input("enter period low value : "))
    high = int(input("enter period high value : "))
    return pricelow, pricehigh, low, high


def create_product():
    price = int(input("enter price value :"))
    name = input("enter the product name : ")
    period = int(input("enter period value :"))
    new_product = {"price": price, "name": name, "period": period}
    final_products.append(new_product)
    get_product(final_products)


def get_product(products):
    for index in products:
        print(index)


def substring_name():
    product_items = []
    substr = input("enter the product name substring: ")
    for i in final_products:
        if substr in i['name']:
            product_items.append(i)
    if len(product_items) == 0:
        print("there are no substring names are available")
    else:
        get_product(product_items)


def oroperation(pricelow, pricehigh, low, high):
    product = []
    for i in range(0, len(final_products)):
        if (pricelow < final_products[i]["price"] <= pricehigh) or (low < final_products[i]["period"] <= high):
            product.append(final_products[i])
    if len(product) == 0:
        print('no products  are available between price and period values')
    else:
        print(" OR operation between price and period ")
        get_product(product)


def andoperation(pricelow, pricehigh, low, high):
    product = []
    for i in range(0, len(final_products)):
        if (pricelow <= final_products[i]["price"] <= pricehigh) and (low <= final_products[i]["period"] <= high):
            product.append(final_products[i])
    if len(product) == 0:
        print('no products  are available between price and period values')
    else:
        print(" AND operation between price and period ")
        get_product(product)


def delete():
    delname = str(input("enter name of the product for delete : "))
    for index in final_products:
        if index['name'] == delname:
            final_products.remove(index)
    get_product(final_products)


def updatePricePeriod():
    updatename = input("enter the name fo update proce and period values : ")
    for index in final_products:
        if index['name'] == updatename:
            pricevalue = input("enter the updated price value :")
            periodvalue = input("enter the updated period value : ")
            index["price"] = pricevalue
            index["period"] = periodvalue
    get_product(final_products)


def Choice(i):
    if i == 1:
        create_product()

    elif i == 2:
        substring_name()

    elif i == 3:
        inner_choice = int(input("enter 1 to filer based on price or period \nenter 2 to filer based on price and"
                                 " period"))
        if inner_choice == 1:
            pricelow, pricehigh, low, high = function()
            oroperation(pricelow, pricehigh, low, high)
        elif inner_choice == 2:
            pricelow, pricehigh, low, high = function()
            andoperation(pricelow, pricehigh, low, high)
        else:
            print("wrong choice")
    elif i == 4:
        delete()
    elif i == 5:
        updatePricePeriod()
    elif i == 6:
        get_product(final_products)
    elif i == 0:
        quit()
    else:
        print("choose correct option")


choice = True
while choice:
    number = int(input("enter 1 to add items to product:  \nenter 2 to get items with subname:  \nenter 3 to filter "
                       "products:  \nenter 4 to delete the product:  \nenter 5 update price and period:  \nenter 6 to "
                       "get all product:  \nenter 0 to exit: "))
    Choice(number)
    input("press enter to continue ")
