import numpy as np
import math
def main():
    p=[[0],[0],[0]]
    print("enter point coordinates in frame B: ")
    for i in range(3):
         p[i][0]=int(input())
        #entering the rotation
    print("enter the rotation about ")
    x=int(input("\nx axis: "))
    y=int(input("\ny axis: "))
    z=int(input("\nz axis: "))
     
    #creating the rotation matrix in x,y,z order in initial frame
    R1=np.array([[1.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0]])
    R1[1][1]=math.cos(math.radians(x))
    R1[1][2]=0.0-math.sin(math.radians(x))
    R1[2][1]=math.sin(math.radians(x))
    R1[2][2]=math.cos(math.radians(x))
    
    R2=np.array([[0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,0]])
    R2[0][0]=math.cos(math.radians(y))
    R2[2][0]=0.0-math.sin(math.radians(y))
    R2[0][2]=math.sin(math.radians(y))
    R2[2][2]=math.cos(math.radians(y))
    
    R3=np.array([[0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,1]])
    R3[0][0]=math.cos(math.radians(z))
    R3[0][1]=0.0-math.sin(math.radians(z))
    R3[1][0]=math.sin(math.radians(z))
    R3[1][1]=math.cos(math.radians(z))
    
    R=R3@R2
    RR=R@R1
    RRR=RR.transpose()
    res=RRR@p
    print("\nThe coordinates in frame A= ",res)
    
main()
