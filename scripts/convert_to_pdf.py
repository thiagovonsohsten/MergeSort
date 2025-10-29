"""
Script para converter relatório Markdown para PDF
Usando pandoc se disponível, ou instruções manuais
"""

import subprocess
import sys
from pathlib import Path

def convert_to_pdf():
    """Converte relatório Markdown para PDF"""
    
    markdown_file = Path("output/relatorio_merge_sort_python_csharp.md")
    pdf_file = Path("output/relatorio_merge_sort_python_csharp.pdf")
    
    if not markdown_file.exists():
        print(f"ERRO: Arquivo {markdown_file} não encontrado!")
        return False
    
    try:
        # Tenta usar pandoc
        result = subprocess.run([
            "pandoc", 
            str(markdown_file),
            "-o", str(pdf_file),
            "--pdf-engine=wkhtmltopdf",
            "--css=styles.css"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"PDF gerado com sucesso: {pdf_file}")
            return True
        else:
            print(f"Erro ao converter com pandoc: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("Pandoc não encontrado. Instruções manuais:")
        print("\n1. Instale o pandoc: https://pandoc.org/installing.html")
        print("2. Execute: pandoc output/relatorio_merge_sort_python_csharp.md -o relatorio.pdf")
        print("\nOu use um conversor online como:")
        print("- https://www.markdowntopdf.com/")
        print("- https://dillinger.io/")
        print("- https://stackedit.io/")
        return False

def create_github_instructions():
    """Cria instruções para GitHub"""
    
    instructions = """
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
"""
    
    with open("GITHUB_INSTRUCTIONS.md", "w", encoding="utf-8") as f:
        f.write(instructions)
    
    print("Instruções do GitHub criadas: GITHUB_INSTRUCTIONS.md")

if __name__ == "__main__":
    print("=== Conversão para PDF ===")
    success = convert_to_pdf()
    
    if not success:
        print("\n=== Instruções Manuais ===")
        print("1. Abra o arquivo: output/relatorio_merge_sort_python_csharp.md")
        print("2. Copie o conteúdo")
        print("3. Cole em um conversor online como:")
        print("   - https://www.markdowntopdf.com/")
        print("   - https://dillinger.io/")
        print("   - https://stackedit.io/")
        print("4. Baixe como PDF")
    
    print("\n=== Instruções do GitHub ===")
    create_github_instructions()
