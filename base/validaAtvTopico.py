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


def validarTopico(navegador, link, contTopico):
    checagemTotal = 0
    navegador.find_element(by=By.LINK_TEXT, value="Expandir tudo").click()  # Abrir
    sleep(1)
    restricao = navegador.find_element(
        By.XPATH, "//h3[@class='accesshide']"
    ).get_attribute(
        "innerHTML"
    )  # PEGAR VALOR DE UMA SPAN
    # print(restricao)
    checagemTotal += 1
    input_TopicoResticao = False
    if restricao != " Conjunto de 0 restrição(ões)":
        # print("excluir")
        # = navegador.find_element(By.CLASS_NAME, "d-inline-block col-form-label availability-delete p-x-1")
        excluirRestricao = navegador.find_element(
            By.XPATH,
            "//a[@class='d-inline-block col-form-label availability-delete p-x-1' and @title='Excluir']",
        )
        excluirRestricao.click()
        contTopico += 1
        input_TopicoResticao = True
    # sleep(1)
    # CLICAR NO BOTÃO DE SALVAR
    navegador.find_element(by=By.ID, value="id_submitbutton").click()
    sleep(1)

    print("Total de verificação: %i " % checagemTotal)
    if contTopico > 0:
        if contTopico < 2:
            print("Total de modificação: %i" % contTopico)
        else:
            print("Totais de modificações: %i" % contTopico)

        if input_TopicoResticao != False:
            print(
                '"Restrições de acesso" foi alterado para o Padrão - PADRÃO (NENHUM).'
            )
    else:
        print("Análise do Tópico foi concluída sem observações!")

    return contTopico
