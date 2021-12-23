import numpy as np
file = open('Power.txt', 'r')

data = []
for line in file:
  line = line.strip()
  line = line.split()
  data.append(line)

data = np.concatenate([np.array(i) for i in data])

ones = []
zeros = []

for item in data:
  if item[0] == '1':
    ones.append(item)
  else:
    zeros.append(item)

if len(zeros) > len(ones):
  Oxy_rate = zeros 
else:
  Oxy_rate = ones
  
for j in range(0, 12):
  Oxy_ones  = []
  Oxy_zeros = []

  for item in Oxy_rate:
    if item[j] == '1':
      Oxy_ones.append(item)
    else:
      Oxy_zeros.append(item)

  if len(Oxy_zeros) > len(Oxy_ones):
    Oxy_rate = Oxy_zeros
  else:
    Oxy_rate = Oxy_ones

print('Oxygen generator Code: ', Oxy_rate)

Oxygen = 0
for k in range(0, len(Oxy_rate[0])):
  Oxygen = Oxygen + (int(Oxy_rate[0][k]) * (2 ** (11 - k)))

print('Oxygen generator Rate: ', Oxygen)

ones = []
zeros = []

for item in data:
  if item[0] == '1':
    ones.append(item)
  else:
    zeros.append(item)

if len(zeros) < len(ones):
  CO2_rate = zeros
else:
  CO2_rate = ones
  

for j in range(1, 12):
  if len(CO2_rate) == 1:
    break
  CO2_ones  = []
  CO2_zeros = []

  for item in CO2_rate:
    if item[j] == '0':
      CO2_ones.append(item)
    else:
      CO2_zeros.append(item)

  if len(CO2_zeros) < len(CO2_ones):
    CO2_rate = CO2_zeros
  else:
    CO2_rate = CO2_ones

print('CO2 generator Code: ', CO2_rate)

CO2 = 0
for k in range(0, len(CO2_rate[0])):
  CO2 = CO2 + (int(CO2_rate[0][k]) * (2 ** (11 - k)))

print('The CO2 generator rate:', CO2)

print('Answer: ', CO2 * Oxygen)
