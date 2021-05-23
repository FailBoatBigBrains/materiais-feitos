idade_adulta = 21
idade_adolescente = 12
idade_crianca = 4
idade_bebe = 0


idades = {
    'adulto': [21, 'infinito'],
    'adolescente: [12, 21],
    'crianca': [4, 12],
    'bebe': [0, 4]
}


alguem_tem_x_anos = 5

idade = 5


# se
if idade >= 21:
    print('sou adulto!')
# se não, se
elif idade >= 12:
    print('sou adolescente!')
# se não, se
elif idade >= 4:
    print('sou criança!')
# se não, se
elif idade >= 0:
    print('sou bebe!')
# se não!
else:
    print('não é possível!')

if idade >= 50:
    print('sou idoso')
else:
    print('não sou idoso!')
