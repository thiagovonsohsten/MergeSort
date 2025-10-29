"""
Implementação do algoritmo Merge Sort em Python
Análise de Complexidade: Teoria da Computação
"""

import time
import random
import statistics
from typing import List, Tuple


def merge_sort(arr: List[int]) -> List[int]:
    """
    Implementação do algoritmo Merge Sort
    
    Args:
        arr: Lista de inteiros para ordenar
        
    Returns:
        Lista ordenada
    """
    if len(arr) <= 1:
        return arr
    
    # Divide o array ao meio
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursivamente ordena as duas metades
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Combina as duas metades ordenadas
    return merge(left_sorted, right_sorted)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Função auxiliar para combinar duas listas ordenadas
    
    Args:
        left: Lista ordenada da esquerda
        right: Lista ordenada da direita
        
    Returns:
        Lista combinada e ordenada
    """
    result = []
    i = j = 0
    
    # Combina os elementos em ordem crescente
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Adiciona elementos restantes
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def generate_test_data(size: int, data_type: str = "random") -> List[int]:
    """
    Gera dados de teste para o algoritmo
    
    Args:
        size: Tamanho do array
        data_type: Tipo de dados ("random", "sorted", "reverse", "duplicates")
        
    Returns:
        Lista de inteiros para teste
    """
    if data_type == "random":
        return [random.randint(1, 1000) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(1, size + 1))
    elif data_type == "reverse":
        return list(range(size, 0, -1))
    elif data_type == "duplicates":
        return [random.randint(1, 10) for _ in range(size)]
    else:
        raise ValueError("Tipo de dados inválido")


def measure_execution_time(arr: List[int], iterations: int = 1) -> float:
    """
    Mede o tempo de execução do Merge Sort
    
    Args:
        arr: Array para ordenar
        iterations: Número de iterações para média
        
    Returns:
        Tempo médio de execução em segundos
    """
    times = []
    
    for _ in range(iterations):
        # Cria uma cópia para não modificar o array original
        test_arr = arr.copy()
        
        start_time = time.perf_counter()
        merge_sort(test_arr)
        end_time = time.perf_counter()
        
        times.append(end_time - start_time)
    
    return statistics.mean(times)


def run_performance_tests():
    """
    Executa testes de performance com diferentes tamanhos de entrada
    """
    sizes = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]
    data_types = ["random", "sorted", "reverse", "duplicates"]
    iterations = 20
    
    results = {}
    
    print("Executando testes de performance...")
    print("=" * 50)
    
    for data_type in data_types:
        results[data_type] = {}
        print(f"\nTipo de dados: {data_type}")
        print("-" * 30)
        
        for size in sizes:
            print(f"Testando com {size} elementos...", end=" ")
            
            # Gera dados de teste
            test_data = generate_test_data(size, data_type)
            
            # Mede o tempo de execução
            avg_time = measure_execution_time(test_data, iterations)
            
            results[data_type][size] = avg_time
            print(f"Tempo médio: {avg_time:.6f}s")
    
    return results


if __name__ == "__main__":
    # Teste básico do algoritmo
    print("Teste básico do Merge Sort:")
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Array original: {test_array}")
    sorted_array = merge_sort(test_array)
    print(f"Array ordenado: {sorted_array}")
    
    # Executa testes de performance
    print("\n" + "=" * 60)
    performance_results = run_performance_tests()
