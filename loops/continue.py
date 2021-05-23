
"""
Continue significa:

    pare ESSA ITERAÇÃO, e vá para a próxima!
"""


for number in range(5):
    
    print('number = ', number)
    if number%2 == 0: 
        print(number, ' é par')
    else:
        print('entrou continue, pulando ', number)
        continue
    print(number, ' era par')
    

