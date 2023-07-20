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

service = FirefoxService(
    executable_path="./geckodriver",
)

options = Options()
options.headless = False  # executar de forma visível ou oculta


def atividadeAvaliativa(navegador, link, contAtividadeAvaliativa):
    contAtvAval = 0
    while contAtvAval < 2:
        total = navegador.find_element(by=By.LINK_TEXT, value=" Questionário")
        if navegador.find_element(by=By.LINK_TEXT, value=" Questionário"):
            contAtvAval += 1
        else:
            print("Acabou")
    else:
        print("Fim do while e o valor do contador é {contAtvAval}")
