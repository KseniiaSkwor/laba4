a = int(input("Введите число a:"))

def numer (a):
    if a==0:
        return "ZeroDivisionError"
    elif a<0:
        return "OtrizatelError"
    else:
        numer = 100/a
        return numer
print (numer(a))

