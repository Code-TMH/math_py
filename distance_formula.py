from tkinter import*
import math

print("     ( x1,y1 )( x2,y2 )\n")
print("    - Distance formula -")
print("  _________________________")
print(" √[( x1-x2 )² + ( y1-y2 )²]\n")

x1 = int(input("Enter X1: "))
y1 = int(input("Enter Y1: "))
x2 = int(input("Enter X2: "))
y2 = int(input("Enter Y2: "))

sub_first_distance = x1 - x2
sub_second_distance = y1 - y2
first_distance = sub_first_distance ** 2
second_distance = sub_second_distance ** 2
third_distance = first_distance + second_distance
distance = math.sqrt(third_distance)

print('')

if distance ** 2 == third_distance:
    print("Answer: √{} = {:.0f}".format(third_distance,distance))

else:
    print("Answer: √{} = {:.2f}".format(third_distance,distance))
