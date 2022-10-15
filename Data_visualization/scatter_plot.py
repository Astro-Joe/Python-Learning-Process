import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = []

for x in x_values:
    Square = x**2
    y_values.append(Square)

plt.scatter(x_values, y_values, s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

#plt.axis([0, 1100, 0, 1100000])

plt.show()