a, b = 0, 1
counter=0
n=int(input('Enter the number of terms you want to add up: '))
for i in range(n):
   a, b = b, a+b
   counter += a
print(counter)