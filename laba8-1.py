def PowerA3(a,b):
    b=a**3
    return b
b = 0
for _ in range(5):
    while True:
        a=input("Введите число: ")
        check=a.replace('.','')
        if len(a)==1:
            if a.isdigit():
                a=float(a)
                break
        else:
            if check[1:].isdigit() and a.count('.')<=1:
                a=float(a)
                break

    print("Результат:",PowerA3(a,b),sep=" ")