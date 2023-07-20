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


def validarSecao(navegador, link, contSecao, notaMinima):
    checagemTotal = 0
    contarSecao = 0
    existeNota = 0
    existeGenerico = 0

    print(
        "Analisando as configurações da Seção: %s"
        % navegador.find_element(by=By.ID, value="id_name_value").get_attribute("value")
    )
    # SE FOR A SEÇÃO DA ÁREA DO PARTICIPANTE, ENTRAR E CHAMAR A FUNÇÃO, SENÃO, APENAS SAIR.
    input_SecaoExisteGenerico = False
    input_SecaoExisteNota = False
    if (
        navegador.find_element(by=By.ID, value="id_name_value").get_attribute("value")
        == "Área do Participante"
    ):
        checagemTotal += 1
        pegarInformacoes = navegador.find_element(
            by=By.ID, value="id_summary_editoreditable"
        )
        todasOpcoes = pegarInformacoes.find_elements(By.TAG_NAME, "p")
        for opcao in todasOpcoes:
            valor = opcao.text
            if valor[5:27] == '{GENERICO:type="user"}':
                # print("Achou generico")
                existeGenerico = 1
                input_SecaoExisteGenerico = True
            if valor[0:27] == "Nota mínima para aprovação:":
                # print("Entrou")
                notaMinima = valor[28:30]
                # print(notaMinima)
                existeNota = 1
                input_SecaoExisteNota = True

        if existeGenerico == 0:
            contSecao += 1
        if existeNota == 0:
            contSecao += 1

    else:
        checagemTotal += 1

    # sleep(1)
    # CLICAR NO BOTÃO DE SALVAR
    inputSecaoSalvar = navegador.find_element(by=By.ID, value="id_submitbutton")
    inputSecaoSalvar.click()
    sleep(1)

    print("Total de verificações: %i " % checagemTotal)
    if contSecao > 0:
        if contSecao < 2:
            print("Total de modificação: %i" % contSecao)
        else:
            print("Totais de modificações: %i" % contSecao)

        if input_SecaoExisteGenerico != False:
            print('Não existe a string procurada: {GENERICO:type="user"}')
        if input_SecaoExisteNota != False:
            print(
                "Não existe a string procurada para pegar a nota: 'Nota mínima para aprovação:'"
            )
    else:
        print("Análise da Seção foi concluída sem observações!")

    return notaMinima
