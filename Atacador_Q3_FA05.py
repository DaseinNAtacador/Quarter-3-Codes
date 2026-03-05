Day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

Steps = [
    [4500, 5200, 4800, 5500, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

total_daily = []

for i in range(len(Day)):
    total = 0
    for h in range(len(Steps)):
        total += Steps[h][i]
    total_daily.append(total)

for j in enumerate(total_daily):
    print(f"{Day[j[0]]}: {j[1]}")

active = total_daily.index(max(total_daily))
print("Most active day: " + Day[active])
print("Most steps: " + str(total_daily[active]))