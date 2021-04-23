import time

selectmode = int(input("Hello. Welcome to Kerbal Kalculator v1.0 /n 1 - Burn time calculator /n 2 - Exit"))

if selectmode == 1:
    fuelamount = float(input("Enter fuel amount: "))
    oxidiseramount = float(input("Enter oxidiser amount: "))

    fuelps = float(input("Enter fuel per second: "))
    oxips = float(input("Enter oxidiser per second: "))

    print("Calculating")
    time.sleep(3)

    burntime = fuelamount / fuelps
    oburntime = oxidiseramount / oxips

    print("You have",burntime,"Seconds of Liquid Fuel")
    
    print("You have",oburntime,"Seconds of Oxidiser")

else:
    exit(0)

input()
