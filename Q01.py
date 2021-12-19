import csv
import numpy as np


y = []

# Open the csv file and read the data
with open('Measurment.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      y.append(row)

      
# Convert a list of lists to a single list using NumPy 
depth = np.concatenate([np.array(i) for i in y])

# Convert data from string to integer
depth = [int(i) for i in depth]

# Count the number of times that the depth increased
count = 0
for i in range(1, len(depth)):
  old_x = depth[i-1]
  x = depth[i]
  # print(x)
  if x > old_x:
    count += 1

print(count)
