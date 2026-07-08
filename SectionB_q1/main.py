from rules.rules import rules
from layout.shapes import Shape
from drc.checks import check_width, check_area

shape1 = Shape("metal1", 0.05, 15)
print("Shape 1:")
print(" Width check:", check_width(shape1, shape1.layer, rules))
print(" Area check:", check_area(shape1, shape1.layer, rules))

shape2 = Shape("metal2", 0.005, 0.01)
print("Shape 2:")
print(" Width check:", check_width(shape2, shape2.layer, rules))
print(" Area check:", check_area(shape2, shape2.layer, rules))
