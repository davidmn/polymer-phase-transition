import random
import math

numbers = []
a = []

for i in range(100):
	numbers.append(random.random())

total = sum(numbers)

for element in numbers:
	a.append(element / total)

for i in range(len(numbers)):
	print numbers[i],a[i]

print sum(a)