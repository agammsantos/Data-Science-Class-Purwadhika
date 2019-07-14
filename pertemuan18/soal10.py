import numpy as np

# 3x=9
# x=?

a=np.array([[3]])
b=np.array([9])
c=np.linalg.solve(a,b)
print(c)

# x+y-z=-3
# x+2y+z=7
# 2x+y+z=4
# x=? y=? z=?

a=np.array([[1,1,-1],[1,2,1],[2,1,1]])
b=np.array([-3,7,4])
c=np.linalg.solve(a,b)
print(c)