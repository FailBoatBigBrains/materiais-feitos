
"""
Break significa:

    pare ESSA iteração mas NÃO vá a proxima iteração!
"""


for number in range(5):
    print('number = ', number)
    if number%2 == 0: 
        print(number, ' é par')
    else:
        print('entrou break, PARE ESSE FOR')
        break
    print(number, ' era par')

