#logical operators
#       OR = at least one condition must be true
#       AND = both conditions must be true
#       NOT = inverts the conditions (not false, not true)

temp = 25
is_sunny = False
if temp >= 28 and is_sunny:
    print("It is hot outside.")
    print("It is sunny.")
elif temp <= 0 and is_sunny:
    print("It is COLD outside.")
    print("It is sunny.")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside.")
    print("It is sunny.")
elif temp >= 28 and not is_sunny:
        print("It is hot outside.")
        print("It is cloudy.")
elif temp <= 0 and not is_sunny:
        print("It is COLD outside.")
        print("It is cloudy.")
elif 28 > temp > 0 and not is_sunny:
        print("It is WARM outside.")
        print("It is cloudy.")