# Instalação da lib do Selenium
# pip3 install selenium

# Instalação Beautifulsoup4
# pip3 install beautifulsoup4

# Instalação lxml
# pip3 install lxml

# username, password, loginbtn

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import Select

from time import sleep

service = FirefoxService(
    executable_path="./geckodriver",
)

# driver = webdriver.Firefox(service=service)
navegador = webdriver.Firefox(service=service)

options = Options()
options.headless = True  # executar de forma visível ou oculta
contQuadroNotas = 0  # Registrar total de modificações no Quado de Notas

# navegador = webdriver.Firefox(options=options)

# Código do Curso para fazer a checagem
# codCurso = input("Digite o Código do Curso: ")

# link = "https://ead.ifrn.edu.br/ava/academico/course/view.php?id=639" #+ codCurso #"639"
link = "https://addiemooc38.escolavirtual.gov.br/course/view.php?id=1102"  # + codCurso #"1102"

navegador.get(url=link)
sleep(1)

# Login do usuário
# userLogin = input("Digite o seu Login da Plataforma: ")

inputUsuario = navegador.find_element(by=By.ID, value="username")
# inputUsuario.send_keys(userLogin) #("69628459287")
# inputUsuario.send_keys("69628459287")
inputUsuario.send_keys("ffo13@hotmail.com")
sleep(1)

inputSenha = navegador.find_element(by=By.ID, value="password")
inputSenha.send_keys("Qualquer21")
sleep(1)

# inputLembrarSenha = navegador.find_element(by=By.ID,value="rememberusername")
# inputLembrarSenha.click()
# sleep(1)

inputLogin = navegador.find_element(by=By.ID, value="loginbtn")
inputLogin.click()
sleep(2)

# ABRINDO O QUADRO DE NOTAS
# Verificar o Quadro de Notas  aggregatesum
# linkQuadroNotas = "https://ead.ifrn.edu.br/ava/academico/grade/edit/tree/index.php?id=639" #+ codCurso #"639"
# navegador.get(url=linkQuadroNotas)
inputQuadroNotas = navegador.find_element(by=By.LINK_TEXT, value="Notas")
inputQuadroNotas.click()
sleep(1)

inputQuadroNotasConfiguracoes = navegador.find_element(
    by=By.LINK_TEXT, value="Configurações"
)
inputQuadroNotasConfiguracoes.click()
sleep(1)

# linkQuadroEditarNotas = "https://ead.ifrn.edu.br/ava/academico/grade/edit/tree/category.php?courseid=639&id=564&gpr_type=edit&gpr_plugin=tree&gpr_courseid=639"
# navegador.get(url=linkQuadroEditarNotas)

inputQuadroNotasConfiguracoesEditar = navegador.find_element(
    by=By.ID, value="action-menu-toggle-0"
)
inputQuadroNotasConfiguracoesEditar.click()
sleep(2)

inputQuadroNotasConfiguracoesEditarConfiguracoes = navegador.find_element(
    by=By.ID, value="actionmenuaction-1"
)
inputQuadroNotasConfiguracoesEditarConfiguracoes.click()
sleep(2)

# EXPANDINDO CATEGORIA DE NOTAS
inputQuadroNotasMostrarMais = navegador.find_element(
    by=By.LINK_TEXT, value="Mostrar mais ..."
)  # Abrir
inputQuadroNotasMostrarMais.click()
sleep(1)

inputQuadroNotasNomeCompleto = navegador.find_element(by=By.ID, value="id_fullname")
# nome = navegador.find_element(by=By.ID,value="id_fullname").get_attribute("value")
input_QuadoNotasNomeCompleto = False
if navegador.find_element(by=By.ID, value="id_fullname").get_attribute("value") != "":
    navegador.find_element(
        by=By.ID, value="id_fullname"
    ).clear()  # Apagando nome, caso exista na categoria
    input_QuadoNotasNomeCompleto = True
    contQuadroNotas += 1
    sleep(1)

# if (!navegador.find_element(by=By.ID,value="id_fullname").get_attribute("")):
#    print("apagar nome")

