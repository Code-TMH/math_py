print(" - Quadrant position finding -")
print("           ( X,Y )")
print()
print("              |        ")
print("         Q2   |   Q1   ")
print("       (-,+)  |  (+,+) ")
print("              |        ")
print("      -----------------")
print("              |        ")
print("         Q3   |   Q4   ")
print("       (-,-)  |  (+,-) ") 
print("              |        ")
print()
print("Let 1 be (+) and  2 be (-).")
print()

user_input_x = int(input("Enter X: "))
user_input_y = int(input("Enter Y: "))
print()

if user_input_x == 1 and user_input_y == 1:
    print("Quadrant 1")

elif user_input_x == 2 and user_input_y == 1:
    print("Quadrant 2")

elif user_input_x == 2 and user_input_y == 2:
    print("Quadrant 3")

elif user_input_x == 1 and user_input_y == 2:
    print("Quadrant 4")
