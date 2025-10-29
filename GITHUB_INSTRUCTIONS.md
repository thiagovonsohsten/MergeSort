
# Instruções para GitHub

## Como criar o repositório:

1. Acesse https://github.com
2. Clique em "New repository"
3. Nome: "MergeSort-Analysis" ou similar
4. Descrição: "Análise de Complexidade do Merge Sort - Teoria da Computação"
5. Marque como "Public"
6. Clique em "Create repository"

## Como fazer upload:

1. Instale o Git: https://git-scm.com/downloads
2. Abra o terminal na pasta do projeto
3. Execute os comandos:

```bash
git init
git add .
git commit -m "Implementação completa do Merge Sort com análise de complexidade"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
git push -u origin main
```

## Estrutura do repositório:

```
MergeSort-Analysis/
├── src/
│   ├── python/
│   │   └── merge_sort.py
│   └── csharp/
│       ├── MergeSort.cs
│       └── MergeSortBenchmark.cs
├── scripts/
│   ├── performance_analysis_python_csharp.py
│   ├── generate_report_python_csharp.py
│   └── generate_slides_python_csharp.py
├── results/
│   └── performance_results_python_csharp.json
├── output/
│   ├── relatorio_merge_sort_python_csharp.md
│   └── apresentacao_merge_sort.html
├── performance_comparison_python_csharp.png
├── language_comparison_python_csharp.png
└── README.md
```

## Link para o relatório:

Adicione o link do GitHub no relatório PDF ou na apresentação.
