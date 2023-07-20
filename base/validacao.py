# Instalação da lib do Selenium
# pip3 install selenium

# Instalação Beautifulsoup4
# pip3 install beautifulsoup4

# Instalação lxml
# pip3 install lxml

# username, password, loginbtn

import time
import validaQuadroNotas
import validaItemDeNota
import validaAtivarEdicao
import validaEditarConfiguracao
import validaAtivarFiltro

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService

from time import sleep

options = Options()
options.headless = False  # executar de forma visível ou oculta
# navegador = webdriver.Firefox(options=options,executable_path=r"D:\Programacao\Robo\RoboMoodle\geckodriver.exe") #MODO OCULTO
service = FirefoxService(
    executable_path="./geckodriver",
)
navegador = webdriver.Firefox(service=service)


contQuadroNotas = 0  # Registrar total de modificações no Quado de Notas
contItemDeNota = 0  # Registrar total de modificações em Item de Nota
contAtivarEdicao = 0  # Registar total de modificações em Ativar Edição
contEditarConfiguracao = 0  # Registrar total de modificações em Editar Configurações
contAtivarFiltro = 0  # Registar o total de modificações em Filtro
contQuestaoQuestionario = 0

# navegador = webdriver.Firefox(options=options)

# Código do Curso para fazer a checagem
# codCurso = input("Digite o Código do Curso: ")

# link = "https://ead.ifrn.edu.br/ava/academico/course/view.php?id=639" #+ codCurso #"639"
# link = "https://addiemooc38.escolavirtual.gov.br/course/view.php?id=1102" #+ codCurso #"1102"
# link = "https://addiemooc38.escolavirtual.gov.br/course/view.php?id=1115" #+ codCurso #"1113"
# link = "https://addiemooc38.escolavirtual.gov.br/course/view.php?id=1117"
# link = "https://addiemooc38.escolavirtual.gov.br/course/view.php?id=1121"
link = "https://addiemooc38.escolavirtual.gov.br/course/view.php?id=" + input(
    "Digite o Código do Curso: "
)  # 1102" #+ codCurso #"1102"

navegador.get(url=link)
sleep(1)
timeInicio = time.perf_counter()  # INÍCIO DA CONTAGEM DO TEMPO
# Login do usuário
# userLogin = input("Digite o seu Login da Plataforma: ")

inputUsuario = navegador.find_element(by=By.ID, value="username")
# inputUsuario.send_keys("DIGTE O SEU LOGIN") #PARA DEIXAR AUTOMÁTICO
inputUsuario.send_keys(input("Digite o seu login: "))
# sleep(1)

inputSenha = navegador.find_element(by=By.ID, value="password")
# inputSenha.send_keys("DIGITE A SUA SENHA") #PARA DEIXAR AUTOMÁTICO
inputSenha.send_keys(input("Digite a sua senha: "))
# sleep(1)

inputLogin = navegador.find_element(by=By.ID, value="loginbtn")
inputLogin.click()
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

# QUADRO DE NOTAS - CONFIGURAÇÕES
print("Analisando as configurações do Quadro de Notas")
contQuadroNotas = validaQuadroNotas.quadroNotas(navegador, link, contQuadroNotas)
print("############ FIM ############")
sleep(1)

# QUADRO DE NOTAS - ITEM DE NOTA
contItemDeNota = validaItemDeNota.itemDeNota(navegador, link, contItemDeNota)
sleep(1)

# CONFIGURAÇÃO DA PÁGINA
contEditarConfiguracao = validaEditarConfiguracao.editarConfiguracao(
    navegador, link, contEditarConfiguracao
)
print("############ FIM ############")
sleep(1)

# VERICAR OS FILTROS
print("Analisando as configurações do Filtro")
contAtivarFiltro = validaAtivarFiltro.ativarFiltro(navegador, link, contAtivarFiltro)
print("############ FIM ############")
sleep(1)

# ATIVAR EDIÇÃO DA PÁGINA
navegador.set_window_size(700, 768)  # ALTERAR RESOLUÇÃO PARA ALINHAR OS ITENS
contAtivarEdicao = validaAtivarEdicao.ativarEdicao(navegador, link, contAtivarEdicao)

timeFim = time.perf_counter()
formatacaoTempo = timeFim - timeInicio
timeHora, timeResto = divmod(formatacaoTempo, 3600)
timeMinutos, timeSegundos = divmod(timeResto, 60)

print(
    "Tempo total de verificação foi: {horas:02.0f}h:{minutos:02.0f}m:{segundos:02.0f}s".format(
        horas=timeHora, minutos=timeMinutos, segundos=timeSegundos
    )
)
# print("Tempo total de verificação foi: {horas:0>2}h:{minutos:0>2}m:{segundos:02.0f}s".format(horas=timeHora, minutos=timeMinutos, segundos=timeSegundos))
