import re
print("Для завершения работы отправьте пустую строку")
a = input("Введите выражение: ")
while len(a) != 0:
    find = input("Введите скобки для проверки: ")
    find = re.findall(r'[(\[{<]', find)
    print(find)
    print("Для завершения работы отправьте пустую строку")
    a = input("Введите выражение: ")
