from rules.rules import rules
from layout.shapes import Rect
from drc.checks import check_area, check_spacing, check_width
from helper.printValues import printShapeValues

rectangles = []

while(True):
    userChoice = input("Enter your choice:\n1. Add rectangle.\n2. Print values.\n3. Run DRC.\n4. Exit the program.\n")

    if userChoice == '1':
        layer = input("Enter rectangle layer (m1, m2 or v1):  ")
        if layer == 'm1' or layer == 'metal1':
            rectLayer = 'metal1'
        elif layer == 'm2' or layer == 'metal2':
            rectLayer = 'metal2'
        elif layer == 'v1' or layer == 'via1':
            rectLayer = 'via1'
        else:
            print("Invalid layer. Please select valid layer.")
            continue
        w = float(input("Insert metal width (um): "))
        l = float(input("Ïnsert metal length (um): "))
        pointX = float(input("Insert base point coordinate (X): "))
        pointY = float(input("Insert base point coordinate (Y): "))
        rectangles.append(Rect(rectLayer, w, l, pointX, pointY))
        print(f"Rectangle on layer {rectLayer}, created sucsessfully.")
        
    elif userChoice == '2':
        for i, rect in enumerate(rectangles):
            print(f"Checking for rectangle rect{i}:")
            printShapeValues(f'rect{i}', rect)

    elif userChoice == '3':
        for i, rect in enumerate(rectangles):
            print(f"Checking rect{i}: ")
            print("Width check:", check_width(rect, rect.layer, rules))
            print("Area check:", check_area(rect, rect.layer, rules))

    elif userChoice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid input. Select valid input.\n")
        continue

print("Process finished.\n")        
