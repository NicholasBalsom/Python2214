print("Table Of Powers")

while True:
    start_num = int(input("Start number: "))
    stop_num = int(input("Stop number: "))
    if start_num > stop_num:
        print("Start number has to be greater than the stop number. Try again. \n")
        continue
    else:
        break

print("Number \t Squared   Cubed\n====== \t =======  =======")
for n in range(start_num, stop_num+1):
    print(f"{n} \t {n**2} \t  {n**3}")
