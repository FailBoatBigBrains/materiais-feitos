print("Perguntas em dict")

perguntas = {
	"Quanto é 3 + 5?": 8
}


for enunciado, gabarito in perguntas.items():
	print(enunciado)
	print(gabarito)


print("Perguntas lista de tuplas")

perguntas = [
	("Quanto é 3 + 5?", 8),
]

for estrutura_pergunta in perguntas:
	print(estrutura_pergunta[0])
	print(estrutura_pergunta[1])


print("Perguntas em lista de dicionários")

perguntas = [
	{
		"enunciado": "Quanto é 3 + 5?",
		"gabarito": 8,
		"resposta": None
	}
]

for estrutura_pergunta in perguntas:
	print(estrutura_pergunta['enunciado'])
	print(estrutura_pergunta['gabarito'])
