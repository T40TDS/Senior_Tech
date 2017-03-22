from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =[1,2,3,4,5,6,7,8,9,10]
y =[5,6,2,3,13,4,1,2,4,8]
z =[2,3,3,3,5,7,9,11,9,10]

for i in range(0,1000):
	ax.scatter(i,i,i, c = "r", marker = 'o')


ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()