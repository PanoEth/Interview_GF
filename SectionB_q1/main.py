from rules.rules import rules
from layout.shapes import Rect
from drc.checks import check_area, check_spacing, check_width

while(True):
    userChoice = input("Enter your choice:\n1. Add rectangle.\n2. Run DRC check.\n3. Exit the program.\n")

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
        count = int(0)
        rectangles = []
        rectangles.append(Rect(rectLayer, w, l, pointX, pointY))
        print(f"Rectangle on layer {rectLayer}, created sucsessfully.")
        count += 1

    elif userChoice == '2':
        print("Running check")
    
    elif userChoice == '3':
        print("Exiting...\n")
        break
    else:
        print("Invalid input. Select valid input.\n")
        continue

print("Process finished.")        
