# BASE VALUES
fruitList = [
    {"product_name": "Apel", "product_price": 10_000 , "product_stock": 12},
    {"product_name": "Jeruk", "product_price": 15_000 , "product_stock": 6},
    {"product_name": "Anggur", "product_price": 20_000 , "product_stock": 3},
]

def showFruits(targetList):
    for i in range(len(targetList)):
        print(f"{fruitList[i]["product_name"]}   | Rp. {fruitList[i]["product_price"]}  | Stok: {fruitList[i]["product_stock"]}")

def addFruit(targetList, newFruitName, newFruitPrice, newFruitStock):
    targetList.append({"product_name": newFruitName, "product_price": newFruitPrice, "product_stock": newFruitStock})

def deleteFruit(targetList, fruitName):
    clearRow = 0
    while clearRow == 0:
        for i in range(len(targetList)):
            if targetList[i]["product_name"] == fruitName:
                clearRow = i
                targetList.pop(clearRow)
                print("Buah berhasil dihapus dari daftar.")
                return 0
        print(f"{fruitName} tidak ada dalam daftar.")
        fruitName = input("Masukkan kembali nama buah yang ingin dihapus: ")

while True:
    print("""
    =============================
    PASAR BUAH
    =============================

    Menu:
    1. Daftar buah
    2. Tambah buah
    3. Hapus buah
    4. Beli buah
    5. Keluar program\n
    """)

    selectMenu = int(input("Masukkan nomor menu: "))
    if selectMenu == 1:
        showFruits(fruitList)
        print()

        print("Menu")
        print("1. Kembali ke menu utama")
        print("2. Keluar dari program\n")
        selectMenu = int(input("Masukkan nomor menu: "))
        if selectMenu == 1:
            print("Kembali ke menu utama.")
        else:
            break
    elif selectMenu == 2:
        fruitName = input("Masukkan nama buah baru: ")
        fruitPrice = int(input(f"Masukkan harga {fruitName} (dalam Rp.): "))
        fruitQty = int(input(f"Masukkan jumlah stok {fruitName}: "))

        addFruit(fruitList, fruitName, fruitPrice, fruitQty)
        print(f"{fruitName} berhasil ditambahkan ke daftar buah.")

        print("Menu")
        print("1. Kembali ke menu utama")
        print("2. Keluar dari program\n")
        selectMenu = int(input("Masukkan nomor menu: "))
        if selectMenu == 1:
            print("Kembali ke menu utama.")
        else:
            break
    elif selectMenu == 3:
        delFruitName = input("Masukkan nama buah yang ingin dihapus: ")
        delFruitName = delFruitName.capitalize()

        deleteFruit(fruitList, fruitName)
        print("Buah berhasil dihapus.")
        print()

        print("Menu")
        print("1. Kembali ke menu utama")
        print("2. Keluar dari program\n")
        selectMenu = int(input("Masukkan nomor menu: "))
        if selectMenu == 1:
            print("Kembali ke menu utama.")
        else:
            break
    elif selectMenu == 4:
        appleQty = int(input("Masukkan jumlah apel: "))
        if appleQty <= fruitList[0]["product_stock"]:
            print(f"Mengambil {appleQty} buah.")
            fruitList[0]["product_stock"] -= appleQty
            print(f"Sekarang stok ada {fruitList[0]["product_stock"]} buah.")
        else:
            while appleQty > fruitList[0]["product_stock"]:
                print(f"Stok apel tidak cukup. Apel hanya tersedia {fruitList[0]["product_stock"]} buah.")
                appleQty = int(input("Masukkan jumlah apel: "))
            print(f"Mengambil {appleQty} buah.")
            fruitList[0]["product_stock"] -= appleQty
            print(f"Sekarang stok ada {fruitList[0]["product_stock"]} buah.")

        orangeQty = int(input("Masukkan jumlah jeruk: "))
        if orangeQty <= fruitList[1]["product_stock"]:
            print(f"Mengambil {orangeQty} buah.")
            fruitList[1]["product_stock"] -= orangeQty
            print(f"Sekarang stok ada {fruitList[1]["product_stock"]} buah.")
        else:
            while orangeQty > fruitList[1]["product_stock"]:
                print(f"Stok apel tidak cukup. Apel hanya tersedia {fruitList[1]["product_stock"]} buah.")
                orangeQty = int(input("Masukkan jumlah apel: "))
            print(f"Mengambil {orangeQty} buah.")
            fruitList[1]["product_stock"] -= orangeQty
            print(f"Sekarang stok ada {fruitList[1]["product_stock"]} buah.")

        grapeQty = int(input("Masukkan jumlah anggur: "))
        if grapeQty <= fruitList[2]["product_stock"]:
            print(f"Mengambil {grapeQty} buah.")
            fruitList[2]["product_stock"] -= grapeQty
            print(f"Sekarang stok ada {fruitList[2]["product_stock"]} buah.")
        else:
            while grapeQty > fruitList[2]["product_stock"]:
                print(f"Stok apel tidak cukup. Apel hanya tersedia {fruitList[2]["product_stock"]} buah.")
                grapeQty = int(input("Masukkan jumlah apel: "))
        print(f"Mengambil {grapeQty} buah.")
        fruitList[2]["product_stock"] -= grapeQty
        print(f"Sekarang stok ada {fruitList[2]["product_stock"]} buah.")


        totalPriceApple = appleQty * fruitList[0]["product_price"]
        totalPriceOrange = orangeQty * fruitList[1]["product_price"]
        totalPriceGrape = grapeQty * fruitList[2]["product_price"]
        totalPrice = totalPriceApple+totalPriceOrange+totalPriceGrape


        print("\nDetail Belanja\n")
        print(f"Apel: {appleQty} x {fruitList[0]["product_price"]} = {totalPriceApple}")
        print(f"Jeruk: {orangeQty} x {fruitList[1]["product_price"]} = {totalPriceOrange}")
        print(f"Anggur: {grapeQty} x {fruitList[2]["product_price"]} = {totalPriceGrape}")
        print(f"\nTotal: {totalPrice}\n")


        #Payment Feature (31 August 2026)       
        print("-"*20)
        payment = int(input("\nMasukkan jumlah bayaran: "))
        selisih = abs(totalPrice - payment)
        while payment < totalPrice:
            print("Transaksi dibatalkan.")
            print(f"Uang kurang sebesar {selisih}")
            payment = int(input("Masukkan jumlah bayaran: "))
        if payment > totalPrice:
            print("Transaksi berhasil. Terima kasih.")
            print(f"Uang kembalian anda: {selisih}")
        else:
            print("Transaksi berhasil. Terima kasih.")
            break
    elif selectMenu == 5:
        print("Terima kasih sudah berbelanja di Pasar Buah")
