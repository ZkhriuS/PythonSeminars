quarter = int(input("Enter quarter -> "))
signs = ['>' if quarter in (1, 4) else '<', '>' if quarter in (1, 2) else '<']
print(f"x {signs[0]} 0, y {signs[1]} 0")
