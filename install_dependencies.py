"""
Script para instalar dependências do projeto Merge Sort
"""

import subprocess
import sys
import os
from pathlib import Path

def install_python_dependencies():
    """Instala dependências Python"""
    print("Instalando dependências Python...")
    
    dependencies = [
        "matplotlib",
        "numpy",
        "pandas"  # Para análise de dados adicional
    ]
    
    for dep in dependencies:
        try:
            print(f"Instalando {dep}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"✅ {dep} instalado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao instalar {dep}: {e}")

def check_cpp_compiler():
    """Verifica se o compilador C++ está disponível"""
    print("\nVerificando compilador C++...")
    
    try:
        # Tenta compilar um programa simples
        test_code = """
#include <iostream>
int main() {
    std::cout << "Teste de compilação" << std::endl;
    return 0;
}
"""
        
        with open("test_compile.cpp", "w") as f:
            f.write(test_code)
        
        subprocess.check_call(["g++", "-o", "test_compile", "test_compile.cpp"], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Limpa arquivos de teste
        os.remove("test_compile.cpp")
        os.remove("test_compile.exe" if os.name == 'nt' else "test_compile")
        
        print("✅ Compilador C++ (g++) encontrado!")
        return True
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Compilador C++ (g++) não encontrado!")
        print("📝 Instruções de instalação:")
        print("   Windows: Instale MinGW-w64 ou Visual Studio")
        print("   Linux: sudo apt install g++")
        print("   macOS: xcode-select --install")
        return False

def create_directories():
    """Cria diretórios necessários"""
    print("\nCriando diretórios...")
    
    directories = [
        "src/python",
        "src/cpp", 
        "scripts",
        "results",
        "output",
        "build"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Diretório {directory}/ criado")

def main():
    print("=== Instalador de Dependências - Merge Sort ===")
    print("Este script irá configurar o ambiente para o projeto.\n")
    
    # Cria diretórios
    create_directories()
    
    # Instala dependências Python
    install_python_dependencies()
    
    # Verifica compilador C++
    cpp_available = check_cpp_compiler()
    
    print("\n" + "="*50)
    print("RESUMO DA INSTALAÇÃO:")
    print("="*50)
    print("✅ Dependências Python: Instaladas")
    print(f"{'✅' if cpp_available else '❌'} Compilador C++: {'Disponível' if cpp_available else 'Não encontrado'}")
    print("✅ Estrutura de diretórios: Criada")
    
    if cpp_available:
        print("\n🎉 Instalação concluída com sucesso!")
        print("📝 Próximos passos:")
        print("   1. Execute: make all")
        print("   2. Execute: make test")
        print("   3. Execute: make analysis")
    else:
        print("\n⚠️  Instalação parcialmente concluída!")
        print("📝 Para usar C++:")
        print("   1. Instale um compilador C++")
        print("   2. Execute: make all")
        print("   3. Execute: make test")

if __name__ == "__main__":
    main()
