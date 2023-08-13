while True:
    a = input("Введите число: ")
    b = input("Введите второе число: ")
    c = input("введите третье число:")
    if a.isdigit() and b.isdigit() and c.isdigit():
        if int(b) == 0:
            print("На ноль делить нельзя")
        else:
            print(int(a)/int(b)/int(c))
            break
    else:
        print("Поддерживаются только числа")