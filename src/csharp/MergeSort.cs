/*
 * Implementação do algoritmo Merge Sort em C#
 * Análise de Complexidade: Teoria da Computação
 * Equipe: Thiago von Sohsten, Felipe Sérgio, Thiago Belo, Luiz Felipe Soriano
 */

using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;

namespace MergeSortAnalysis
{
    public class MergeSort
    {
        /// <summary>
        /// Implementação principal do Merge Sort
        /// </summary>
        /// <param name="arr">Array para ordenar</param>
        /// <returns>Array ordenado</returns>
        public static int[] Sort(int[] arr)
        {
            if (arr.Length <= 1)
                return arr;

            int mid = arr.Length / 2;
            int[] left = new int[mid];
            int[] right = new int[arr.Length - mid];

            // Divide o array em duas metades
            Array.Copy(arr, 0, left, 0, mid);
            Array.Copy(arr, mid, right, 0, arr.Length - mid);

            // Recursivamente ordena as duas metades
            left = Sort(left);
            right = Sort(right);

            // Combina as duas metades ordenadas
            return Merge(left, right);
        }

        /// <summary>
        /// Função auxiliar para combinar duas listas ordenadas
        /// </summary>
        /// <param name="left">Array ordenado da esquerda</param>
        /// <param name="right">Array ordenado da direita</param>
        /// <returns>Array combinado e ordenado</returns>
        private static int[] Merge(int[] left, int[] right)
        {
            int[] result = new int[left.Length + right.Length];
            int i = 0, j = 0, k = 0;

            // Combina os elementos em ordem crescente
            while (i < left.Length && j < right.Length)
            {
                if (left[i] <= right[j])
                {
                    result[k] = left[i];
                    i++;
                }
                else
                {
                    result[k] = right[j];
                    j++;
                }
                k++;
            }

            // Adiciona elementos restantes
            while (i < left.Length)
            {
                result[k] = left[i];
                i++;
                k++;
            }

            while (j < right.Length)
            {
                result[k] = right[j];
                j++;
                k++;
            }

            return result;
        }

        /// <summary>
        /// Gera dados de teste para o algoritmo
        /// </summary>
        /// <param name="size">Tamanho do array</param>
        /// <param name="dataType">Tipo de dados</param>
        /// <returns>Array de inteiros para teste</returns>
        public static int[] GenerateTestData(int size, string dataType)
        {
            Random random = new Random();
            int[] data = new int[size];

            switch (dataType.ToLower())
            {
                case "random":
                    for (int i = 0; i < size; i++)
                    {
                        data[i] = random.Next(1, 1001);
                    }
                    break;

                case "sorted":
                    for (int i = 0; i < size; i++)
                    {
                        data[i] = i + 1;
                    }
                    break;

                case "reverse":
                    for (int i = 0; i < size; i++)
                    {
                        data[i] = size - i;
                    }
                    break;

                case "duplicates":
                    for (int i = 0; i < size; i++)
                    {
                        data[i] = random.Next(1, 11);
                    }
                    break;

                default:
                    throw new ArgumentException("Tipo de dados inválido");
            }

            return data;
        }

        /// <summary>
        /// Mede o tempo de execução do Merge Sort
        /// </summary>
        /// <param name="arr">Array para ordenar</param>
        /// <returns>Tempo de execução em segundos</returns>
        public static double MeasureExecutionTime(int[] arr)
        {
            Stopwatch stopwatch = Stopwatch.StartNew();
            Sort(arr);
            stopwatch.Stop();
            return stopwatch.Elapsed.TotalSeconds;
        }

        /// <summary>
        /// Verifica se o array está ordenado
        /// </summary>
        /// <param name="arr">Array para verificar</param>
        /// <returns>True se estiver ordenado, False caso contrário</returns>
        public static bool IsSorted(int[] arr)
        {
            for (int i = 1; i < arr.Length; i++)
            {
                if (arr[i] < arr[i - 1])
                    return false;
            }
            return true;
        }

        /// <summary>
        /// Executa testes de performance
        /// </summary>
        public static void RunPerformanceTests()
        {
            int[] sizes = { 100, 500, 1000, 2000, 5000, 10000, 20000, 50000 };
            string[] dataTypes = { "random", "sorted", "reverse", "duplicates" };
            int iterations = 25;

            Console.WriteLine("=== Análise de Performance - Merge Sort (C#) ===");
            Console.WriteLine("Executando testes de performance...\n");

            foreach (string dataType in dataTypes)
            {
                Console.WriteLine($"Tipo de dados: {dataType}");
                Console.WriteLine("----------------------------------------");

                foreach (int size in sizes)
                {
                    Console.Write($"Testando com {size} elementos... ");

                    List<double> times = new List<double>();

                    for (int i = 0; i < iterations; i++)
                    {
                        int[] testData = GenerateTestData(size, dataType);
                        double executionTime = MeasureExecutionTime(testData);
                        times.Add(executionTime);
                    }

                    // Calcula estatísticas
                    double mean = times.Average();
                    double variance = times.Select(t => Math.Pow(t - mean, 2)).Average();
                    double stdDev = Math.Sqrt(variance);

                    Console.WriteLine($"Média: {mean:F6}s (±{stdDev:F6}s)");
                }
                Console.WriteLine();
            }
        }

        /// <summary>
        /// Executa teste básico do algoritmo
        /// </summary>
        public static void TestBasic()
        {
            Console.WriteLine("=== Teste Básico do Merge Sort (C#) ===");

            int[] testArray = { 64, 34, 25, 12, 22, 11, 90 };

            Console.Write("Array original: ");
            Console.WriteLine(string.Join(" ", testArray));

            int[] sortedArray = Sort(testArray);

            Console.Write("Array ordenado: ");
            Console.WriteLine(string.Join(" ", sortedArray));

            if (IsSorted(sortedArray))
            {
                Console.WriteLine("✓ Array está ordenado corretamente!");
            }
            else
            {
                Console.WriteLine("✗ Erro: Array não está ordenado!");
            }
            Console.WriteLine();
        }

        /// <summary>
        /// Método principal
        /// </summary>
        public static void Main(string[] args)
        {
            Console.WriteLine("Implementação do Merge Sort em C#");
            Console.WriteLine("Equipe: Thiago von Sohsten, Felipe Sérgio, Thiago Belo, Luiz Felipe Soriano");
            Console.WriteLine("Disciplina: Teoria da Computação - Prof. Daniel Bezerra\n");

            // Executa teste básico
            TestBasic();

            // Executa testes de performance
            RunPerformanceTests();

            Console.WriteLine("=== Análise Concluída ===");
            Console.WriteLine("Complexidade: O(n log n) em todos os casos");
            Console.WriteLine("Espaço: O(n)");
            Console.WriteLine("Classe P: Sim (complexidade polinomial)");
            Console.WriteLine("Linguagem: C# (.NET)");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}
