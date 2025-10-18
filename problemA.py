import math

## Speed range (distance/time)
def v(int):
    v >= 1
    v <= 100000

## Number of corners
def n(int):
    n >= 3
    n <= 500

## X and Y coordinates of vertex
def x(int):
    x >= 0

def y(int):
    y <= 100000

## Range of X and Y
x_userinput = int(input("Enter any coordinate number for x: "))
y_userinput = int(input("Enter any coordinate number for y: "))
locationinput = int(input("How many locations have fire right now?! "))

# If statement for X rule
if x_userinput >= 0 and x_userinput <= 100000:
    # Y input value
    if y_userinput >= 0 and y_userinput <= 100000:
        pass
    else:
        print("Your Y value is not meeting the rule!")
else:
    print("Your X value is not meeting the rule!")

# Square root value
sqr = 1 / 2

# Distance for X
distance1 = float((x_userinput * x_userinput) ** sqr)

# Distance for Y
distance2 = float((y_userinput * y_userinput) ** sqr)

# Total distance (scaled by number of fire locations)
Final_distance = (distance1 + distance2) * locationinput;

# Time speed per second
Time = 0.1

# Speed calculation formula
firespeed = Final_distance / Time

# Final speed output
print("Final Fire Speed in the forest:", firespeed, "per second")
