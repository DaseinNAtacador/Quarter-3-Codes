temperature = [[24, 24, 22, 24, 24, 25, 15],
               [24, 24, 24, 24, 26, 24, 25],
]

cities = ["Davao, Manila"]

temperature_total = []

for i in range(len(temperature)):  
    total = 0
    highest = temperature[i][0]
    lowest = temperature[i][0]

    for j in range(len(temperature[i])):
        total += temperature[i][j]
        if temperature[i][j] > highest:
            highest = temperature[i][j]
        if temperature[i][j] < lowest:
            lowest = temperature[i][j]

    temperature_total.append(total)
    print(temperature[i], "total temperature:", total)

average = total / len(temperature[i])

print(
    "| Total temperature: ", total,
    "| Average: ", average,
    "| Min: ", lowest,
    "| Max: ", highest
)