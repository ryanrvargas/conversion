#github.com/ryanrvargas

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
