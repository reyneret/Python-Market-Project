applePrice = 10_000
orangePrice = 15_000
grapePrice = 20_000

appleQty = int(input("Masukkan jumlah apel: "))
orangeQty = int(input("Masukkan jumlah jeruk: "))
grapeQty = int(input("Masukkan jumlah anggur: "))

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
if payment < totalPrice:
    print("Transaksi dibatalkan.")
    print(f"Uang kurang sebesar {selisih}")
elif payment > totalPrice:
    print("Transaksi berhasil. Terima kasih.")
    print(f"Uang kembalian anda: {selisih}")
else:
    print("Transaksi berhasil. Terima kasih.")