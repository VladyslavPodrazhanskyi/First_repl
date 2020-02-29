n_1 = int(input('input first number: '))
n_2 = int(input('input second number: '))
n_3 = int(input('input third number: '))

if n_1 == n_2 == n_3:
    print(3)
elif n_1 == n_2 or n_1 == n_3 or n_2 == n_3:
    print(2)
else:
    print(0)


