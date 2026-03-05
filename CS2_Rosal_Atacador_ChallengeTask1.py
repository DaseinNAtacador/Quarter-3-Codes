temperature = [[24, 24, 22, 24, 24, 25, 15],
               [24, 24, 24, 24, 26, 24, 25],
]

cities = ["Davao", "Baguio"]

totals = []

# Calculate total temperature for each city
for i in range(len(temperature)):
    total = sum(temperature[i])
    totals.append(total)
    print(cities[i], "total temperature:", total)

# Find highest and lowest totals
highest_total = max(totals)
lowest_total = min(totals)

# Identify city with highest total
highest_index = totals.index(highest_total)
highest_city = cities[highest_index]

print("City with highest total temperature:", highest_city)
print("Highest total temperature:", highest_total)

# Display difference
difference = highest_total - lowest_total
print("Difference between highest and lowest total:", difference)