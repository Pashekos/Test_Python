print('Калькулятор')
    
a= input('Введите операцию с целыми числами: ')

#проверяем длину строки:
if len(a) == "" or len(a) >5 or len(a) <3: 
    print ('Введите числа от 1 до 10 и знак операции')
    
else:
    #ищем знак операции
    
    
    if '*' in a:
         znak= '*'
         delim= a.split(znak)
         a1= delim[0]
         b1= delim[1]
         
         #проверяем на числа
         if a1.isdigit() and b1.isdigit(): 
             a1=int(a1)
             b1=int(b1) 
             
             #проверяем размер чисел
             if 0<=a1<11 and 0<=b1<11:
                 
                 #проверяем количество знаков операции
                 if a.count(znak)>1: 
                     print('Нужно ввести только 1 знак операции')
                 else: print('Результат умножения: ', a1*b1)
             else: print('Введите числа от 0 до 10')
         else: print('Введите числа от 0 до 10')
         
         
    elif '+' in a:
         znak= '+'
         delim= a.split(znak)
         a1= delim[0]
         b1= delim[1]
         
         #проверяем на числа
         if a1.isdigit() and b1.isdigit(): 
             a1=int(a1)
             b1=int(b1) 
             
             #проверяем размер чисел
             if 0<=a1<11 and 0<=b1<11:
                 
                 #проверяем количество знаков операции
                 if a.count(znak)>1: 
                     print('Нужно ввести только 1 знак операции')
                 else: print('Результат сложения: ', a1+b1)
             else: print('Введите числа от 0 до 10')
         else: print('Введите числа от 0 до 10')
         
         
    elif '-' in a:
         znak= '-'
         delim= a.split(znak)
         a1= delim[0]
         b1= delim[1]
         
         #проверяем на числа
         if a1.isdigit() and b1.isdigit(): 
             a1=int(a1)
             b1=int(b1) 
             
             #проверяем размер чисел
             if 0<=a1<11 and 0<=b1<11:
                 
                 #проверяем количество знаков операции
                 if a.count(znak)>1: 
                     print('Нужно ввести только 1 знак операции')
                 else: print('Результат вычитания: ', a1-b1)
             else: print('Введите числа от 0 до 10')
         else: print('Введите числа от 0 до 10')
         
         
    elif '/' in a:
         znak= '/'
         delim= a.split(znak)
         a1= delim[0]
         b1= delim[1]
         
         #проверяем на числа
         if a1.isdigit() and b1.isdigit(): 
             a1=int(a1)
             b1=int(b1) 
             
             #проверяем размер чисел
             if b1==0:
                 print('На "0" делить нельзя!') 
             elif 0<=a1<11 and 0<b1<11:
                 
                 #проверяем количество знаков операции
                 if a.count(znak)>1: 
                     print('Нужно ввести только 1 знак операции')
                 else: print('Результат деления ', a1/b1)
             else: print('Введите числа от 0 до 10')
         else: print('Введите числа от 0 до 10')
         
         
         
         
    else: print('Неуорректный знак операции') 


