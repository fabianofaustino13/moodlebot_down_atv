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

from time import sleep

service = FirefoxService(
    executable_path="./geckodriver",
)

options = Options()
options.headless = False  # executar de forma visível ou oculta


def validarQuestaoDissertacao(navegador, link, contQuestaoDissertacao):
    # timeInicio = time.perf_counter()
    # print("Analisando as configurações da Questão Dissertação: %s" % navegador.find_element(by=By.ID,value="id_name").get_attribute('value'))
    checagemTotal = 0
    contQuestao = 0

    # EXPANDINDO TUDO
    navegador.find_element(by=By.LINK_TEXT, value="Expandir tudo").click()  # Abrir
    sleep(1)

    # FEEDBACK PARA A OPÇÃO GERAL
    checagemTotal += 1
    input_QuestaoFeedbackGeral = False
    # print(navegador.find_element(by=By.ID,value="id_feedbacktrueeditable").text)
    if navegador.find_element(by=By.ID, value="id_generalfeedbackeditable").text == "":
        # print("Feedback Geral vazio")
        input_QuestaoFeedbackGeral = True
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

        if input_QuestaoFeedbackGeral != False:
            print("'Feedback geral' está vazio.")
    else:
        print("Análise da Questão foi concluída sem observações!")
    """ 
    timeFim = time.perf_counter()
    formatacaoTempo = timeFim - timeInicio
    timeHora, timeResto = divmod(formatacaoTempo, 3600)
    timeMinutos, timeSegundos = divmod(timeResto, 60)

    print("Tempo total de verificação foi: {horas:02.0f}h:{minutos:02.0f}m:{segundos:02.0f}s".format(horas=timeHora, minutos=timeMinutos, segundos=timeSegundos))
    """
    # return contQuestaoDissertacao
