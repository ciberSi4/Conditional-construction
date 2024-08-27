# Условная конструкция. Операторы if, elif, else

first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")
print("Вами введены числа: ", first, second, third)
if first == second == third:
    print("Все три числа равны между собой: - 3")
elif first == second or second == third or first == third:
    print ("Два их трёх чисел равны между собой: - 2")
else:
    print("Равных между собой чисел нет: - 0")