import matplotlib.pyplot as plt

# Generating the squares of numbers 1 to 1000
x = 1
plot_list = []

for i in range(1000):
    plot_list.append(x**2)
    x += 1

# Plot, labels
plt.plot(plot_list)

plt.title('Squares of Numbers from 1 to 1000')
plt.xlabel('Number (x)')
plt.ylabel('Square (x²)')
plt.grid(True)
