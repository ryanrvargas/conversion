#github.com/ryanrvargas

def getTsp(unit, num):
    match unit.lower():
        case "ounces" | "oz":s
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
            
def getOzs(unit, num):
    match unit.lower():
        case "tsp":s
            return num * .16
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
            

