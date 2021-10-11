import os #operating system 作業系統模組

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, "r", encoding = "utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue  #繼續
            name, price = line.strip().split(",")  #先把換行處理掉，在用逗點做切割
            products.append([name, price])
    return products

#讓使用者輸入 
def user_input(products):
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
    return products

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], "的價格是", p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, "w", encoding = "utf-8") as f:
        f.write("商品,價格\n")
        for p in products:
            f.write(p[0] + "," + str(p[1]) + "\n")


def main():   ##主要執行的程式碼
    filename = "products.csv"
    if os.path.isfile(filename): #來檢查檔案在不在這個系統中（路徑有差）
        print("找到檔案")
        products = read_file(filename)
    else:
        print("找不到檔案")

    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()