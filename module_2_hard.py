n = int(input('Введите целое число от 3 до 20: '))
def get_password(number):
    pas = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                pas += str(i) + str(j)
    return pas
result = get_password(n)
print('Пароль:', result)
