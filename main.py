a = """
Choose conversion:
num1 : miles to km
num2 : km to miles
num3 : kg to lbs
num4 : lbs to kgs
num5 : liters to quarts
num6 : quarts to liters
num7 : mph to km/s
num8 : water gallon(lbs) to liters
num9 : input temperature to retrieve water state
num10: compound interest(5%)
num11: compound interest(8%) 1-10 years
"""

while True:
    print(a)
    choose = input("Pick a conversion: ")
    if choose in ('num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'num10', 'num11'):
        if choose == "num1":
            milesToKM = float(input("How many miles?: "))
            km = milesToKM * 1.609344
            print(round(km, 2), "kilometers")

        elif choose == "num2":
            KmToMiles = float(input("How many kilometers?: "))
            miles = KmToMiles * 0.621371
            print(round(miles, 2), "miles")

        elif choose == "num3":
            KGToPounds = float(input("How many kilogram?: "))
            pounds = KGToPounds * 2.205
            print(round(pounds, 2), "lbs")

        elif choose == "num4":
            poundsToKG = float(input("How many pounds?: "))
            kgs = poundsToKG / 2.205
            print(round(kgs, 2), "kilograms")

        elif choose == "num5":
            litersToQuarts = float(input("How many liters?: "))
            quarts = litersToQuarts * 1.057
            print(round(quarts, 2), "quarts")

        elif choose == "num6":
            QuartsToLiters = float(input("How many quarts?: "))
            liters = QuartsToLiters / 1.057
            print(round(liters, 2), "liters")

        elif choose == "num7":
            mphToKms = float(input("How many miles per hour?: "))
            kms = mphToKms * 1.609 * (1 / 3600)
            print(round(kms, 2), "kilometers per second!")

        elif choose == "num8":
            water_in_gallons = float(input("How many gallons of water?: "))
            gallon_lbs = water_in_gallons * (8.345 / 1)
            water_liters = gallon_lbs * 0.453592
            print(round(water_liters, 2), "liters of water")
        elif choose == "num9":
            asktemperature = float(input("What is the temperature?: "))
            if asktemperature <= 0:
                print("Ice")
            elif asktemperature > 0 and asktemperature < 100:
                print("Liquid water")
            elif asktemperature >= 100:
                print("Steam")
        elif choose == "num10":
            p = float(input("What is the initial investment?: "))
            a = p * (1 + 0.05 / 12) ** 12 * 1
            print("$", round(a, 2))
        elif choose == "num11":
            p = float(input("What is the initial investment?: "))
            for i in range(1, 11):
                a = p * (1 + 0.08 / 12) ** (i * 1)
                print("Year", i, ":", round(a, 2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            print("Goodbye!")
            break

    else:
        print("invalid input")
