a=int(input("Введите число a: "))
def numer (a):
    if a % 3==0:
        yes="делится на 3"
        return yes
    else:
        noy = "не делится на 3"
        return noy
print (numer(a))

