#Defined checks for Width, Spacing and Enclosure.
def check_width(shape, layer, rules):
    if shape.width < rules[layer]["minWidth"]:
        return f"{layer} minimal width error."
    return "Pass"

def check_spacing(shape, shape2, layer, rules):
    if distance(shape1, shape2) < rules[layer]["minSpacing"]:
        return f"{layer} spacing error."
    return "Pass"

def check_area(shape, layer, rules):
    if shape.area < rules[layer]["minArea"]:
        return f"{layer} minimum area error."
    return "Pass"

def check_enclosure(shape, shape2, rules):
    if enclosure(layer, via) < rules["minEnclosure"]:
        return "Enclosure error."
    return "Pass"
