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


def validarSumario(navegador, link, contGlossario):
    checagemTotal = 0
    contSumario = 0
    # ENTRANDO NO LIVRO
    # EXPANDINDO TUDO
    inputPastaExpandirTudo = navegador.find_element(
        by=By.LINK_TEXT, value="Expandir tudo"
    )  # Abrir
    inputPastaExpandirTudo.click()
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
        contGlossario += 1
        sleep(1)
    # GERAL - TIPO DE GLOSSÁRIO, PODE SER QUALQUER UM - PRINCIPAL OU SECUNDÁRIO

    # ITEM - APROVAÇÃO IMEDIATA DE NOVOS ITENS
    checagemTotal += 1
    input_ItemAprovacaoImediataNovoItem = False
    inputItemAprovacaoImediataNovoItem = Select(
        navegador.find_element(by=By.ID, value="id_defaultapproval")
    )
    if (
        navegador.find_element(by=By.ID, value="id_defaultapproval").get_attribute(
            "value"
        )
        != "1"
    ):  # 1 É PADRÃO(SIM)
        inputItemAprovacaoImediataNovoItem.select_by_value("1")  # 1 É PADRÃO(SIM)
        input_ItemAprovacaoImediataNovoItem = True
        contGlossario += 1
        sleep(1)
    # ITEM - SEMPRE PERMITIR EDIÇÃO
    checagemTotal += 1
    input_ItemSemprePermitirEdicao = False
    inputItemSemprePermitirEdicao = Select(
        navegador.find_element(by=By.ID, value="id_editalways")
    )
    if (
        navegador.find_element(by=By.ID, value="id_editalways").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(NÃO)
        inputItemSemprePermitirEdicao.select_by_value("0")  # 0 É PADRÃO(NÃO)
        input_ItemSemprePermitirEdicao = True
        contGlossario += 1
        sleep(1)
    # ITEM - PERMITIR ITENS DUPLICADOS
    checagemTotal += 1
    input_ItemPermitirItensDuplicados = False
    inputItemPermitirItensDuplicados = Select(
        navegador.find_element(by=By.ID, value="id_allowduplicatedentries")
    )
    if (
        navegador.find_element(
            by=By.ID, value="id_allowduplicatedentries"
        ).get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(NÃO)
        inputItemPermitirItensDuplicados.select_by_value("0")  # 0 É PADRÃO(NÃO)
        input_ItemPermitirItensDuplicados = True
        contGlossario += 1
        sleep(1)
    # ITEM - PERMITIR COMENTÁRIOS
    checagemTotal += 1
    input_ItemPermitirComentarios = False
    inputItemPermitirComentarios = Select(
        navegador.find_element(by=By.ID, value="id_allowcomments")
    )
    if (
        navegador.find_element(by=By.ID, value="id_allowcomments").get_attribute(
            "value"
        )
        != "0"
    ):  # 0 É PADRÃO(NÃO)
        inputItemPermitirComentarios.select_by_value("0")  # 0 É PADRÃO(NÃO)
        input_ItemPermitirComentarios = True
        contGlossario += 1
        sleep(1)
    # ITEM - FAZER O LINK AUTOMÁTICO DOS ITENS
    checagemTotal += 1
    input_ItemFazerLinkAutoItens = False
    inputItemFazerLinkAutoItens = Select(
        navegador.find_element(by=By.ID, value="id_usedynalink")
    )
    if (
        navegador.find_element(by=By.ID, value="id_usedynalink").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(SIM)
        inputItemFazerLinkAutoItens.select_by_value("1")  # 1 É PADRÃO(SIM)
        input_ItemFazerLinkAutoItens = True
        contGlossario += 1
        sleep(1)

    # APARENCIA - FORMATO DE VISUALIZAÇÃO
    checagemTotal += 1
    input_AparenciaFormatoVisualizacao = False
    inputAparenciaFormatoVisualizacao = Select(
        navegador.find_element(by=By.ID, value="id_displayformat")
    )
    if (
        navegador.find_element(by=By.ID, value="id_displayformat").get_attribute(
            "value"
        )
        != "dictionary"
    ):  # dictionary É PADRÃO(SIMPLES, ESTILO DICIONÁRIO)
        inputAparenciaFormatoVisualizacao.select_by_value(
            "dictionary"
        )  # dictionary É PADRÃO(SIMPLES, ESTILO DICIONÁRIO)
        input_AparenciaFormatoVisualizacao = True
        contGlossario += 1
        sleep(1)
    # APARENCIA - FORMATO DA EXIBIÇÃO DE APROVAÇÃO
    checagemTotal += 1
    input_AparenciaFormatoExibicaoAprovacao = False
    inputAparenciaFormatoExibicaoAprovacao = Select(
        navegador.find_element(by=By.ID, value="id_approvaldisplayformat")
    )
    if (
        navegador.find_element(
            by=By.ID, value="id_approvaldisplayformat"
        ).get_attribute("value")
        != "default"
    ):  # default É PADRÃO(PADRÃO PARA O MESMO FORMATO DE EXIBIÇÃO)
        inputAparenciaFormatoExibicaoAprovacao.select_by_value(
            "default"
        )  # default É PADRÃO(PADRÃO PARA O MESMO FORMATO DE EXIBIÇÃO)
        input_AparenciaFormatoExibicaoAprovacao = True
        contGlossario += 1
        sleep(1)
    # APARENCIA - NÚMERO DE ITENS MOSTRADOS EM CADA PÁGINA
    checagemTotal += 1
    input_AparenciaNumItemPagina = False
    inputAparenciaNumItemPagina = navegador.find_element(by=By.ID, value="id_entbypage")
    if (
        navegador.find_element(by=By.ID, value="id_entbypage").get_attribute("value")
        != "10"
    ):  # 10 É O PADRÃO
        inputAparenciaNumItemPagina.clear()
        inputAparenciaNumItemPagina.send_keys("10")
        input_AparenciaNumItemPagina = True
        # print("Item de Nota em Compensação foi alterado para o Padrão - 0,0000.")
        contGlossario += 1
        sleep(1)
    # APARENCIA - MOSTRAR ALFABETO EM LINKS
    checagemTotal += 1
    input_AparenciaMostrarAlfabetoLinks = False
    inputAparenciaMostrarAlfabetoLinks = Select(
        navegador.find_element(by=By.ID, value="id_showalphabet")
    )
    if (
        navegador.find_element(by=By.ID, value="id_showalphabet").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(SIM)
        inputAparenciaMostrarAlfabetoLinks.select_by_value("1")  # 1 É PADRÃO(SIM)
        input_AparenciaMostrarAlfabetoLinks = True
        contGlossario += 1
        sleep(1)
    # APARENCIA - MOSTRAR O LINK 'TODOS'
    checagemTotal += 1
    input_AparenciaMostrarLinkTodos = False
    inputAparenciaMostrarLinkTodos = Select(
        navegador.find_element(by=By.ID, value="id_showall")
    )
    if (
        navegador.find_element(by=By.ID, value="id_showall").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(SIM)
        inputAparenciaMostrarLinkTodos.select_by_value("1")  # 1 É PADRÃO(SIM)
        input_AparenciaMostrarLinkTodos = True
        contGlossario += 1
        sleep(1)
    # APARENCIA - MOSTRAR LINK 'ESPECIAL'
    checagemTotal += 1
    input_AparenciaMostrarLinkEspecial = False
    inputAparenciaMostrarLinkEspecial = Select(
        navegador.find_element(by=By.ID, value="id_showspecial")
    )
    if (
        navegador.find_element(by=By.ID, value="id_showspecial").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(SIM)
        inputAparenciaMostrarLinkEspecial.select_by_value("1")  # 1 É PADRÃO(SIM)
        input_AparenciaMostrarLinkEspecial = True
        contGlossario += 1
        sleep(1)
    # APARENCIA - PERMITIR VISUALIZAR IMPRESSÃO
    checagemTotal += 1
    input_AparenciaPermitirVisualizarImpressao = False
    inputAparenciaPermitirVisualizarImpressao = Select(
        navegador.find_element(by=By.ID, value="id_allowprintview")
    )
    if (
        navegador.find_element(by=By.ID, value="id_allowprintview").get_attribute(
            "value"
        )
        != "1"
    ):  # 1 É PADRÃO(SIM)
        inputAparenciaPermitirVisualizarImpressao.select_by_value(
            "1"
        )  # 1 É PADRÃO(SIM)
        input_AparenciaPermitirVisualizarImpressao = True
        contGlossario += 1
        sleep(1)

    # AVALIAÇÕES - TIPO AGREGADO
    checagemTotal += 1
    input_AvaliacoesTipoAgregado = False
    inputAvaliacoesTipoAgregado = Select(
        navegador.find_element(by=By.ID, value="id_assessed")
    )
    if (
        navegador.find_element(by=By.ID, value="id_assessed").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(NENHUMA AVALIAÇÃO)
        inputAvaliacoesTipoAgregado.select_by_value(
            "0"
        )  # 0 É PADRÃO(NENHUMA AVALIAÇÃO)
        input_AvaliacoesTipoAgregado = True
        contGlossario += 1
        sleep(1)

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
        contGlossario += 1
        sleep(1)
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
        contGlossario += 1
        sleep(1)
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
            contGlossario += 1
            sleep(1)
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
            contGlossario += 1
            sleep(1)
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
            contGlossario += 1
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
            contGlossario += 1
            sleep(1)
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
            contGlossario += 1
            sleep(1)

    # CONCLUSÇÃO DE ATIVIDADE - REQUER ENTRADAS
    checagemTotal += 1
    input_ConclusaoAtividadeRequerEntradas = False
    inputConclusaoAtividadeRequerEntradas = navegador.find_element(
        by=By.ID, value="id_completionentriesenabled"
    )
    if navegador.find_element(
        by=By.ID, value="id_completionentriesenabled"
    ).is_selected():  # PADRÃO É DESMARCADO! SE ESTIVER MARCADO, ENTRE E DESMARQUE
        inputConclusaoAtividadeRequerEntradas.click()
        input_ConclusaoAtividadeRequerEntradas = True
        contGlossario += 1
        sleep(1)
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
        contGlossario += 1
        sleep(1)

    # CLICAR NO BOTÃO DE SALVAR
    inputLivroSalvar = navegador.find_element(by=By.ID, value="id_submitbutton2")
    inputLivroSalvar.click()
    sleep(1)

    print("Total de verificações: %i " % checagemTotal)
    if contGlossario > 0:
        if contGlossario < 2:
            print("Total de modificação: %i" % contGlossario)
        else:
            print("Totais de modificações: %i" % contGlossario)

        if input_GeralExibirDescricaoNaPaginaCurso != False:
            print(
                "'Exibir descrição na página do curso' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_ItemAprovacaoImediataNovoItem != False:
            print(
                "'Aprovação imediata de novos itens' foi alterado para o Padrão - PADRÃO (SIM)."
            )
        if input_ItemSemprePermitirEdicao != False:
            print("'Sempre permitir edição' foi alterado para o Padrão - PADRÃO (NÃO).")
        if input_ItemPermitirItensDuplicados != False:
            print(
                "'Permitir itens duplicados' foi alterado para o Padrão - PADRÃO (NÃO)."
            )
        if input_ItemPermitirComentarios != False:
            print("'Permitir comentários' foi alterado para o Padrão - PADRÃO (NÃO).")
        if input_ItemFazerLinkAutoItens != False:
            print(
                "'Fazer o link automático dos itens' foi alterado para o Padrão - PADRÃO (SIM)."
            )
        if input_AparenciaFormatoVisualizacao != False:
            print(
                "'Formato de visualização' foi alterado para o Padrão - PADRÃO (SIMPLES, ESTILO DISCIONÁRIO)"
            )
        if input_AparenciaFormatoExibicaoAprovacao != False:
            print(
                "'Formato da exibição de aprovação' foi alterado para o Padrão - PADRÃO (PADRÃO PARA O MESMO FORMATO DE EXIBIÇÃO)"
            )
        if input_AparenciaNumItemPagina != False:
            print(
                "'Número de itens mostrados em cada página' foi alterado para o Padrão - PADRÃO (10)"
            )
        if input_AparenciaMostrarAlfabetoLinks != False:
            print(
                "'Mostrar alfabeto em links' foi alterado para o Padrão - PADRÃO (SIM)"
            )
        if input_AparenciaMostrarLinkTodos != False:
            print("Mostrar o link 'TODOS' foi alterado para o Padrão - PADRÃO (SIM)")
        if input_AparenciaMostrarLinkEspecial != False:
            print("Mostrar link 'ESPECIAL' foi alterado para o Padrão - PADRÃO (SIM)")
        if input_AparenciaPermitirVisualizarImpressao != False:
            print(
                "'Permitir visualizar impressão' foi alterado para o Padrão - PADRÃO (SIM)"
            )
        if input_AvaliacoesTipoAgregado != False:
            print(
                "'Tipo agregado' foi alterado para o Padrão - PADRÃO (NENHUMA AVALIAÇÃO)"
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
        if input_ConclusaoAtividadeRequerEntradas != False:
            print(
                "'Requer entradas' foi alterado para o Padrão - PADRÃO ('DESMARCADO')."
            )
        if input_ConclusaoAtividadeConclusaoEsperadaEm != False:
            print(
                "'Conclusão esperada em' foi alterado para o Padrão - PADRÃO ('DESMARCADO')."
            )
    else:
        print("Análise do Glossário foi concluída sem observações!")
    return contGlossario
