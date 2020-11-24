# Definimos a matriz do sistema linear
matrix = [
	[  0,  5, -1,  4 ],
	[ 13,  0,  1, 15 ],
	[  1, -1, -1,  0 ]
]
print(matrix)

# Fazemos o pivotamento parcial da função para que não existam zeros na diagonal principal
for i in range(len(matrix)):
	if matrix[i][i] == 0:
		for j in range(1, len(matrix) - i, 1):
			if matrix[i + j][i] != 0:
				matrix[i], matrix[i + j] = matrix[i + j], matrix[i]
				print(matrix)
print('Done!')

# Agora, fazemos combinações lineares na matriz para encontrar a matriz superior
for col in range(0, len(matrix[0]) - 1, 1):
	for lin in range(col + 1, len(matrix), 1):
		if matrix[lin][col] != 0:
			for i in range(col, len(matrix)):
				if i != lin:
					if matrix[i][col] != 0:
						factor = - matrix[lin][col] / matrix[i][col]
						for j in range(len(matrix[lin])):
							matrix[lin][j] += factor * matrix[i][j]
						print(matrix)
print('Done!')

# Resolvemos o sistema:
vec = []

for i in range(1, len(matrix) + 1, 1):
	current = matrix[-i][-1]

	for j in range(i - 1):
		current -= matrix[-i][-j - 2] * vec[j]

	vec.append(current / matrix[-i][-i - 1])

print(vec[::-1])