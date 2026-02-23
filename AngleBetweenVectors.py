import numpy as np
import math

whichVector = 1
u = []
v = []
while(whichVector < 3):
    inp = input("Enter a number to go into vector " + str(whichVector) + ("\nPress enter once completed to move to next vector\n:" if whichVector == 1 else "\nPress enter to calculate angle\n:"))
    if(inp != ""):
        if(whichVector == 1):
            u.append(int(inp))
        else:
            v.append(int(inp))
    else:
        whichVector += 1

dotProduct = np.dot(u,v)
uNorm = math.sqrt(np.dot(u,u))
vNorm = math.sqrt(np.dot(v,v))
cosTheta = dotProduct/(uNorm * vNorm)
theta = math.acos(cosTheta)
print("The angle between the vectors is:", theta, "Radians or", np.degrees(theta), "Degrees")