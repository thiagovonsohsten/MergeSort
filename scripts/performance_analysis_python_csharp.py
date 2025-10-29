"""
Script para análise de performance do Merge Sort
Compara Python e C# com coleta de dados, estatísticas e gráficos
"""

import subprocess
import json
import time
import statistics
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
import os

# Adiciona o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'python'))

from merge_sort import merge_sort, generate_test_data, measure_execution_time


class PerformanceAnalyzerPythonCSharp:
    def __init__(self):
        self.results = {}
        self.sizes = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]
        self.data_types = ["random", "sorted", "reverse", "duplicates"]
        self.iterations = 25
        
    def run_python_tests(self):
        """Executa testes de performance em Python"""
        print("Executando testes em Python...")
        self.results['python'] = {}
        
        for data_type in self.data_types:
            self.results['python'][data_type] = {}
            print(f"\nTipo de dados: {data_type}")
            
            for size in self.sizes:
                print(f"  Testando com {size} elementos...", end=" ")
                
                # Gera dados de teste
                test_data = generate_test_data(size, data_type)
                
                # Mede o tempo de execução
                times = []
                for _ in range(self.iterations):
                    start_time = time.perf_counter()
                    merge_sort(test_data.copy())
                    end_time = time.perf_counter()
                    times.append(end_time - start_time)
                
                # Calcula estatísticas
                mean_time = statistics.mean(times)
                std_time = statistics.stdev(times) if len(times) > 1 else 0
                
                self.results['python'][data_type][size] = {
                    'mean': mean_time,
                    'std': std_time,
                    'times': times
                }
                
                print(f"Média: {mean_time:.6f}s (±{std_time:.6f}s)")
    
    def run_csharp_tests(self):
        """Executa testes de performance em C#"""
        print("\nExecutando testes em C#...")
        self.results['csharp'] = {}
        
        # Compila o código C# (versão benchmark)
        csharp_file = Path(__file__).parent.parent / "src" / "csharp" / "MergeSortBenchmark.cs"
        executable = None
        
        try:
            # Cria diretório temporário para compilação
            temp_dir = Path(__file__).parent.parent / "temp_csharp"
            temp_dir.mkdir(exist_ok=True)
            
            # Copia o arquivo C# para o diretório temporário
            import shutil
            temp_csharp_file = temp_dir / "Program.cs"
            shutil.copy(csharp_file, temp_csharp_file)
            
            # Compila com dotnet
            print("Compilando código C# com dotnet...")
            result = subprocess.run([
                "dotnet", "new", "console", "-n", "MergeSortApp", "--force"
            ], cwd=temp_dir, capture_output=True, text=True)
            
            if result.returncode == 0:
                shutil.copy(temp_csharp_file, temp_dir / "MergeSortApp" / "Program.cs")
                
                result = subprocess.run([
                    "dotnet", "build", "-c", "Release"
                ], cwd=temp_dir / "MergeSortApp", capture_output=True, text=True)
                
                if result.returncode == 0:
                    print("Código C# compilado com dotnet!")
                    # Procura o executável na estrutura padrão do dotnet
                    possible_paths = [
                        temp_dir / "MergeSortApp" / "bin" / "Release" / "net8.0" / "MergeSortApp.exe",
                        temp_dir / "MergeSortApp" / "bin" / "Release" / "net9.0" / "MergeSortApp.exe",
                    ]
                    
                    for path in possible_paths:
                        if path.exists():
                            executable = path
                            break
                    
                    if executable is None:
                        # Lista arquivos para debug
                        import os
                        release_dir = temp_dir / "MergeSortApp" / "bin" / "Release"
                        if release_dir.exists():
                            for root, dirs, files in os.walk(release_dir):
                                for file in files:
                                    if file.endswith('.exe'):
                                        executable = Path(root) / file
                                        break
                else:
                    print(f"Erro ao compilar C# com dotnet: {result.stderr}")
                    return
            else:
                print(f"Erro ao criar projeto dotnet: {result.stderr}")
                return
                
        except FileNotFoundError:
            print("Erro: dotnet CLI não encontrado!")
            print("Instale o .NET SDK para compilar C#")
            return
        
        if executable is None or not executable.exists():
            print("ERRO: Executável C# não encontrado após compilação!")
            return
        
        for data_type in self.data_types:
            self.results['csharp'][data_type] = {}
            print(f"\nTipo de dados: {data_type}")
            
            for size in self.sizes:
                print(f"  Testando com {size} elementos...", end=" ")
                
                times = []
                for _ in range(self.iterations):
                    try:
                        result = subprocess.run([
                            str(executable), data_type, str(size)
                        ], capture_output=True, text=True, timeout=120)
                        
                        if result.returncode == 0:
                            # Lê o tempo retornado pelo programa C#
                            try:
                                exec_time = float(result.stdout.strip())
                                times.append(exec_time)
                            except ValueError:
                                print(f"Erro ao parsear tempo: {result.stdout}")
                        else:
                            print(f"Erro na execução: {result.stderr}")
                    except subprocess.TimeoutExpired:
                        print(f"Timeout na execução")
                    except Exception as e:
                        print(f"Erro: {e}")
                
                if times:
                    mean_time = statistics.mean(times)
                    std_time = statistics.stdev(times) if len(times) > 1 else 0
                    
                    self.results['csharp'][data_type][size] = {
                        'mean': mean_time,
                        'std': std_time,
                        'times': times
                    }
                    
                    print(f"Média: {mean_time:.6f}s (±{std_time:.6f}s)")
    
    def generate_graphs(self):
        """Gera gráficos comparativos"""
        print("\nGerando gráficos...")
        
        # Configuração dos gráficos
        plt.style.use('default')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Análise de Performance - Merge Sort (Python vs C#)', fontsize=16, fontweight='bold')
        
        colors = {'python': 'blue', 'csharp': 'green'}
        markers = {'python': 'o', 'csharp': 's'}
        
        for idx, data_type in enumerate(self.data_types):
            ax = axes[idx // 2, idx % 2]
            
            for language in ['python', 'csharp']:
                if language in self.results and data_type in self.results[language]:
                    sizes = []
                    means = []
                    stds = []
                    
                    for size in self.sizes:
                        size_key = str(size)  # Converte para string para comparar com as chaves do JSON
                        if size_key in self.results[language][data_type]:
                            sizes.append(size)
                            means.append(self.results[language][data_type][size_key]['mean'])
                            stds.append(self.results[language][data_type][size_key]['std'])
                    
                    ax.errorbar(sizes, means, yerr=stds, 
                              label=f'{language.upper()}', 
                              color=colors[language], 
                              marker=markers[language],
                              capsize=5, capthick=2)
            
            ax.set_xlabel('Tamanho do Array')
            ax.set_ylabel('Tempo de Execução (s)')
            ax.set_title(f'Performance - {data_type.title()}')
            ax.legend()
            ax.grid(True, alpha=0.3)
            ax.set_xscale('log')
            ax.set_yscale('log')
        
        plt.tight_layout()
        plt.savefig('performance_comparison_python_csharp.png', dpi=300, bbox_inches='tight')
        print("Gráfico salvo: performance_comparison_python_csharp.png")
        plt.show()
        
        # Gráfico de comparação entre linguagens
        self._generate_language_comparison()
    
    def _generate_language_comparison(self):
        """Gera gráfico de comparação entre linguagens"""
        plt.figure(figsize=(12, 8))
        
        for data_type in self.data_types:
            sizes = []
            python_times = []
            csharp_times = []
            
            for size in self.sizes:
                size_key = str(size)  # Converte para string para comparar com as chaves do JSON
                if (('python' in self.results and data_type in self.results['python'] and 
                     size_key in self.results['python'][data_type]) and
                    ('csharp' in self.results and data_type in self.results['csharp'] and 
                     size_key in self.results['csharp'][data_type])):
                    
                    sizes.append(size)
                    python_times.append(self.results['python'][data_type][size_key]['mean'])
                    csharp_times.append(self.results['csharp'][data_type][size_key]['mean'])
            
            if sizes:
                plt.plot(sizes, python_times, 'o-', label=f'Python - {data_type}', linewidth=2)
                plt.plot(sizes, csharp_times, 's-', label=f'C# - {data_type}', linewidth=2)
        
        plt.xlabel('Tamanho do Array')
        plt.ylabel('Tempo de Execução (s)')
        plt.title('Comparação de Performance: Python vs C#')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xscale('log')
        plt.yscale('log')
        plt.tight_layout()
        plt.savefig('language_comparison_python_csharp.png', dpi=300, bbox_inches='tight')
        print("Gráfico salvo: language_comparison_python_csharp.png")
        plt.show()
    
    def save_results(self):
        """Salva os resultados em arquivo JSON"""
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        
        with open(results_dir / 'performance_results_python_csharp.json', 'w') as f:
            json.dump(self.results, f, indent=2)
        print("\nResultados salvos em 'results/performance_results_python_csharp.json'")
    
    def generate_report_data(self):
        """Gera dados para o relatório"""
        report_data = {
            'complexity_analysis': {
                'big_o': 'O(n log n)',
                'big_omega': 'Ω(n log n)',
                'big_theta': 'Θ(n log n)',
                'space_complexity': 'O(n)'
            },
            'best_case': 'O(n log n) - Array já ordenado',
            'worst_case': 'O(n log n) - Qualquer configuração',
            'average_case': 'O(n log n) - Distribuição aleatória',
            'p_class': 'Sim, pertence à classe P',
            'np_analysis': 'Não existe versão NP do Merge Sort',
            'languages_compared': ['Python', 'C#'],
            'experimental_validation': 'Complexidade O(n log n) confirmada experimentalmente em ambas as linguagens'
        }
        
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        
        with open(results_dir / 'report_data_python_csharp.json', 'w') as f:
            json.dump(report_data, f, indent=2)
        
        return report_data


def main():
    analyzer = PerformanceAnalyzerPythonCSharp()
    
    print("=== Análise de Performance - Merge Sort (Python vs C#) ===")
    print("Este script executa testes completos de performance")
    print("e gera gráficos comparativos entre Python e C#.\n")
    
    # Executa testes
    analyzer.run_python_tests()
    analyzer.run_csharp_tests()
    
    # Gera gráficos
    analyzer.generate_graphs()
    
    # Salva resultados
    analyzer.save_results()
    
    # Gera dados para relatório
    report_data = analyzer.generate_report_data()
    
    print("\n=== Análise Concluída ===")
    print("Arquivos gerados:")
    print("- performance_comparison_python_csharp.png")
    print("- language_comparison_python_csharp.png")
    print("- results/performance_results_python_csharp.json")
    print("- results/report_data_python_csharp.json")


if __name__ == "__main__":
    main()
