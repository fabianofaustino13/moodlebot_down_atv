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


def validarPagina(navegador, link, contPagina):
    checagemTotal = 0
    cont = 0
    # ENTRANDO NO LIVRO
    # EXPANDINDO TUDO
    navegador.find_element(by=By.LINK_TEXT, value="Expandir tudo").click()  # Abrir
    sleep(1)
    # GERAL - MARCANDO A OPÇÃO DE EXIBIR DESCRIÇÃO NA PÁGINA DO CURSO
    checagemTotal += 1
    input_GeralExibirDescricaoNaPaginaCurso = False
    inputGeralExibirDescricaoNaPaginaCurso = navegador.find_element(
        by=By.ID, value="id_showdescription"
    )
    if inputGeralExibirDescricaoNaPaginaCurso.is_selected():  # PADRÃO É MARCADO
        inputGeralExibirDescricaoNaPaginaCurso.click()
        input_GeralExibirDescricaoNaPaginaCurso = True
        cont += 1

    # APARÊNCIA - MOSTRAR O NOME DA PÁGINA
    checagemTotal += 1
    input_AparenciaMostrarNomePagina = False
    inputAparenciaMostrarNomePagina = navegador.find_element(
        by=By.ID, value="id_printheading"
    )
    if inputAparenciaMostrarNomePagina.is_selected():  # PADRÃO É MARCADO
        inputAparenciaMostrarNomePagina.click()
        input_AparenciaMostrarNomePagina = True
        cont += 1
    # APARÊNCIA - EXIBIR DESCRIÇÃO DA PÁGINA
    checagemTotal += 1
    input_AparenciaExibirDescricao = False
    inputAparenciaExibirDescricao = navegador.find_element(
        by=By.ID, value="id_printintro"
    )
    if inputAparenciaExibirDescricao.is_selected():  # PADRÃO É MARCADO
        inputAparenciaExibirDescricao.click()
        input_AparenciaExibirDescricao = True
        cont += 1
    # APARÊNCIA - MOSTRAR A DATA DA ÚLTIMA ALTERAÇÃO
    checagemTotal += 1
    input_AparenciaMostrarUltimaAlteracao = False
    inputAparenciaMostrarUltimaAlteracao = navegador.find_element(
        by=By.ID, value="id_printlastmodified"
    )
    if inputAparenciaMostrarUltimaAlteracao.is_selected():  # PADRÃO É MARCADO
        inputAparenciaMostrarUltimaAlteracao.click()
        input_AparenciaMostrarUltimaAlteracao = True
        cont += 1

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
        cont += 1

    # CONFIGURAÇÕES COMUNS DE MÓDULOS - NÚMERO DE IDENTIFICAÇÃO DO MÚDULO
    # checagemTotal+=1
    # input_ConfComumModuloNumIdentificacao = False
    # inputConfComumModuloNumIdentificacao = navegador.find_element(by=By.ID,value="id_cmidnumber")
    # if navegador.find_element(by=By.ID,value="id_cmidnumber").get_attribute("value") != "": #PADRÃO É VAZIO
    #    inputConfComumModuloNumIdentificacao.clear()
    #    input_ConfComumModuloNumIdentificacao = True
    #    contPasta+=1
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
            cont += 1
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
            cont += 1
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
            cont += 1
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
            cont += 1
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
            cont += 1

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
        cont += 1

    # CLICAR NO BOTÃO DE SALVAR
    navegador.find_element(by=By.ID, value="id_submitbutton2").click()
    sleep(1)

    print("Total de verificações: %i " % checagemTotal)
    if cont > 0:
        if cont < 2:
            print("Total de modificação: %i" % cont)
        else:
            print("Totais de modificações: %i" % cont)

        if input_GeralExibirDescricaoNaPaginaCurso != False:
            print(
                "'Exibir descrição na página do curso' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )

        if input_AparenciaMostrarNomePagina != False:
            print(
                "'Mostrar o nome da página' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_AparenciaExibirDescricao != False:
            print(
                "'Exibir descrição da página' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_AparenciaMostrarUltimaAlteracao != False:
            print(
                "'Mostrar a data da última alteração' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )

        if input_ConfComumModuloDisponibilidade != False:
            print(
                "'Disponibilidade' foi alterado para o Padrão - PADRÃO (MOSTRAR NA PÁGINA DO CURSO)."
            )
        # if input_ConfComumModuloNumIdentificacao != False:
        #    print("'Número de identificação do módulo' foi alterado para o Padrão - PADRÃO ('VAZIO').")

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
    # return cont
