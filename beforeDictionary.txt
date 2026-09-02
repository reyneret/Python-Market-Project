# BASE VALUES
fruitList = [
    #product_name, price, stock
    ["Apel", 10_000, 12],
    ["Jeruk", 15_000, 6],
    ["Anggur", 20_000, 3]
]

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
        for i in range(0, len(fruitList)):
            print(f"{fruitList[i][0]}   | Rp. {fruitList[i][1]}  | Stok: {fruitList[i][2]}")
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

        newFruit = [fruitName, fruitPrice, fruitQty]
        fruitList.append(newFruit)
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
        clearRow = 100000
        while clearRow == 100000:
            for i in range(len(fruitList)-1):
                if delFruitName in fruitList[i]:
                    clearRow = i
                    break
                else:
                    print(f"{delFruitName} tidak ada dalam daftar.")
                    delFruitName = input("Masukkan kembali nama buah yang ingin dihapus: ")
                    delFruitName.capitalize()
        fruitList.pop(clearRow)
        print(f"{delFruitName} berhasil dihapuskan dari daftar.")
    elif selectMenu == 4:
        appleQty = int(input("Masukkan jumlah apel: "))
        if appleQty <= fruitList[0][2]:
            print(f"Mengambil {appleQty} apel.")
            fruitList[0][2] -= appleQty
            print(f"Sekarang stok apel ada {fruitList[0][2]} buah.")
        else:
            while appleQty > fruitList[0][2]:
                print(f"Stok apel tidak cukup. Apel hanya tersedia {fruitList[0][2]} buah.")
                appleQty = int(input("Masukkan jumlah apel: "))
            print(f"Mengambil {appleQty} apel.")
            fruitList[0][2] -= appleQty
            print(f"Sekarang stok apel ada {fruitList[0][2]} buah.")

        orangeQty = int(input("Masukkan jumlah jeruk: "))
        if orangeQty <= fruitList[1][2]:
            print(f"Mengambil {orangeQty} apel.")
            fruitList[1][2] -= orangeQty
            print(f"Sekarang stok apel ada {fruitList[1][2]} buah.")
        else:
            while orangeQty > fruitList[1][2]:
                print(f"Stok apel tidak cukup. Apel hanya tersedia {fruitList[1][2]} buah.")
                orangeQty = int(input("Masukkan jumlah apel: "))
            print(f"Mengambil {orangeQty} apel.")
            fruitList[1][2] -= orangeQty
            print(f"Sekarang stok apel ada {fruitList[1][2]} buah.")

        grapeQty = int(input("Masukkan jumlah anggur: "))
        if grapeQty <= fruitList[2][2]:
            print(f"Mengambil {grapeQty} apel.")
            fruitList[2][2] -= grapeQty
            print(f"Sekarang stok apel ada {fruitList[2][2]} buah.")
        else:
            while grapeQty > fruitList[2][2]:
                print(f"Stok apel tidak cukup. Apel hanya tersedia {fruitList[2][2]} buah.")
                grapeQty = int(input("Masukkan jumlah apel: "))
        print(f"Mengambil {grapeQty} apel.")
        fruitList[2][2] -= grapeQty
        print(f"Sekarang stok apel ada {fruitList[2][2]} buah.")


        totalPriceApple = appleQty * fruitList[0][1]
        totalPriceOrange = orangeQty * fruitList[1][1]
        totalPriceGrape = grapeQty * fruitList[2][1]
        totalPrice = totalPriceApple+totalPriceOrange+totalPriceGrape


        print("\nDetail Belanja\n")
        print(f"Apel: {appleQty} x {fruitList[0][1]} = {totalPriceApple}")
        print(f"Jeruk: {orangeQty} x {fruitList[1][1]} = {totalPriceOrange}")
        print(f"Anggur: {grapeQty} x {fruitList[2][1]} = {totalPriceGrape}")
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
