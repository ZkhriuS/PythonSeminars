from cmath import sqrt


points = []
for i in range(2):
    points.append([float(input(f"Enter x{i+1} -> ")),
                   float(input(f"Enter y{i+1} -> "))])
distance = sqrt((points[0][0]-points[1][0])*(points[0][0]-points[1][0]) +
                (points[0][1]-points[1][1])*(points[0][1]-points[1][1])).real
print(f"Distance between points is {distance}")
