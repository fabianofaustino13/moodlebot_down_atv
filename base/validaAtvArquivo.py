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


def validarArquivo(navegador, link, contArquivo):
    checagemTotal = 0
    contArquivo = 0
    # ENTRANDO NO LIVRO
    # EXPANDINDO TUDO
    navegador.find_element(by=By.LINK_TEXT, value="Expandir tudo").click()  # Abrir
    # sleep(1)

    navegador.find_element(by=By.LINK_TEXT, value="Mostrar mais ...").click()  # Abrir
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
        contArquivo += 1
        # sleep(1)

    # APARÊNCIA - EXIBIR
    checagemTotal += 1
    input_AparenciaExibir = False
    inputAparenciaExibir = Select(navegador.find_element(by=By.ID, value="id_display"))
    if (
        navegador.find_element(by=By.ID, value="id_display").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(AUTOMÁTICO)
        inputAparenciaExibir.select_by_value("0")  # 0 É PADRÃO(AUTOMÁTICO)
        input_AparenciaExibir = True
        contArquivo += 1
        # sleep(1)
    # APARÊNCIA - MOSTRAR TAMANHO
    checagemTotal += 1
    input_AparenciaMostrarTamanho = False
    inputAparenciaMostrarTamanho = navegador.find_element(by=By.ID, value="id_showsize")
    if navegador.find_element(
        by=By.ID, value="id_showsize"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputAparenciaMostrarTamanho.click()
        input_AparenciaMostrarTamanho = True
        contArquivo += 1
        # sleep(1)
    # APARÊNCIA - MOSTRAR TIPO
    checagemTotal += 1
    input_AparenciaMostrarTipo = False
    inputAparenciaMostrarTipo = navegador.find_element(by=By.ID, value="id_showtype")
    if navegador.find_element(
        by=By.ID, value="id_showtype"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputAparenciaMostrarTipo.click()
        input_AparenciaMostrarTipo = True
        contArquivo += 1
        # sleep(1)
    # APARÊNCIA - EXIBIR DATA DE ENVIO/MODIFICAÇÃO
    checagemTotal += 1
    input_AparenciaMostrarData = False
    inputAparenciaMostrarData = navegador.find_element(by=By.ID, value="id_showdate")
    if navegador.find_element(
        by=By.ID, value="id_showdate"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputAparenciaMostrarData.click()
        input_AparenciaMostrarData = True
        contArquivo += 1
        # sleep(1)
    # APARÊNCIA - EXIBIR A DESCRIÇÃO DOS RECURSOS
    checagemTotal += 1
    input_AparenciaExibirDescricaoRecurso = False
    inputAparenciaExibirDescricaoRecurso = navegador.find_element(
        by=By.ID, value="id_printintro"
    )
    if (
        navegador.find_element(by=By.ID, value="id_printintro").is_selected() == False
    ):  # PADRÃO É MARCADO
        inputAparenciaExibirDescricaoRecurso.click()
        input_AparenciaExibirDescricaoRecurso = True
        contArquivo += 1
        # sleep(1)
    # APARÊNCIA - USAR FILTROS NO CONTEÚDO DO ARQUIVO
    checagemTotal += 1
    input_AparenciaUsarFiltro = False
    inputAparenciaUsarFiltro = Select(
        navegador.find_element(by=By.ID, value="id_filterfiles")
    )
    if (
        navegador.find_element(by=By.ID, value="id_filterfiles").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(NENHUM)
        inputAparenciaUsarFiltro.select_by_value("0")  # 0 É PADRÃO(NENHUM)
        input_AparenciaUsarFiltro = True
        contArquivo += 1
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
        contArquivo += 1
        # sleep(1)
    # CONFIGURAÇÕES COMUNS DE MÓDULOS - NÚMERO DE IDENTIFICAÇÃO DO MÚDULO
    """ checagemTotal+=1
    input_ConfComumModuloNumIdentificacao = False
    inputConfComumModuloNumIdentificacao = navegador.find_element(by=By.ID,value="id_cmidnumber")
    if navegador.find_element(by=By.ID,value="id_cmidnumber").get_attribute("value") != "": #PADRÃO É VAZIO
        inputConfComumModuloNumIdentificacao.clear()
        input_ConfComumModuloNumIdentificacao = True
        contArquivo+=1
        sleep(1) """
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
            contArquivo += 1
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
            contArquivo += 1
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
            # print("entrou para desbloquear")
            atvBloqueada = navegador.find_element(by=By.ID, value="id_unlockcompletion")
            atvBloqueada.click()
            input_ConclusaoAtividadeBloqueada = True
            contArquivo += 1
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
            contArquivo += 1
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
            contArquivo += 1
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
        contArquivo += 1
        # sleep(1)

    # COMPETÊNCIAS - APÓS CONCLUSÃO DA ATIVIDADE
    checagemTotal += 1
    input_CompetenciaAposConclusao = False
    inputCompetenciaAposConclusao = Select(
        navegador.find_element(by=By.ID, value="id_competency_rule")
    )
    if (
        navegador.find_element(by=By.ID, value="id_competency_rule").get_attribute(
            "value"
        )
        != "0"
    ):  # 0 É PADRÃO(FAZER NADA)
        inputCompetenciaAposConclusao.select_by_value("0")  # 0 É PADRÃO(FAZER NADA)
        input_CompetenciaAposConclusao = True
        contArquivo += 1
        # sleep(1)

    # CLICAR NO BOTÃO DE SALVAR
    navegador.find_element(by=By.ID, value="id_submitbutton2").click()
    sleep(1)

    print("Total de verificações: %i " % checagemTotal)
    if contArquivo > 0:
        if contArquivo < 2:
            print("Total de modificação: %i" % contArquivo)
        else:
            print("Totais de modificações: %i" % contArquivo)
        # print("Validação em Ativar Edição concluída.")
        # else:
        #    print("Validação em Ativar Edição concluída sem alteração")
        # if contLivro > 0:
        if input_GeralExibirDescricaoNaPaginaCurso != False:
            print(
                "'Exibir descrição na página do curso' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )

        if input_AparenciaExibir != False:
            print("'Exibir' foi alterado para o Padrão - PADRÃO (AUTOMÁTICO).")
        if input_AparenciaMostrarTamanho != False:
            print("'Mostrar tamanho' foi alterado para o Padrão - PADRÃO (DESMARCADO).")
        if input_AparenciaMostrarTipo != False:
            print("'Mostrar tipo' foi alterado para o Padrão - PADRÃO (DESMARCADO).")
        if input_AparenciaMostrarData != False:
            print(
                "'Exibir data de envio/modificação' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_AparenciaExibirDescricaoRecurso != False:
            print(
                "'Exibir a descrição dos recursos' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_AparenciaUsarFiltro != False:
            print(
                "'Usar filtros no conteúdo do arquivo' foi alterado para o Padrão - PADRÃO (NENHUM)."
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

        if input_CompetenciaAposConclusao != False:
            print(
                "'Após conclusão da atividade' foi alterado para o Padrão - PADRÃO ('FAZER NADA')."
            )
    else:
        print("Análise do Arquivo foi concluída sem observações!")
    # sleep(1)
    return contArquivo
