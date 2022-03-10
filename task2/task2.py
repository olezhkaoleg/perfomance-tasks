adrs = input('circle data address ')
adrs2 = input('points data address ')

circle = []
points = []

with open(adrs) as f:
  for line in f:
    circle.append(line.strip())

with open(adrs2) as g:
  for line in g:
    points.append(line.strip())

cx = float(circle[0].split(' ')[0])
cy = float(circle[0].split(' ')[1])
r = float(circle[1])

def point_in_circle(x, y, cx, cy, r):
    return 1 if ((x - cx) ** 2 + (y - cy) ** 2) ** (1 / 2) < r else 0 if ((x - cx) ** 2 + (y - cy) ** 2) ** (1 / 2) == r else 2 

for i in points:
  x = float(i.split(' ')[0])
  y = float(i.split(' ')[1])
  print(point_in_circle(x, y, cx, cy, r))
