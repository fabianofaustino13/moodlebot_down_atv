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


def validarPasta(navegador, link, contPasta):
    checagemTotal = 0
    contPasta = 0
    # ENTRANDO NO LIVRO
    # EXPANDINDO TUDO
    navegador.find_element(by=By.LINK_TEXT, value="Expandir tudo").click()  # Abrir
    sleep(1)
    # GERAL - DESMARCANDO A OPÇÃO DE EXIBIR DESCRIÇÃO NA PÁGINA DO CURSO
    checagemTotal += 1
    input_GeralExibirDescricaoNaPaginaCurso = False
    inputGeralExibirDescricaoNaPaginaCurso = navegador.find_element(
        by=By.ID, value="id_showdescription"
    )
    if navegador.find_element(
        by=By.ID, value="id_showdescription"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputGeralExibirDescricaoNaPaginaCurso.click()
        input_GeralExibirDescricaoNaPaginaCurso = True
        contPasta += 1
        # sleep(1)
    # CONTEÚDO - EXIBIR O CONTEÚDO DA PASTA
    checagemTotal += 1
    input_ConteudoExibirConteudoPasta = False
    inputConteudoExibirConteudoPasta = Select(
        navegador.find_element(by=By.ID, value="id_display")
    )
    if (
        navegador.find_element(by=By.ID, value="id_display").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(EM UMA PÁGINA SEPARADA)
        inputConteudoExibirConteudoPasta.select_by_value(
            "0"
        )  # 0 É PADRÃO(EM UMA PÁGINA SEPARADA)
        input_ConteudoExibirConteudoPasta = True
        contPasta += 1
        # sleep(1)
    # CONTEÚDO - DESMARCANDO A OPÇÃO DE MOSTRAR SUBPASTAS EXPANDIDAS
    checagemTotal += 1
    input_ConteudoMostrarSubPastasExpandidas = False
    inputConteudoMostrarSubPastasExpandidas = navegador.find_element(
        by=By.ID, value="id_showexpanded"
    )
    if navegador.find_element(
        by=By.ID, value="id_showexpanded"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputConteudoMostrarSubPastasExpandidas.click()
        input_ConteudoMostrarSubPastasExpandidas = True
        contPasta += 1
        # sleep(1)
    # CONTEÚDO - MARCANDO A OPÇÃO DE EXIBIR BOTÃO DE DOWNLOAD DA PASTA
    checagemTotal += 1
    input_ConteudoExibirBotaoDownload = False
    inputConteudoExibirBotaoDownload = navegador.find_element(
        by=By.ID, value="id_showdownloadfolder"
    )
    if (
        navegador.find_element(by=By.ID, value="id_showdownloadfolder").is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputConteudoExibirBotaoDownload.click()
        input_ConteudoExibirBotaoDownload = True
        contPasta += 1
        # sleep(1)
    # CONFIGURAÇÕES COMUNS DE MÓDULOS - DISPONIBILIDADE
    checagemTotal += 1
    input_ConfComumModuloDisponibilidade = False
    inputConfComumModuloDisponibilidade = Select(
        navegador.find_element(by=By.ID, value="id_visible")
    )
    if (
        navegador.find_element(by=By.ID, value="id_visible").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(MOSTRAR NA PÁGINA DO CURSO)
        inputConfComumModuloDisponibilidade.select_by_value(
            "1"
        )  # 1 É PADRÃO(MOSTRAR NA PÁGINA DO CURSO)
        input_ConfComumModuloDisponibilidade = True
        # print("Item de Nota em Pontos Decimais Geral foi alterado para o Padrão - PADRÃO(2).")
        contPasta += 1
        # sleep(1)
    # CONFIGURAÇÕES COMUNS DE MÓDULOS - NÚMERO DE IDENTIFICAÇÃO DO MÚDULO
    checagemTotal += 1
    input_ConfComumModuloNumIdentificacao = False
    inputConfComumModuloNumIdentificacao = navegador.find_element(
        by=By.ID, value="id_cmidnumber"
    )
    if (
        navegador.find_element(by=By.ID, value="id_cmidnumber").get_attribute("value")
        != ""
    ):  # PADRÃO É VAZIO
        inputConfComumModuloNumIdentificacao.clear()
        input_ConfComumModuloNumIdentificacao = True
        contPasta += 1
        # sleep(1)
    # RESTRINGIR ACESSO - NÃO SERÁ TRATADO

    # CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO
    try:
        checagemTotal += 1
        input_ConclusaoAtividadeBloqueada = False
        input_ConclusaoAtividadeAcompanhamento = False
        inputConclusaoAtividadeAcompanhamento = Select(
            navegador.find_element(by=By.ID, value="id_completion")
        )
        if (
            navegador.find_element(by=By.ID, value="id_completion").get_attribute(
                "value"
            )
            != "2"
        ):  # 2 É PADRÃO(MOSTRAR ATIVIDADE COMO CONCLUÍDA QUANDO AS CONDIÇÕES FOREM SATISFEITAS)
            inputConclusaoAtividadeAcompanhamento.select_by_value(
                "2"
            )  # 2 É PADRÃO(MOSTRAR ATIVIDADE COMO CONCLUÍDA QUANDO AS CONDIÇÕES FOREM SATISFEITAS)
            input_ConclusaoAtividadeAcompanhamento = True
            # print("Item de Nota em Pontos Decimais Geral foi alterado para o Padrão - PADRÃO(2).")
            contPasta += 1
            # sleep(1)
        # CONCLUSÇÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO
        checagemTotal += 1
        input_ConclusaoAtividadeRequerVisualizacao = False
        inputConclusaoAtividadeRequerVisualizacao = navegador.find_element(
            by=By.ID, value="id_completionview"
        )
        if (
            navegador.find_element(by=By.ID, value="id_completionview").is_selected()
            == False
        ):  # PADRÃO É MARCADO! SE ESTIVER DESMARCADO, ENTRE E MARQUE
            inputConclusaoAtividadeRequerVisualizacao.click()
            input_ConclusaoAtividadeRequerVisualizacao = True
            contPasta += 1
            # sleep(1)
    except:
        # CONCLUSÃO DE ATIVIDADE - BLOQUEADO
        checagemTotal += 1
        input_ConclusaoAtividadeBloqueada = False
        input_ConclusaoAtividadeAcompanhamento = False
        input_ConclusaoAtividadeRequerVisualizacao = False
        if (
            navegador.find_element(by=By.ID, value="id_unlockcompletion").get_attribute(
                "value"
            )
            == "Desbloquear opções de conclusão"
        ):
            print("entrou para desbloquear")
            atvBloqueada = navegador.find_element(by=By.ID, value="id_unlockcompletion")
            atvBloqueada.click()
            input_ConclusaoAtividadeBloqueada = True
            contPasta += 1
            sleep(1)
        # CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO
        checagemTotal += 1
        input_ConclusaoAtividadeAcompanhamento = False
        inputConclusaoAtividadeAcompanhamento = Select(
            navegador.find_element(by=By.ID, value="id_completion")
        )
        if (
            navegador.find_element(by=By.ID, value="id_completion").get_attribute(
                "value"
            )
            != "2"
        ):  # 2 É PADRÃO(MOSTRAR ATIVIDADE COMO CONCLUÍDA QUANDO AS CONDIÇÕES FOREM SATISFEITAS)
            inputConclusaoAtividadeAcompanhamento.select_by_value(
                "2"
            )  # 2 É PADRÃO(MOSTRAR ATIVIDADE COMO CONCLUÍDA QUANDO AS CONDIÇÕES FOREM SATISFEITAS)
            input_ConclusaoAtividadeAcompanhamento = True
            # print("Item de Nota em Pontos Decimais Geral foi alterado para o Padrão - PADRÃO(2).")
            contPasta += 1
            # sleep(1)
        # CONCLUSÇÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO
        checagemTotal += 1
        input_ConclusaoAtividadeRequerVisualizacao = False
        inputConclusaoAtividadeRequerVisualizacao = navegador.find_element(
            by=By.ID, value="id_completionview"
        )
        if (
            navegador.find_element(by=By.ID, value="id_completionview").is_selected()
            == False
        ):  # PADRÃO É MARCADO! SE ESTIVER DESMARCADO, ENTRE E MARQUE
            inputConclusaoAtividadeRequerVisualizacao.click()
            input_ConclusaoAtividadeRequerVisualizacao = True
            contPasta += 1
            # sleep(1)

    # CONCLUSÇÃO DE ATIVIDADE - CONCLUSÃO ESPERADA EM
    checagemTotal += 1
    input_ConclusaoAtividadeConclusaoEsperadaEm = False
    inputConclusaoAtividadeConclusaoEsperadaEm = navegador.find_element(
        by=By.ID, value="id_completionexpected_enabled"
    )
    if navegador.find_element(
        by=By.ID, value="id_completionexpected_enabled"
    ).is_selected():  # PADRÃO É DESMARCADO! SE ESTIVER MARCADO, ENTRE E DESMARQUE
        inputConclusaoAtividadeConclusaoEsperadaEm.click()
        input_ConclusaoAtividadeConclusaoEsperadaEm = True
        contPasta += 1
        # sleep(1)

    # CLICAR NO BOTÃO DE SALVAR
    navegador.find_element(by=By.ID, value="id_submitbutton2").click()
    sleep(1)

    print("Total de verificações: %i " % checagemTotal)
    if contPasta > 0:
        if contPasta < 2:
            print("Total de modificação: %i" % contPasta)
        else:
            print("Totais de modificações: %i" % contPasta)
        # print("Validação em Ativar Edição concluída.")
        # else:
        #    print("Validação em Ativar Edição concluída sem alteração")
        # if contLivro > 0:
        if input_GeralExibirDescricaoNaPaginaCurso != False:
            print(
                "'Exibir descrição na página do curso' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_ConteudoExibirConteudoPasta != False:
            print(
                "'Exibir o conteúdo da pasta' foi alterado para o Padrão - PADRÃO (EM UMA PÁGINA SEPARADA)."
            )
        if input_ConteudoMostrarSubPastasExpandidas != False:
            print(
                "'Mostrar subpastas expandidas' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_ConteudoExibirBotaoDownload != False:
            print(
                "'Exibir botão de download da pasta' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_ConfComumModuloDisponibilidade != False:
            print(
                "'Disponibilidade' foi alterado para o Padrão - PADRÃO (MOSTRAR NA PÁGINA DO CURSO)."
            )
        if input_ConfComumModuloNumIdentificacao != False:
            print(
                "'Número de identificação do módulo' foi alterado para o Padrão - PADRÃO ('VAZIO')."
            )
        if input_ConclusaoAtividadeBloqueada != False:
            print(
                "'Acompanhamento de conclusão bloqueada.' Foi desbloqueada para habilitar o padrão"
            )
        if input_ConclusaoAtividadeAcompanhamento != False:
            print(
                "'Acompanhamento de conclusão' foi alterado para o Padrão - PADRÃO (MOSTRAR ATIVIDADE COMO CONCLUÍDA QUANDO AS CONDIÇÕES FOREM SATISFEITAS)."
            )
        if input_ConclusaoAtividadeRequerVisualizacao != False:
            print(
                "'Requer visualização' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_ConclusaoAtividadeConclusaoEsperadaEm != False:
            print(
                "'Conclusão esperada em' foi alterado para o Padrão - PADRÃO ('DESMARCADO')."
            )
    else:
        print("Análise da Pasta foi concluída sem observações!")
    return contPasta
