#github.com/ryanrvargas
import sys
import argparse
import decimal
from rich import print as rprint

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

#This function converts other units into Ounces. Fluid Ounces         
def getFloz(unit, num):
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

#This function converts other units into Gallons.
def getGallons(unit, num):
    match unit.lower():
        case "tsp": return num / 768
        case "tbsp": return num / 256
        case "ounce" | "ounces": return num / 128
        case "cup" | "cups": return num / 15.772
        case "pint" | "pints": return num / 8
        case "quart" | "quarts" | "qt": return num / 4
        case "liter" | "liters" | "l": return num / 3.785
        case "milliliter" | "milliliters" | "ml": return num / 3785
        case _: print("Inproper input")

#This function converts other units to ounces
def getOunces(unit, num):
    match unit.lower():
        case "pounds" | "lbs" | "pound": return num * 16 
        case "stone": return num * 224
        case "microgram" | "micrograms": return num / 2.835e+7
        case "milligram" | "ml" | "milligrams": return num / 28350
        case "gram" | "g" | "grams": return num / 28.35
        case "kg" | "kilogram" | "kilograms": return num * 35.274
        
#This function converts other units to degrees Fahrenheit        
def getF(unit, num):
    match unit.lower():
        case "kelvin" | "k": return (num - 273.15) * 9/5 + 32
        case "celcius" | "c": return (num * 1.8) + 32
        case _: print("Improper input")
        
#This function converts other units to degrees Celcius        
def getC(unit, num):
    match unit.lower():
        case "kelvin" | "k": return num - 273.15
        case "fahrenheit" | "f": return 5/9 * ((num)-32)
        case _: print("Improper input")
        
#This function converts other units to degrees Kelvin        
def getK(unit, num):
    match unit.lower():
        case "celcius" | "c": return num + 273.15
        case "fahrenheit" | "f": return ((num)-32) * 5/9 + 273.15
        case _: print("Improper input")

#This function converts other units to duckpower
def getDuck(unit, num):
    match unit.lower():
        case "horsepower" | "hp": return num * 131.2
        
#This function converts other units to grams        
def getGrams(unit, num):
    match unit.lower():
        case "milligrams" | "milligram" | "Milligrams" | "Milligram" | "mg": return num / 1000
        case "kilograms" | "kilogram" | "Kilograms" | "kilograms" | "kg": return num * 1000
        case "pounds" | "lbs" | "lb" | "pound": return num * 453.6
        case "ounces" | "Ounces" | "oz" | "ozs" | "oz.": return num * 28.35
        case _: print("Improper input")
        
#This function converts other units to Inches.        
def getInches(unit, num):
    match unit.lower():
        case "foot" | "feet" | "ft": return num * 12 
        case "yard" | "yards" | "yd": return num * 36
        case "mile" | "miles" | "mi": return num * 63360
        case "micrometer" | "micrometers": return num / 25400
        case "millimeter" | "millimeters" | "mm": return num / 25.4
        case "centimeter" | "centimeters" | "cm": return num / 2.54
        case "meter" | "meters" | "m": return num * 39.37
        case "kilometer" | "kilometers" | "km": return num * 39370      

#This function converts other units to Feet.        
def getFeet(unit, num):
    match unit.lower():
        case "inch" | "inches" | "in": return num / 12 
        case "yard" | "yards" | "yd": return num * 3
        case "mile" | "miles" | "mi": return num * 5280
        case "micrometer" | "micrometers": return num / 304800
        case "millimeter" | "millimeters" | "mm": return num / 304.8
        case "centimeter" | "centimeters" | "cm": return num / 30.48
        case "meter" | "meters" | "m": return num * 3.281
        case "kilometer" | "kilometers" | "km": return num * 3281  

#This function converts other units to Yards.        
def getYards(unit, num):
    match unit.lower():
        case "inch" | "inches" | "in": return num / 36
        case "feet" | "feetss" | "ft": return num / 3
        case "mile" | "miles" | "mi": return num * 1760
        case "micrometer" | "micrometers": return num / 914400
        case "millimeter" | "millimeters" | "mm": return num / 914.4
        case "centimeter" | "centimeters" | "cm": return num / 91.44
        case "meter" | "meters" | "m": return num * 1.094
        case "kilometer" | "kilometers" | "km": return num * 1094  

#This function converts other units to Yards.        
def getMiles(unit, num):
    match unit.lower():
        case "inch" | "inches" | "in": return num / 63360
        case "feet" | "feetss" | "ft": return num / 5280
        case "yard" | "yards" | "yd": return num / 1760
        case "micrometer" | "micrometers": return num / 1.609e+9
        case "millimeter" | "millimeters" | "mm": return num / 1.609e+6
        case "centimeter" | "centimeters" | "cm": return num / 160900
        case "meter" | "meters" | "m": return num / 1609
        case "kilometer" | "kilometers" | "km": return num / 1.609

#This function converts other units to Micrometer. 
def getMicrometer(unit, num):
    match unit.lower():
        case "inch" | "inches" | "in": return num * 25400
        case "feet" | "feetss" | "ft": return num * 304800
        case "yard" | "yards" | "yd": return num * 914400
        case "mile" | "miles": return num * 1.609e+9
        case "millimeter" | "millimeters" | "mm": return num * 1000
        case "centimeter" | "centimeters" | "cm": return num * 10000
        case "meter" | "meters" | "m": return num * 1e+6
        case "kilometer" | "kilometers" | "km": return num * 1e+9

