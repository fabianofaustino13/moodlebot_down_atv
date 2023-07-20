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


def validarLivro(navegador, link, contLivro):
    checagemTotal = 0
    contLivro = 0
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
        contLivro += 1
        # sleep(1)
    # APARENCIA - FORMATAÇÃO DE CAPÍTULOS
    checagemTotal += 1
    input_AparenciaFormatacaoCapitulo = False
    inputAparenciaFormatacaoCapitulo = Select(
        navegador.find_element(by=By.ID, value="id_numbering")
    )
    if (
        navegador.find_element(by=By.ID, value="id_numbering").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(NÚMEROS)
        inputAparenciaFormatacaoCapitulo.select_by_value("1")  # 1 É PADRÃO(NÚMEROS)
        input_AparenciaFormatacaoCapitulo = True
        contLivro += 1
        # sleep(1)
    # APARENCIA - ESTILO DE NAVEGAÇÃO
    checagemTotal += 1
    input_AparenciaEstiloNavegacao = False
    inputAparenciaEstiloNavegacao = Select(
        navegador.find_element(by=By.ID, value="id_navstyle")
    )
    if (
        navegador.find_element(by=By.ID, value="id_navstyle").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(IMAGENS)
        inputAparenciaEstiloNavegacao.select_by_value("1")  # 1 É PADRÃO(IMAGENS)
        input_AparenciaEstiloNavegacao = True
        contLivro += 1
        # sleep(1)
    # APARENCIA - DESMARCANDO A OPÇÃO DE TÍTULOS PERSONALIZADOS
    checagemTotal += 1
    input_AparenciaTituloPersonalizado = False
    inputAparenciaTituloPersonalizado = navegador.find_element(
        by=By.ID, value="id_customtitles"
    )
    if navegador.find_element(
        by=By.ID, value="id_customtitles"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputAparenciaTituloPersonalizado.click()
        input_AparenciaTituloPersonalizado = True
        contLivro += 1
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
        contLivro += 1
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
        # inputConfComumModuloNumIdentificacao.send_keys("0,00")
        input_ConfComumModuloNumIdentificacao = True
        contLivro += 1
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
            contLivro += 1
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
            contLivro += 1
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
            atvBloqueada = navegador.find_element(by=By.ID, value="id_unlockcompletion")
            atvBloqueada.click()
            input_ConclusaoAtividadeBloqueada = True
            contLivro += 1
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
            contLivro += 1
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
            contLivro += 1
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
        contLivro += 1
        # sleep(1)

    # CLICAR NO BOTÃO DE SALVAR
    navegador.find_element(by=By.ID, value="id_submitbutton2").click()
    sleep(1)
    # COMPETENCIAS - APÓS CONCLUSÃO DA ATIVIDADE
    """ input_CompetenciaAposConclusaoAtividade = False
    inputCompetenciaAposConclusaoAtividade = Select(navegador.find_element(by=By.ID,value="id_competency_rule"))
    if navegador.find_element(by=By.ID,value="id_competency_rule").get_attribute("value") != "0": # 0 É PADRÃO(FAZER NADA)
        inputCompetenciaAposConclusaoAtividade.select_by_value("0") # 2 É PADRÃO(FAZER NADA)
        input_CompetenciaAposConclusaoAtividade = True
        #print("Item de Nota em Pontos Decimais Geral foi alterado para o Padrão - PADRÃO(2).")
        contLivro+=1
        sleep(2)   """
    print("Total de verificações: %i " % checagemTotal)
    if contLivro > 0:
        if contLivro < 2:
            print("Total de modificação: %i" % contLivro)
        else:
            print("Totais de modificações: %i" % contLivro)

        if input_GeralExibirDescricaoNaPaginaCurso != False:
            print(
                "'Exibir descrição na página do curso' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_AparenciaFormatacaoCapitulo != False:
            print(
                "'Formatação de capítulo' foi alterado para o Padrão - PADRÃO (NÚMEROS)."
            )
        if input_AparenciaEstiloNavegacao != False:
            print(
                "'Estilo de navegação' foi alterado para o Padrão - PADRÃO (IMAGENS)."
            )
        if input_AparenciaTituloPersonalizado != False:
            print(
                "'Títulos personalizados' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
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
        print("Análise do Livro foi concluída sem observações!")
    return contLivro
