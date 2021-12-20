# Open the csv file and read the data
forward = []
up = []
aim = 0
down = []
depths = []

with open('/content/drive/MyDrive/Colab Notebooks/GitHub/Direction.csv', 'r') as file:
  lines = file.readlines()
  for line in lines:
    sline = line.strip() 
    sline = sline.split(' ')

    if sline[0] == 'forward':
      forward.append(int(sline[1]))
      depth = aim * int(sline[1])
      depths.append(depth)

    elif sline[0] == 'up':
      up.append(int(sline[1]))
      aim = aim - int(sline[1])

    elif sline[0] == 'down':
      down.append(int(sline[1]))
      aim = aim + int(sline[1])
      
print('Forward: ', len(forward), '       | Up: ', len(up), '       | Down: ', len(down))
print('Total Forward: ', sum(forward), '| Total Up: ', sum(up), '| Total Down: ', sum(down))
print('Current depth:', sum(depths))
print('Answer: ', sum(forward) * sum(depths))
