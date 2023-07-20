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


def ativarFiltro(navegador, link, contAtivarFiltro):
    totalVerificacao = 0
    sleep(1)
    # CLICAR NA CATRACA PARA ATIVAR E EDIÇÃO
    inputClicarCatraca = navegador.find_element(by=By.ID, value="action-menu-toggle-2")
    inputClicarCatraca.click()
    sleep(1)
    # CLICA NO BOTÃO DE ATIVAR A EDIÇÃO
    inputClicarFiltro = navegador.find_element(
        by=By.LINK_TEXT, value="Filtros"
    )  # Abrir
    inputClicarFiltro.click()
    sleep(1)

    totalVerificacao += 1
    contAtivarFiltro = 0
    input_ExibirH5P = False
    inputExibirH5P = Select(navegador.find_element(by=By.ID, value="menudisplayh5p"))
    if (
        navegador.find_element(by=By.ID, value="menudisplayh5p").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(HABILITADO)
        inputExibirH5P.select_by_value("0")  # 0 É PADRÃO(HABILITADO)
        input_ExibirH5P = True
        contAtivarFiltro += 1
        sleep(1)

    totalVerificacao += 1
    input_MatjhJax = False
    inputMatjhJax = Select(navegador.find_element(by=By.ID, value="menumathjaxloader"))
    if (
        navegador.find_element(by=By.ID, value="menumathjaxloader").get_attribute(
            "value"
        )
        != "0"
    ):  # 0 É PADRÃO(HABILITADO)
        inputMatjhJax.select_by_value("0")  # 0 É PADRÃO(HABILITADO)
        input_MatjhJax = True
        contAtivarFiltro += 1
        sleep(1)

    totalVerificacao += 1
    input_LinkAutomatico = False
    inputLinkAutomatico = Select(
        navegador.find_element(by=By.ID, value="menuactivitynames")
    )
    if (
        navegador.find_element(by=By.ID, value="menuactivitynames").get_attribute(
            "value"
        )
        != "0"
    ):  # 0 É PADRÃO(HABILITADO)
        inputLinkAutomatico.select_by_value("0")  # 0 É PADRÃO(HABILITADO)
        input_LinkAutomatico = True
        contAtivarFiltro += 1
        sleep(1)

    totalVerificacao += 1
    input_PluginMultimidia = False
    inputPluginMultimidia = Select(
        navegador.find_element(by=By.ID, value="menumediaplugin")
    )
    if (
        navegador.find_element(by=By.ID, value="menumediaplugin").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(HABILITADO)
        inputPluginMultimidia.select_by_value("0")  # 0 É PADRÃO(HABILITADO)
        input_PluginMultimidia = True
        contAtivarFiltro += 1
        sleep(1)

    totalVerificacao += 1
    input_Generico = False
    inputGenerico = Select(navegador.find_element(by=By.ID, value="menugenerico"))
    if (
        navegador.find_element(by=By.ID, value="menugenerico").get_attribute("value")
        != "0"
    ):  # 0 É PADRÃO(HABILITADO)
        inputGenerico.select_by_value("0")  # 0 É PADRÃO(HABILITADO)
        input_Generico = True
        contAtivarFiltro += 1
        sleep(1)

    # CLICAR NO BOTÃO DE SALVAR
    # inputFiltroSalvar = navegador.find_element(By.CLASS_NAME, "buttons")
    inputFiltroSalvar = navegador.find_element(By.NAME, "savechanges")
    inputFiltroSalvar.click()
    sleep(1)
    # print("Foram feitas %i " % totalVerificacao % " verificações")
    if contAtivarFiltro > 0:
        if input_ExibirH5P != False:
            print("Exibir H5P foi alterado para o Padrão - PADRÃO (HABILITADO).")
        if input_MatjhJax != False:
            print("input_MatjhJax foi alterado para o Padrão - PADRÃO (HABILITADO).")
        if input_LinkAutomatico != False:
            print(
                "Link automático de nomes de atividades foi alterado para o Padrão - PADRÃO (HABILITADO)."
            )
        if input_PluginMultimidia != False:
            print(
                "Plugins multimídia foi alterado para o Padrão - PADRÃO (HABILITADO)."
            )
        if input_Generico != False:
            print("Genérico foi alterado para o Padrão - PADRÃO (HABILITADO).")
    else:
        print("Análise do Filtro foi concluída sem observações!")

    sleep(1)
    # VOLTAR PARA A PÁGINA INICIAL DO CURSO
    paginaInicialCurso = navegador.find_element(By.CLASS_NAME, "media-body ")
    paginaInicialCurso.click()
    sleep(1)
    return contAtivarFiltro
