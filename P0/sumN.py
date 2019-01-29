def sum1():
    n = input ('please enter the number you want')
    count = 0
    for i in range(int(n)+1):
        count += i
    print(count)
    return
sum1()

def sum(n):
    total = 0
    for i in range(n):
        total = total + i + 1

    return total

num = int(input('please enter n'))
print('the total sum is', sum(num))
