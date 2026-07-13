from layout.shapes import Rect

def printShapeValues(name, rect):
    print(f"Shape name: {name} located on layer {rect.layer} has values:")
    print(f"Anchor point: ({rect.edgeX_left}, {rect.edgeY_bottom}). \nWidth: {rect.width} um, Length: {rect.length}um, Area: {rect.area}um^2.")
    print(f"Bottom side: ({rect.edgeX_left}, {rect.edgeY_bottom}) to ({rect.edgeX_right}, {rect.edgeY_bottom})")
    print(f"Left side: ({rect.edgeX_left}, {rect.edgeY_bottom}) to ({rect.edgeX_left}, {rect.edgeY_top})")
    print(f"Top side: ({rect.edgeX_left}, {rect.edgeY_top}) to ({rect.edgeX_right}, {rect.edgeY_top})")
    print(f"Top side: ({rect.edgeX_right}, {rect.edgeY_top}) to ({rect.edgeX_right}, {rect.edgeY_bottom})")
    print("\n")
    