#include <stdio.h>
int main()
{
	int x;
	scanf("%d", &x);
	getchar();
	int matriz[9][9];
	int l, c;
	int y;
	int contador = 1;
	while(contador <= x)
	{
		int linha = 0, coluna = 0, mat = 0;
		int contadorlinha = 0, contadorcoluna = 0, contadormat = 0;
		for(l = 0; l < 9; l++)
		{
			for(c = 0; c < 9; c++)
			{
				scanf("%d", &matriz[l][c]);
			}
		}
		//VERIFICAR LINHAS
		for(l = 0; l < 9; l++)
		{
			linha = 0;
			int arrayl[9]={1, 2, 3, 4, 5, 6, 7, 8, 9};
			for(c = 0; c < 9; c++)
			{				
				for (y = 0; y < 9; y++)
				{
					if (matriz[l][c] == arrayl[y])
					{
						arrayl[y] = 0;
						linha++;                                     // SE LINHA = 9 e contadorlinha = 9, verdadeiro.
					}
				}
				if (linha == 9)
				{
					contadorlinha++;
				}
			}
		}
		//VERIFICAR COLUNAS
		for (c = 0; c < 9; c++)
		{
			coluna = 0;
			int arrayc[9]={1, 2, 3, 4, 5, 6, 7, 8, 9};
			for (l = 0; l < 9; l++)
			{
				for(y = 0; y < 9;y++)
				{
					if (matriz[l][c] == arrayc[y])
					{
						arrayc[y] = 0;
						coluna++;
					}
				}
				if (coluna == 9)
				{
					contadorcoluna++;                                 // SE COLUNA = 0 E CONTADORCOLUNA = 9, VERDADEIRO
				}
			}
		}
		//VERIFICAR MATRIZES SECUNDARIAS
		for (mat = 0, l = 0; l < 3; l++) // matriz 00 a 22
		{
			int arraym1[9]={1, 2, 3, 4, 5, 6, 7, 8, 9};
			for (c = 0; c < 3; c++)
			{
				for (y = 0; y < 9; y++)
				{
					if (matriz[l][c] == arraym1[y])
					{
						arraym1[y] = 0;
						mat++;
					}
				}
				if (mat == 9)
				{
					contadormat++;
				}
			}
		}
		for (mat = 0, l = 0; l < 3; l++) // matriz 03 a 25
		{
			int arraym2[9]={1, 2, 3, 4, 5, 6, 7, 8, 9};
			for (c = 3; c < 6; c++)
			{
				for (y = 0; y < 9; y++)
				{
					if (matriz[l][c] == arraym2[y])
					{
						arraym2[y] = 0;
						mat++;
					}
				}
				if (mat == 9)
				{
					contadormat++;
				}
			}
		}
		for (mat = 0, l = 0; l < 3; l++) // matriz 06 a 28
		{
			int arraym3[9]={1, 2, 3, 4, 5, 6, 7, 8, 9};
			for (c = 6; c < 9; c++)
			{
				for (y = 0; y < 9; y++)
				{
					if (matriz[l][c] == arraym3[y])
					{
						arraym3[y] = 0;
						mat++;
					}
				}
				if (mat == 9)
				{
					contadormat++;
				}
			}
		}
		//PROXIMAS 3
		for (mat = 0, l = 3; l < 6; l++) // matriz 30 a 52
		{
			int arraym4[9]={1, 2, 3, 4, 5, 6, 7, 8, 9};
			for (c = 0; c < 3; c++)
			{
				for (y = 0; y < 9; y++)
				{
					if (matriz[l][c] == arraym4[y])
					{
						arraym4[y] = 0;
						mat++;
					}
				}
				if (mat == 9)
				{
					contadormat++;
				}
			}
		}
		for (mat = 0, l = 3; l < 6; l++) // matriz 33 a 55
		{
			int arraym5[9]={1, 2, 3, 4, 5, 6, 7, 8, 9};
			for (c = 3; c < 6; c++)
			{
				for (y = 0; y < 9; y++)
				{
					if (matriz[l][c] == arraym5[y])
					{
						arraym5[y] = 0;
						mat++;
					}
				}
				if (mat == 9)
				{
					contadormat++;
				}
			}
		}
		for (mat = 0, l = 3; l < 6; l++) // matriz 36 a 58
		{
			int arraym6[9]={1, 2, 3, 4, 5, 6, 7, 8, 9};
			for (c = 6; c < 9; c++)
			{
				for (y = 0; y < 9; y++)
				{
					if (matriz[l][c] == arraym6[y])
					{
						arraym6[y] = 0;
						mat++;
					}
				}
				if (mat == 9)
				{
					contadormat++;
				}
			}
		}
		//PROXIMAS 3
		for (mat = 0, l = 6; l < 9; l++) // matriz 60 a 82
		{
			int arraym7[9]={1, 2, 3, 4, 5, 6, 7, 8, 9};
			for (c = 0; c < 3; c++)
			{
				for (y = 0; y < 9; y++)
				{
					if (matriz[l][c] == arraym7[y])
					{
						arraym7[y] = 0;
						mat++;
					}
				}
				if (mat == 9)
				{
					contadormat++;
				}
			}
		}
		for (mat = 0, l = 6; l < 9; l++) // matriz 63 a 85
		{
			int arraym8[9]={1, 2, 3, 4, 5, 6, 7, 8, 9};
			for (c = 3; c < 6; c++)
			{
				for (y = 0; y < 9; y++)
				{
					if (matriz[l][c] == arraym8[y])
					{
						arraym8[y] = 0;
						mat++;
					}
				}
				if (mat == 9)
				{
					contadormat++;
				}
			}
		}
		for (mat = 0, l = 6; l < 9; l++) // matriz 36 a 58
		{
			int arraym9[9]={1, 2, 3, 4, 5, 6, 7, 8, 9};
			for (c = 6; c < 9; c++)
			{
				for (y = 0; y < 9; y++)
				{
					if (matriz[l][c] == arraym9[y])
					{
						arraym9[y] = 0;
						mat++;
					}
				}
				if (mat == 9)
				{
					contadormat++;
				}
			}
		}
		//printf("linha = %d\ncoluna = %d\nmat = %d\n", linha, coluna, mat);
		if (contadorlinha == 9 && contadorcoluna == 9 && contadormat == 9)
		{
			printf("Instancia %d\nSIM\n\n", contador);
		}
		else
		{
			printf("Instancia %d\nNAO\n\n", contador);
		}
		contador++;
	}
}
