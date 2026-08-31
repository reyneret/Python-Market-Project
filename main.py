applePrice = 10_000
orangePrice = 15_000
grapePrice = 20_000

appleStock = 12
orangeStock = 6
grapeStock = 3

appleQty = int(input("Masukkan jumlah apel: "))
if appleQty <= appleStock:
    print(f"Mengambil {appleQty} apel.")
    appleStock -= appleQty
    print(f"Sekarang stok apel ada {appleStock} buah.")
else:
    while appleQty > appleStock:
        print(f"Stok apel tidak cukup. Apel hanya tersedia {appleStock} buah.")
        appleQty = int(input("Masukkan jumlah apel: "))
    print(f"Mengambil {appleQty} apel.")
    appleStock -= appleQty
    print(f"Sekarang stok apel ada {appleStock} buah.")

orangeQty = int(input("Masukkan jumlah jeruk: "))
if orangeQty <= orangeStock:
    print(f"Mengambil {orangeQty} apel.")
    orangeStock -= orangeQty
    print(f"Sekarang stok apel ada {orangeStock} buah.")
else:
    while orangeQty > orangeStock:
        print(f"Stok apel tidak cukup. Apel hanya tersedia {orangeStock} buah.")
        orangeQty = int(input("Masukkan jumlah apel: "))
    print(f"Mengambil {orangeQty} apel.")
    orangeStock -= orangeQty
    print(f"Sekarang stok apel ada {orangeStock} buah.")

grapeQty = int(input("Masukkan jumlah anggur: "))
if grapeQty <= grapeStock:
    print(f"Mengambil {grapeQty} apel.")
    grapeStock -= grapeQty
    print(f"Sekarang stok apel ada {grapeStock} buah.")
else:
    while grapeQty > grapeStock:
        print(f"Stok apel tidak cukup. Apel hanya tersedia {grapeStock} buah.")
        grapeQty = int(input("Masukkan jumlah apel: "))
    print(f"Mengambil {grapeQty} apel.")
    grapeStock -= grapeQty
    print(f"Sekarang stok apel ada {grapeStock} buah.")

totalPriceApple = appleQty * applePrice
totalPriceOrange = orangeQty * orangePrice
totalPriceGrape = grapeQty * grapePrice
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