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


def validarQuestionario(navegador, link, contQuestionario):
    # timeInicio = time.perf_counter()

    checagemTotal = 0
    contQuestionario = 0
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
        contQuestionario += 1
        sleep(1)

    # DURAÇÃO - ABRIR O QUESTIONÁRIO
    checagemTotal += 1
    input_DuracaoAbrirQuestionario = False
    inputDuracaoAbrirQuestionario = navegador.find_element(
        by=By.ID, value="id_timeopen_enabled"
    )
    if navegador.find_element(
        by=By.ID, value="id_timeopen_enabled"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputDuracaoAbrirQuestionario.click()
        input_DuracaoAbrirQuestionario = True
        contQuestionario += 1
        # sleep(1)
    # DURAÇÃO - ENCERRAR O QUESTIONÁRIO
    checagemTotal += 1
    input_DuracaoEncerrarQuestionario = False
    inputDuracaoEncerrarQuestionario = navegador.find_element(
        by=By.ID, value="id_timeclose_enabled"
    )
    if navegador.find_element(
        by=By.ID, value="id_timeclose_enabled"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputDuracaoEncerrarQuestionario.click()
        input_DuracaoEncerrarQuestionario = True
        contQuestionario += 1
        # sleep(1)
    # DURAÇÃO - LIMITE DE TEMPO
    checagemTotal += 1
    input_DuracaoLimiteTempo = False
    inputDuracaoLimiteTempo = navegador.find_element(
        by=By.ID, value="id_timelimit_enabled"
    )
    if navegador.find_element(
        by=By.ID, value="id_timelimit_enabled"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputDuracaoLimiteTempo.click()
        input_DuracaoLimiteTempo = True
        contQuestionario += 1
        # sleep(1)
    # DURAÇÃO - QUANDO O TEMPO EXPIRAR
    checagemTotal += 1
    input_DuracaoQndoTempoExpirar = False
    inputDuracaoQndoTempoExpirar = Select(
        navegador.find_element(by=By.ID, value="id_overduehandling")
    )
    if (
        navegador.find_element(by=By.ID, value="id_overduehandling").get_attribute(
            "value"
        )
        != "autosubmit"
    ):  # autosubmit É PADRÃO(AS TENTATIVAS ABERTAS SÃO ENVIADAS AUTOMATICAMENTE)
        inputDuracaoQndoTempoExpirar.select_by_value(
            "autosubmit"
        )  # autosubmit É PADRÃO(AS TENTATIVAS ABERTAS SÃO ENVIADAS AUTOMATICAMENTE)
        input_DuracaoQndoTempoExpirar = True
        contQuestionario += 1
        # sleep(1)

    # NOTA - CATEGORIA DE NOTAS
    checagemTotal += 1
    input_NotaCategoriaNotas = False
    inputNotaCategoriaNotas = navegador.find_element(
        By.XPATH, "//select[@id='id_gradecat' and @name='gradecat']"
    )
    todasOpcoes = inputNotaCategoriaNotas.find_elements(By.TAG_NAME, "option")
    for opcao in todasOpcoes:
        # print("Valores são: %s" % opcao.get_attribute("value"))
        # print(opcao.text)
        if opcao.text != "Não categorizado":  # O É PADRÃO(NÃO CATEGORIZADO)
            # print("O valor é: %s" % opcao.get_attribute("value"))
            opcao.click()
            input_NotaCategoriaNotas = True
            contQuestionario += 1
            # sleep(1)

    # NOTA - NOTA PARA APROVAÇÃO
    checagemTotal += 1
    input_NotaNotaParaAprovacao = False
    inputNotaNotaParaAprovacao = navegador.find_element(by=By.ID, value="id_gradepass")
    if (
        navegador.find_element(by=By.ID, value="id_gradepass").get_attribute("value")
        != "0,00"
    ):  # VAZIO
        inputNotaNotaParaAprovacao.clear()
        inputNotaNotaParaAprovacao.send_keys("0,00")
        input_NotaNotaParaAprovacao = True
        contQuestionario += 1
        # sleep(1)
    # NOTA - TENTATIVAS PERMITIDAS
    checagemTotal += 1
    input_NotaTentativasPermitidas = False
    # inputNotaTentativasPermitidas = Select(navegador.find_element(by=By.ID,value="id_attempts"))
    # if navegador.find_element(by=By.ID,value="id_attempts").get_attribute("value") != "1": # 1 É PADRÃO(1 TENTATIVA)
    #    inputNotaTentativasPermitidas.select_by_value("1") # 1 É PADRÃO(1 TENTATIVA)
    #    input_NotaTentativasPermitidas = True
    #    contQuestionario+=1
    # sleep(1)
    input_NotaTentativasPermitidas = True
    inputNotaTentativasPermitidas = navegador.find_element(
        by=By.ID, value="id_attempts"
    ).get_attribute("value")
    contQuestionario += 1

    # LAYOUT - NOVA PÁGINA
    checagemTotal += 1
    input_LayoutNovaPagina = False
    inputLayoutNovaPagina = Select(
        navegador.find_element(by=By.ID, value="id_questionsperpage")
    )
    if (
        navegador.find_element(by=By.ID, value="id_questionsperpage").get_attribute(
            "value"
        )
        != "5"
    ):  # 5 É PADRÃO(CADA 5 QUESTÕES)
        inputLayoutNovaPagina.select_by_value("5")  # 5 É PADRÃO(CADA 5 QUESTÕES)
        input_LayoutNovaPagina = True
        contQuestionario += 1
        # sleep(1)
    # LAYOUT - REPAGINAR - SEMPRE REPAGINAR PARA CONFIRMAR AS 5 QUESTÕES POR PÁGINA
    checagemTotal += 1
    input_LayoutRepaginar = False
    inputLayoutRepaginar = navegador.find_element(by=By.ID, value="id_repaginatenow")
    if (
        navegador.find_element(by=By.ID, value="id_repaginatenow").is_selected()
        == False
    ):  # PADRÃO É DESMARCADO, MAS É NECESSÁRIO MARCAR PARA ORGANIZAR CASO AS QUESTÕES ESTEJAM ORGANIZADAS DE FORMA ERRADA.
        inputLayoutRepaginar.click()
        input_LayoutRepaginar = True
        # contQuestionario+=1
        # sleep(1)
    # LAYOUT - MOSTRAR MAIS...
    navegador.find_element(
        by=By.LINK_TEXT, value="Mostrar mais ..."
    ).click()  # Mostrar mais ...
    sleep(1)
    # LAYOUT - MÉTODO DE NAVEGAÇÃO
    checagemTotal += 1
    input_LayoutMetodoNavegacao = False
    inputLayoutMetodoNavegacao = Select(
        navegador.find_element(by=By.ID, value="id_navmethod")
    )
    if (
        navegador.find_element(by=By.ID, value="id_navmethod").get_attribute("value")
        != "free"
    ):  # free É PADRÃO (LIVRE)
        inputLayoutMetodoNavegacao.select_by_value("free")  # free É PADRÃO(LIVRE)
        input_LayoutMetodoNavegacao = True
        contQuestionario += 1
        # sleep(1)

    # COMPORTAMENTO DA QUESTÃO - MISTURAR ENTRE AS QUESTÕES
    checagemTotal += 1
    input_ComportamentoQuestaoMisturarEntreQuestao = False
    inputComportamentoQuestaoMisturarEntreQuestao = Select(
        navegador.find_element(by=By.ID, value="id_shuffleanswers")
    )
    if (
        navegador.find_element(by=By.ID, value="id_shuffleanswers").get_attribute(
            "value"
        )
        != "0"
    ):  # 0 É PADRÃO (NÃO)
        inputComportamentoQuestaoMisturarEntreQuestao.select_by_value(
            "0"
        )  # 0 É PADRÃO(NÃO)
        input_ComportamentoQuestaoMisturarEntreQuestao = True
        contQuestionario += 1
        # sleep(1)
    # COMPORTAMENTO DA QUESTÃO - COMO AS QUESTÕES SE COMPORTAM
    checagemTotal += 1
    input_ComportamentoQuestaoComoComportam = False
    inputComportamentoQuestaoComoComportam = Select(
        navegador.find_element(by=By.ID, value="id_preferredbehaviour")
    )
    if (
        navegador.find_element(by=By.ID, value="id_preferredbehaviour").get_attribute(
            "value"
        )
        != "deferredfeedback"
    ):  # deferredfeedback É PADRÃO (FEEDBACK ADIADO)
        inputComportamentoQuestaoComoComportam.select_by_value(
            "deferredfeedback"
        )  # deferredfeedback É PADRÃO(FEEDBACK ADIADO)
        input_ComportamentoQuestaoComoComportam = True
        contQuestionario += 1
        # sleep(1)

    # OPÇÕES DE REVISÃO - APÓS A TENTATIVA - A TENTATIVA
    checagemTotal += 1
    input_OpcaoRevisaoAposTentativaATentativa = False
    inputOpcaoRevisaoAposTentativaATentativa = navegador.find_element(
        by=By.ID, value="id_attemptimmediately"
    )
    if (
        navegador.find_element(by=By.ID, value="id_attemptimmediately").is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoAposTentativaATentativa.click()
        input_OpcaoRevisaoAposTentativaATentativa = True
        contQuestionario += 1
        # sleep(1)
    # OPÇÕES DE REVISÃO - APÓS A TENTATIVA - ACERTOS/ERROS
    checagemTotal += 1
    input_OpcaoRevisaoAposTentativaAcertosErros = False
    inputOpcaoRevisaoAposTentativaAcertosErros = navegador.find_element(
        by=By.ID, value="id_correctnessimmediately"
    )
    if (
        navegador.find_element(
            by=By.ID, value="id_correctnessimmediately"
        ).is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoAposTentativaAcertosErros.click()
        input_OpcaoRevisaoAposTentativaAcertosErros = True
        contQuestionario += 1
        # sleep(1)
    # OPÇÕES DE REVISÃO - APÓS A TENTATIVA - NOTAS
    checagemTotal += 1
    input_OpcaoRevisaoAposTentativaNotas = False
    inputOpcaoRevisaoAposTentativaNotas = navegador.find_element(
        by=By.ID, value="id_marksimmediately"
    )
    if (
        navegador.find_element(by=By.ID, value="id_marksimmediately").is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoAposTentativaNotas.click()
        input_OpcaoRevisaoAposTentativaNotas = True
        contQuestionario += 1
        # sleep(1)
    # OPÇÕES DE REVISÃO - APÓS A TENTATIVA - FEEDBACK ESPECÍFICO
    checagemTotal += 1
    input_OpcaoRevisaoAposTentativaFeedBackEspecifico = False
    inputOpcaoRevisaoAposTentativaFeedBackEspecifico = navegador.find_element(
        by=By.ID, value="id_specificfeedbackimmediately"
    )
    if (
        navegador.find_element(
            by=By.ID, value="id_specificfeedbackimmediately"
        ).is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoAposTentativaFeedBackEspecifico.click()
        input_OpcaoRevisaoAposTentativaFeedBackEspecifico = True
        contQuestionario += 1
        # sleep(1)
    # OPÇÕES DE REVISÃO - APÓS A TENTATIVA - FEEDBACK GERAL
    checagemTotal += 1
    input_OpcaoRevisaoAposTentativaFeedBackGeral = False
    inputOpcaoRevisaoAposTentativaFeedBackGeral = navegador.find_element(
        by=By.ID, value="id_generalfeedbackimmediately"
    )
    if (
        navegador.find_element(
            by=By.ID, value="id_generalfeedbackimmediately"
        ).is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoAposTentativaFeedBackGeral.click()
        input_OpcaoRevisaoAposTentativaFeedBackGeral = True
        contQuestionario += 1
        # sleep(1)
    # OPÇÕES DE REVISÃO - APÓS A TENTATIVA - RESPOSTA CORRETA
    checagemTotal += 1
    input_OpcaoRevisaoAposTentativaRespostaCorreta = False
    inputOpcaoRevisaoAposTentativaRespostaCorreta = navegador.find_element(
        by=By.ID, value="id_rightanswerimmediately"
    )
    if (
        navegador.find_element(
            by=By.ID, value="id_rightanswerimmediately"
        ).is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoAposTentativaRespostaCorreta.click()
        input_OpcaoRevisaoAposTentativaRespostaCorreta = True
        contQuestionario += 1
        # sleep(1)
    # OPÇÕES DE REVISÃO - APÓS A TENTATIVA - FEEDBACK FINAL
    checagemTotal += 1
    input_OpcaoRevisaoAposTentativaFeedBackFinal = False
    inputOpcaoRevisaoAposTentativaFeedBackFinal = navegador.find_element(
        by=By.ID, value="id_overallfeedbackimmediately"
    )
    if (
        navegador.find_element(
            by=By.ID, value="id_overallfeedbackimmediately"
        ).is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoAposTentativaFeedBackFinal.click()
        input_OpcaoRevisaoAposTentativaFeedBackFinal = True
        contQuestionario += 1
        # sleep(1)

    # OPÇÕES DE REVISÃO - MAIS TARDE, ENQUANTO AINDA ESTIVER ABERTO - A TENTATIVA
    checagemTotal += 1
    input_OpcaoRevisaoMaisTardeATentativa = False
    inputOpcaoRevisaoMaisTardeATentativa = navegador.find_element(
        by=By.ID, value="id_attemptopen"
    )
    if (
        navegador.find_element(by=By.ID, value="id_attemptopen").is_selected() == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoMaisTardeATentativa.click()
        input_OpcaoRevisaoMaisTardeATentativa = True
        contQuestionario += 1
        # sleep(1)
    # OPÇÕES DE REVISÃO - MAIS TARDE, ENQUANTO AINDA ESTIVER ABERTO - ACERTOS/ERROS
    checagemTotal += 1
    input_OpcaoRevisaoMaisTardeAcertosErros = False
    inputOpcaoRevisaoMaisTardeAcertosErros = navegador.find_element(
        by=By.ID, value="id_correctnessopen"
    )
    if (
        navegador.find_element(by=By.ID, value="id_correctnessopen").is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoMaisTardeAcertosErros.click()
        input_OpcaoRevisaoMaisTardeAcertosErros = True
        contQuestionario += 1
        # sleep(1)
    # OPÇÕES DE REVISÃO - MAIS TARDE, ENQUANTO AINDA ESTIVER ABERTO - NOTAS
    checagemTotal += 1
    input_OpcaoRevisaoMaisTardeNotas = False
    inputOpcaoRevisaoMaisTardeNotas = navegador.find_element(
        by=By.ID, value="id_marksopen"
    )
    if (
        navegador.find_element(by=By.ID, value="id_marksopen").is_selected() == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoMaisTardeNotas.click()
        input_OpcaoRevisaoMaisTardeNotas = True
        contQuestionario += 1
        # sleep(1)
    # OPÇÕES DE REVISÃO - MAIS TARDE, ENQUANTO AINDA ESTIVER ABERTO - FEEDBACK ESPECÍFICO
    checagemTotal += 1
    input_OpcaoRevisaoMaisTardeFeedBackEspecifico = False
    inputOpcaoRevisaoMaisTardeFeedBackEspecifico = navegador.find_element(
        by=By.ID, value="id_specificfeedbackopen"
    )
    if (
        navegador.find_element(by=By.ID, value="id_specificfeedbackopen").is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoMaisTardeFeedBackEspecifico.click()
        input_OpcaoRevisaoMaisTardeFeedBackEspecifico = True
        contQuestionario += 1
        # sleep(1)
    # OPÇÕES DE REVISÃO - MAIS TARDE, ENQUANTO AINDA ESTIVER ABERTO - FEEDBACK GERAL
    checagemTotal += 1
    input_OpcaoRevisaoMaisTardeFeedBackGeral = False
    inputOpcaoRevisaoMaisTardeFeedBackGeral = navegador.find_element(
        by=By.ID, value="id_generalfeedbackopen"
    )
    if (
        navegador.find_element(by=By.ID, value="id_generalfeedbackopen").is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoMaisTardeFeedBackGeral.click()
        input_OpcaoRevisaoMaisTardeFeedBackGeral = True
        contQuestionario += 1
        # sleep(1)
    # OPÇÕES DE REVISÃO - MAIS TARDE, ENQUANTO AINDA ESTIVER ABERTO - RESPOSTA CORRETA
    checagemTotal += 1
    input_OpcaoRevisaoMaisTardeRespostaCorreta = False
    inputOpcaoRevisaoMaisTardeRespostaCorreta = navegador.find_element(
        by=By.ID, value="id_rightansweropen"
    )
    if (
        navegador.find_element(by=By.ID, value="id_rightansweropen").is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoMaisTardeRespostaCorreta.click()
        input_OpcaoRevisaoMaisTardeRespostaCorreta = True
        contQuestionario += 1
        # sleep(1)
    # OPÇÕES DE REVISÃO - MAIS TARDE, ENQUANTO AINDA ESTIVER ABERTO - FEEDBACK FINAL
    checagemTotal += 1
    input_OpcaoRevisaoMaisTardeFeedBackFinal = False
    inputOpcaoRevisaoMaisTardeFeedBackFinal = navegador.find_element(
        by=By.ID, value="id_overallfeedbackopen"
    )
    if (
        navegador.find_element(by=By.ID, value="id_overallfeedbackopen").is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputOpcaoRevisaoMaisTardeFeedBackFinal.click()
        input_OpcaoRevisaoMaisTardeFeedBackFinal = True
        contQuestionario += 1
        # sleep(1)

    # APARENCIA - MOSTRAR MAIS...
    navegador.find_element(
        By.XPATH,
        "//a[@class='moreless-toggler' and @aria-controls='fitem_id_questiondecimalpoints fitem_id_showblocks']",
    ).click()
    sleep(1)
    # APARENCIA - MOSTRAR A FOTOGRAFIA DO USUÁRIO
    checagemTotal += 1
    input_AparenciaMostrarFoto = False
    inputAparenciaMostrarFoto = Select(
        navegador.find_element(by=By.ID, value="id_showuserpicture")
    )
    if (
        navegador.find_element(by=By.ID, value="id_showuserpicture").get_attribute(
            "value"
        )
        != "0"
    ):  # 0 É PADRÃO(NENHUMA IMAGEM)
        inputAparenciaMostrarFoto.select_by_value("0")  # 3 É PADRÃO(NENHUMA IMAGEM)
        input_AparenciaMostrarFoto = True
        contQuestionario += 1
        # sleep(1)
    # APARENCIA - CASAS DECIMAIS NAS NOTAS
    checagemTotal += 1
    input_AparenciaCasasDecimais = False
    inputAparenciaCasasDecimais = Select(
        navegador.find_element(by=By.ID, value="id_decimalpoints")
    )
    if (
        navegador.find_element(by=By.ID, value="id_decimalpoints").get_attribute(
            "value"
        )
        != "2"
    ):  # 2 É PADRÃO(2 CASAS DECIMAIS)
        inputAparenciaCasasDecimais.select_by_value("2")  # 2 É PADRÃO(2 CASAS DECIMAIS)
        input_AparenciaCasasDecimais = True
        contQuestionario += 1
        # sleep(1)
    # APARENCIA - CASAS DECIMAIS NAS NOTAS DA QUESTÃO
    checagemTotal += 1
    input_AparenciaCasasDecimaisQuestao = False
    inputAparenciaCasasDecimaisQuestao = Select(
        navegador.find_element(by=By.ID, value="id_questiondecimalpoints")
    )
    if (
        navegador.find_element(
            by=By.ID, value="id_questiondecimalpoints"
        ).get_attribute("value")
        != "-1"
    ):  # -1 É PADRÃO(O MESMO QUE PARA AS AVALIAÇÕES EM GERAL)
        inputAparenciaCasasDecimaisQuestao.select_by_value(
            "-1"
        )  # -1 É PADRÃO(O MESMO QUE PARA AS AVALIAÇÕES EM GERAL)
        input_AparenciaCasasDecimaisQuestao = True
        contQuestionario += 1
        # sleep(1)
    # APARENCIA - MOSTRAR BLOCOS DURANTE AS TENTATIVAS DO QUESTIONÁRIO
    checagemTotal += 1
    input_AparenciaMostrarBloco = False
    inputAparenciaMostrarBloco = Select(
        navegador.find_element(by=By.ID, value="id_showblocks")
    )
    if (
        navegador.find_element(by=By.ID, value="id_showblocks").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(NÃO)
        inputAparenciaMostrarBloco.select_by_value("0")  # 0 É PADRÃO(NÃO)
        input_AparenciaMostrarBloco = True
        contQuestionario += 1
        # sleep(1)
    # RESTRIÇÕES EXTRAS NAS TENTATIVAS - MOSTRAR MAIS ...
    # inputLayoutMostrarMais = navegador.find_element(by=By.LINK_TEXT,value="Mostrar mais ...") #Mostrar mais ...
    # inputLayoutMostrarMais.click()
    # sleep(1)
    # RESTRIÇÕES EXTRAS NAS TENTATIVAS - SENHA NECESSÁRIA
    checagemTotal += 1
    input_RestricaoExtrasNaTentativaSenhaNecessaria = False
    inputRestricaoExtrasNaTentativaSenhaNecessaria = navegador.find_element(
        by=By.ID, value="id_quizpassword"
    )
    if (
        navegador.find_element(by=By.ID, value="id_quizpassword").get_attribute("value")
        != ""
    ):  # VAZIO
        inputRestricaoExtrasNaTentativaSenhaNecessaria.clear()
        # inputNotaNotaParaAprovacao.send_keys("0,00")
        input_RestricaoExtrasNaTentativaSenhaNecessaria = True
        contQuestionario += 1
        # sleep(1)
    # RESTRIÇÕES EXTRAS NAS TENTATIVAS - REQUER ENDEREÇO DE REDE
    checagemTotal += 1
    input_RestricaoExtrasNaTentativaRequerEnderecoRede = False
    inputRestricaoExtrasNaTentativaRequerEnderecoRede = navegador.find_element(
        by=By.ID, value="id_subnet"
    )
    if (
        navegador.find_element(by=By.ID, value="id_subnet").get_attribute("value") != ""
    ):  # VAZIO
        inputRestricaoExtrasNaTentativaRequerEnderecoRede.clear()
        # inputNotaNotaParaAprovacao.send_keys("0,00")
        input_RestricaoExtrasNaTentativaRequerEnderecoRede = True
        contQuestionario += 1
        # sleep(1)
    # RESTRIÇÕES EXTRAS NAS TENTATIVAS - SEGURANÇA DO NAVEGADOR
    checagemTotal += 1
    input_RestricaoExtrasNaTentativaSegurancaNavegador = False
    inputRestricaoExtrasNaTentativaSegurancaNavegador = Select(
        navegador.find_element(by=By.ID, value="id_browsersecurity")
    )
    if (
        navegador.find_element(by=By.ID, value="id_browsersecurity").get_attribute(
            "value"
        )
        != "-"
    ):  # - É PADRÃO(NENHUM)
        inputRestricaoExtrasNaTentativaSegurancaNavegador.select_by_value(
            "-"
        )  # - É PADRÃO(NENHUM)
        input_RestricaoExtrasNaTentativaSegurancaNavegador = True
        contQuestionario += 1
        # sleep(1)
    # RESTRIÇÕES EXTRAS NAS TENTATIVAS - PERMITIR QUE O QUESTIONÁRIO SEJA REALIZADO OFFLINE PELO APLICATIVO MÓVEL
    checagemTotal += 1
    input_RestricaoExtrasNaTentativaPermitirOffLine = False
    inputRestricaoExtrasNaTentativaPermitirOffLine = Select(
        navegador.find_element(by=By.ID, value="id_allowofflineattempts")
    )
    if (
        navegador.find_element(by=By.ID, value="id_allowofflineattempts").get_attribute(
            "value"
        )
        != "0"
    ):  # 0 É PADRÃO(NÃO)
        inputRestricaoExtrasNaTentativaPermitirOffLine.select_by_value(
            "0"
        )  # 0 É PADRÃO(NÃO)
        input_RestricaoExtrasNaTentativaPermitirOffLine = True
        contQuestionario += 1
        # sleep(1)

    # FEEDBACK FINAL

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
        contQuestionario += 1
        # sleep(1)
    # CONFIGURAÇÕES COMUNS DE MÓDULOS - NÚMERO DE IDENTIFICAÇÃO DO MÚDULO
    # checagemTotal+=1
    # input_ConfComumModuloNumIdentificacao = False
    # inputConfComumModuloNumIdentificacao = navegador.find_element(by=By.ID,value="id_cmidnumber")
    # if navegador.find_element(by=By.ID,value="id_cmidnumber").get_attribute("value") != "": #PADRÃO É VAZIO
    #    inputConfComumModuloNumIdentificacao.clear()
    #    input_ConfComumModuloNumIdentificacao = True
    #    contQuestionario+=1
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
        contQuestionario += 1
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
            contQuestionario += 1
            # sleep(1)
        # CONCLUSÇÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO
        checagemTotal += 1
        input_ConclusaoAtividadeRequerVisualizacao = False
        inputConclusaoAtividadeRequerVisualizacao = navegador.find_element(
            by=By.ID, value="id_completionview"
        )
        if navegador.find_element(
            by=By.ID, value="id_completionview"
        ).is_selected():  # PADRÃO É DESMARCADO! SE ESTIVER MARCADO, ENTRE E DESMARQUE
            inputConclusaoAtividadeRequerVisualizacao.click()
            input_ConclusaoAtividadeRequerVisualizacao = True
            contQuestionario += 1
            # sleep(1)
        # CONCLUSÇÃO DE ATIVIDADE - REQUER NOTA
        checagemTotal += 1
        input_ConclusaoAtividadeRequerNota = False
        inputConclusaoAtividadeRequerNota = navegador.find_element(
            by=By.ID, value="id_completionusegrade"
        )
        if (
            navegador.find_element(
                by=By.ID, value="id_completionusegrade"
            ).is_selected()
            == False
        ):  # PADRÃO É MARCADO! SE ESTIVER DESMARCADO, ENTRE E MARQUE
            inputConclusaoAtividadeRequerNota.click()
            input_ConclusaoAtividadeRequerNota = True
            contQuestionario += 1
            # sleep(1)
        # CONCLUSÇÃO DE ATIVIDADE - EXIGIR NOTA DE APROVAÇÃO
        checagemTotal += 1
        input_ConclusaoAtividadeExigirNotaAprovacao = False
        inputConclusaoAtividadeExigirNotaAprovacao = navegador.find_element(
            by=By.ID, value="id_completionpass"
        )
        if navegador.find_element(
            by=By.ID, value="id_completionpass"
        ).is_selected():  # PADRÃO É DESMARCADO! SE ESTIVER MARCADO, ENTRE E DESMARQUE
            inputConclusaoAtividadeExigirNotaAprovacao.click()
            input_ConclusaoAtividadeExigirNotaAprovacao = True
            contQuestionario += 1
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
            contQuestionario += 1
            sleep(1)
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
            contQuestionario += 1
            # sleep(1)
        # CONCLUSÇÃO DE ATIVIDADE - REQUER VISUALIZAÇÃO
        checagemTotal += 1
        input_ConclusaoAtividadeRequerVisualizacao = False
        inputConclusaoAtividadeRequerVisualizacao = navegador.find_element(
            by=By.ID, value="id_completionview"
        )
        if navegador.find_element(
            by=By.ID, value="id_completionview"
        ).is_selected():  # PADRÃO É DESMARCADO! SE ESTIVER MARCADO, ENTRE E DESMARQUE
            inputConclusaoAtividadeRequerVisualizacao.click()
            input_ConclusaoAtividadeRequerVisualizacao = True
            contQuestionario += 1
            # sleep(1)
        # CONCLUSÇÃO DE ATIVIDADE - REQUER NOTA
        checagemTotal += 1
        input_ConclusaoAtividadeRequerNota = False
        inputConclusaoAtividadeRequerNota = navegador.find_element(
            by=By.ID, value="id_completionusegrade"
        )
        if (
            navegador.find_element(
                by=By.ID, value="id_completionusegrade"
            ).is_selected()
            == False
        ):  # PADRÃO É MARCADO! SE ESTIVER DESMARCADO, ENTRE E MARQUE
            inputConclusaoAtividadeRequerNota.click()
            input_ConclusaoAtividadeRequerNota = True
            contQuestionario += 1
            # sleep(1)
        # CONCLUSÇÃO DE ATIVIDADE - EXIGIR NOTA DE APROVAÇÃO
        checagemTotal += 1
        input_ConclusaoAtividadeExigirNotaAprovacao = False
        inputConclusaoAtividadeExigirNotaAprovacao = navegador.find_element(
            by=By.ID, value="id_completionpass"
        )
        if navegador.find_element(
            by=By.ID, value="id_completionpass"
        ).is_selected():  # PADRÃO É DESMARCADO! SE ESTIVER MARCADO, ENTRE E DESMARQUE
            inputConclusaoAtividadeExigirNotaAprovacao.click()
            input_ConclusaoAtividadeExigirNotaAprovacao = True
            contQuestionario += 1
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
        contQuestionario += 1
        # sleep(1)

    # COMPETÊNCIA - APÓS CONCLUSÃO
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
        contQuestionario += 1
        # sleep(1)

    # sleep(1)
    # CLICAR NO BOTÃO DE SALVAR
    inputLivroSalvar = navegador.find_element(by=By.ID, value="id_submitbutton2")
    inputLivroSalvar.click()
    sleep(1)

    print("Total de verificações: %i " % checagemTotal)
    if contQuestionario > 0:
        if contQuestionario < 2:
            print("Total de modificação: %i" % contQuestionario)
        else:
            print("Totais de modificações: %i" % contQuestionario)

        if input_GeralExibirDescricaoNaPaginaCurso != False:
            print(
                "'Exibir descrição na página do curso' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )

        if input_DuracaoAbrirQuestionario != False:
            print(
                "'Abrir o questionário' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_DuracaoEncerrarQuestionario != False:
            print(
                "'Encerrar o questionário' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_DuracaoLimiteTempo != False:
            print("'Limite de tempo' foi alterado para o Padrão - PADRÃO (DESMARCADO).")
        if input_DuracaoQndoTempoExpirar != False:
            print(
                "'Quando o tempo expirar' foi alterado para o Padrão - PADRÃO (AS TENTATIVAS ABERTAS SÃO ENVIADAS AUTOMATICAMENTE)."
            )

        if input_NotaCategoriaNotas != False:
            print(
                "'Categoria de notas' foi alterado para o Padrão - PADRÃO (NÃO CATEGORIZADO)."
            )
        if input_NotaNotaParaAprovacao != False:
            print("'Nota para aprovação' foi alterado para o Padrão - PADRÃO (ZERO).")
        # if input_NotaTentativasPermitidas != False:
        #    print("'Tentativas permitidas' foi alterado para o Padrão - PADRÃO (UMA).")
        if input_NotaTentativasPermitidas != False:
            print(f"Total de 'Tentativas permitidas': {inputNotaTentativasPermitidas}.")

        if input_LayoutNovaPagina != False:
            print(
                "'Nova página' foi alterado para o Padrão - PADRÃO (CADA 5 QUESTÕES)."
            )
        # if input_LayoutRepaginar != False:
        #    print("'Repaginar agora' foi alterado para o Padrão - PADRÃO (DESMARCADO).")
        if input_LayoutMetodoNavegacao != False:
            print("'Método de navegação' foi alterado para o Padrão - PADRÃO (LIVRE).")

        if input_ComportamentoQuestaoMisturarEntreQuestao != False:
            print(
                "'Misturar entre as questões' foi alterado para o Padrão - PADRÃO (NÃO)."
            )
        if input_ComportamentoQuestaoComoComportam != False:
            print(
                "'Como as questões se comportam' foi alterado para o Padrão - PADRÃO (FEEDBACK ADIADO)."
            )

        if input_OpcaoRevisaoAposTentativaATentativa != False:
            print(
                "'Opção de Revisão - Após a Tentativa - A tentativa' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_OpcaoRevisaoAposTentativaAcertosErros != False:
            print(
                "'Opção de Revisão - Após a Tentativa - Acertos/Erros' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_OpcaoRevisaoAposTentativaNotas != False:
            print(
                "'Opção de Revisão - Após a Tentativa - Notas' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_OpcaoRevisaoAposTentativaFeedBackEspecifico != False:
            print(
                "'Opção de Revisão - Após a Tentativa - Feedback específico' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_OpcaoRevisaoAposTentativaFeedBackGeral != False:
            print(
                "'Opção de Revisão - Após a Tentativa - Feedback geral' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_OpcaoRevisaoAposTentativaRespostaCorreta != False:
            print(
                "'Opção de Revisão - Após a Tentativa - Resposta correta' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_OpcaoRevisaoAposTentativaFeedBackFinal != False:
            print(
                "'Opção de Revisão - Após a Tentativa - Feedback final ' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )

        if input_OpcaoRevisaoMaisTardeATentativa != False:
            print(
                "'Opção de Revisão - Mais tarde, enquanto ainda estiver aberto - A tentativa' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_OpcaoRevisaoMaisTardeAcertosErros != False:
            print(
                "'Opção de Revisão - Mais tarde, enquanto ainda estiver aberto - Acertos/Erros' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_OpcaoRevisaoMaisTardeNotas != False:
            print(
                "'Opção de Revisão - Mais tarde, enquanto ainda estiver aberto - Notas' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_OpcaoRevisaoMaisTardeFeedBackEspecifico != False:
            print(
                "'Opção de Revisão - Mais tarde, enquanto ainda estiver aberto - Feedback específico' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_OpcaoRevisaoMaisTardeFeedBackGeral != False:
            print(
                "'Opção de Revisão - Mais tarde, enquanto ainda estiver aberto - Feedback geral' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )
        if input_OpcaoRevisaoMaisTardeRespostaCorreta != False:
            print(
                "'Opção de Revisão - Mais tarde, enquanto ainda estiver aberto - Resposta correta' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_OpcaoRevisaoMaisTardeFeedBackFinal != False:
            print(
                "'Opção de Revisão - Mais tarde, enquanto ainda estiver aberto - Feedback final ' foi alterado para o Padrão - PADRÃO (MARCADO)."
            )

        if input_AparenciaMostrarFoto != False:
            print(
                "'Mostrar a fotografia do usuário' foi alterado para o Padrão - PADRÃO (NENHUMA IMAGEM)."
            )
        if input_AparenciaCasasDecimais != False:
            print(
                "'Casas decimais nas notas' foi alterado para o Padrão - PADRÃO (2 CASAS DECIMAIS)."
            )
        if input_AparenciaCasasDecimaisQuestao != False:
            print(
                "'Casas decimais nas notas da questão' foi alterado para o Padrão - PADRÃO (O MESMO QUE PARA AS AVALIAÇÕES EM GERAL)."
            )
        if input_AparenciaMostrarBloco != False:
            print(
                "'Mostrar blocos durante as tentativas do questionário' foi alterado para o Padrão - PADRÃO (NÃO)."
            )

        if input_RestricaoExtrasNaTentativaSenhaNecessaria != False:
            print("'Senha necessária' foi alterado para o Padrão - PADRÃO (SEM SENHA).")
        if input_RestricaoExtrasNaTentativaRequerEnderecoRede != False:
            print(
                "'Requer endereço de rede' foi alterado para o Padrão - PADRÃO (VAZIO/EM BRANCO)."
            )
        if input_RestricaoExtrasNaTentativaSegurancaNavegador != False:
            print(
                "'Segurança do navegador' foi alterado para o Padrão - PADRÃO (NENHUM)."
            )
        if input_RestricaoExtrasNaTentativaPermitirOffLine != False:
            print(
                "'Permitir que o questionário seja realizado offline pelo aplicativo móvel' foi alterado para o Padrão - PADRÃO (NÃO)."
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
        if input_ConclusaoAtividadeRequerNota != False:
            print("'Requer nota' foi alterado para o Padrão - PADRÃO (MARCADO).")
        if input_ConclusaoAtividadeExigirNotaAprovacao != False:
            print(
                "'Exigir nota de aprovação ' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_ConclusaoAtividadeConclusaoEsperadaEm != False:
            print(
                "'Conclusão esperada em' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )

        if input_CompetenciaAposConclusao != False:
            print(
                "'Após conclusão da atividade' foi alterado para o Padrão - PADRÃO (FAZER NADA)"
            )
    else:
        print("Análise do Questionário foi concluída sem observações!")

    """ timeFim = time.perf_counter()
    formatacaoTempo = timeFim - timeInicio
    timeHora, timeResto = divmod(formatacaoTempo, 3600)
    timeMinutos, timeSegundos = divmod(timeResto, 60)

    print("Tempo total de verificação foi: {horas:02.0f}h:{minutos:02.0f}m:{segundos:02.0f}s".format(horas=timeHora, minutos=timeMinutos, segundos=timeSegundos))
    """
    return contQuestionario
