import sys

N = int(input())
points = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

sorted_points = sorted(points, key=lambda x: (x[1], x[0]))

for point in sorted_points:
    print(point[0], point[1])