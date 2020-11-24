# Matriz com as duas primeiras linhas já permutadas
matriz = [
	[ 13,  0,  1, 15 ],
	[  0,  5, -1, 4  ],
	[  1, -1, -1, 0  ]
]

# Instanciamos as variáveis com os valores iniciais
vec = [ 1, 1, 1 ]
stop = False
k = 0

# Iteramos o sistema enquanto os erros forem maiores de 1E-4
while not stop:
	new_vec = []

	# Fazemos as iterações para cada variável
	for i in range(len(matriz)):
		new_vec.append(matriz[i][-1])
		for j in range(len(matriz[i]) - 1):
			if i != j:
				new_vec[-1] -= matriz[i][j] * vec[j]
		new_vec[-1] = new_vec[-1] / matriz[i][i]

	# Avaliamos os erros
	errors = []
	for i in range(len(vec)):
		stop = True
		errors.append(abs(new_vec[i] - vec[i]))
		if abs(new_vec[i] - vec[i]) > 1E-4:
			stop = False

	# Imprimimos as tabelas
	vec = new_vec
	print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(k, vec[0], vec[1], vec[2], errors[0], errors[1], errors[2]))
	k += 1