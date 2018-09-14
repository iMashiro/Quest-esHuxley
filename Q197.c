#include <stdio.h>
int main()
{
	int tamanho;
	int k = 0;
	scanf("%d", &tamanho);
	
	int matriz[tamanho][tamanho];
	int i = 0, j = 0;

	int aux = 0;
	int aux2 = 1;

 	while (k < (tamanho * tamanho))
 	{
 		for(i = aux, j = aux; i <= (tamanho - aux2); i++, k++)
 		{
 			scanf("%d", &matriz[i][j]);
 		}
 		for (j = aux2, i = tamanho - aux2; j <= (tamanho - aux2); j++, k++)
 		{
 			scanf("%d", &matriz[i][j]);
 		}
 		aux2++;
 		for (i = tamanho - aux2, j = (tamanho - aux - 1); i >= aux; i--, k++)
 		{
 			scanf("%d", &matriz[i][j]);
 		}
 		aux++;
 		for (j = (tamanho - aux2), i = (aux - 1); j >= aux; j--, k++)
 		{
 			scanf("%d", &matriz[i][j]);
 		}
 	}
 	for (i = 0; i < tamanho; i++)
 	{
 		for (j = 0; j < tamanho; j++)
 		{
 			printf("%d\n", matriz[i][j]);
 		}
 	}
 	return 0;
}
