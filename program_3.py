coords = [float(input("Enter x -> ")), float(input("Enter y -> "))]
if coords[0]*coords[1] > 0:
    print(f"({coords[0]}, {coords[1]}) - {1 if coords[0] > 0 else 3} quarter")
elif coords[0]*coords[1] < 0:
    print(f"({coords[0]}, {coords[1]}) - {4 if coords[0] > 0 else 2} quarter")
else:
    print("Point is on axis")
