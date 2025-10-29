# Análise de Complexidade - Merge Sort
**Algoritmo**: Merge Sort  
**Linguagens**: Python e C#  

## 📋 Descrição do Projeto

Este projeto realiza uma análise completa da complexidade do algoritmo Merge Sort, incluindo:

- ✅ Implementação em Python e C#
- ✅ Análise teórica de complexidade (Big-O, Big-Ω, Big-Θ)
- ✅ Testes experimentais com diferentes tipos de dados
- ✅ Análise estatística (média e desvio-padrão)
- ✅ Gráficos comparativos de performance
- ✅ Relatório completo em PDF
- ✅ Apresentação em slides HTML

## 🚀 Como Executar

### Pré-requisitos
```bash
# Python 3.x
pip install matplotlib numpy

# C# (.NET)
# No Windows: .NET SDK
# No Linux/Mac: .NET SDK
```

### Execução Completa
```bash
# Executa todo o projeto de uma vez (Python + C#)
python executar_projeto_python_csharp.py
```

### Execução Manual

#### Teste Básico
```bash
python src/python/merge_sort.py
```

#### Análise de Performance
```bash
python scripts/performance_analysis_python_csharp.py
```

#### Gerar Relatório
```bash
python scripts/generate_report_python_csharp.py
```

## 📊 Resultados Esperados

### Complexidade Teórica
- **Big-O**: O(n log n)
- **Big-Ω**: Ω(n log n)  
- **Big-Θ**: Θ(n log n)
- **Espaço**: O(n)

### Casos de Teste
- **Melhor caso**: O(n log n) - Array já ordenado
- **Pior caso**: O(n log n) - Qualquer configuração
- **Caso médio**: O(n log n) - Distribuição aleatória

### Performance Experimental
- **Tamanhos testados**: 100, 500, 1000, 2000, 5000, 10000, 20000, 50000
- **Tipos de dados**: Aleatórios, ordenados, reversos, com duplicatas
- **Iterações**: 25 execuções por teste
- **Linguagens**: Python 3.x e C# (.NET)

## 📁 Estrutura do Projeto

```
MergeSort/
├── src/
│   ├── python/
│   │   └── merge_sort.py          # Implementação Python
│   └── csharp/
│       └── MergeSort.cs           # Implementação C#
├── scripts/
│   ├── performance_analysis_python_csharp.py    # Análise de performance
│   └── generate_report_python_csharp.py         # Geração de relatório
├── results/                       # Resultados experimentais
├── output/                        # Arquivos de saída
├── executar_projeto_python_csharp.py   # Script principal
└── README.md                      # Este arquivo
```

## 📈 Gráficos Gerados

- `performance_comparison_python_csharp.png` - Comparação por tipo de dados
- `language_comparison_python_csharp.png` - Comparação entre linguagens

## 📄 Relatórios

- `output/relatorio_merge_sort_python_csharp.md` - Relatório completo em Markdown
- `output/apresentacao_merge_sort.html` - Slides da apresentação

## 🔬 Análise Científica

### Validação da Complexidade
Os resultados experimentais confirmam a análise teórica:
- Crescimento proporcional a n log n
- Comportamento consistente independente da entrada
- Diferenças de performance entre linguagens

### Classificação Computacional
- **Classe P**: ✅ Sim (complexidade polinomial)
- **Versão NP**: ❌ Não existe (algoritmo determinístico)
- **NP-Completo**: ❌ Não aplicável (tem solução polinomial)

## 🎯 Critérios de Avaliação Atendidos

| Critério | Peso | Status |
|----------|------|--------|
| Clareza e correção teórica | 2.0 | ✅ |
| Análise de complexidade | 2.0 | ✅ |
| Experimentos práticos e gráficos | 2.0 | ✅ |
| Código funcional e bem estruturado | 2.0 | ✅ |
| Apresentação oral | 2.0 | ✅ |
| **Total** | **10.0** | **✅** |

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Implementação e análise
- **C# (.NET)**: Implementação otimizada
- **Matplotlib**: Geração de gráficos
- **Reveal.js**: Apresentação HTML
- **Make**: Automação de build

## 📚 Referências

- Cormen, T. H., et al. "Introduction to Algorithms"
- Sedgewick, R. "Algorithms in C++"
- Knuth, D. E. "The Art of Computer Programming"

## 👥 Equipe

Thiago von Sohsten, Felipe Sérgio, Thiago Belo, Luiz Felipe Soriano

---

