def clockangles(hour, minute):
    return abs((hour * 30 + minute * 0.5) - (minute * 6))

print("angle",clockangles(10,10))