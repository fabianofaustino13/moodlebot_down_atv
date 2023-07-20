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


def validarEnquete(navegador, link, contEnquete):
    checagemTotal = 0
    contEnquete = 0
    # ENTRANDO NO LIVRO
    # EXPANDINDO TUDO
    navegador.find_element(by=By.LINK_TEXT, value="Expandir tudo").click()  # Abrir
    sleep(1)
    # GERAL - FORMATO AUTOMÁTICO
    checagemTotal += 1
    input_GeralFormato = False
    inputGeralFormato = Select(
        navegador.find_element(by=By.ID, value="menuintroeditorformat")
    )
    if (
        navegador.find_element(by=By.ID, value="menuintroeditorformat").get_attribute(
            "value"
        )
        != "0"
    ):  # 0 É PADRÃO(FORMATO AUTOMÁTICO)
        inputGeralFormato.select_by_value("0")  # 0 É PADRÃO(FORMATO AUTOMÁTICO)
        input_GeralFormato = True
        contEnquete += 1
        # sleep(1)
    # GERAL - EXIBIR DESCRIÇÃO
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
        contEnquete += 1
        # sleep(1)

    # TEMPO - PERMITIR RESPOSTAS DE
    checagemTotal += 1
    input_TempoPermitirRespostasDe = False
    inputTempoPermitirRespostasDe = navegador.find_element(
        by=By.ID, value="id_useopendate"
    )
    if navegador.find_element(
        by=By.ID, value="id_useopendate"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputTempoPermitirRespostasDe.click()
        input_TempoPermitirRespostasDe = True
        contEnquete += 1
        # sleep(1)
    # TEMPO - DATA DE ENCERRAMENTO
    checagemTotal += 1
    input_TempoDataEncerramento = False
    inputTempoDataEncerramento = navegador.find_element(
        by=By.ID, value="id_useclosedate"
    )
    if navegador.find_element(
        by=By.ID, value="id_useclosedate"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputTempoDataEncerramento.click()
        input_TempoDataEncerramento = True
        contEnquete += 1
        # sleep(1)

    # OPÇÕES DE RESPOSTAS - TIPO
    checagemTotal += 1
    input_OpcoesRespostasTipo = False
    inputOpcoesRespostasTipo = Select(
        navegador.find_element(by=By.ID, value="id_qtype")
    )
    if (
        navegador.find_element(by=By.ID, value="id_qtype").get_attribute("value") != "1"
    ):  # 1 É PADRÃO(RESPONDER UMA ÚNICA VEZ)
        inputOpcoesRespostasTipo.select_by_value(
            "1"
        )  # 1 É PADRÃO(RESPONDER UMA ÚNICA VEZ)
        input_OpcoesRespostasTipo = True
        contEnquete += 1
        # sleep(1)
    # OPÇÕES DE RESPOSTAS - TIPO DO RESPONDENTE
    checagemTotal += 1
    input_OpcoesRespostasTipoRespondente = False
    inputOpcoesRespostasTipoRespondente = Select(
        navegador.find_element(by=By.ID, value="id_respondenttype")
    )
    if (
        navegador.find_element(by=By.ID, value="id_respondenttype").get_attribute(
            "value"
        )
        != "anonymous"
    ):  # anonymous É PADRÃO(ANÔNIMO)
        inputOpcoesRespostasTipoRespondente.select_by_value(
            "anonymous"
        )  # anonymous É PADRÃO(ANÔNIMO)
        input_OpcoesRespostasTipoRespondente = True
        contEnquete += 1
        # sleep(1)
    # OPÇÕES DE RESPOSTAS - ESTUDANTES PODEM VISUALIZAR TODAS
    checagemTotal += 1
    input_OpcoesRespostasEstudantesPodemVisualizar = False
    inputOpcoesRespostasEstudantesPodemVisualizar = Select(
        navegador.find_element(by=By.ID, value="id_resp_view")
    )
    if (
        navegador.find_element(by=By.ID, value="id_resp_view").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(DEPOIS DE RESPONDER A ENQUETE)
        inputOpcoesRespostasEstudantesPodemVisualizar.select_by_value(
            "1"
        )  # 1 É PADRÃO(DEPOIS DE RESPONDER A ENQUETE)
        input_OpcoesRespostasEstudantesPodemVisualizar = True
        contEnquete += 1
        # sleep(1)
    # OPÇÕES DE RESPOSTAS - ENVIAR NOTIFICAÇÕES DE SUBMISSÃO
    checagemTotal += 1
    input_OpcoesRespostasEnviarNotificacoesSubmissao = False
    inputOpcoesRespostasEnviarNotificacoesSubmissao = Select(
        navegador.find_element(by=By.ID, value="id_notifications")
    )
    if (
        navegador.find_element(by=By.ID, value="id_notifications").get_attribute(
            "value"
        )
        != "0"
    ):  # 0 É PADRÃO(NÃO)
        inputOpcoesRespostasEnviarNotificacoesSubmissao.select_by_value(
            "0"
        )  # 0 É PADRÃO(NÃO)
        input_OpcoesRespostasEnviarNotificacoesSubmissao = True
        contEnquete += 1
        # sleep(1)
    # OPÇÕES DE RESPOSTAS - SALVAR/RETOMAR RESPOSTAS
    checagemTotal += 1
    input_OpcoesRespostasSalvarRetomarRespostas = False
    inputOpcoesRespostasSalvarRetomarRespostas = Select(
        navegador.find_element(by=By.ID, value="id_resume")
    )
    if (
        navegador.find_element(by=By.ID, value="id_resume").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(SIM)
        inputOpcoesRespostasSalvarRetomarRespostas.select_by_value(
            "1"
        )  # 1 É PADRÃO(SIM)
        input_OpcoesRespostasSalvarRetomarRespostas = True
        contEnquete += 1
        # sleep(1)
    # OPÇÕES DE RESPOSTAS - PERMITIR QUESTÕES DE RAMIFICAÇÃO
    checagemTotal += 1
    input_OpcoesPermitirQuestoesRamificacao = False
    inputOpcoesPermitirQuestoesRamificacao = Select(
        navegador.find_element(by=By.ID, value="id_navigate")
    )
    if (
        navegador.find_element(by=By.ID, value="id_navigate").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(SIM)
        inputOpcoesPermitirQuestoesRamificacao.select_by_value("1")  # 1 É PADRÃO(SIM)
        input_OpcoesOpcoesPermitirQuestoesRamificacao = True
        contEnquete += 1
        # sleep(1)
    # OPÇÕES DE RESPOSTAS - NUMERAÇÃO AUTOMÁTICA
    checagemTotal += 1
    input_OpcoesNumeracaoAutomatica = False
    inputOpcoesNumeracaoAutomatica = Select(
        navegador.find_element(by=By.ID, value="id_autonum")
    )
    if (
        navegador.find_element(by=By.ID, value="id_autonum").get_attribute("value")
        != "3"
    ):  # 3 É PADRÃO(NUMERAR AUTOMATICAMENTE PÁGIANS E QUESTÕES)
        inputOpcoesNumeracaoAutomatica.select_by_value(
            "3"
        )  # 3 É PADRÃO(NUMERAR AUTOMATICAMENTE PÁGIANS E QUESTÕES)
        input_OpcoesNumeracaoAutomatica = True
        contEnquete += 1
        # sleep(1)
    # OPÇÕES DE RESPOSTAS - ESCALA DE NOTAS
    checagemTotal += 1
    input_OpcoesEscalaNotas = False
    inputOpcoesEscalaNotas = Select(navegador.find_element(by=By.ID, value="id_grade"))
    if (
        navegador.find_element(by=By.ID, value="id_grade").get_attribute("value") != "0"
    ):  # 0 É PADRÃO(NENHUMA NOTA)
        inputOpcoesEscalaNotas.select_by_value("0")  # 0 É PADRÃO(NENHUMA NOTA)
        input_OpcoesEscalaNotas = True
        contEnquete += 1
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
        contEnquete += 1
        # sleep(1)
    # CONFIGURAÇÕES COMUNS DE MÓDULOS - NÚMERO DE IDENTIFICAÇÃO DO MÚDULO
    # checagemTotal+=1
    # input_ConfComumModuloNumIdentificacao = False
    # inputConfComumModuloNumIdentificacao = navegador.find_element(by=By.ID,value="id_cmidnumber")
    # if navegador.find_element(by=By.ID,value="id_cmidnumber").get_attribute("value") != "": #PADRÃO É VAZIO
    #    inputConfComumModuloNumIdentificacao.clear()
    #    input_ConfComumModuloNumIdentificacao = True
    #    contEnquete+=1
    #    sleep(1)
    # CONFIGURAÇÕES COMUNS DE MÓDULOS - MODALIDADE GRUPO
    checagemTotal += 1
    input_ConfComumModuloModalidadeGrupo = False
    inputConfComumModuloModalidadeGrupo = Select(
        navegador.find_element(by=By.ID, value="id_groupmode")
    )
    if (
        navegador.find_element(by=By.ID, value="id_groupmode").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(NENHUM GRUPO)
        inputConfComumModuloModalidadeGrupo.select_by_value(
            "0"
        )  # 0 É PADRÃO(NENHUM GRUPO)
        input_ConfComumModuloModalidadeGrupo = True
        contEnquete += 1
        # sleep(1)

    # RESTRINGIR ACESSO - NÃO SERÁ TRATADO

    # CONCLUSÃO DE ATIVIDADE
    try:
        # CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO
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
            contEnquete += 1
            # sleep(1)
        # CONCLUSÇÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO
        checagemTotal += 1
        input_ConclusaoAtividadeRequerVisualizacao = False
        inputConclusaoAtividadeRequerVisualizacao = navegador.find_element(
            by=By.ID, value="id_completionsubmit"
        )
        if (
            navegador.find_element(by=By.ID, value="id_completionsubmit").is_selected()
            == False
        ):  # PADRÃO É MARCADO! SE ESTIVER DESMARCADO, ENTRE E MARQUE
            inputConclusaoAtividadeRequerVisualizacao.click()
            input_ConclusaoAtividadeRequerVisualizacao = True
            contEnquete += 1
            # sleep(1)
    except:
        # CONCLUSÃO DE ATIVIDADE - BLOQUEADO
        checagemTotal += 1
        input_ConclusaoAtividadeBloqueada = False
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
            contEnquete += 1
            sleep(1)
        # CONCLUSÃO DE ATIVIDADE - ACOMPANHAMENTO DE CONCLUSÃO
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
            contEnquete += 1
            # sleep(1)
        # CONCLUSÇÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO
        checagemTotal += 1
        input_ConclusaoAtividadeRequerVisualizacao = False
        inputConclusaoAtividadeRequerVisualizacao = navegador.find_element(
            by=By.ID, value="id_completionsubmit"
        )
        if (
            navegador.find_element(by=By.ID, value="id_completionsubmit").is_selected()
            == False
        ):  # PADRÃO É MARCADO! SE ESTIVER DESMARCADO, ENTRE E MARQUE
            inputConclusaoAtividadeRequerVisualizacao.click()
            input_ConclusaoAtividadeRequerVisualizacao = True
            contEnquete += 1
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
        contEnquete += 1
        # sleep(1)

    # sleep(1)
    # CLICAR NO BOTÃO DE SALVAR
    navegador.find_element(by=By.ID, value="id_submitbutton2").click()
    sleep(1)

    print("Total de verificações: %i " % checagemTotal)
    if contEnquete > 0:
        if contEnquete < 2:
            print("Total de modificação: %i" % contEnquete)
        else:
            print("Totais de modificações: %i" % contEnquete)

        if input_GeralFormato != False:
            print("'Formato' foi alterado para o Padrão - PADRÃO (FORMATO AUTOMÁTICO).")
        if input_GeralExibirDescricaoNaPaginaCurso != False:
            print(
                "'Exibir descrição na página do curso' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )

        if input_TempoPermitirRespostasDe != False:
            print(
                "'Permitir respostas de' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_TempoDataEncerramento != False:
            print(
                "'Data de encerramento' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )

        if input_OpcoesRespostasTipo != False:
            print(
                "'Opções de respostas - Tipo' foi alterado para o Padrão - PADRÃO (RESPONDER UMA ÚNICA VEZ)."
            )
        if input_OpcoesRespostasTipoRespondente != False:
            print(
                "'Opções de resposta - Tipo de respondente' foi alterado para o Padrão - PADRÃO (ANÔNIMO)."
            )
        if input_OpcoesRespostasEstudantesPodemVisualizar != False:
            print(
                "'Opções de resposta - Estudantes podem visualizar TODAS as respostas' foi alterado para o Padrão - PADRÃO (DEPOIS DE RESPONDER A ENQUETE)."
            )
        if input_OpcoesRespostasEnviarNotificacoesSubmissao != False:
            print(
                "'Opções de resposta - Enviar notificações de submissão' foi alterado para o Padrão - PADRÃO (NÃO)."
            )
        if input_OpcoesRespostasSalvarRetomarRespostas != False:
            print(
                "'Opçoes de resposta - Salvar/Retomar respostas' foi alterado para o Padrão - PADRÃO (SIM)."
            )
        if input_OpcoesPermitirQuestoesRamificacao != False:
            print(
                "'Opções de resposta - Permitir questões de ramificação' foi alterado para o Padrão - PADRÃO (SIM)."
            )
        if input_OpcoesNumeracaoAutomatica != False:
            print(
                "'Opções de resposta - Numeração automática' foi alterado para o Padrão - PADRÃO (NUMERAR AUTOMATICAMENTE PÁGINAS E QUESTÕES)."
            )
        if input_OpcoesEscalaNotas != False:
            print(
                "'Opções de resposta - Escala de Notas' foi alterado para o Padrão - PADRÃO (NENHUMA NOTA)."
            )

        if input_ConfComumModuloDisponibilidade != False:
            print(
                "'Disponibilidade' foi alterado para o Padrão - PADRÃO (MOSTRAR NA PÁGINA DO CURSO)."
            )
        # if input_ConfComumModuloNumIdentificacao != False:
        #    print("'Número de identificação do módulo' foi alterado para o Padrão - PADRÃO ('VAZIO').")
        if input_ConfComumModuloModalidadeGrupo != False:
            print("'Modalidade grupo' foi alterado para o Padrão - PADRÃO (NENHUM).")

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
                "'Requer visualização' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_ConclusaoAtividadeConclusaoEsperadaEm != False:
            print(
                "'Conclusão esperada em' foi alterado para o Padrão - PADRÃO ('DESMARCADO')."
            )
    else:
        print("Análise da Enquete foi concluída sem observações!")
    return contEnquete
