import csv
import numpy as np


y = []

# Open the csv file and read the data
with open('/content/drive/MyDrive/Colab Notebooks/Measurment.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      y.append(row)

      
# Convert a list of lists to a single list using NumPy 
depth = np.concatenate([np.array(i) for i in y])

# Convert data from string to integer
depth = [int(i) for i in depth]


# Create a while loop to iterate over depths and create 3-member groups of it
# Then, calculate sum of of every group and append it to a list
# Note that we are using .pop() method to delete the first element of the list in every iteration
# For more information about how the code works, read it please *.*
length = len(depth)
sum_depth = []

while length >= 3:
  sub_depth = depth[0] + depth[1] + depth[2]
  sum_depth.append(sub_depth)
  depth.pop(0)
  length = len(depth)
  
count = 0
for i in range(1, len(sum_depth)):
  old_x = sum_depth[i-1]
  x = sum_depth[i]
  # print(x)
  if x > old_x:
    count += 1

print(count)
