/*
 * Versão simplificada para benchmarks - retorna apenas o tempo
 * Usado pelo script Python para coletar dados de performance
 */

using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;

namespace MergeSortBenchmark
{
    public class MergeSortBenchmark
    {
        public static int[] Sort(int[] arr)
        {
            if (arr.Length <= 1)
                return arr;

            int mid = arr.Length / 2;
            int[] left = new int[mid];
            int[] right = new int[arr.Length - mid];

            Array.Copy(arr, 0, left, 0, mid);
            Array.Copy(arr, mid, right, 0, arr.Length - mid);

            left = Sort(left);
            right = Sort(right);

            return Merge(left, right);
        }

        private static int[] Merge(int[] left, int[] right)
        {
            int[] result = new int[left.Length + right.Length];
            int i = 0, j = 0, k = 0;

            while (i < left.Length && j < right.Length)
            {
                if (left[i] <= right[j])
                    result[k++] = left[i++];
                else
                    result[k++] = right[j++];
            }

            while (i < left.Length)
                result[k++] = left[i++];

            while (j < right.Length)
                result[k++] = right[j++];

            return result;
        }

        public static int[] GenerateTestData(int size, string dataType)
        {
            Random random = new Random(42); // Seed fixo para reprodutibilidade
            int[] data = new int[size];

            switch (dataType.ToLower())
            {
                case "random":
                    for (int i = 0; i < size; i++)
                        data[i] = random.Next(1, 1001);
                    break;
                case "sorted":
                    for (int i = 0; i < size; i++)
                        data[i] = i + 1;
                    break;
                case "reverse":
                    for (int i = 0; i < size; i++)
                        data[i] = size - i;
                    break;
                case "duplicates":
                    for (int i = 0; i < size; i++)
                        data[i] = random.Next(1, 11);
                    break;
            }

            return data;
        }

        public static void Main(string[] args)
        {
            if (args.Length < 2)
            {
                Console.WriteLine("Uso: MergeSortBenchmark <tipo_dados> <tamanho>");
                return;
            }

            string dataType = args[0];
            int size = int.Parse(args[1]);

            // Gera dados de teste
            int[] testData = GenerateTestData(size, dataType);

            // Mede o tempo de execução
            Stopwatch stopwatch = Stopwatch.StartNew();
            Sort(testData);
            stopwatch.Stop();

            // Retorna apenas o tempo em segundos
            Console.WriteLine(stopwatch.Elapsed.TotalSeconds);
        }
    }
}
