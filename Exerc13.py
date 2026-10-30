# Write a function that calculates the fine for speeding.
# It takes two parameters: the maximum speed and the measured speed.
# 0 to 10 km/h over: 53 euros
# More than 10 km/h over: 53 euros + 6 euros per km/h above 10
# More than 40 km/h over: a random amount between 80 and 4000 euros

import random   # library to generate random numbers


def speeding_fine(max_speed, measured_speed):
    excess = measured_speed - max_speed
    if excess <= 0:
        return 0
    elif excess <= 10:
        return 53
    elif excess <= 40:
        return 53 + 6 * (excess - 10)
    else:
        return random.randint(80, 4000)


print(speeding_fine(90, 85))   # 0, not speeding
print(speeding_fine(90, 95))   # 53
print(speeding_fine(90, 110))  # 53 + 6 * 10 = 113
print(speeding_fine(90, 150))  # random between 80 and 4000