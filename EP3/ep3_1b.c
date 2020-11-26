#include <stdio.h>
#include <math.h>

double func(double x) {
	return 7 - 5 * pow(x, 4);
}

int main() {
	FILE* fptr;
	fptr = fopen("data_1b.txt", "w");

	for (int p = 1; p < 26; p++) {
		int N = pow(2, p);

		double sum = 0.0f;
		for (int i = 0; i < N; i++)
			sum += ( func((double)i / N) + func((double)(i+1) / N) ) * (1.0f / N) / 2;
		double error = fabs(6 - sum);

		fprintf(fptr, "%d\t%f\n", p, log10(error));
		printf("%d\t%d\t%.16f\t%.16f\n", p, N, sum, error);
	}

	fclose(fptr);
	return 0;
}