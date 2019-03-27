
# I have done this exercise in two possible ways,
# one in wich the input is inside the function and one
# in which the input is outside

def sum1():
    n = input ('please enter the number you want: ')
    count = 0
    for i in range(int(n)+1):
        count += i
    print(count)
    return
sum1()

def sum(n):
    total = 0
    for i in range(n+1):
        total += i

    return total

num = int(input('please enter n: '))
print('the total sum is', sum(num))
