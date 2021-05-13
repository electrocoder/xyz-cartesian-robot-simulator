from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import time

ax = plt.figure().add_subplot(projection='3d')
# X, Y, Z = axes3d.get_test_data(0.05)


# cset = ax.contour(10, 10, 10, cmap=cm.coolwarm)  # Plot contour curves
# ax.clabel(cset, fontsize=9, inline=True)


# ax.legend()

ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_zlim(-100, 100)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
# ax.view_init(elev=20., azim=-35)

plt.plot(5, 6, 3, 'ro')

plt.pause(1)

for i in range(5):
    x = input("x: ")
    plt.cla()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.plot(int(x), i, i, 'ro')
    plt.pause(1)

print("end")
plt.show()
