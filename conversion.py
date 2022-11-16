#github.com/ryanrvargas
import sys
import argparse

#This function converts other units into Tsp
def getTsp(unit, nums):
    global num
    num = nums
    match unit.lower():
        case "ounces" | "oz":
            num = nums * 6
        case "tbsp":
            num = nums * 3
        case "cup" | "cups":
            num = nums * 48.6922
        case "pint" | "pints":
            num = nums * 96
        case "quart" | "quarts":
            num = nums * 192
        case "gallon" | "gallons":
            num = nums * 768
        case "liter" | "liters" | "l":
            num = nums * 202.884
        case "milliliter" | "milliliters" | "ml":
            num = nums / 4.929
        case _:
            print("Inproper input")
#This function converts other units into Tbsp         
def getTbsp(unit, nums):
    global num
    num = nums
    match unit.lower():
        case "ounces" | "oz":
            num = nums * 2
        case "tsp":
            num = nums / 3
        case "cup" | "cups":
            num = nums * 16.2307
        case "pint" | "pints":
            num = nums * 32
        case "quart" | "quarts":
            num = nums * 64
        case "gallon" | "gallons":
            num = nums * 256
        case "liter" | "liters" | "l":
            num = nums * 67.628
        case "milliliter" | "milliliters" | "ml":
            num = nums / 14.787
        case _:
            print("Inproper input")
            
#This function converts other units into Ounces           
def getOzs(unit, nums):
    global num
    num = nums
    match unit.lower():
        case "tsp":
            num = nums * .16
        case "tbsp":
            num = nums * .5
        case "cup" | "cups":
            num = nums * 8
        case "pint" | "pints":
            num = nums * 16
        case "quart" | "quarts":
            num = nums * 32
        case "gallon" | "gallons":
            num = nums * 123
        case "liter" | "liters" | "l":
            num = nums * 33.814
        case "milliliter" | "milliliters" | "ml":
            num = nums / 29.574
        case _:
            print("Inproper input")
            
#This function converts other units into Cups              
def getCups(unit, nums):
    global num
    num = nums
    match unit.lower():
        case "tsp":
            num = nums / 48.692
        case "tbsp":
            num = nums / 16.231
        case "ounce" | "ounces":
            num = nums / 8.115
        case "pint" | "pints":
            num = nums * 1.972
        case "quart" | "quarts":
            num = nums * 3.943
        case "gallon" | "gallons":
            num = nums * 15.773
        case "liter" | "liters" | "l":
            num = nums * 4.167
        case "milliliter" | "milliliters" | "ml":
            num = nums / 260
        case _:
            print("Inproper input")
            
#This function converts other units into Pints
def getPints(unit, nums):
    global num
    num = nums
    match unit.lower():
        case "tsp":
            num = nums / 96
        case "tbsp":
            num = nums / 32
        case "ounce" | "ounces":
            num = nums / 16
        case "cup" | "cups":
            num = nums / 1.972
        case "quart" | "quarts":
            num = nums / 2
        case "gallon" | "gallons":
            num = nums * 8
        case "liter" | "liters" | "l":
            num = nums * 2.113
        case "milliliter" | "milliliters" | "ml":
            num = nums / 473.2
        case _:
            print("Inproper input")
            
#This function converts other units into Quarts.
def getQuarts(unit, nums):
    global num
    num = nums
    match unit.lower():
        case "tsp":
            num = nums / 192
        case "tbsp":
            num = nums / 64
        case "ounce" | "ounces":
            num = nums / 32
        case "cup" | "cups":
            num = nums / 3.943
        case "pint" | "pints":
            num = nums / 2
        case "gallon" | "gallons":
            num = nums * 4
        case "liter" | "liters" | "l":
            num = nums * 1.057
        case "milliliter" | "milliliters" | "ml":
            num = nums / 946.4
        case _:
            print("Inproper input")
            
#This is just a test. Nothing here is needed
unit = "ounces"
amount = 16
#i want to convert Ozs to tsp
getTsp(unit, amount)
print(str(num) + "Teaspoons")
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
#add test comment