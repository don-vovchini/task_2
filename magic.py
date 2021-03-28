print("Для завершения работы отправьте пустую строку")
n = input("Введите число не меньше 4 и не больше 1000: ")
while len(n) != 0:
    try:
        n = int(n)
    except ValueError:
        n = input("Введите число не меньше 4 и не больше 1000: ")
    else:
        mat = [[0]*n for i in range(n)]
        l = 0
        if n % 2 > 0:
            mat[n//2][n//2] = n ** 2
        for i in range(n // 2):
            print(i)
        for i in mat:
            print(*i)
        print("Для завершения работы отправьте пустую строку")
        n = input("Введите число не меньше 4 и не больше 1000: ")