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

for p in products:
    print(p)

for p in products:
    print(p[0]) #只印出商品名字

for p in products:
    print(p[0], "的價格是", p[1])


with open("products.csv", "w", encoding = "utf-8") as f:
    f.write("商品,價格\n")
    for p in products:
        f.write(p[0] + "," + str(p[1]) + "\n")


    