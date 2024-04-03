a = int(input("Введите день (DD):"))
b = int(input("Введите месяц (MM):"))
c = int(input("Введите год (YYYY):"))
def numer (a,b,c):
    otrezat = c % 100
    if a*b==otrezat:
        return True
    else:
        return False
print (numer(a,b,c))

