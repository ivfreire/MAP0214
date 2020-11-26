#include <stdio.h>
#include <math.h>

// Número máximo de pontos gerados para análise
#define	MAX_POINTS	99999

// Função do integrando da integral presente na relação de T
double func(double x, double k) {
	return 1.0f / sqrt(1 - pow(k * sin(x), 2));
}

int main() {
	// Período para ângulos pequenos
	double T_0 = 2 * M_PI * sqrt( 1 / 9.81 );

	int N = 100;	// Número de valores de theta entre [0, pi)
	for (int i = 0; i < N; i++) {
		double S		= 0.0f;				// Soma da integral
		double theta	= M_PI * i / N;		// thata_0 inicial
		double k		= sin(theta / 2);	// Constante k

		// Iteramos sobre os pontos entre os limites de integração
		for (int j = 0; j < MAX_POINTS; j++) {
			int weight = 1;														// Peso predefinido
			if (j != 0 && j != MAX_POINTS - 1) weight = 4 - 2 * (j % 2);		// Muda o peso de acordo com j
			S += weight * func((M_PI / 2) * ((float)j / MAX_POINTS), k);		// Soma o produto do valor do ponto com o peso respectivo
		}
		S = S * ((M_PI / 2) / (MAX_POINTS - 1)) / 3;							// Faz o produto pelo fator restante

		// Calcula T para um pêndulo de 1 metro de comprimento
		double T = 4 * sqrt(1 / 9.81) * S;

		// Imprime os valore obtidos na tela
		printf("%.16f\t%.16f\n", theta, T/T_0);
	}

	// Finaliza
	return 0;
}