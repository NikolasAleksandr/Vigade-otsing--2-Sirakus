print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisestage täisarv => "))) #Поменял порядок слов и правильно поставил скобки
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi ette võtta")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrame, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c = b = a # Нужен один знак равенства
    paaris = 0 # Лишние знаки равенства
    paaritu = 0
    while b > 0: # Вместо ; нужно :
            if b % 2 == 0: # Нужно писать 2 знака равенства
                    paaris += 1 # равенство и плюс надо было поменять местами
            else:
                    paaritu += 1
            b = b // 10 
    
    print("Paarisarvud:",paaris) # Нужна была запятая
    print("Paarituarvud:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörame* sisestatud number")
    print()
    b=0
    while a > 0: # Вместо ; нужно :
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #Сдвинул на пробел назад ,равенство и плюс надо было поменять местами
    print("*Ümberpööratud* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Siracuse hüpoteesi testimine")
    print()
    if c % 2 == 0: #Добавил знак равенства
        print("c on paarisarv. Jagame 2-ga.")
    else:
        print("c on paaritu arv. Korrutame 3-ga, lisame 1 ja jagame 2-ga.")
    while c != 1:
            if c % 2 == 0: #Добавил знак равенства
                    c = c // 2 # Убрал знак равенства и добавил слэш для целосного деления
            else:
                    c = (3 * c + 1) // 2 # Убрал знак равенства и добавил слэш для целосного деления
            print(c, end=" ") # не хватало ковычек и пробела 
    print()
    print("Hüpotees on õige")
    #Проверил примеры работы программы в окне Shell, все работает
