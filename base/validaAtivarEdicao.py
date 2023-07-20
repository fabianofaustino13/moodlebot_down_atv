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

import time
import validaAtvLivro
import validaAtvPasta
import validaAtvGlossario
import validaAtvURL
import validaAtvQuestionario
import validaAtvEnquete
import validaAtvBotao
import validaAtvTopico
import validaAtvArquivo
import validaAtvQuestaoQuestionario
import validaAtvPagina
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from time import sleep

service = FirefoxService(
    executable_path="./geckodriver",
)

options = Options()
options.headless = True  # executar de forma visível ou oculta


def ativarEdicao(navegador, link, contAtivarEdicao):
    timeInicio = time.perf_counter()
    # sleep(1)
    # print("Entrou aqui")
    # teste = navegador.find_element(by=By.LINK_TEXT,value="Guia do Participante").get_attribute("value")
    # secao1 = navegador.find_element(by=By.ID,value="section-1")
    # secao1.click()
    # inputatividadeAvaliativa = navegador.find_element(by=By.LINK_TEXT,value="Conteúdo em PDF")
    # CLICAR NA CATRACA PARA ATIVAR E EDIÇÃO DO CURSO
    inputClicarCatraca = navegador.find_element(
        by=By.ID, value="action-menu-toggle-2"
    )  # action-menu-toggle-2 É SEMPRE O BOTÃO DE ATIVAR A EDIÇÃO
    inputClicarCatraca.click()
    sleep(1)
    # CLICA NO BOTÃO DE ATIVAR A EDIÇÃO
    inputClicarAtivar = navegador.find_element(
        by=By.LINK_TEXT, value="Ativar edição"
    )  # Abrir
    inputClicarAtivar.click()
    sleep(1)

    # inputQuadroNotasConfiguracoes = navegador.find_element(by=By.LINK_TEXT,value="Configurações")
    # inputQuadroNotasConfiguracoes.click()
    # sleep(1)
    # lista = navegador.find_elements(By.CLASS_NAME, "gradeitemheader")sectionname
    # numSecao = 0
    """ while numSecao < 10:
        nomeSecao = "section-" + str(numSecao)
        lista2 = navegador.find_elements(By.ID, nomeSecao)
        if len(lista2) == 1:
            print(len(lista2))
            print(nomeSecao)
        else:
            print("valor igual a 0")
            break
        #print("section-" + str(numSecao))
        #lista = navegador.find_elements(By.CLASS_NAME, "sectionname")
        
        #print(len(lista))
        numSecao+=1 """
    # CONTANDO O NÚMERO DE SEÇÕES DO CURSO
    # nomeSecao = "section-" + str(numSecao)
    # lista2 = navegador.find_elements(By.ID, nomeSecao)
    # print("Total de Seção(ões) %s" % len(lista2))
    # while len(lista2) != 0:
    #    nomeSecao = "section-" + str(numSecao)
    #    lista2 = navegador.find_elements(By.ID, nomeSecao)
    #    if len(lista2) == 1:
    # print(nomeSecao)
    # listaClass = navegador.find_elements(By.CLASS_NAME, "sectionname")
    # for j in listaClass:
    #    print("Lista é: %s" % j.text)

    #        numSecao+=1
    #    else:
    #   print("Saiu")
    #        break
    # numSecao+=1
    # print(numSecao)
    numAtv = 4  # 4 SEMPRE É A PRIMEIRA ATIVIDADE/RECURSO
    contLivro = 0
    contPasta = 0
    contGlossario = 0
    contURL = 0
    contQuestionario = 0
    contEnquete = 0
    contBotao = 0
    notaMinima = 0
    contSecao = 0
    contTopico = 0
    contArquivo = 0
    contQuetionarioQuestao = 0
    contPagina = 0
    # editarAtv = "action-menu-toggle-" + str(numAtv)
    # listaEditarAtv = navegador.find_elements(By.ID, editarAtv)
    # print(listaEditarAtv)
    # print(len(listaEditarAtv))
    # while len(listaEditarAtv) != 0:

    editarAtv = "action-menu-toggle-" + str(numAtv)
    moduloQuestao = "action-menu-" + str(numAtv)
    numEditarAtv = navegador.find_elements(by=By.ID, value=editarAtv)
    divEditar = "action-menu-" + str(numAtv)
    # print("EDITAR ATV FORA DO WHILE - %s" %editarAtv)
    # print("NUM EDITAR ATV FORA DO WHILE - %s" % numEditarAtv)
    contSection = 0
    nomeSection = "section-" + str(contSection)
    while len(numEditarAtv) != 0:
        # nomeSetor = navegador.find_element(By.CLASS_NAME, "menu-action-text").text
        # print(nomeSetor)
        # atributo = navegador.find_elements(by=By.ID,value=editarAtv).get_attribute("value")
        # teste = navegador.find_element(by=By.LINK_TEXT,value="menu-action-text").get_attribute("value")
        # print(teste)

        # numEditarAtvTeste = navegador.find_elements(by=By.ID,value="action-menu-4-menu").get_attribute("value")
        # print(numEditarAtvTeste)
        # print("EDITAR ATV DENTRO DO WHILE %s" % editarAtv)
        # print("NUM EDITAR ATV DENTRO DO WHILE - %s" % len(numEditarAtv))
        if len(numEditarAtv) != 0:
            # print(numAtv)
            # print(len(numEditarAtv))
            print(editarAtv)
            inputEditarAtv = navegador.find_element(by=By.ID, value=editarAtv)
            # inputEditarAtv2 = navegador.find_element(By.CSS_SELECTOR,'#'+editarAtv)

            # print(inputEditarAtv.text)
            sleep(1)
            inputEditarAtv.click()
            # restricao = navegador.find_element(By.XPATH, "//a[@class='dropdown-item edit menu-action']").get_attribute("text") #PEGAR VALOR DE UMA SPAN
            # print("Testou")
            # print("Valor restricao %s" % restricao)
            # pesquisarSection = testeSection.find_elements(by=By.LINK_TEXT,value="Editar seção")
            # pesquisarSection.click()
            # print(pesquisarSection.get_attribute('value'))

            # webdriver(navegador, 30).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id=divEditar]")))
            # webdriver(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@id=editarAtv]"))).click()
            # WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='delete-overlay']")))
            # clicar = WebDriverWait(navegador, 20).until(EC.element_to_be_clickable(By.ID,value='action-menu-toggle-7'))
            # clicar.click()
            # WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='divEditar']")))
            # WebDriverWait(navegador, 10).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id='divEditar']"))).click()
            # print(len(numEditarAtv))

            # listaClassTipo = navegador.find_elements(By.CLASS_NAME, "menu-action-text")
            # for j in listaClassTipo:
            #    print("Lista é: %s" % j.text)

            # nomeSetor = navegador.find_element(By.CLASS_NAME, "summary").text
            # print(nomeSetor)
            sleep(1)
            # inputEditarAtv.send_keys(Keys.ESCAPE)
            # inputEditarSecao = navegador.find_element(by=By.LINK_TEXT,value="Editar seção") #Abrir
            # print(inputEditarSecao.text)
            # print("passou")
            # editarSecao = navegador.find_element(by=By.LINK_TEXT,value="Editar seção")
            # editarSecao.click()
            # novoTeste = navegador.find_element(by=By.LINK_TEXT,value="Editar seção")
            # print(novoTeste)
            try:
                # print(nomeSection)
                # editarSecaoX = navegador.find_element(By.XPATH, "//a[@id='editarAtv']").get_attribute("innerHTML") #PEGAR VALOR DE UMA SPAN
                # print("passou")
                # print(editarSecaoX)
                editarSecao = navegador.find_element(
                    by=By.LINK_TEXT, value="Editar seção"
                )
                # numSection = navegador.find_element(by=By.ID,value=nomeSection)
                # editarSecao = numSection.find_element(by=By.ID,value=editarAtv)
                # editarSecao.click()
                sleep(1)
                # notaMinima = validaAtvSecao.validarSecao(navegador,link,contSecao,notaMinima)
                print("############ FIM ############")
                editarSecao.send_keys(Keys.ESCAPE)

            except:
                naoExisteSecao = False
            #    print("SEÇÃO NÃO EXISTE")

            try:
                editarConf = navegador.find_element(
                    by=By.LINK_TEXT, value="Editar configurações"
                )

                editarConf.click()

                tipoAtividade = navegador.find_element(
                    by=By.NAME, value="modulename"
                ).get_attribute("value")
                # print(tipoAtividade) #MOSTRAR O TIPO DE ATIVIDADE/RECURSO
                if tipoAtividade == "book":  # SE A ATIVIDADE FOR UM LIVRO
                    print(
                        "Analisando as configurações do Livro: %s"
                        % navegador.find_element(
                            by=By.ID, value="id_name"
                        ).get_attribute("value")
                    )
                    contLivro = validaAtvLivro.validarLivro(navegador, link, contLivro)
                elif tipoAtividade == "folder":
                    print(
                        "Analisando as configurações da Pasta: %s"
                        % navegador.find_element(
                            by=By.ID, value="id_name"
                        ).get_attribute("value")
                    )
                    contPasta = validaAtvPasta.validarPasta(navegador, link, contPasta)
                elif tipoAtividade == "glossary":
                    print(
                        "Analisando as configurações do Glossário: %s"
                        % navegador.find_element(
                            by=By.ID, value="id_name"
                        ).get_attribute("value")
                    )
                    contGlossario = validaAtvGlossario.validarGlossario(
                        navegador, link, contGlossario
                    )
                elif tipoAtividade == "url":
                    print(
                        "Analisando as configurações da URL: %s"
                        % navegador.find_element(
                            by=By.ID, value="id_name"
                        ).get_attribute("value")
                    )
                    contURL = validaAtvURL.validarURL(navegador, link, contURL)
                elif tipoAtividade == "quiz":
                    print(
                        "Analisando as configurações do Questionário: %s"
                        % navegador.find_element(
                            by=By.ID, value="id_name"
                        ).get_attribute("value")
                    )
                    contQuestionario = validaAtvQuestionario.validarQuestionario(
                        navegador, link, contQuestionario
                    )
                    sleep(1)
                    # print("Analisando as configurações das Questões do Questionário")
                    contQuetionarioQuestao = (
                        validaAtvQuestaoQuestionario.validarQuestaoQuestionario(
                            navegador, link, numAtv
                        )
                    )
                elif tipoAtividade == "questionnaire":
                    print(
                        "Analisando as configurações da Enquete: %s"
                        % navegador.find_element(
                            by=By.ID, value="id_name"
                        ).get_attribute("value")
                    )
                    contEnquete = validaAtvEnquete.validarEnquete(
                        navegador, link, contEnquete
                    )
                elif tipoAtividade == "label":
                    contBotao = validaAtvBotao.validarBotao(
                        navegador, link, contBotao, notaMinima
                    )
                elif tipoAtividade == "resource":
                    print(
                        "Analisando as configurações do Arquivo: %s"
                        % navegador.find_element(
                            by=By.ID, value="id_name"
                        ).get_attribute("value")
                    )
                    contArquivo = validaAtvArquivo.validarArquivo(
                        navegador, link, contArquivo
                    )
                elif tipoAtividade == "page":
                    print(
                        "Analisando as configurações da Página: %s"
                        % navegador.find_element(
                            by=By.ID, value="id_name"
                        ).get_attribute("value")
                    )
                    contPagina = validaAtvPagina.validarPagina(
                        navegador, link, contPagina
                    )
                else:
                    print(
                        f"Atividade/Recurso não configurada para validação: {navegador.find_element(by=By.ID,value='id_name').get_attribute('value')} - Tipo: {tipoAtividade}"
                    )
                    navegador.find_element(by=By.ID, value="id_cancel").click()
                    sleep(1)

                print("############ FIM ############")

            except:  # NoSuchElementException:
                naoExisteConfiguracao = False
                # print("TIPO DE ATIVIDADE NÃO EXISTE")
                # editarLivroTeste = navegador.find_element(by=By.NAME, value="modulename").get_attribute("value")
                # print(editarLivroTeste)

            # EDITAR TÓPICO
            try:
                editarTopico = navegador.find_element(
                    by=By.LINK_TEXT, value="Editar tópico"
                )
                # print(novoTeste)
                # print("EDITAR TÓPICO")
                # novoTeste.send_keys(Keys.ESCAPE)
                editarTopico.click()
                print(
                    "Analisando as configurações do Tópico: %s"
                    % navegador.find_element(
                        by=By.ID, value="id_name_value"
                    ).get_attribute("value")
                )
                contTopico = validaAtvTopico.validarTopico(navegador, link, contTopico)

                print("############ FIM ############")

            except NoSuchElementException:
                nãoExisteTopico = False
                # print("Editar tópico Element does not exist")

            # paginaInicialCurso = navegador.find_element(By.CLASS_NAME, "media-body ")
            # paginaInicialCurso.click()
            """ else:
                print("Deu erro") """
            # teste = navegador.find_element(By.CLASS_NAME, "menu-action-text")
            # user = navegador.find_element(by_xpath('//span[@title = "{}"]'.format(names))
            # teste = navegador.find_element(By.XPATH, ".//*[@class='menu-action-text']").get_dom_attribute()
            # teste = navegador.find_element(By.TAG_NAME, "span")
            # attr = navegador.switch_to.active_element.get_attribute("menu-action-text")
            # print(teste)

            # teste = navegador.find_element(By.CSS_SELECTOR, 'span.menu-action-text')
            # print(teste.get_attribute("innerText"))

            # print("Editar Seção")
            #            print(inputEditarSecao.text)
            # print("Próximo")

            # listaClass = navegador.find_elements(By.CLASS_NAME, "sectionname")
            # for j in numEditarAtv:
            #    print("Lista é: %s" % j.text)

            contSection += 1
            numAtv += 1
            sleep(1)

        # else:
        #    sleep(1)
        #    print("Entrou no ELSE")
        # break
        # inputEditarAtv = navegador.find_element(by=By.ID,value=editarAtv)
        # print(inputEditarAtv)
        # inputEditarAtv.click()
        # inputEditarAtv.send_keys(Keys.ESCAPE)
        # if len(listaEditarAtv) == 1:
        # print(nomeSecao)
        # listaClass = navegador.find_elements(By.CLASS_NAME, "sectionname")
        # for j in listaClass:
        #    print("Lista é: %s" % j.text)
        # numSecao+=1
        # else:
        #    print("Saiu")
        #    break

        # contSection+=1
        # numAtv+=1

        # sleep(1)
        # print(numSecao)

        # listaClass = navegador.find_elements(By.CLASS_NAME, "sectionname")
        # listaClassInstanceName = navegador.find_elements(By.CLASS_NAME, "instancename")

        # print(len(listaClass))
        # print(len(listaClassInstanceName))
        # for x in listaClassInstanceName:
        #    print(x.text)
        # if x.text == "Guia do Participante":
        #    print("Entrou em Guia")

        # id="action-menu-toggle-0"

        # lista = navegador.find_elements(By.CLASS_NAME, "sectionname")
        # teste = navegador.find_element(by=By.LINK_TEXT,value="Guia do Participante").get_attribute("value")

        # lista = navegador.find_elements(by=By.ID,value="section-" + numSecao)

        # secao1.click()
        # print(len(lista2))
        # print(len(lista))
        # qntAtv = len(listaClassInstanceName)
        # print(qntAtv)
        # print("Total de atividades: %i" % qntAtv)
        # i = 1
        # x = 2
        # contItemDeNota = 0
        # vetor = list(range(qntAtv))
        # k = 0
        # for j in lista:
        #    i += 1
        #    print("Validando.....")
        #    print("Lista é: %s" % j.text)

        # print(k)
        #    vetor[k] = j.text
        # print(vetor[k])
        #    k+=1

        # k = 0
        # while x <= 30:
        # print("X é: %i" % x)
        # print(listaAtv[k])
        # k+=1
        # print("Valor de X: %i" % x)
        #    variavel = "action-menu-toggle-" + str(x)
        #    print(variavel)
        # print(variavel)
        # print("Validando o " + j.text)
        # print(vetor[k])
        # k+=1
        #    if x > 3:
        #        print(variavel)
        # inputQuadroNotasConfiguracoesEditar = navegador.find_element(by=By.ID,value=variavel)
        # inputQuadroNotasConfiguracoesEditar.click()
        # sleep(1)
        # inputQuadroNotasEditar = navegador.find_element(by=By.LINK_TEXT,value="Editar configurações") #Abrir
        # inputQuadroNotasEditar.click()
        #    sleep(1)
        #    x+=1

        # ÚLTIMA LINHA DO WHILE
        # numAtv+=1
        # print("############FIM############")
        # nomeSection = "section-" + str(contSection)
        editarAtv = "action-menu-toggle-" + str(numAtv)
        numEditarAtv = navegador.find_elements(by=By.ID, value=editarAtv)
        # print(editarAtv)
        # print(numEditarAtv)

    # timeFim = time.perf_counter()
    # print(f"Tempo total de verificação foi: {timeFim - timeInicio:0.4f} segundos")
    # timeFim = time.perf_counter()
    # formatacaoTempo = timeFim - timeInicio
    # timeHora, timeResto = divmod(formatacaoTempo, 3600)
    # timeMinutos, timeSegundos = divmod(timeResto, 60)

    # print("Tempo total de verificação foi: {horas:02.0f}h:{minutos:02.0f}m:{segundos:02.0f}s".format(horas=timeHora, minutos=timeMinutos, segundos=timeSegundos))

    return contAtivarEdicao
