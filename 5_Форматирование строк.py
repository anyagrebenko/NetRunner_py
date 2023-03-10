text1 = "Hi, my name {0}".format("Trip") #Пример использования метода format
print (text1)

text2 = "---{0}---" #Значения, которые подставляются в фигурные скобки, могут быть разного типа. Например, это может быть строка, число или список или даже словарь
print (text2.format([10, 20, 30, 40, 50]))
print (text2.format(500_000))
print (text2.format({"name" : "Trip", "sex" : True}))

list1 = [10, 20, 30] #Можно вывести данные столбцами одинаковой ширины по 15 символов с выравниванием по правой стороне
a = list1[0]
b = list1[1]
c = list1[2]
print ("{2:>5} {0:>5} {1:>5}".format(a, b, c))

ip_sample = """
IP address :
{0}
"""
ip1 = "345.624.534.5"
ip2 = "423.234.456.7"
ip3 = "234.456.234.2"
ip4 = "745.523.235.8"
print (ip_sample.format(ip1)) #Шаблон для вывода может быть и многострочным

text3 = "Pay me {:.3f}" #Например, можно указать, сколько цифр после запятой выводить
print (text3.format(500_000 / 25))

print ("{0:b} {1:b} {2:b}".format(10, 20, 30)) #С помощью форматирования строк можно конвертировать числа в двоичный формат

text4 = "---{ip}---   ---{mask}---" #В фигурных скобках можно указывать имена. Это позволяет передавать аргументы в любом порядке, а также делает шаблон более понятным
print (text4.format(ip = ip1, mask = 50)) 

ip_template = """
IP address
{0} {1} {2} {3}
{0:>15} {1:>15} {2:>15} {3:>15}
{0:>25} {1:>25} {2:>25} {3:>25}
"""
print (ip_template.format(ip1, ip2, ip3, ip4))