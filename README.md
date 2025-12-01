# Análise de Complexidade - Merge Sort

**Disciplina**: Teoria da Computação  
**Professor**: Daniel Bezerra  
**Algoritmo**: Merge Sort  
**Linguagens**: Python e C  
**Equipe**: Thiago von Sohsten, Felipe Sérgio, Thiago Belo, Luiz Felipe Soriano

## 📋 Descrição do Projeto

Este projeto realiza uma análise completa da complexidade do algoritmo Merge Sort, implementado em duas linguagens de programação diferentes (Python e C), com foco na análise teórica e experimental da complexidade de tempo.

## 🚀 Como Executar

### Pré-requisitos

- **Python 3.x**: Já instalado na maioria dos sistemas
- **Compilador C**: 
  - Windows: MinGW ou Visual Studio
  - Linux: `gcc` (geralmente já instalado)
  - macOS: Xcode Command Line Tools

### Execução

#### Python
```bash
python mergesort.py
```

#### C
```bash
# Compilar
gcc -O2 -o mergesort mergesort.c

# Executar (Windows)
mergesort.exe

# Executar (Linux/Mac)
./mergesort
```

## 📊 Resultados Esperados

### Complexidade Teórica

- **Big-O**: O(n log n) - Limite superior
- **Big-Ω**: Ω(n log n) - Limite inferior
- **Big-Θ**: Θ(n log n) - Complexidade exata
- **Espaço**: O(n) - Arrays auxiliares

### Análise de Casos

- **Melhor caso**: O(n log n) - Array já ordenado
- **Pior caso**: O(n log n) - Qualquer configuração
- **Caso médio**: O(n log n) - Distribuição aleatória

### Performance Experimental

- **Tamanho testado**: 1.000.000 elementos
- **Tipo de dados**: Aleatórios (rand() % 1000000)
- **Medição**: Tempo em milissegundos e microssegundos
- **Linguagens**: Python e C

## 🔬 Análise Teórica

### Descrição do Algoritmo

O Merge Sort é um algoritmo de ordenação baseado na técnica de **divisão e conquista** (divide and conquer):

1. **Divisão**: Divide o array em duas metades aproximadamente iguais
2. **Conquista**: Ordena recursivamente cada metade
3. **Combinação**: Combina as duas metades ordenadas em uma única lista ordenada

### Pseudocódigo

```
MERGE-SORT(A, p, r)
1  if p < r
2     q = floor((p + r) / 2)
3     MERGE-SORT(A, p, q)
4     MERGE-SORT(A, q + 1, r)
5     MERGE(A, p, q, r)

MERGE(A, p, q, r)
1  n1 = q - p + 1
2  n2 = r - q
3  let L[1..n1+1] and R[1..n2+1] be new arrays
4  for i = 1 to n1
5     L[i] = A[p + i - 1]
6  for j = 1 to n2
7     R[j] = A[q + j]
8  L[n1 + 1] = infinity
9  R[n2 + 1] = infinity
10 i = 1, j = 1
11 for k = p to r
12    if L[i] <= R[j]
13       A[k] = L[i], i = i + 1
14    else A[k] = R[j], j = j + 1
```

### Justificativa da Complexidade

- **Cada nível de recursão**: O(n) operações para combinar
- **Número de níveis**: log₂ n (divide pela metade a cada nível)
- **Total**: O(n) × log n = **O(n log n)**

### Classificação Assintótica

- **Big-O (O)**: O(n log n) - Tempo nunca excede c·n·log n
- **Big-Ω (Ω)**: Ω(n log n) - Tempo sempre ≥ c·n·log n
- **Big-Θ (Θ)**: Θ(n log n) - Complexidade exata

## 🎯 Aplicabilidade Prática

### Vantagens

- ✅ **Estabilidade**: Mantém ordem relativa de elementos iguais
- ✅ **Previsibilidade**: Complexidade consistente O(n log n) em todos os casos
- ✅ **Paralelização**: Fácil de paralelizar devido à divisão independente
- ✅ **Ordenação externa**: Adaptável para arquivos grandes que não cabem na memória

### Desvantagens

- ❌ **Uso de memória**: Requer O(n) de espaço adicional para arrays auxiliares
- ❌ **Overhead**: Maior overhead comparado a algoritmos in-place como Quick Sort
- ❌ **Constantes**: Pode ser mais lento que Quick Sort em média devido a constantes maiores

### Contextos de Aplicação

- **Sistemas críticos**: Onde previsibilidade é essencial
- **Ordenação externa**: Arquivos grandes que não cabem na memória
- **Algoritmos híbridos**: Base para outros algoritmos de ordenação (ex: Tim Sort)
- **Aplicações paralelas**: Fácil de paralelizar devido à independência das metades

## 📈 Comparação de Linguagens

### Python
- **Características**: Interpretado, dinâmico, legível
- **Performance**: Mais lento devido à interpretação
- **Uso**: Prototipagem rápida, desenvolvimento ágil

### C
- **Características**: Compilado, tipado estaticamente, controle de memória
- **Performance**: Significativamente mais rápido (10-50x)
- **Uso**: Sistemas críticos, máxima performance

### Resultados Esperados

Para 1.000.000 de elementos:
- **Python**: ~500-2000 ms (dependendo do hardware)
- **C**: ~50-200 ms (dependendo do hardware)
- **Diferença**: C é aproximadamente 10-20x mais rápido

## 🔬 Classificação Computacional

### Classe P: ✅ SIM

- **Definição**: Problemas solucionáveis em tempo polinomial
- **Justificativa**: O(n log n) é polinomial (n log n = O(n²))
- **Implicação**: Algoritmo eficiente para problemas práticos

### Versão NP: ❌ NÃO EXISTE

- **Razão**: O Merge Sort é um algoritmo determinístico com complexidade polinomial
- **NP refere-se a**: Problemas de decisão verificáveis em tempo polinomial por máquina não-determinística
- **Conclusão**: Não há versão NP do Merge Sort

### Problemas NP-Completos Relacionados: ❌ NÃO APLICÁVEL

- **Ordenação**: Não é NP-completo, pois tem solução polinomial eficiente
- **Problemas de otimização**: Alguns problemas relacionados à ordenação podem ser NP-completos, mas a ordenação em si não é

## 📁 Estrutura do Projeto

```
MergeSort/
├── mergesort.py          # Implementação em Python
├── mergesort.c           # Implementação em C
└── README.md             # Este arquivo
```



## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Implementação interpretada
- **C (gcc)**: Implementação compilada
- **Windows API**: QueryPerformanceCounter para medição precisa (C)

## 📚 Referências

- Cormen, T. H., et al. "Introduction to Algorithms" (3rd ed.)
- Sedgewick, R. "Algorithms in C" (Parts 1-4)
- Knuth, D. E. "The Art of Computer Programming" (Vol. 3)

## 📅 Informações do Projeto

**Data de entrega**: 30/11/2025, 23:59h  
**Apresentação**: 01 Dezembro de 2025  
**Disciplina**: Teoria da Computação 

---

*Projeto desenvolvido para análise de complexidade do algoritmo Merge Sort*
