import math
ab_length = int(input())
bc_length = int(input())

arc_tan = math.atan(ab_length / bc_length)
degree = round(arc_tan * 180 / math.pi)

print(str(degree) + u"\N{DEGREE SIGN}")
