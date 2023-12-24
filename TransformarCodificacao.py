from pathlib import Path

# Caminho para a pasta de dados
data_folder = Path(r"C:\Users\rdosa\source\repos\Identificar_Codificacao")

# Caminho para os arquivos de entrada e saída
alvo = data_folder / "alvo.txt"
resultado = data_folder / "resultado.txt"

# Função para verificar se um byte está na faixa ASCII
def is_ascii(byte):
    return 0 <= byte <= 127

# Função principal
def main():
    # Abre o arquivo de entrada em modo binário
    with open(alvo, "rb") as arquivo_alvo:
        # Lê os bytes do arquivo
        bytes_texto = arquivo_alvo.read()
        
        # Imprime os bytes no terminal
        print("Bytes do arquivo:", bytes_texto)

    # Filtra os bytes que estão na faixa ASCII e converte para caracteres
    caracteres_ascii = [chr(byte) for byte in bytes_texto if is_ascii(byte)]

    # Abre o arquivo de saída em modo de texto (UTF-8) e escreve os caracteres ASCII
    with open(resultado, "w", encoding="utf-8") as arquivo_resultado:
        arquivo_resultado.write("".join(caracteres_ascii))

# Executa a função principal se este script for executado diretamente
if __name__ == "__main__":
    main()
