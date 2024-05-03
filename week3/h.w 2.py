import math
radius=int(input("enter the radius"))
area_square=int(input("square's perimeter"))
Circumference_circle =2 * 3.14 * radius
square_perimeter = (math.sqrt(area_square)) * 4

if Circumference_circle > square_perimeter :
    print(True)
else:
    print(False)




