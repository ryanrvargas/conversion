#github.com/ryanrvargas
import sys
import argparse

def getTsp(unit, num):
    global num
    match unit.lower():
        case "ounces" | "oz":
            num = num * 6
        case "tbsp":
            num = num * 3
        case "cup" | "cups":
            num = num * 48.6922
        case "pint" | "pints":
            num = num * 96
        case "quart" | "quarts":
            num = num * 192
        case "gallon" | "gallons":
            num = num * 768
        case "liter" | "liters" | "l":
            num = num * 202.884
        case "milliliter" | "milliliters" | "ml":
            num = num / 4.929
            
def getTbsp(unit, num):
    global num
    match unit.lower():
        case "ounces" | "oz":s
            num = num * 2
        case "tsp":
            num = num / 3
        case "cup" | "cups":
            num = num * 16.2307
        case "pint" | "pints":
            num = num * 32
        case "quart" | "quarts":
            num = num * 64
        case "gallon" | "gallons":
            num = num * 256
        case "liter" | "liters" | "l":
            num = num * 67.628
        case "milliliter" | "milliliters" | "ml":
            num = num / 14.787
            
def getOzs(unit, num):
    global num
    match unit.lower():
        case "tsp":
            print(num * .16, "ozs")
        case "tbsp":
            num = num * .5
        case "cup" | "cups":
            num = num * 8
        case "pint" | "pints":
            num = num * 16
        case "quart" | "quarts":
            num = num * 32
        case "gallon" | "gallons":
            num = num * 123
        case "liter" | "liters" | "l":
            num = num * 33.814
        case "milliliter" | "milliliters" | "ml":
            num = num / 29.574
            
def getCups(unit, num):
    global num
    match unit.lower():
        case "tsp":
            num = num / 48.692
        case "tbsp":
            num = num / 16.231
        case "ounce" | "ounces":
            num = num / 8.115
        case "pint" | "pints":
            num = num * 1.972
        case "quart" | "quarts":
            num = num * 3.943
        case "gallon" | "gallons":
            num = num * 15.773
        case "liter" | "liters" | "l":
            num =num * 4.167
        case "milliliter" | "milliliters" | "ml":
            num = num / 260

def getPints(unit, num):
    global num
    match unit.lower():
        case "tsp":
            num = num / 48.692
        case "tbsp":
            num = num / 16.231
        case "ounce" | "ounces":
            num = num / 8.115
        case "pint" | "pints":
            num = num * 1.972
        case "quart" | "quarts":
            num = num * 3.943
        case "gallon" | "gallons":
            num = num * 15.773
        case "liter" | "liters" | "l":
            num = num * 4.167
        case "milliliter" | "milliliters" | "ml":
            num = num / 473.2
# Main block
"""
if __name__ == '__main__':
    parser = parser = argparse.ArgumentParser()
    parser.add_argument("num1", help="first number as int or float", type=float)
    parser.add_argument("unit_from", help="unit of measure that you want to convert")
    parser.add_argument("operation", help=" to ")
    parser.add_argument(u"unit_to", help="unit of measure that you want")
    
    args = parser.parse_args()
    
    var1 = args.num1
    var1 = float(args.num1)
    print(f'Converting {args.num1}{args.unit_from} {args.operation} {args.unit_to}. Please wait....')
"""
