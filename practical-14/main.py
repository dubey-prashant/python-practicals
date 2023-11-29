import matplotlib.pyplot as plt

# Data for the line chart
x1 = [1, 2, 3, 4, 5]
y1 = [1, 2, 4, 8, 16]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x1, y1, 'o-')
plt.title('Line chart')
plt.xlabel('x')
plt.ylabel('y')

# Data for the bar graph
x2 = ['A', 'B', 'C', 'D', 'E']
y2 = [5, 7, 3, 8, 6]

plt.subplot(1, 2, 2)
plt.bar(x2, y2)
plt.title('Bar graph')
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.tight_layout()
plt.show()
