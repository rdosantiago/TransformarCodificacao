from pathlib import Path

# Caminho para a pasta de dados
data_folder = Path(r"C:\Users\rdosa\source\repos\Identificar_Codificacao")

# Caminho para os arquivos de entrada e sa�da
alvo = data_folder / "alvo.txt"
resultado = data_folder / "resultado.txt"

# Fun��o para verificar se um byte est� na faixa ASCII
def is_ascii(byte):
    return 0 <= byte <= 127

# Fun��o principal
def main():
    # Abre o arquivo de entrada em modo bin�rio
    with open(alvo, "rb") as arquivo_alvo:
        # L� os bytes do arquivo
        bytes_texto = arquivo_alvo.read()
        
        # Imprime os bytes no terminal
        print("Bytes do arquivo:", bytes_texto)

    # Filtra os bytes que est�o na faixa ASCII e converte para caracteres
    caracteres_ascii = [chr(byte) for byte in bytes_texto if is_ascii(byte)]

    # Abre o arquivo de sa�da em modo de texto (UTF-8) e escreve os caracteres ASCII
    with open(resultado, "w", encoding="utf-8") as arquivo_resultado:
        arquivo_resultado.write("".join(caracteres_ascii))

# Executa a fun��o principal se este script for executado diretamente
if __name__ == "__main__":
    main()
