n = int(input())
m = int(input())
new_list = list(range(1, n + 1))

new_list = new_list * m
for i in range(0, len(new_list), m - 1):
  if i != 0 and new_list[i] == new_list[0]:
    break
  else:
    print(new_list[i], end = ' ')
