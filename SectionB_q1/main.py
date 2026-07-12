from rules.rules import rules
from layout.shapes import Shape
from drc.checks import check_width, check_area

shape1 = Rect ("metal1", 0.05, 15, 0.0, 0.0)
print("Shape 1:")
print(" Width check:", check_width(shape1, shape1.layer, rules))
print(" Area check:", check_area(shape1, shape1.layer, rules))
shape2 = Rect ("metal1", 0.02, 10, 0.06, 0.0)
print("Shape 2: ")
print(" Width check:", check_width(shape2, shape2.layer, rules))
print(" Area check:", check_area(shape2, shape2.layer, rules))


shape3 = Rect("metal2", 0.005, 0.01, 0.0, 0.0)
print("Shape 2:")
print(" Width check:", check_width(shape2, shape2.layer, rules))
print(" Area check:", check_area(shape2, shape2.layer, rules))
