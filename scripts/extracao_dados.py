import os
import pymupdf
import re


def limpar_texto(texto):
    """Remove ruídos comuns de conversão de PDF."""
    texto = re.sub(r'\n\s*\d+\s*\n', '\n', texto)  # Números de páginas isolados
    texto = re.sub(r'\n+', '\n', texto)  # Quebras de linha excessivas
    texto = re.sub(r'[ \t]+', ' ', texto)  # Espaços duplos/tabulações
    return texto.strip()


def processar_ficheiros(pasta_origem='../dados_brutos', pasta_destino='./dados_limpos'):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_origem = os.path.normpath(os.path.join(base_dir, pasta_origem))
    caminho_destino = os.path.normpath(os.path.join(base_dir, pasta_destino))

    os.makedirs(caminho_destino, exist_ok=True)

    if not os.path.exists(caminho_origem):
        print(f"Erro: A pasta '{caminho_origem}' não existe. Crie a pasta e adicione os ficheiros.")
        return

    ficheiros = os.listdir(caminho_origem)
    if not ficheiros:
        print(f"Nenhum ficheiro encontrado na pasta '{caminho_origem}'.")
        return

    for ficheiro in ficheiros:
        caminho_arq = os.path.join(caminho_origem, ficheiro)
        texto_bruto = ""

        try:
            if ficheiro.endswith('.pdf'):
                doc = pymupdf.open(caminho_arq)
                for pagina in doc:
                    texto_bruto += pagina.get_text("text") + "\n"
            elif ficheiro.endswith('.txt'):
                with open(caminho_arq, 'r', encoding='utf-8') as f:
                    texto_bruto = f.read()
            else:
                continue

            texto_tratado = limpar_texto(texto_bruto)

            nome_txt = os.path.splitext(ficheiro)[0] + '.txt'
            caminho_txt = os.path.join(caminho_destino, nome_txt)

            with open(caminho_txt, 'w', encoding='utf-8') as f:
                f.write(texto_tratado)

            print(f"✓ Extração e limpeza concluídas: '{ficheiro}' -> '{nome_txt}'")
        except Exception as e:
            print(f"Erro ao processar '{ficheiro}': {e}")


if __name__ == "__main__":
    processar_ficheiros()