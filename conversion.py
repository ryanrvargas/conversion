#github.com/ryanrvargas
import sys
import argparse

#This function converts other units into Tsp
def getTsp(unit, num):
    match unit.lower():
        case "ounces" | "oz": return num /  6
        case "tbsp": return num * 3
        case "cup" | "cups": return num * 48.6922
        case "pint" | "pints": return num * 96
        case "quart" | "quarts": return num * 192
        case "gallon" | "gallons": return num * 768
        case "liter" | "liters" | "l": return num * 202.884
        case "milliliter" | "milliliters" | "ml": return num / 4.929
        case _: print("Inproper input")

#This function converts other units into Tbsp         
def getTbsp(unit, num):
    match unit.lower():
        case "ounces" | "oz": return num * 2
        case "tsp": return num / 3
        case "cup" | "cups": return num * 16.2307
        case "pint" | "pints": return num * 32
        case "quart" | "quarts": return num * 64
        case "gallon" | "gallons": return num * 256
        case "liter" | "liters" | "l": return num * 67.628
        case "milliliter" | "milliliters" | "ml": return num / 14.787
        case _: print("Inproper input")

#This function converts other units into Ounces           
def getOzs(unit, num):
    match unit.lower():
        case "tsp": return num * .16
        case "tbsp": return num * .5
        case "cup" | "cups": return num * 8
        case "pint" | "pints": return num * 16
        case "quart" | "quarts": return num * 32
        case "gallon" | "gallons": return num * 123
        case "liter" | "liters" | "l": return num * 33.814
        case "milliliter" | "milliliters" | "ml": return num / 29.574
        case _: print("Inproper input")

#This function converts other units into Cups
def getCups(unit, num):
    match unit.lower():
        case "tsp": return num / 48.692
        case "tbsp": return num / 16.231
        case "ounce" | "ounces": return num / 8.115
        case "pint" | "pints": return num * 1.972
        case "quart" | "quarts": return num * 3.943
        case "gallon" | "gallons": return num * 15.773
        case "liter" | "liters" | "l": return num * 4.167
        case "milliliter" | "milliliters" | "ml": return num / 260
        case _: print("Inproper input")

#This function converts other units into Pints
def getPints(unit, num):
    match unit.lower():
        case "tsp": return num / 96
        case "tbsp": return num / 32
        case "ounce" | "ounces": return num / 16
        case "cup" | "cups": return num / 1.972
        case "quart" | "quarts": return num / 2
        case "gallon" | "gallons": return num * 8
        case "liter" | "liters" | "l": return num * 2.113
        case "milliliter" | "milliliters" | "ml": return num / 473.2
        case _: print("Inproper input")

#This function converts other units into Quarts.
def getQuarts(unit, num):
    match unit.lower():
        case "tsp": return num / 192
        case "tbsp": return num / 64
        case "ounce" | "ounces": return num / 32
        case "cup" | "cups": return num / 3.943
        case "pint" | "pints": return num / 2
        case "gallon" | "gallons": return num * 4
        case "liter" | "liters" | "l": return num * 1.057
        case "milliliter" | "milliliters" | "ml": return num / 946.4
        case _: print("Inproper input")

'''#This is just a test. Nothing here is needed
unit = "ounces"
amount = 16
#i want to convert Ozs to tsp
getTsp(unit, amount)
print(str(num) + "Teaspoons")'''
# Main block

if __name__ == '__main__':
    parser = parser = argparse.ArgumentParser()
    parser.add_argument("num1", help="first number as int or float", type=float)
    parser.add_argument("unit_from", help="unit of measure that you want to convert")
    parser.add_argument("operation", help=" to ")
    parser.add_argument(u"unit_to", help="unit of measure that you want")

    args = parser.parse_args()

    var1 = args.num1
    var1 = float(args.num1)
    print(f'Converting {args.num1} {args.unit_from} {args.operation} {args.unit_to}. Please wait....')

    if args.unit_to == "tsp":# add variables to dict
        result = getTsp(args.unit_from, args.num1)
        print(result)

    elif args.unit_to == "tbsp":# add variables to dict
        result = getTbsp(args.unit_from, args.num1)
        print(result)

    elif args.unit_to == "oz": # add variables to dict
        result = getOzs(args.unit_from, args.num1)
        print(result)

    elif args.unit_to == "cups": # add variables to dict
        result = getCups (args.unit_from, args.num1)
        print(result)

    elif args.unit_to == "pints": # add variables to dict
        result = getPints (args.unit_from, args.num1)
        print(result)

    elif args.unit_to == "quarts": # add variables to dict
        result = getQuarts (args.unit_from, args.num1)
        print(result)

    else:
        print("Not a valid conversion")
