# Instalação da lib do Selenium
# pip3 install selenium

# Instalação Beautifulsoup4
# pip3 install beautifulsoup4

# Instalação lxml
# pip3 install lxml

# ABRINDO O QUADRO DE NOTAS
# Verificar o Quadro de Notas  aggregatesum
# linkQuadroNotas = "https://ead.ifrn.edu.br/ava/academico/grade/edit/tree/index.php?id=639" #+ codCurso #"639"
# navegador.get(url=linkQuadroNotas)

import re  # alterar a string
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import Select

from time import sleep

service = FirefoxService(
    executable_path="./geckodriver",
)

options = Options()
options.headless = False  # executar de forma visível ou oculta


def editarConfiguracao(navegador, link, contEditarConfiguracao):
    print("Analisando as Configurações do Curso")
    checagemTotal = 0
    cont = 0

    # CLICAR NA CATRACA PARA ATIVAR E EDIÇÃO
    navegador.find_element(by=By.ID, value="action-menu-toggle-2").click()
    sleep(1)

    # CLICA NO BOTÃO DE ATIVAR A EDIÇÃO
    navegador.find_element(
        by=By.LINK_TEXT, value="Editar configurações"
    ).click()  # Abrir
    sleep(1)

    # EXPANDINDO TUDO
    navegador.find_element(by=By.LINK_TEXT, value="Expandir tudo").click()  # Abrir
    sleep(1)

    # GERAL - DATA DE TÉRMINO DO CURSO
    checagemTotal += 1
    input_GeralDataTermino = False
    # inputGeralDataTermino = navegador.find_element(by=By.ID,value="id_enddate_enabled")
    if navegador.find_element(
        by=By.ID, value="id_enddate_enabled"
    ).is_selected():  # PADRÃO É DESMARCADO!
        # inputGeralDataTermino.click()
        navegador.find_element(by=By.ID, value="id_enddate_enabled").click()
        input_GeralDataTermino = True
        cont += 1
    # GERAL - NÚMERO DE IDENTIFICAÇÃO DO CURSO
    checagemTotal += 1
    input_GeralNumIdentificacaoCursoSem = False
    input_GeralNumIdentificacaoCursoOk = False
    input_DescricaoImagemCurso = False
    if (
        navegador.find_element(by=By.ID, value="id_idnumber").get_attribute("value")
        == ""
    ):  # VAZIO
        # inputGeralNumIdentificacaoCurso.clear()
        # inputNotaNotaParaAprovacao.send_keys("0,00")
        input_GeralNumIdentificacaoCursoSem = True
        cont += 1
    else:
        input_GeralNumIdentificacaoCursoOk = True
        input_DescricaoImagemCurso = True
        # ATUALIZAR O NOME DO ARQUIVO DA IMAGEM DO CURSO
        inputGeralNumIdentificacaoCurso = navegador.find_element(
            by=By.ID, value="id_idnumber"
        ).get_attribute("value")

        nomeImagem = re.sub("\-MATRIZ|\_MATRIZ", "", inputGeralNumIdentificacaoCurso)
        # print(nomeImagem)
        nomeImagemCurso = f"imagem_curso_{str(nomeImagem)}.png"
        # print(nomeImagemCurso)
        # print(nomeImagemCurso)

        nomeImagemAtual = navegador.find_element(By.CLASS_NAME, "fp-filename")
        # print(nomeImagemAtual.text)
        nomeImagemAtual.click()
        sleep(1)
        atualizarImagemCurso = navegador.find_elements(
            By.XPATH, "//label[@class='form-control-label col-4 px-0']"
        )
        # print(len(atualizarImagemCurso))
        for opcao in atualizarImagemCurso:
            if opcao.text == "Nome":
                idImagem = opcao.get_attribute("for")
                # print(idImagem)
                updateNomeImagem = navegador.find_element(by=By.ID, value=idImagem)
                updateNomeImagem.clear()
                updateNomeImagem.send_keys(nomeImagemCurso)
                navegador.find_element(
                    By.XPATH, "//button[@class='fp-file-update btn-primary btn']"
                ).click()
                sleep(1)
        cont += 1

    # APARÊNCIA - FORÇAR IDIOMA
    checagemTotal += 1
    input_AparenciaForcarIdioma = False
    inputAparenciaForcarIdioma = Select(
        navegador.find_element(by=By.ID, value="id_lang")
    )
    if (
        navegador.find_element(by=By.ID, value="id_lang").get_attribute("value") != ""
    ):  # VAZIO É PADRÃO(NÃO FORÇAR)
        inputAparenciaForcarIdioma.select_by_value("")  # - VAZIO É PADRÃO(NÃO FORÇAR)
        input_AparenciaForcarIdioma = True
        cont += 1
    # APARÊNCIA - NÚMERO DE AVISOS
    checagemTotal += 1
    input_AparenciaNumAvisos = False
    inputAparenciaNumAvisos = Select(
        navegador.find_element(by=By.ID, value="id_newsitems")
    )
    if (
        navegador.find_element(by=By.ID, value="id_newsitems").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(ZERO)
        inputAparenciaNumAvisos.select_by_value("0")  # 0 É PADRÃO(ZERO)
        input_AparenciaNumAvisos = True
        cont += 1
    # APARÊNCIA - MOSTRAR LIVRO DE NOTAS AOS ESTUDANTES
    checagemTotal += 1
    input_AparenciaMostrarLivro = False
    inputAparenciaMostrarLivro = Select(
        navegador.find_element(by=By.ID, value="id_showgrades")
    )
    if (
        navegador.find_element(by=By.ID, value="id_showgrades").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(SIM)
        inputAparenciaMostrarLivro.select_by_value("1")  # 1 É PADRÃO(SIM)
        input_AparenciaMostrarLivro = True
        cont += 1
    # APARÊNCIA - MOSTRAR RELATÓRIO DAS ATIVIDADES
    checagemTotal += 1
    input_AparenciaMostrarRelatorio = False
    inputAparenciaMostrarRelatorio = Select(
        navegador.find_element(by=By.ID, value="id_showreports")
    )
    if (
        navegador.find_element(by=By.ID, value="id_showreports").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(SIM)
        inputAparenciaMostrarRelatorio.select_by_value("1")  # 1 É PADRÃO(SIM)
        input_AparenciaMostrarRelatorio = True
        cont += 1

    # ARQUIVOS E UPLOADS - ARQUIVOS DE CURSO LEGADOS
    checagemTotal += 1
    input_ArquivoUploadsLegados = False
    inputArquivoUploadsLegados = Select(
        navegador.find_element(by=By.ID, value="id_legacyfiles")
    )
    if (
        navegador.find_element(by=By.ID, value="id_legacyfiles").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(NÃO)
        inputArquivoUploadsLegados.select_by_value("1")  # 1 É PADRÃO(NÃO)
        input_ArquivoUploadsLegados = True
        cont += 1
    # ARQUIVOS E UPLOADS - TAMANHO MÁXIMO DE UPLOAD
    checagemTotal += 1
    input_ArquivoUploadsLimiteUpload = False
    inputArquivoUploadsLimiteUpload = Select(
        navegador.find_element(by=By.ID, value="id_maxbytes")
    )
    if (
        navegador.find_element(by=By.ID, value="id_maxbytes").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(LIMITE DE UPLOAD PARA SITE (4Gb))
        inputArquivoUploadsLimiteUpload.select_by_value(
            "0"
        )  # 0 É PADRÃO(LIMITE DE UPLOAD PARA SITE (4Gb))
        input_ArquivoUploadsLimiteUpload = True
        cont += 1

    # ACOMPANHAMENTO DE CONCLUSÃO - ATIVAR ACOMPANHAMENTO DE CONCLUSÃO
    checagemTotal += 1
    input_AcompanhamentoConclusao = False
    inputAcompanhamentoConclusao = Select(
        navegador.find_element(by=By.ID, value="id_enablecompletion")
    )
    if (
        navegador.find_element(by=By.ID, value="id_enablecompletion").get_attribute(
            "value"
        )
        != "1"
    ):  # 1 É PADRÃO(SIM)
        inputAcompanhamentoConclusao.select_by_value("1")  # 1 É PADRÃO(SIM)
        input_AcompanhamentoConclusao = True
        cont += 1

    # GRUPOS - MODALIDADE GRUPO
    checagemTotal += 1
    input_GruposModalidade = False
    inputGruposModalidade = Select(
        navegador.find_element(by=By.ID, value="id_groupmode")
    )
    if (
        navegador.find_element(by=By.ID, value="id_groupmode").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(NENHUM GRUPO)
        inputGruposModalidade.select_by_value("0")  # 0 É PADRÃO(NENHUM GRUPO)
        input_GruposModalidade = True
        cont += 1
    # GRUPOS - FORÇAR MODALIDADE GRUPO
    checagemTotal += 1
    input_GruposForçarModalidade = False
    inputGruposForçarModalidade = Select(
        navegador.find_element(by=By.ID, value="id_groupmodeforce")
    )
    if (
        navegador.find_element(by=By.ID, value="id_groupmodeforce").get_attribute(
            "value"
        )
        != "0"
    ):  # 0 É PADRÃO(NÃO)
        inputGruposForçarModalidade.select_by_value("0")  # 0 É PADRÃO(NÃO)
        input_GruposForçarModalidade = True
        cont += 1
    # GRUPOS - AGRUPAMENTO PADRÃO
    checagemTotal += 1
    input_GruposAgrupamento = False
    inputGruposAgrupamento = Select(
        navegador.find_element(by=By.ID, value="id_defaultgroupingid")
    )
    if (
        navegador.find_element(by=By.ID, value="id_defaultgroupingid").get_attribute(
            "value"
        )
        != "0"
    ):  # 0 É PADRÃO(NENHUM)
        inputGruposAgrupamento.select_by_value("0")  # 0 É PADRÃO(NENHUM)
        input_GruposAgrupamento = True
        cont += 1

    # CLICAR NO BOTÃO DE SALVAR
    navegador.find_element(by=By.ID, value="id_saveanddisplay").click()
    sleep(1)

    # MOSTRAR O ID DO CURSO
    if input_GeralNumIdentificacaoCursoOk != False:
        print(
            f"==> 'Número de identificação do curso' é: {inputGeralNumIdentificacaoCurso} <=="
        )
    if input_GeralNumIdentificacaoCursoSem != False:
        print(
            "==> 'Número de identificação do curso' está vazio. Solicitar um ID para o Curso. <=="
        )
    print("Total de verificações: %i " % checagemTotal)
    if cont > 0:
        if cont < 2:
            print("Total de modificação: %i" % cont)
        else:
            print("Totais de modificações: %i" % cont)

        if input_GeralDataTermino != False:
            print(
                "'Data de término do curso' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_DescricaoImagemCurso != False:
            print(
                "'O nome da Imagem do curso' foi alterado para o Padrão - PADRÃO (imagem_curso_id.png)"
            )
        if input_AparenciaForcarIdioma != False:
            print("'Forçar idioma' foi alterado para o Padrão - PADRÃO (NÃO FORÇAR).")
        if input_AparenciaNumAvisos != False:
            print("'Número de avisos' foi alterado para o Padrão - PADRÃO (ZERO).")
        if input_AparenciaMostrarLivro != False:
            print(
                "'Mostrar livro de notas aos estudantes' foi alterado para o Padrão - PADRÃO (SIM)."
            )
        if input_AparenciaMostrarRelatorio != False:
            print(
                "'Mostrar relatório das atividades' foi alterado para o Padrão - PADRÃO (SIM)."
            )

        if input_ArquivoUploadsLegados != False:
            print(
                "'Arquivos de curso legados' foi alterado para o Padrão - PADRÃO (NÃO)."
            )
        if input_ArquivoUploadsLimiteUpload != False:
            print(
                "'Tamanho máximo de upload' foi alterado para o Padrão - PADRÃO (LIMITE DE UPLOAD PARA SITE (4Gb))."
            )

        if input_AcompanhamentoConclusao != False:
            print(
                "'Ativar acompanhamento de conclusão' foi alterado para o Padrão - PADRÃO (SIM)."
            )

        if input_GruposModalidade != False:
            print(
                "'Modalidade grupo' foi alterado para o Padrão - PADRÃO (NENHUM GRUPO)."
            )
        if input_GruposForçarModalidade != False:
            print(
                "'Forçar modalidade grupo' foi alterado para o Padrão - PADRÃO (NÃO)."
            )
        if input_GruposAgrupamento != False:
            print("'Agrupamento padrão' foi alterado para o Padrão - PADRÃO (NENHUM).")
    else:
        print("Análise da Configuração do Curso foi concluída sem observações!")

    # print("Verificação concluída")
