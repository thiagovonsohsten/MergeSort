#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#define TAMANHO 1000000

void intercala (int inicio, int meio, int fim, int v[], int aux[]);
void mergesort (int inicio, int fim, int v[], int aux[]);

int main () {
    LARGE_INTEGER inicio, fim, frequencia;
    double tempo_ms;
    
    int *vetor = (int*) malloc(TAMANHO * sizeof(int));
    int *aux = (int*) malloc(TAMANHO * sizeof(int));
    
    if (vetor == NULL || aux == NULL) {
        printf("Erro ao alocar memória!\n");
        return 1;
    }
    
    srand(time(NULL));
    printf("Gerando vetor com %d elementos aleatórios...\n\n", TAMANHO);
    for (int i = 0; i < TAMANHO; i++) {
        vetor[i] = rand() % 1000000;
    }
    
    // Obtém a frequência do contador de performance
    QueryPerformanceFrequency(&frequencia);
    
    printf("Iniciando ordenação...\n");
    
    // Marca o tempo inicial
    QueryPerformanceCounter(&inicio);
    mergesort(0, TAMANHO - 1, vetor, aux);
    // Marca o tempo final
    QueryPerformanceCounter(&fim);
    
    // Calcula o tempo em milissegundos
    tempo_ms = (double)(fim.QuadPart - inicio.QuadPart) * 1000.0 / frequencia.QuadPart;
    
    printf("\n=== RESULTADOS ===\n");
    printf("Tamanho do vetor: %d elementos\n", TAMANHO);
    printf("Tempo de execução: %.6f milissegundos\n", tempo_ms);
    printf("Tempo de execução: %.6f microssegundos\n", tempo_ms * 1000);
    
    // Verificação
    printf("\nVerificando se está ordenado...\n");
    int ordenado = 1;
    for (int i = 0; i < TAMANHO - 1; i++) {
        if (vetor[i] > vetor[i + 1]) {
            ordenado = 0;
            break;
        }
    }
    
    if (ordenado) {
        printf("Vetor ordenado corretamente!\n");
    } else {
        printf("Erro na ordenação!\n");
    }
    
    free(vetor);
    free(aux);
    
    return 0;
}

void intercala (int inicio, int meio, int fim, int v[], int aux[]) {
    int i = inicio, j = meio + 1, k = 0;
    
    while (i <= meio && j <= fim) {
        if (v[i] <= v[j]) {
            aux[k++] = v[i++];
        } else {
            aux[k++] = v[j++];
        }
    }
    
    while (i <= meio) {
        aux[k++] = v[i++];
    }
    
    while (j <= fim) {
        aux[k++] = v[j++];
    }
    
    for (i = inicio, k = 0; i <= fim; i++, k++) {
        v[i] = aux[k];
    }
}

void mergesort (int inicio, int fim, int v[], int aux[]) {
    if (inicio < fim) {
        int meio = (inicio + fim) / 2;
        mergesort(inicio, meio, v, aux);
        mergesort(meio + 1, fim, v, aux);
        intercala(inicio, meio, fim, v, aux);
    }
}