'''
Фибоначчи с рекурсией (очень долго выполняется при больших значениях n)

def fib_func(x):
    if x == 1:
        return 0
    if x == 2:
        return 1

    return fib_func(x-1) + fib_func(x-2)

'''


'''
Числа Фибоначчи
С циклом и массивом

'''

fibonacci = [0, 1]

n = 70 # n = input("Введите граничное значение")

for i in range(2, n):
    next_fib = (fibonacci[i-1] + fibonacci[i-2])
    fibonacci.append(next_fib)

if n <= 0:
    print("Ошибка, число меньше 1")
elif n == 1:
    print(fibonacci[0])
elif n == 2:
    print(fibonacci[0:2])
else:
    print(fibonacci)