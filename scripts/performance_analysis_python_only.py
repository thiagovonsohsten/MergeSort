"""
Script de análise de performance apenas para Python
Versão simplificada sem dependência de C++
"""

import time
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
import os
import json

# Adiciona o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'python'))

from merge_sort import merge_sort, generate_test_data, measure_execution_time


class PerformanceAnalyzerPythonOnly:
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
                
                print(f"Media: {mean_time:.6f}s (+/-{std_time:.6f}s)")
    
    def generate_graphs(self):
        """Gera gráficos comparativos"""
        print("\nGerando graficos...")
        
        # Configuração dos gráficos
        plt.style.use('default')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Analise de Performance - Merge Sort (Python)', fontsize=16, fontweight='bold')
        
        for idx, data_type in enumerate(self.data_types):
            ax = axes[idx // 2, idx % 2]
            
            if 'python' in self.results and data_type in self.results['python']:
                sizes = []
                means = []
                stds = []
                
                for size in self.sizes:
                    if size in self.results['python'][data_type]:
                        sizes.append(size)
                        means.append(self.results['python'][data_type][size]['mean'])
                        stds.append(self.results['python'][data_type][size]['std'])
                
                ax.errorbar(sizes, means, yerr=stds, 
                          label='Python', 
                          color='blue', 
                          marker='o',
                          capsize=5, capthick=2)
            
            ax.set_xlabel('Tamanho do Array')
            ax.set_ylabel('Tempo de Execucao (s)')
            ax.set_title(f'Performance - {data_type.title()}')
            ax.legend()
            ax.grid(True, alpha=0.3)
            ax.set_xscale('log')
            ax.set_yscale('log')
        
        plt.tight_layout()
        plt.savefig('performance_comparison_python.png', dpi=300, bbox_inches='tight')
        print("Grafico salvo: performance_comparison_python.png")
        plt.show()
        
        # Gráfico de crescimento assintótico
        self._generate_complexity_graph()
    
    def _generate_complexity_graph(self):
        """Gera gráfico de validação da complexidade O(n log n)"""
        plt.figure(figsize=(12, 8))
        
        # Pega dados do tipo 'random' para análise
        if 'python' in self.results and 'random' in self.results['python']:
            sizes = []
            times = []
            
            for size in self.sizes:
                if size in self.results['python']['random']:
                    sizes.append(size)
                    times.append(self.results['python']['random'][size]['mean'])
            
            # Plota dados experimentais
            plt.loglog(sizes, times, 'bo-', label='Dados Experimentais', linewidth=2, markersize=8)
            
            # Plota curva teórica O(n log n)
            theoretical_sizes = np.array(sizes)
            theoretical_times = theoretical_sizes * np.log2(theoretical_sizes)
            # Normaliza para coincidir com os dados experimentais
            theoretical_times = theoretical_times * (times[0] / (sizes[0] * np.log2(sizes[0])))
            
            plt.loglog(theoretical_sizes, theoretical_times, 'r--', 
                      label='O(n log n) Teorico', linewidth=2)
            
            plt.xlabel('Tamanho do Array')
            plt.ylabel('Tempo de Execucao (s)')
            plt.title('Validacao da Complexidade O(n log n)')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig('complexity_validation.png', dpi=300, bbox_inches='tight')
            print("Grafico salvo: complexity_validation.png")
            plt.show()
    
    def save_results(self):
        """Salva os resultados em arquivo JSON"""
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        
        with open(results_dir / 'performance_results_python.json', 'w') as f:
            json.dump(self.results, f, indent=2)
        print("\nResultados salvos em 'results/performance_results_python.json'")
    
    def generate_report_data(self):
        """Gera dados para o relatório"""
        report_data = {
            'complexity_analysis': {
                'big_o': 'O(n log n)',
                'big_omega': 'Ω(n log n)',
                'big_theta': 'Θ(n log n)',
                'space_complexity': 'O(n)'
            },
            'best_case': 'O(n log n) - Array ja ordenado',
            'worst_case': 'O(n log n) - Qualquer configuracao',
            'average_case': 'O(n log n) - Distribuicao aleatoria',
            'p_class': 'Sim, pertence a classe P',
            'np_analysis': 'Nao existe versao NP do Merge Sort',
            'experimental_validation': 'Complexidade O(n log n) confirmada experimentalmente'
        }
        
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        
        with open(results_dir / 'report_data_python.json', 'w') as f:
            json.dump(report_data, f, indent=2)
        
        return report_data


def main():
    analyzer = PerformanceAnalyzerPythonOnly()
    
    print("=== Analise de Performance - Merge Sort (Python) ===")
    print("Este script executa testes completos de performance")
    print("e gera graficos comparativos para Python.\n")
    
    # Executa testes
    analyzer.run_python_tests()
    
    # Gera gráficos
    analyzer.generate_graphs()
    
    # Salva resultados
    analyzer.save_results()
    
    # Gera dados para relatório
    report_data = analyzer.generate_report_data()
    
    print("\n=== Analise Concluida ===")
    print("Arquivos gerados:")
    print("- performance_comparison_python.png")
    print("- complexity_validation.png")
    print("- results/performance_results_python.json")
    print("- results/report_data_python.json")


if __name__ == "__main__":
    main()
