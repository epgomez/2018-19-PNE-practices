a, b = 0, 1
n=int(input('Enter the number of terms: '))
for i in range(n):
   print(a, end=' ')
   a, b = b, a+b
