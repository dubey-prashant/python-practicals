import matplotlib.pyplot as plt

# Data for the histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

plt.hist(data, bins=5, edgecolor='black')

plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()
