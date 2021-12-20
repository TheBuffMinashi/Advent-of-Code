file = open('/content/drive/MyDrive/Colab Notebooks/GitHub/Power.txt', 'r')

data = []
for line in file:
  line = line.strip()
  line = line.split()
  data.append(line)

data = np.concatenate([np.array(i) for i in data])
# print('All in one:', data)

# The cool thing about this part is that we want to iterate over 12 different 
# digits in 1000 binary codes. Creating the for-loops was a little challening for me. :)

sum_chars = 0
count = []

for j in range(0,len(i)):
  sum_chars = 0
  for i in data:  
    sum_chars = sum_chars + int(i[j])
  count.append(sum_chars)

# print('Times that number (1) repeated in a position:', count)

# Create an empty array to save binary digits to calculate the 'Epsilon rate'
conj = []

for k in range(0, len(count)):
  if count[k] > 500:
    count[k] = 1
    conj.append(0)
  else:
    count[k] = 0
    conj.append(1)


gamma = 0
epsilon = 0

# Here's the second challenging part of the code, 
# You have to use (11 - k) to calculate the gamma and epsilon rates correctly
# Because of the way that lists are indexed in programming

for k in range(0, len(count)):
  gamma = gamma + (count[k] * (2 ** (11 - k)))
  epsilon = epsilon + (conj[k] * (2 ** (11 - k)))

print('The power consumption of the submarine:', gamma * epsilon)
