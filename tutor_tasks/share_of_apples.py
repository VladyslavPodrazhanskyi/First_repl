n = int(input('input number of pupils: '))
k = int(input('input quantity of apples: '))
share = k // n
basket = k % n
print(f'Every pupil receives {share} apples, {basket} apples leaves in the basket')