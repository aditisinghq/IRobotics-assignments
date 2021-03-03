import numpy as np
import math
def main():
	p=[[2],[3],[0]]
	#for rotation about x axis twice by 30 degrees
	r1=np.array([[1,0,0],[0, 0.5, -0.866],[0, 8.66, 0.5]])
	#for rotation about y axis by 30 degrees
	r2=np.array([[0.866,0,0.5],[0,1,0],[-0.5,0,0.866]])
	r=np.matmul(r2,r1)
	rr=r.transpose()
	res=np.matmul(rr,p)
	print(res)
main()
