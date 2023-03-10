import datetime

x = datetime.datetime(2019, 10, 1)


print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%m"))
print(x.strftime("%d"))

def formateDate(date):
    lista = []
    lista.append(date.strftime("%Y"))
    lista.append(date.strftime("%m"))
    lista.append(date.strftime("%d"))
    return "-".join(lista)


print(formateDate(x))