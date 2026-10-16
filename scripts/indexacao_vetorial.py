import os
import chromadb
from chromadb.utils import embedding_functions
from langchain_text_splitters import RecursiveCharacterTextSplitter


def identificar_orgao(nome_ficheiro):
    """Atribui automaticamente o órgão de origem para filtro de metadados."""
    nome = nome_ficheiro.lower()
    if 'acnur' in nome or 'refugiado' in nome:
        return 'ACNUR'
    elif 'policia' in nome or 'pf' in nome or 'rnm' in nome or 'crnm' in nome:
        return 'Policia_Federal'
    elif 'sus' in nome or 'saude' in nome:
        return 'Ministerio_da_Saude'
    elif 'trabalho' in nome or 'ctps' in nome or 'mte' in nome:
        return 'MTE'
    elif 'conare' in nome or 'sisconare' in nome:
        return 'CONARE'
    elif 'mec' in nome or 'carolina_bori' in nome or 'diploma' in nome:
        return 'MEC'
    elif 'cadunico' in nome or 'bolsa_familia' in nome:
        return 'MDS'
    return 'Geral'


def indexar_textos(pasta_textos='./dados_limpos', caminho_db='../chromadb_local'):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_textos = os.path.normpath(os.path.join(base_dir, pasta_textos))
    caminho_banco = os.path.normpath(os.path.join(base_dir, caminho_db))

    print(f"A ligar ao banco vetorial em: {caminho_banco}")
    cliente = chromadb.PersistentClient(path=caminho_banco)

    funcao_embedding = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    colecao = cliente.get_or_create_collection(
        name="documentos_oficiais",
        embedding_function=funcao_embedding
    )

    divisor = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
    )

    if not os.path.exists(caminho_textos):
        print(f"Erro: Pasta '{caminho_textos}' não encontrada.")
        return

    ficheiros = [f for f in os.listdir(caminho_textos) if f.endswith('.txt')]
    if not ficheiros:
        print(f"Nenhum ficheiro .txt encontrado em '{caminho_textos}'. Execute 'extracao_dados.py' primeiro.")
        return

    for ficheiro in ficheiros:
        caminho_txt = os.path.join(caminho_textos, ficheiro)

        with open(caminho_txt, 'r', encoding='utf-8') as f:
            texto_completo = f.read()

        fatias = divisor.split_text(texto_completo)
        if not fatias:
            continue

        orgao = identificar_orgao(ficheiro)
        ids = [f"{ficheiro}_chunk_{i}" for i in range(len(fatias))]

        metadados = [
            {
                "arquivo_origem": ficheiro,
                "orgao": orgao,
                "projeto": "ConectMundi"
            }
            for _ in fatias
        ]

        colecao.upsert(documents=fatias, metadatas=metadados, ids=ids)
        print(f"✓ Indexado: {len(fatias)} fatias de '{ficheiro}' [Órgão: {orgao}]")


if __name__ == "__main__":
    indexar_textos()