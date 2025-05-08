# Code for visualising the population growth using for and while loops

import matplotlib.pyplot as plt #Importing the module for plotting

# Assumptions
initial_population = 100
growth_rate = 0.05  # 5% per year
years = 20

# Using a for loop
population_for = [initial_population]
for year in range(1, years + 1):
    new_population = population_for[-1] * (1 + growth_rate)
    population_for.append(new_population)

# Using a while loop
population_while = [initial_population]
year = 1
while year <= years:
    new_population = population_while[-1] * (1 + growth_rate)
    population_while.append(new_population)
    year += 1

# Visualization/Code for plot
plt.figure(figsize=(10, 6))
plt.plot(range(0, years + 1), population_for, label='For Loop Simulation', marker='o')
plt.plot(range(0, years + 1), population_while, label='While Loop Simulation', marker='x', linestyle='--')
plt.title('Population Growth Over Time')
plt.xlabel('Years')
plt.ylabel('Population')
plt.grid(True)

