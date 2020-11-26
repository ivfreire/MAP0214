#include <stdio.h>
#include <math.h>

// Função para o integrando do problema
float func(float x) {
	return 7 - 5 * pow(x, 4);
}

int main() {
	// Arquivo para salvar dados em tabela para uso posterior
	FILE* fptr;
	fptr = fopen("data_1a.txt", "w");

	// Loop principal iterante sobre todos os valores de p
	for (int p = 1; p < 26; p++) {
		int N = pow(2, p);	// Número de partições do intervalo

		// Fazemos a soma das áreas dos trapézios
		float sum = 0.0f;
		for (int i = 0; i < N; i++)
			sum += ( func((float)i / N) + func((float)(i+1) / N) ) * (1.0f / N) / 2;
		float error = fabs(6 - sum);	// Erro comparado com o valor obtido analiticamente: 6

		// Imprimimos a tabela com valores na tela e no arquivo de dados
		fprintf(fptr, "%d\t%f\n", p, (float)log10(error));
		printf("%d\t%d\t%f\t%f\n", p, N, sum, error);
	}

	// Finalização do algoritmo
	fclose(fptr);
	return 0;
}