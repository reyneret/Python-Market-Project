applePrice = 10_000
orangePrice = 15_000
grapePrice = 20_000

appleQty = int(input("Masukkan jumlah apel: "))
orangeQty = int(input("Masukkan jumlah jeruk: "))
grapeQty = int(input("Masukkan jumlah anggur: "))

totalPriceApple = appleQty * applePrice
totalPriceOrange = orangeQty * orangePrice
totalPriceGrape = grapeQty * grapePrice

print("\nDetail Belanja\n")
print(f"Apel: {appleQty} x {applePrice} = {totalPriceApple}")
print(f"Jeruk: {orangeQty} x {orangePrice} = {totalPriceOrange}")
print(f"Anggur: {grapeQty} x {grapePrice} = {totalPriceGrape}")

print(f"\nTotal: {totalPriceApple+totalPriceOrange+totalPriceGrape}")
