products = []

while True:
    name = input("請輸入商品名稱：")
    if name == "q":
        break
    price = input("請輸入商品價格：")
    
    #little_products.append(name)
    #little_products.append(price)
    little_products = [name, price]  #上面兩行簡化版

    products.append(little_products)
print(products)