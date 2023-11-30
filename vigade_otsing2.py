print("*** Game with numbers ***")
print()

while 1:
    try:
        a = abs(int(input("Input the integer number => "))) #a = (abs(int(input("Input the integer number => "))
        break
    except ValueError:
         print("It is not a integer number")
    if a==0:
        print("There is no point in doing anything with zero")
    else:
        print("Determine how many even and how many odd digits are in the number")
        c = b = a #c==b==a
        even = 0 #paaris ==0
        odd = 0 #paaritu == 0
        while b > 0: #;
            if b % 2 == 0: #=
                even += 1 #paaris =+ 1
            else:
                odd += 1 #paaritu =+ 1
            b = b // 10    
            print("Even digits:", even) #print("Чётных цифр:"paaris)
            print("Odd digits:", odd) #print("Нечётных цифр:"paaritu)    
         
        
        print("*FLIP IT OVER* the entered number")
        print()
        b = 0
        while a > 0: #ne bqlo :
            number = a % 10
            a = a // 10
            b = b * 10
            b =+ number
        print("*The reversed* number", b)
        print()
        
        print("Testing the Syracuse hypothesis") #print(("Проверяем гипотезу Сиракуз")
        print()
        if c % 2 == 0: #if c % 2 = 0:
            print("c - the even number. Devide by 2.")
        else:
            print("c - the odd number. Multiply by 3, add 1 and devide by 2.")
        while c != 1:
            if c % 2 == 0: #if c % 2 = 0:
                c == c / 2
            else:
                c == (3*c + 1) / 2
            print(c, end = " ")
                
        print("Hypothesis is True") #print("Гипотеза верна'')