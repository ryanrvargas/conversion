#github.com/ryanrvargas
import sys
import argparse

def getTsp(unit, num):
    match unit.lower():
        case "ounces" | "oz":
            return num * 6
        case "tbsp":
            return num * 3
        case "cup" | "cups":
            return num * 48.6922
        case "pint" | "pints":
            return num * 96
        case "quart" | "quarts":
            return num * 192
        case "gallon" | "gallons":
            return num * 768
        case "liter" | "liters" | "l":
            return num * 202.884
        case "milliliter" | "milliliters" | "ml":
            return num / 4.929
            
def getTbsp(unit, num):
    match unit.lower():
        case "ounces" | "oz":s
            return num * 2
        case "tsp":
            return num / 3
        case "cup" | "cups":
            return num * 16.2307
        case "pint" | "pints":
            return num * 32
        case "quart" | "quarts":
            return num * 64
        case "gallon" | "gallons":
            return num * 256
        case "liter" | "liters" | "l":
            return num * 67.628
        case "milliliter" | "milliliters" | "ml":
            return num / 14.787
def getOzs(unit, num):
    match unit.lower():
        case "tsp":
            print(num * .16, "ozs")
        case "tbsp":
            return num * .5
        case "cup" | "cups":
            return num * 8
        case "pint" | "pints":
            return num * 16
        case "quart" | "quarts":
            return num * 32
        case "gallon" | "gallons":
            return num * 123
        case "liter" | "liters" | "l":
            return num * 33.814
        case "milliliter" | "milliliters" | "ml":
            return num / 29.574
            
def getCups(unit, num):
    match unit.lower():
        case "tsp":
            return num / 48.692
        case "tbsp":
            return num / 16.231
        case "ounce" | "ounces":
            return num / 8.115
        case "pint" | "pints":
            return num * 1.972
        case "quart" | "quarts":
            return num * 3.943
        case "gallon" | "gallons":
            return num * 15.773
        case "liter" | "liters" | "l":
            return num * 4.167
        case "milliliter" | "milliliters" | "ml":
            return num / 260


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
