from rules.rules import rules
from layout.shapes import Rect
from drc.checks import check_area, check_spacing, check_width

shape1 = Rect ("metal1", 0.05, 15, 0.0, 0.0) 
print("Shape 1:")
print(" Width check:", check_width(shape1, shape1.layer, rules))
print(" Area check:", check_area(shape1, shape1.layer, rules))

shape2 = Rect ("metal1", 0.009, 15, 0.04, 0.0) 
print("Shape 2: ")
print(" Width check:", check_width(shape2, shape2.layer, rules))
print(" Area check:", check_area(shape2, shape2.layer, rules))

if shape1.layer and shape2.layer:
    layoutLayer = shape1.layer
    print("Spacing shape1 and shape2:", check_spacing(shape1, shape2, layoutLayer, rules))

shape3 = Rect("metal2", 0.005, 0.01, 0.0, 0.0)
print("Shape 2:")
print(" Width check:", check_width(shape3, shape3.layer, rules))
print(" Area check:", check_area(shape3, shape3.layer, rules))
