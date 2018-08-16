import matplotlib.pyplot as plt

from RandomWalk import RandmWalk

rw = RandmWalk()
rw.fill_walk()

x_values = rw.x_values
y_values = rw.y_values

start_x = rw.x_values[0]
start_y = rw.y_values[0]
end_x = rw.x_values[-1]
end_y = rw.y_values[-1]

plt.plot(x_values, y_values)

# highlight the start point and end point
plt.scatter(start_x, start_y, c='green', s=100)
plt.scatter(end_x, end_y, c='red', s=100)

# hide the axis
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()