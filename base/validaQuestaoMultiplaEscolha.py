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


def validarQuestaoMultiplaEscolha(navegador, link, contQuestaoMultiplaEscolha):
    # timeInicio = time.perf_counter()
    # print("Analisando as configurações da Questão Múltipla escolha: %s" % navegador.find_element(by=By.ID,value="id_name").get_attribute('value'))
    checagemTotal = 0
    contQuestao = 0

    # EXPANDINDO TUDO
    navegador.find_element(by=By.LINK_TEXT, value="Expandir tudo").click()  # Abrir
    sleep(1)

    # GERAL - FEEDBACK PARA A OPÇÃO GERAL
    checagemTotal += 1
    input_GeralQuestaoFeedbackGeral = False
    if navegador.find_element(by=By.ID, value="id_generalfeedbackeditable").text == "":
        # print("Feedback Geral vazio")
        input_GeralQuestaoFeedbackGeral = True
        contQuestao += 1
    # GERAL - UMA OU MÚLTIPLAS RESPOSTAS?
    checagemTotal += 1
    input_GeralQuestaoMultiplasRespostas = False
    inputGeralQuestaoMultiplasRespostas = Select(
        navegador.find_element(by=By.ID, value="id_single")
    )
    if (
        navegador.find_element(by=By.ID, value="id_single").get_attribute("value")
        != "1"
    ):  # 1 É PADRÃO(APENAS UMA RESPOSTA)
        inputGeralQuestaoMultiplasRespostas.select_by_value(
            "1"
        )  # 1 É PADRÃO(APENAS UMA RESPOSTA)
        input_GeralQuestaoMultiplasRespostas = True
        contQuestao += 1
    # GERAL - MISTURAR AS OPÇÕES?
    checagemTotal += 1
    input_GeralQuestaoMisturarOpcoes = False
    inputGeralQuestaoMisturarOpcoes = navegador.find_element(
        by=By.ID, value="id_shuffleanswers"
    )
    if navegador.find_element(
        by=By.ID, value="id_shuffleanswers"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputGeralQuestaoMisturarOpcoes.click()
        input_GeralQuestaoMisturarOpcoes = True
        contQuestao += 1
    # GERAL - NUMERAR AS OPÇÕES?
    checagemTotal += 1
    input_GeralQuestaoNumerarOpcoes = False
    inputGeralQuestaoGeralQuestaoNumerarOpcoes = Select(
        navegador.find_element(by=By.ID, value="id_answernumbering")
    )
    if (
        navegador.find_element(by=By.ID, value="id_answernumbering").get_attribute(
            "value"
        )
        != "abc"
    ):  # abc É PADRÃO(ABC)
        inputGeralQuestaoGeralQuestaoNumerarOpcoes.select_by_value(
            "abc"
        )  # abc É PADRÃO(ABC)
        input_GeralQuestaoGeralQuestaoNumerarOpcoes = True
        contQuestao += 1

    # CONTANDO O NÚMERO DE RESPOSTAS
    numero = 0
    numeroOpcao = "id_fraction_" + str(numero)
    totalOpcao = navegador.find_element(by=By.ID, value=numeroOpcao)
    try:
        while totalOpcao != 0:
            numero += 1
            numeroOpcao = "id_fraction_" + str(numero)
            totalOpcao = navegador.find_element(by=By.ID, value=numeroOpcao)
    except:
        erro = True

    # CONTAR QUANTAS RESPOSTAS ESTÁ MARCADA COM 100%
    contCemPorCento = 0
    contNenhum = 0
    totalContNenhum = 0
    w = 0
    numeroOpcao = "id_fraction_" + str(w)
    while w < numero:
        # print("Aqui")
        resposta = navegador.find_element(by=By.ID, value=numeroOpcao).get_attribute(
            "value"
        )
        # print(resposta)
        if resposta == "1.0":
            contCemPorCento += 1
        if resposta == "0.0":
            contNenhum += 1
        w += 1
        numeroOpcao = "id_fraction_" + str(w)
    # print(contResp)
    totalContNenhum = numero - contCemPorCento
    # print("Total de contNenhum")
    # print(totalContNenhum)
    # print("contNenhm")
    # print(contNenhum)

    # MÚLTIPLAS TENTATIVAS - PENALIDADE
    checagemTotal += 1
    input_MultiplasTentativasPenalidade = False
    inputMultiplasTentativasPenalidade = Select(
        navegador.find_element(by=By.ID, value="id_penalty")
    )
    if (
        navegador.find_element(by=By.ID, value="id_penalty").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO (0%)
        inputMultiplasTentativasPenalidade.select_by_value("0")  # 0 É PADRÃO(0%)
        input_MultiplasTentativasPenalidade = True
        contQuestao += 1

    # CLICAR NO BOTÃO DE SALVAR
    navegador.find_element(by=By.ID, value="id_submitbutton").click()
    sleep(1)

    print("Total de verificações: %i " % checagemTotal)
    if contQuestao > 0:
        if contQuestao < 2:
            print("Total de modificação: %i" % contQuestao)
        else:
            print("Totais de modificações: %i" % contQuestao)

        if input_GeralQuestaoFeedbackGeral != False:
            print("'Feedback geral' está vazio.")

        if input_GeralQuestaoMultiplasRespostas != False:
            print(
                "'Uma ou múltiplas respostas?' foi alterado para o Padrão - PADRÃO (APENAS UMA RESPOSTA)."
            )
        if input_GeralQuestaoMisturarOpcoes != False:
            print(
                "'Misturar as opções?' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )
        if input_GeralQuestaoNumerarOpcoes != False:
            print(
                "'Numerar as opções?' foi alterado para o Padrão - PADRÃO (a.,b.,c.,...)."
            )

        if contCemPorCento != 1:
            print(
                "'Existe mais de uma alternativa Correta, ou seja, 100% - PADRÃO (APENAS UMA ALTERNATIVA CORRETA - 100%)."
            )

        if contNenhum != totalContNenhum:
            print("Número de alternativas com resposta NENHUM divergente.")

        if input_MultiplasTentativasPenalidade != False:
            print(
                "'Penalidade para cada tentativa incorreta' foi alterado para o Padrão - PADRÃO (0)."
            )
    else:
        print("Análise da Questão foi concluída sem observações!")

    """  timeFim = time.perf_counter()
    formatacaoTempo = timeFim - timeInicio
    timeHora, timeResto = divmod(formatacaoTempo, 3600)
    timeMinutos, timeSegundos = divmod(timeResto, 60)

    print("Tempo total de verificação foi: {horas:02.0f}h:{minutos:02.0f}m:{segundos:02.0f}s".format(horas=timeHora, minutos=timeMinutos, segundos=timeSegundos))
    """
    # return contQuestao
