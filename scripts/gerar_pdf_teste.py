import os
from fpdf import FPDF


def criar_pdf_teste():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_destino = os.path.normpath(os.path.join(base_dir, '../dados_brutos', 'diretriz_teste_01.pdf'))

    os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    linhas = [
        "PROJETO CONECTMUNDI - DOCUMENTO DE TESTE OFICIAL",
        "Orgao: Policia Federal e ACNUR",
        "",
        "O Registro Nacional Migratorio (RNM) e o documento oficial de identificacao",
        "de estrangeiros residentes no Brasil. Ele e fundamental para a emissao da",
        "Carteira de Trabalho Digital e acesso integral ao Sistema Unico de Saude (SUS).",
        "",
        "Para solicitar o refugio, o cidadao estrangeiro deve acessar o sistema SISCONARE",
        "e preencher o formulario de solicitacao inicial."
    ]

    for linha in linhas:
        pdf.cell(200, 10, txt=linha, ln=True)

    pdf.output(caminho_destino)
    print(f"✓ PDF de teste gerado com sucesso em: '{caminho_destino}'")


if __name__ == "__main__":
    criar_pdf_teste()