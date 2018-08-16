import matplotlib.pyplot as plt

# squares = [1, 4, 9, 16, 25]
# plt.plot(squares, lineWidth=5)

x_values = [1,2,3,4,5]
y_values = [1, 4, 9, 16, 25]

plt.plot(x_values, y_values, linewidth=5)

# set the display settings.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()