inputQuadroNotasAgregacaoNotas = Select(
    navegador.find_element(by=By.ID, value="id_aggregation")
)
inputQuadroNotasAgregacaoNotas.select_by_value(
    "13"
)  # Escolher a opção: Soma das notas - Natural

# Desconsiderar notas vazias
input_QuadroNotasDesconsiderarNotasVazias = False
inputQuadroNotasDesconsiderarNotasVazias = navegador.find_element(
    by=By.ID, value="id_aggregateonlygraded"
)
if navegador.find_element(by=By.ID, value="id_aggregateonlygraded").get_attribute(
    "checked"
):
    inputQuadroNotasDesconsiderarNotasVazias.click()
    input_QuadroNotasDesconsiderarNotasVazias = True
    contQuadroNotas += 1

# Incluir resultado da aprendizagem na agregação
# input_QuadroNotasResultadoAgregacao = False
# inputQuadroNotasResultadoAgregacao = navegador.find_element(by=By.ID,value="id_aggregateoutcomes")
# if navegador.find_element(by=By.ID,value="id_aggregateoutcomes").get_attribute('checked'):
#    inputQuadroNotasResultadoAgregacao.click()
#    input_QuadroNotasResultadoAgregacao = True
#    contQuadroNotas+=1

# EXPANDINDO TOTAL DA CATEGORIA
inputQuadroNotasMostrarMais = navegador.find_element(
    by=By.LINK_TEXT, value="Mostrar mais ..."
)  # Abrir
inputQuadroNotasMostrarMais.click()
sleep(1)

inputQuadroNotasNomeTotalCategoria = navegador.find_element(
    by=By.ID, value="id_grade_item_itemname"
)
input_QuadroNotasNomeTotalCategoria = False
if (
    navegador.find_element(by=By.ID, value="id_grade_item_itemname").get_attribute(
        "value"
    )
    != ""
):
    navegador.find_element(
        by=By.ID, value="id_grade_item_itemname"
    ).clear()  # Apagando nome, caso exista
    input_QuadroNotasNomeTotalCategoria = True
    contQuadroNotas += 1
    sleep(1)

inputQuadroNotasInformacaoItem = navegador.find_element(
    by=By.ID, value="id_grade_item_iteminfo"
)
input_QuadroNotasInformacaoItem = False
if (
    navegador.find_element(by=By.ID, value="id_grade_item_iteminfo").get_attribute(
        "value"
    )
    != ""
):
    navegador.find_element(
        by=By.ID, value="id_grade_item_iteminfo"
    ).clear()  # Apagando nome, caso exista
    input_QuadroNotasInformacaoItem = True
    contQuadroNotas += 1
    sleep(1)

inputQuadroNotasNumIdentificacaoModulo = navegador.find_element(
    by=By.ID, value="id_grade_item_idnumber"
)
input_QuadroNotasNumIdentificacaoModulo = False
if (
    navegador.find_element(by=By.ID, value="id_grade_item_idnumber").get_attribute(
        "value"
    )
    != ""
):
    navegador.find_element(
        by=By.ID, value="id_grade_item_idnumber"
    ).clear()  # Apagando nome, caso exista
    input_QuadroNotasNumIdentificacaoModulo = True
    contQuadroNotas += 1
    sleep(1)

input_QuadroNotasNotaAprovacao = False
inputQuadroNotasNotaAprovacao = navegador.find_element(
    by=By.ID, value="id_grade_item_gradepass"
).get_attribute("value")
# inputNotaAprovacao = navegador.find_element(by=By.ID,value="id_grade_item_gradepass").get_attribute("value")
if (
    navegador.find_element(by=By.ID, value="id_grade_item_gradepass").get_attribute(
        "value"
    )
    != "0,00"
) and (
    navegador.find_element(by=By.ID, value="id_grade_item_gradepass").get_attribute(
        "value"
    )
    != "0"
):
    # if inputNotaAprovacao != "0,00" and inputNotaAprovacao != "0":
    navegador.find_element(by=By.ID, value="id_grade_item_gradepass").clear()
    # inputQuadroNotasNotaAprovacao.send_keys(0)
    input_QuadroNotasNotaAprovacao = True
    contQuadroNotas += 1
    sleep(1)

