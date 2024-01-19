import matplotlib.pyplot as plt

x_values_line = [1, 6]
y_values_line = [2, 8]

x_values_dotted_line = [1, 2, 6, 8]
y_values_dotted_line = [3, 8, 1, 10]

plt.plot(x_values_line, y_values_line, label='Line', marker='o')
plt.plot(x_values_dotted_line, y_values_dotted_line, label='Dotted Line', linestyle='dotted', marker='o')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line and Dotted Line in a Diagram')

plt.legend()

plt.grid(True)
plt.show()