import string

#Вводим данные

g = input("Пожалуйста, введите температуру в градусах Цельсия или Фаренгейта. (например, 40C или 150.5F): ")
g = g.strip()

#Проверяем корректность ввода

grad = ("C", "F",)
num = g[0:-1]


if  len(g) < 2:
    print("Некорректный ввод")
    exit(1)

if g[-1] not in grad:
    print("Некорректный ввод")
    exit(1)  
        
if not num.isdigit: 
    print("Некорректный ввод")
    exit(1)
    
#Переводим строку в число

m = float(num)

#Считаем по формулам, выводим ответ

if g[-1] == grad[0]:
    answer = 9/5*m+32
    print (answer, grad[-1])
    
elif g[-1] == grad[-1]:
    answer = 5/9*(m-32)
    print (answer, grad[0])