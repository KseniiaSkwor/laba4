try:
    n = int(input("Введите число: "))
    print(f"100 / {n} = {100/n%.0}")
except ValueError:
    print("[ОШИБКА] Нужно вводить число!")
except ZeroDivisionError:
     print("[Ошибка] Деление на ноль!")