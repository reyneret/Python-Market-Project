# BASE VALUES
fruitList = [
    #product_name, price, stock
    ["apple", 10_000, 12],
    ["orange", 15_000, 6],
    ["grape", 20_000, 3]
]

#========================================
print("""
=============================
PASAR BUAH PITON
=============================

Menu:
1. Daftar buah
2. Tambah buah
3. Hapus buah
4. Beli buah
5. Keluar program\n
""")
selectMenu = int(input("Masukkan nomor menu: "))

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
print(f"Apel: {appleQty} x {applePrice} = {totalPriceApple}")
print(f"Jeruk: {orangeQty} x {orangePrice} = {totalPriceOrange}")
print(f"Anggur: {grapeQty} x {grapePrice} = {totalPriceGrape}")
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