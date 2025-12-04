
velocity = float(input("Input velocity: "))
acceleration = float(input("Input acceleration: "))

length = (velocity ** 2)/(2 * acceleration)

print("The minimum runway length for this airplane is ", round(length, 2))