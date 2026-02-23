import numpy as np
whichVector = 1
u = []
v = []
while(whichVector < 3):
    inp = input("Enter a number to go into vector " + str(whichVector) + ("\nPress enter once completed to move to next vector\n:" if whichVector == 1 else "\nPress enter to calculate dot product\n:"))
    if(inp != ""):
        if(whichVector == 1):
            u.append(int(inp))
        else:
            v.append(int(inp))
    else:
        whichVector += 1
print(np.dot(u,v))