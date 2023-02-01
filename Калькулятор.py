#Калькулятор


print('Калькулятор')

a=float(input('Число 1 = '))
b=float(input('Число 2 = '))
znak=input('Введите знак(+,-,*,/)')
if znak=='+':
    print(a+b)
elif znak=='-':
    print(a-b)
elif znak=='*':
    print(a*b)
elif znak=='/':
    print(a/b)
else:
    print('Неизвестная операция')
input()
