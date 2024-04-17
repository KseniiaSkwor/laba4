ticket =input("Введите номер билета: ")

def a(b):
    if len(b) % 2 !=0:
        return False

    polovina=len(b)//2
    fpolovina=0
    spolovina=0

    for i in range(polovina):
        fpolovina +=int(b[i])
        spolovina += int(b[i+polovina])
    return fpolovina == spolovina

print (a(ticket))


#в первую часть добавляем числа сначала, а во вторую часть первый элемент второй части
