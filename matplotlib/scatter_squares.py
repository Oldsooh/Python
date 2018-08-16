import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, s=40)

# no edge color specifed
# plt.scatter(x_values, y_values, s=40, edgecolors='none', c='green')

# using color maps
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40)


plt.title('Scatter points')
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

# save figure to local file
plt.savefig('matplotlib/test_files/scatter_plot.png', bbox_inches='tight')

# show figure
plt.show()

