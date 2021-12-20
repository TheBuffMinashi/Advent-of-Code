# Open the csv file and read the data
forward = 0
sum_forward = 0
up = 0
sum_up = 0
down = 0
sum_down = 0

with open('Direction.csv', 'r') as file:
  lines = file.readlines()
  for line in lines:
    sline = line.strip() 
    sline = sline.split(' ')

    if sline[0] == 'forward':
      forward += 1
      sum_forward = sum_forward + int(sline[1])

    elif sline[0] == 'up':
      up += 1
      sum_up = sum_up + int(sline[1])

    elif sline[0] == 'down':
      down += 1
      sum_down = sum_down + int(sline[1])

print('Forward: ', forward, '| Up: ', up, '| Down: ', down)
print('Total Forward: ', sum_forward, '|Total Up: ', sum_up, '| Total Down: ', sum_down)
final_depth = sum_down - sum_up
print(final_depth * sum_forward)
