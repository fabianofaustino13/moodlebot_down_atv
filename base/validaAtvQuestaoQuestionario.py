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

import re  # alterar a string
import validaQuestaoVF
import validaQuestaoMultiplaEscolha
import validaQuestaoDissertacao
import validaQuestaoAssociacao
import validaQuestaoSelecionarPalavrasQueFaltam
import validaQuestaoArrastarSoltarSobreTexto
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


def validarQuestaoQuestionario(navegador, link, numAtv):
    # timeInicio = time.perf_counter()
    # print("Entrou questão")
    checagemTotal = 0
    contQuestaoQuestionario = 0
    contQuestaoVF = 0
    contQuestaoMultiplaEscolha = 0
    contQuestaoDissertacao = 0
    contQuestaoAssociacao = 0
    contQuestaoSelecionarPalavrasQueFaltam = 0
    contQuestaoArrastarSoltarSobreTexto = 0
    # ENTRANDO NO LIVRO
    # EXPANDINDO TUDO
    moduloQuestao = "action-menu-" + str(numAtv)
    # print(numAtv)
    # print(moduloQuestao)

    modulo = navegador.find_element(by=By.ID, value=moduloQuestao).get_attribute(
        "data-owner"
    )  # PEGANDO O ID DO QUESTIONÁRIO
    # print("MODULO")
    # print(modulo)
    modulo = re.sub("\#module-", "", modulo)
    # print(f"Valor de módulo é {modulo}")

    questionarioQuestoes = navegador.find_element(
        By.XPATH,
        f"//span[@class='inplaceeditable inplaceeditable-text' and @data-itemid='{modulo}']",
    )
    questionarioQuestoes.click()
    sleep(1)
    navegador.find_element(by=By.ID, value="action-menu-toggle-3").click()
    sleep(1)
    navegador.find_element(
        by=By.LINK_TEXT, value="Editar questionário"
    ).click()  # Abrir
    sleep(1)

    # QUANTIFICAR O NÚMERO DE QUESTÕES
    contTotalQuestoes = navegador.find_elements(By.XPATH, "//span[@class='slotnumber']")
    # print(len(contTotalQuestoes))
    # print("Qntificar")
    tipoQuestoes = navegador.find_elements(
        By.XPATH, "//img[@class='icon activityicon']"
    )  # .get_attribute('title')

    x = 0
    tipoQuestoes = navegador.find_elements(
        By.XPATH, "//img[@class='icon activityicon']"
    )  # .get_attribute('title')
    questoesQuestionario = navegador.find_elements(By.CLASS_NAME, "questionname")
    # print(len(questoesQuestionario))
    while x < len(questoesQuestionario):
        print(
            f"==> Analisando as configurações da questão: {questoesQuestionario[x].text} - Tipo: {tipoQuestoes[x].get_attribute('title')} <=="
        )
        if tipoQuestoes[x].get_attribute("title") == "Verdadeiro/Falso":
            # print(tipoQuestoes[x].get_attribute('title'))
            tipoQuestoes[x].click()
            checagemTotal += validaQuestaoVF.validarQuestaoVF(
                navegador, link, contQuestaoVF
            )
        elif tipoQuestoes[x].get_attribute("title") == "Múltipla escolha":
            # print(tipoQuestoes[x].get_attribute('title'))
            tipoQuestoes[x].click()
            checagemTotal += validaQuestaoMultiplaEscolha.validarQuestaoMultiplaEscolha(
                navegador, link, contQuestaoMultiplaEscolha
            )
        elif tipoQuestoes[x].get_attribute("title") == "Dissertação":
            # print(tipoQuestoes[x].get_attribute('title'))
            tipoQuestoes[x].click()
            checagemTotal += validaQuestaoDissertacao.validarQuestaoDissertacao(
                navegador, link, contQuestaoDissertacao
            )
        elif tipoQuestoes[x].get_attribute("title") == "Associação":
            # print(tipoQuestoes[x].get_attribute('title'))
            tipoQuestoes[x].click()
            checagemTotal += validaQuestaoAssociacao.validarQuestaoAssociacao(
                navegador, link, contQuestaoAssociacao
            )
        elif (
            tipoQuestoes[x].get_attribute("title")
            == "Selecionar as palavras que faltam"
        ):
            # print(tipoQuestoes[x].get_attribute('title'))
            tipoQuestoes[x].click()
            checagemTotal += validaQuestaoSelecionarPalavrasQueFaltam.validarQuestaoSelecionarPalavrasQueFaltam(
                navegador, link, contQuestaoSelecionarPalavrasQueFaltam
            )
        elif (
            tipoQuestoes[x].get_attribute("title") == "Arrastar e soltar sobre o texto"
        ):
            # print(tipoQuestoes[x].get_attribute('title'))
            tipoQuestoes[x].click()
            checagemTotal += validaQuestaoArrastarSoltarSobreTexto.validarQuestaoArrastarSoltarSobreTexto(
                navegador, link, contQuestaoArrastarSoltarSobreTexto
            )
        else:
            print(
                f"Tipo de Questão não habilitada para validação - Tipo: {tipoQuestoes[x].get_attribute('title')}"
            )

        sleep(1)

        tipoQuestoes = navegador.find_elements(
            By.XPATH, "//img[@class='icon activityicon']"
        )  # .get_attribute('title')
        questoesQuestionario = navegador.find_elements(By.CLASS_NAME, "questionname")
        x += 1

    # MISTURAR AS QUESTÕES
    checagemTotal += 1
    input_MisturarQuestoes = False
    inputMisturarQuestoes = navegador.find_element(
        By.XPATH,
        "//input[@class='cm-edit-action' and @data-action='shuffle_questions']",
    )
    if inputMisturarQuestoes.is_selected():  # PADRÃO É DESMARCADO
        inputMisturarQuestoes.click()
        input_MisturarQuestoes = True
        contQuestaoQuestionario += 1
        # sleep(1)

    # SALVAR
    navegador.find_element(
        By.XPATH, "//input[@class='btn btn-secondary ml-1' and @name='savechanges']"
    ).click()
    sleep(1)
    # EXPANDIR MENU LATERAL SE ESTIVER OCULTO
    botaoExpandido = navegador.find_element(
        By.XPATH,
        "//button[@class='btn nav-link float-sm-left mr-1 btn-light bg-gray' and @aria-controls='nav-drawer']",
    ).get_attribute("aria-expanded")
    # print(botaoExpandido)
    if botaoExpandido == "false":
        navegador.find_element(
            By.XPATH, "//i[@class='icon fa fa-bars fa-fw ' and @aria-hidden='true']"
        ).click()

    # VOLTAR PARA A PÁGINA INICIAL DO CURSO
    paginaInicialCurso = navegador.find_element(By.CLASS_NAME, "media-body ")
    paginaInicialCurso.click()
    sleep(1)

    """ timeFim = time.perf_counter()
    formatacaoTempo = timeFim - timeInicio
    timeHora, timeResto = divmod(formatacaoTempo, 3600)
    timeMinutos, timeSegundos = divmod(timeResto, 60)

    print("Tempo total de verificação foi: {horas:02.0f}h:{minutos:02.0f}m:{segundos:02.0f}s".format(horas=timeHora, minutos=timeMinutos, segundos=timeSegundos))
    """

    # return contQuestaoQuestionario
