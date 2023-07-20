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


def validarQuestaoSelecionarPalavrasQueFaltam(
    navegador, link, contQuestaoSelecionarPalavrasQueFaltam
):
    # timeInicio = time.perf_counter()
    # print("Analisando as configurações da Questão Associação: %s" % navegador.find_element(by=By.ID,value="id_name").get_attribute('value'))
    checagemTotal = 0
    contQuestao = 0

    # EXPANDINDO TUDO
    navegador.find_element(by=By.LINK_TEXT, value="Expandir tudo").click()  # Abrir
    sleep(1)

    # GERAL - FEEDBACK PARA A OPÇÃO GERAL
    checagemTotal += 1
    input_GeralQuestaoFeedbackGeral = False
    if navegador.find_element(by=By.ID, value="id_generalfeedbackeditable").text == "":
        input_GeralQuestaoFeedbackGeral = True
        contQuestao += 1

    # GERAL - EMBARALHAR
    checagemTotal += 1
    input_GeralQuestaoEmbaralhar = False
    inputGeralQuestaoGeralQuestaoEmbaralhar = navegador.find_element(
        by=By.ID, value="id_shuffleanswers"
    )
    if (
        navegador.find_element(by=By.ID, value="id_shuffleanswers").is_selected()
        == False
    ):  # PADRÃO É MARCADO
        inputGeralQuestaoGeralQuestaoEmbaralhar.click()
        input_GeralQuestaoGeralQuestaoEmbaralhar = True
        contQuestao += 1

    # FEEDBACK COMBINADO - MOSTRAR O NÚMERO DE RESPOSTAS CORRETAS UMA VEZ TERMINADA A QUESTÃO
    checagemTotal += 1
    input_GeralQuestaoMostrarNumRespCorreta = False
    inputGeralQuestaoMostrarNumRespCorreta = navegador.find_element(
        by=By.ID, value="id_shownumcorrect"
    )
    if navegador.find_element(
        by=By.ID, value="id_shownumcorrect"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputGeralQuestaoMostrarNumRespCorreta.click()
        input_GeralQuestaoMostrarNumRespCorreta = True
        contQuestao += 1

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
        if input_GeralQuestaoEmbaralhar != False:
            print("'Embaralhar' foi alterado para o Padrão - PADRÃO (DESMARCADO).")
        if input_GeralQuestaoMostrarNumRespCorreta != False:
            print(
                "'Mostrar o número de respostas corretas uma vez terminada a questão' foi alterado para o Padrão - PADRÃO (DESMARCADO)."
            )

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
    return checagemTotal
