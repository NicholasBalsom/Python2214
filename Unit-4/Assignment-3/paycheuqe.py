print("\nPay check calculator.\n")

hours = int(input("Hours worked: "))
payrate = float(input("Hourly pay rate: "))
taxrate = 18
grosspay = hours * payrate
taxamount = grosspay * (float(taxrate) / 100)
totalpay = grosspay - taxamount

print(f"\nGross pay: {grosspay:.2f}")
print(f"Tax rate: {taxrate}%")
print(f"Tax amount: {taxamount:.2f}")
print(f"Take home pay: {totalpay:.2f}")