#This function converts other units to Millimeter. 
def getMillimeter(unit, num):
    match unit.lower():
        case "inch" | "inches" | "in": return num * 25.4
        case "feet" | "feetss" | "ft": return num * 304.8
        case "yard" | "yards" | "yd": return num * 914.4
        case "mile" | "miles": return num * 1.609e+6
        case "micrometer" | "micrometers": return num / 1000
        case "centimeter" | "centimeters" | "cm": return num * 10
        case "meter" | "meters" | "m": return num * 1000
        case "kilometer" | "kilometers" | "km": return num * 1e+6

#The following remarks are for future additions
    
    #This function converts other units to milligrams
    #This function converts other units to kilograms
    #This function converts other units to miles
    #This function converts other units to feet
    #This function converts other units to inches
    #This function converts other units to kilometers
    #This function converts other units to meters
    #This function converts other units to centimeters
    #This function converts other units to millometer
    #This function converts other units to natutical miles
    #liters
    #mL
    #cu
    #acre/hectare/ sqmi
    
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
    print(f'Converting {args.num1} {args.unit_from} {args.operation} {args.unit_to}. Please wait....\n')

    if args.unit_to in ['Teaspoon', 'Teaspoons', 'teaspoons', 'teaspoon', 'Tsps', 'tsps', 'Tsp', 'tsp', 'tsps', 'Tsp.', 'tsp.']:
        result = getTsp(args.unit_from, args.num1)
        result_x = decimal.Decimal(result)
        result_y = result_x.quantize(decimal.Decimal('0.00'))
        rprint(f'The result is {result_y} {args.unit_to}.')

    elif args.unit_to in ['Tablespoon', 'Tablespoons', 'tablespoon', 'tablespoons', 'Tbsps', 'tbsps', 'Tbsp.', 'tbsp', 'tbsp.', 'Tbs', 'tbs']:
        result = getTbsp(args.unit_from, args.num1)
        result_x = decimal.Decimal(result)
        result_y = result_x.quantize(decimal.Decimal('0.00'))
        rprint(f'The result is {result_y} {args.unit_to}.')

    elif args.unit_to in ['fluidounces', 'floz', 'floz']:
        result = getFloz(args.unit_from, args.num1)
        result_x = decimal.Decimal(result)
        result_y = result_x.quantize(decimal.Decimal('0.00'))
        rprint(f'The result is {result_y} {args.unit_to}.')

    elif args.unit_to in ['Cups', 'cups', 'Cup', 'cup', 'C.', 'c.']:
        result = getCups (args.unit_from, args.num1)
        result_x = decimal.Decimal(result)
        result_y = result_x.quantize(decimal.Decimal('0.00'))
        rprint(f'The result is {result_y} {args.unit_to}.')

    elif args.unit_to in ['Pints', 'pints', 'Pint', 'pint', 'Pt', 'PT']:
        result = getPints (args.unit_from, args.num1)
        result_x = decimal.Decimal(result)
        result_y = result_x.quantize(decimal.Decimal('0.00'))
        rprint(f'The result is {result_y} {args.unit_to}.')

    elif args.unit_to in ['Qt', 'Qts', 'qt', 'qts', 'Quart', 'Quarts', 'quart', 'quarts' 'qt.']:
        result = getQuarts (args.unit_from, args.num1)
        result_x = decimal.Decimal(result)
        result_y = result_x.quantize(decimal.Decimal('0.00'))
        rprint(f'The result is {result_y} {args.unit_to}.')
        
    elif args.unit_to in ['F', 'f', 'fehrenheit', 'Fehrenheit']:
        result = getF (args.unit_from, args.num1)
        result_x = decimal.Decimal(result)
        result_y = result_x.quantize(decimal.Decimal('0.00'))
        rprint(f'The result is {result_y} {args.unit_to}.')
        
    elif args.unit_to in ['Celcius', 'celcius', 'C', 'c']:
        result = getC (args.unit_from, args.num1)
        result_x = decimal.Decimal(result)
        result_y = result_x.quantize(decimal.Decimal('0.00'))
        rprint(f'The result is {result_y} {args.unit_to}.')

    elif args.unit_to in ['K', 'k', 'Kelvin', 'kelvin', 'degK']:
        result = getK (args.unit_from, args.num1)
        result_x = decimal.Decimal(result)
        result_y = result_x.quantize(decimal.Decimal('0.00'))
        rprint(f'The result is {result_y} {args.unit_to}.')
    
    elif args.unit_to in ['DP', 'dp', 'duckpower', 'Duckpower']:
        result = getDuck (args.unit_from, args.num1)
        result_x = decimal.Decimal(result)
        result_y = result_x.quantize(decimal.Decimal('0.00'))
        rprint(f'The result is {result_y} {args.unit_to}.')
        
    elif args.unit_to in ['grams', 'gram', 'Grams', 'grams', 'g', 'gm', 'gm.']:
        result = getGrams (args.unit_from, args.num1)
        result_x = decimal.Decimal(result)
        result_y = result_x.quantize(decimal.Decimal('0.00'))
        rprint(f'The result is {result_y} {args.unit_to}.')
        
    elif args.unit_to in ['', 'gram', 'Grams', 'grams', 'g', 'gm', 'gm.']:
        result = getOunces (args.unit_from, args.num1)
        result_x = decimal.Decimal(result)
        result_y = result_x.quantize(decimal.Decimal('0.00'))
        rprint(f'The result is {result_y} {args.unit_to}.')
    
    else:
        print("Not a valid conversion")
