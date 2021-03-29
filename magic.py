print("Для завершения работы отправьте пустую строку")
n = input("Введите число не меньше 4 и не больше 1000: ")
while len(n) != 0:
    try:
        n = int(n)
    except ValueError:
        n = input("Введите число не меньше 4 и не больше 1000: ")
    else:
        mat = [[0]*n for i in range(n)]
        m = 1
        if n % 2 > 0:
            mat[n // 2][n // 2] = n ** 2
        for i in range(n // 2):
            for k in range(n - 2 * i - 1):
                mat[i][k + i] = m + k
                mat[k + i][n - 1 - i] = m + k + n - 2 * i - 1
                mat[n - 1 - i][n - 1 - i - k] = m + k + 2 * (n - 2 * i - 1)
                mat[n - 1 - i - k][i] = m + k + 3 * (n - 2 * i - 1)
            m = m + 4 * (n - (1 + 2 * i))
        for i in mat:
            print(*i)
        print("Для завершения работы отправьте пустую строку")
        n = input("Введите число не меньше 4 и не больше 1000: ")
