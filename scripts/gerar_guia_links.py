import os


def gerar_arquivo_links():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_destino = os.path.normpath(os.path.join(base_dir, '../dados_brutos', 'portais_e_links_oficiais.txt'))

    os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)

    conteudo = """GUIA DE PORTAIS E LINKS OFICIAIS DE SERVIÇOS MIGRATÓRIOS
PROJETO CONECTMUNDI - BASE DE CONHECIMENTO (RAG)

1. POLÍCIA FEDERAL - REGISTRO E DOCUMENTAÇÃO MIGRATÓRIA
- Agendamento do Registro Nacional Migratório (RNM / CRNM):
  Link oficial: https://www.gov.br/pt-br/servicos/registrar-se-como-estrangeiro-no-brasil

- Portal de Imigração e Autorização de Residência (Polícia Federal):
  Link oficial: https://www.gov.br/pf/pt-br/assuntos/imigracao

2. CONARE - SOLICITAÇÃO E ACOMPANHAMENTO DE REFÚGIO
- Sistema SISCONARE (Solicitação de Refúgio):
  Link oficial: https://sisconare.mj.gov.br/

- Acompanhamento do Processo no CONARE:
  Link oficial: https://www.gov.br/mj/pt-br/assuntos/seus-direitos/refugiados

3. ACNUR BRASIL - PLATAFORMA DE APOIO AO REFUGIADO
- Portal HELP ACNUR Brasil:
  Link oficial: https://help.unhcr.org/brazil/

- Onde Buscar Ajuda (Rede de Acolhimento ACNUR):
  Link oficial: https://help.unhcr.org/brazil/onde-buscar-ajuda/

4. RECEITA FEDERAL - EMISSÃO E REGULARIZAÇÃO DO CPF
- Inscrição no CPF para Estrangeiros:
  Link oficial: https://www.gov.br/receitafederal/pt-br/assuntos/meu-cpf

5. MINISTÉRIO DO TRABALHO E EMPREGO (MTE) - CTPS DIGITAL
- Carteira de Trabalho Digital (MTE):
  Link oficial: https://www.gov.br/pt-br/servicos/obter-a-carteira-de-trabalho-e-previdencia-social

- Portal Emprega Brasil:
  Link oficial: https://empregabrasil.mte.gov.br/

6. MINISTÉRIO DA SAÚDE - CARTÃO SUS (MEU SUS DIGITAL)
- Portal Meu SUS Digital (Cartão Nacional de Saúde):
  Link oficial: https://meususdgt.saude.gov.br/

7. MINISTÉRIO DA EDUCAÇÃO (MEC) - REVALIDAÇÃO DE DIPLOMAS
- Plataforma Carolina Bori (MEC):
  Link oficial: https://carolinabori.mec.gov.br/

- Portal Gov.br - Serviço de Revalidação de Diplomas:
  Link oficial: https://www.gov.br/pt-br/servicos/reconhecer-ou-revalidar-diploma-de-curso-superior-obtido-no-exterior

8. MINISTÉRIO DO DESENVOLVIMENTO SOCIAL (MDS) - CADÚNICO
- Portal do Cadastro Único (CadÚnico):
  Link oficial: https://cadunico.dataprev.gov.br/

9. INFORMATIVOS E GUIAS ESPECÍFICOS POR POPULAÇÃO (ACNUR BRASIL)
- Informativos para a População Venezuelana (ACNUR):
  Link oficial: https://help.unhcr.org/brazil/informativos-para/populacao-venezuelana/
  Emergência Venezuela: https://www.acnur.org/br/emergencias/venezuela

- Informativos para a População Haitiana (ACNUR):
  Link oficial: https://help.unhcr.org/brazil/informativos-para/haitian-population/
  Atuação no Haiti: https://www.acnur.org/br/haiti

- Informativos para a População Afegã (ACNUR):
  Link oficial: https://help.unhcr.org/brazil/informativos-para/populacao-afega/
  Emergência Afeganistão: https://www.acnur.org/br/emergencias/afeganistao
"""

    with open(caminho_destino, 'w', encoding='utf-8') as f:
        f.write(conteudo)

    print(f"✓ Ficheiro de links atualizado com sucesso em: '{caminho_destino}'")


if __name__ == "__main__":
    gerar_arquivo_links()