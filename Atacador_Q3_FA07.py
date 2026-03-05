temperature = [[24, 24, 22, 24, 24, 25, 15],
               [24, 24, 24, 24, 26, 24, 25],
]

print("Total in each row:")
print("1st: ", sum(temperature[0]), "|| 2nd: ", sum(temperature[1]))
print(" ")
print("Average in each row:")
print("1st: ", sum(temperature[0])/len(temperature[0]), "|| 2nd: ", sum(temperature[1])/len(temperature[1]))

# 1. Using a 2D array helped organize the data clearly, making it easy to differentiate between the
# different days from two sets of temperature reading from different cities.

# 2. Calculating the total and average temperatures for each row was easy because we were taught
# and because the sum() function and len() functions helped me to quickly compute the numbers.