#include <stdio.h>
#include <math.h>

// Função que gera um aleatório Z baseado numa semente inicial.
unsigned long int random(unsigned long int z) {
	return (1103515245 * z + 12345) % 2147483647;
}

int main() {

	int N 				= 100;			// Número total de pontos por tentativa
	unsigned long int z = 9;			// Semente inicial fornecida ao gerador randômico

	float Im[17]		= {};			// Array com valores médios de I
	float sI[17]		= {};			// Array com desvios-padrões amostrais de I
	float sIm[17]		= {};			// Array com desvios-padrões amostrais de I

	// Loop principal
	for (int i = 0; i < 17; i++) {
		int M = pow(2, i+1);	// Número de tentativas M por linha

		float I[M];				// Array com valores da área armazenados

		// Fazemos cada simulação por Monte Carlo
		for (int j = 0; j < M; j++) {
			int n = 0;		// Número de pontos abaixo do gráfico de y

			// Geração dos pontos
			for (int k = 0; k < N; k++) {
				z = random(z);						// Geramos novo z
				float x = (float)z / 2147483647;	// Geramos x baseado em z

				z = random(z);						// Geramos novo z
				float y = (float)z / 2147483647;	// Geramos y baseado em z

				// Se o ponto está abaixo de y, então incrementamos n por 1
				if (y <= pow(x, 4)) n++;
			}

			// Área do gráfico em 0 < x < 1 (a área total é unitária, portanto a área sob o gráfico é equivalente à razão dos pontos internos e pontos totais)
			float ratio = (float)n / N;
			I[j] = ratio;
		}
		
		// Calculamos o valor médio de I
		Im[i] = 0.0f;
		for (int j = 0; j < M; j++)
			Im[i] += I[j] / M;

		// Calculamos o desvio-padrão amostral de I
		sI[i] = 0.0f;
		for (int j = 0; j < M; j++)
			sI[i] += pow(I[j] - Im[i], 2);
		sI[i] = sqrt(sI[i] / (M - 1));

		// Calculamos o desvio-padrão da média de Im
		sIm[i] = sI[i] / sqrt(M);
	}

	// Imprimimos a tabela
	for (int i = 0; i < 17; i++)
		printf("%d\t%f\t%f\t%f\n", (int)pow(2, i+1), Im[i], sI[i], sIm[i]);

	return 0;
}