# ALTERAR TIPO DE APRESENTAÇÃO DE NOTA PARA PADRÃO REAL
inputQuadroNotasTipoApresentacaoNota = Select(
    navegador.find_element(by=By.ID, value="id_grade_item_display")
)
inputQuadroNotasTipoApresentacaoNota.select_by_value("0")

# LATERAR PONTOS DECIMAIS PARA 2 CASAS
inputQuadroNotasPontosDecimaisGeral = Select(
    navegador.find_element(by=By.ID, value="id_grade_item_decimals")
)
inputQuadroNotasPontosDecimaisGeral.select_by_value("-1")

# DESMARCAR OPÇÃO - PONTOS DECIMAIS GERAL OCULTO
input_QuadroNotasPontosDecimaisGeralOculto = False
inputQuadroNotasPontosDecimaisGeralOculto = navegador.find_element(
    by=By.ID, value="id_grade_item_hidden"
)
if navegador.find_element(by=By.ID, value="id_grade_item_hidden").get_attribute(
    "checked"
):
    inputQuadroNotasPontosDecimaisGeralOculto.click()
    input_QuadroNotasPontosDecimaisGeralOculto = True
    contQuadroNotas += 1

# DESMARCAR OPÇÃO - OCULTO ATÉ
input_QuadroNotasOcultoAte = False
inputQuadroNotasOcultoAte = navegador.find_element(
    by=By.ID, value="id_grade_item_hiddenuntil_enabled"
)
if navegador.find_element(
    by=By.ID, value="id_grade_item_hiddenuntil_enabled"
).get_attribute("checked"):
    inputQuadroNotasOcultoAte.click()
    input_QuadroNotasOcultoAte = True
    contQuadroNotas += 1


# DESMARCAR OPÇÃO - TRAVADO
input_QuadroNotasTravado = False
inputQuadroNotasTravado = navegador.find_element(by=By.ID, value="id_grade_item_locked")
if navegador.find_element(by=By.ID, value="id_grade_item_locked").get_attribute(
    "checked"
):
    inputQuadroNotasTravado.click()
    input_QuadroNotasTravado = True
    contQuadroNotas += 1

# DESMARCAR OPÇÃO - TRAVAR DEPOIS DE
input_QuadroNotasTravarDepoisDe = False
inputQuadroNotasTravarDepoisDe = navegador.find_element(
    by=By.ID, value="id_grade_item_locktime_enabled"
)
if navegador.find_element(
    by=By.ID, value="id_grade_item_locktime_enabled"
).get_attribute("checked"):
    inputQuadroNotasTravarDepoisDe.click()
    input_QuadroNotasTravarDepoisDe = True
    contQuadroNotas += 1

inputQuadroNotasConfiguracoesEditarConfiguracoesSalvar = navegador.find_element(
    by=By.ID, value="id_submitbutton"
)
inputQuadroNotasConfiguracoesEditarConfiguracoesSalvar.click()
sleep(2)

if contQuadroNotas > 0:
    print("Total de modificações: %i" % contQuadroNotas)

if input_QuadoNotasNomeCompleto != False:
    print("Houve alteração no Quadro de Notas: Nome Completo")

if input_QuadroNotasDesconsiderarNotasVazias != False:
    print("Houve alteração no Quadro de Notas: Desconsideração Notas limpas")

# if input_QuadroNotasResultadoAgregacao != False:
#    print("Houve alteração no Quadro de Notas: Resultado Agregação" )

if input_QuadroNotasNomeTotalCategoria != False:
    print("Houve alteração no Quadro de Notas: Nome Total Categoria")

if input_QuadroNotasInformacaoItem != False:
    print("Houve alteração no Quadro de Notas: Informação Item")

if input_QuadroNotasNumIdentificacaoModulo != False:
    print("Houve alteração no Quadro de Notas: Número de Identificação do Módulo")

if input_QuadroNotasNotaAprovacao != False:
    print("Houve alteração no Quadro de Notas: Nota para Aprovação")
