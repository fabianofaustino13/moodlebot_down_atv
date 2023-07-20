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


def quadroNotas(navegador, link, contQuadroNotas):
    checagemTotal = 0

    navegador.find_element(by=By.LINK_TEXT, value="Notas").click()
    sleep(1)

    navegador.find_element(by=By.LINK_TEXT, value="Configurações").click()
    sleep(1)

    navegador.find_element(by=By.ID, value="action-menu-toggle-0").click()
    sleep(1)

    navegador.find_element(by=By.ID, value="actionmenuaction-1").click()
    sleep(1)

    # EXPANDINDO CATEGORIA DE NOTAS
    navegador.find_element(by=By.LINK_TEXT, value="Mostrar mais ...").click()  # Abrir
    sleep(1)

    checagemTotal += 1
    inputQuadroNotasNomeCompleto = navegador.find_element(by=By.ID, value="id_fullname")
    input_QuadroNotasNomeCompleto = False
    if (
        navegador.find_element(by=By.ID, value="id_fullname").get_attribute("value")
        != ""
    ):
        valorAnteriorNomeCompleto = navegador.find_element(
            by=By.ID, value="id_fullname"
        ).get_attribute("value")
        navegador.find_element(
            by=By.ID, value="id_fullname"
        ).clear()  # Apagando nome, caso exista na categoria
        input_QuadroNotasNomeCompleto = True
        contQuadroNotas += 1
        # sleep(1)

    # PEGAR O VALOR DO SELECT (Forma de agregação das notas)
    checagemTotal += 1
    input_QuadroNotasAgregacaoNotas = False
    inputQuadroNotasAgregacaoNotas = Select(
        navegador.find_element(by=By.ID, value="id_aggregation")
    )
    if (
        navegador.find_element(by=By.ID, value="id_aggregation").get_attribute("value")
        != "13"
    ):  # Valor 0 é para Média das Notas e 13 para Soma das Notas - Natural
        valorAnteriorQuadroNotasAgragacaoNotas = navegador.find_element(
            by=By.ID, value="id_aggregation"
        ).get_attribute("value")
        inputQuadroNotasAgregacaoNotas.select_by_value(
            "13"
        )  # Escolher a opção: Soma das notas - Natural
        input_QuadroNotasAgregacaoNotas = True
        contQuadroNotas += 1
        # sleep(1)

    # DESCONSIDERAR NOTAS VAZIAS
    checagemTotal += 1
    input_QuadroNotasDesconsiderarNotasVazias = False
    inputQuadroNotasDesconsiderarNotasVazias = navegador.find_element(
        by=By.ID, value="id_aggregateonlygraded"
    )
    if navegador.find_element(
        by=By.ID, value="id_aggregateonlygraded"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputQuadroNotasDesconsiderarNotasVazias.click()
        input_QuadroNotasDesconsiderarNotasVazias = True
        contQuadroNotas += 1
        # sleep(1)

    # Incluir resultado da aprendizagem na agregação
    # input_QuadroNotasResultadoAgregacao = False
    # inputQuadroNotasResultadoAgregacao = navegador.find_element(by=By.ID,value="id_aggregateoutcomes")
    # if navegador.find_element(by=By.ID,value="id_aggregateoutcomes").get_attribute('checked'):
    #    inputQuadroNotasResultadoAgregacao.click()
    #    input_QuadroNotasResultadoAgregacao = True
    #    contQuadroNotas+=1

    # EXPANDINDO TOTAL DA CATEGORIA
    navegador.find_element(by=By.LINK_TEXT, value="Mostrar mais ...").click()  # Abrir
    sleep(1)

    # TOTAL DA CATEGORIA - NOME PARA O TOTAL DA CATEGORIA
    checagemTotal += 1
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
        valorAnteriorQuadroNotasNomeTotalCategoria = navegador.find_element(
            by=By.ID, value="id_grade_item_itemname"
        ).get_attribute("value")
        navegador.find_element(
            by=By.ID, value="id_grade_item_itemname"
        ).clear()  # Apagando nome, caso exista
        input_QuadroNotasNomeTotalCategoria = True
        contQuadroNotas += 1
        # sleep(1)
    # TOTAL DA CATEGORIA - INFORMAÇÃO DO ITEM
    checagemTotal += 1
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
        valorAnteriorQuadroNotasInformacaoItem = navegador.find_element(
            by=By.ID, value="id_grade_item_iteminfo"
        ).get_attribute("value")
        navegador.find_element(
            by=By.ID, value="id_grade_item_iteminfo"
        ).clear()  # Apagando nome, caso exista
        input_QuadroNotasInformacaoItem = True
        contQuadroNotas += 1
        # sleep(1)
    # TOTAL DA CATEGORIA - NÚMERO DE IDENTIFICAÇÃO DO MÓDULO
    checagemTotal += 1
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
        valorAnteriorQuadroNotasNumIdentificacaoModulo = navegador.find_element(
            by=By.ID, value="id_grade_item_idnumber"
        ).get_attribute("value")
        navegador.find_element(
            by=By.ID, value="id_grade_item_idnumber"
        ).clear()  # Apagando nome, caso exista
        input_QuadroNotasNumIdentificacaoModulo = True
        contQuadroNotas += 1
        # sleep(1)
    # TOTAL DA CATEGORIA - NOTA PARA APROVAÇÃO
    checagemTotal += 1
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
        valorAnteriorQuadroNotasNotaAprovacao = navegador.find_element(
            by=By.ID, value="id_grade_item_gradepass"
        ).get_attribute("value")
        navegador.find_element(by=By.ID, value="id_grade_item_gradepass").clear()
        input_QuadroNotasNotaAprovacao = True
        contQuadroNotas += 1
        # sleep(1)

    # TOTAL DA CATEGORIA - TIPO DE APRESENTAÇÃO DA NOTA
    checagemTotal += 1
    input_QuadroNotasTipoApresentacaoNota = False
    if (
        navegador.find_element(by=By.ID, value="id_grade_item_display").get_attribute(
            "value"
        )
        != "0"
    ):
        valorAnteriorQuadroNotasTipoApresentacaoNota = navegador.find_element(
            by=By.ID, value="id_grade_item_display"
        ).get_attribute("value")
        inputQuadroNotasTipoApresentacaoNota = Select(
            navegador.find_element(by=By.ID, value="id_grade_item_display")
        )
        inputQuadroNotasTipoApresentacaoNota.select_by_value("0")
        input_QuadroNotasTipoApresentacaoNota = True
        contQuadroNotas += 1
        # sleep(1)

    # TOTAL DA CATEGORIA - PONTOS DECIMAIS GERAL
    checagemTotal += 1
    input_QuadroNotasPontosDecimaisGeral = False
    if (
        navegador.find_element(by=By.ID, value="id_grade_item_decimals").get_attribute(
            "value"
        )
        != "-1"
    ):
        valorAnteriorQuadroNotasPontosDecimaisGeral = navegador.find_element(
            by=By.ID, value="id_grade_item_decimals"
        ).get_attribute("value")
        inputQuadroNotasPontosDecimaisGeral = Select(
            navegador.find_element(by=By.ID, value="id_grade_item_decimals")
        )
        inputQuadroNotasPontosDecimaisGeral.select_by_value("-1")
        input_QuadroNotasPontosDecimaisGeral = True
        contQuadroNotas += 1
        # sleep(1)
    # TOTAL DA CATEGORIA - OCULTO - DESMARCAR OPÇÃO - PONTOS DECIMAIS GERAL OCULTO
    checagemTotal += 1
    input_QuadroNotasPontosDecimaisGeralOculto = False
    inputQuadroNotasPontosDecimaisGeralOculto = navegador.find_element(
        by=By.ID, value="id_grade_item_hidden"
    )
    if navegador.find_element(
        by=By.ID, value="id_grade_item_hidden"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputQuadroNotasPontosDecimaisGeralOculto.click()
        input_QuadroNotasPontosDecimaisGeralOculto = True
        contQuadroNotas += 1
        # sleep(1)

    # TOTAL DA CATEGORIA - DESMARCAR OPÇÃO - OCULTO ATÉ
    checagemTotal += 1
    input_QuadroNotasOcultoAte = False
    inputQuadroNotasOcultoAte = navegador.find_element(
        by=By.ID, value="id_grade_item_hiddenuntil_enabled"
    )
    if navegador.find_element(
        by=By.ID, value="id_grade_item_hiddenuntil_enabled"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputQuadroNotasOcultoAte.click()
        input_QuadroNotasOcultoAte = True
        contQuadroNotas += 1
        # sleep(1)

    # TOTAL DA CATEGORIA - DESMARCAR OPÇÃO - TRAVADO
    checagemTotal += 1
    input_QuadroNotasTravado = False
    inputQuadroNotasTravado = navegador.find_element(
        by=By.ID, value="id_grade_item_locked"
    )
    if navegador.find_element(
        by=By.ID, value="id_grade_item_locked"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputQuadroNotasTravado.click()
        input_QuadroNotasTravado = True
        contQuadroNotas += 1
        # sleep(1)

    # TOTAL DA CATEGORIA - DESMARCAR OPÇÃO - TRAVAR DEPOIS DE
    checagemTotal += 1
    input_QuadroNotasTravarDepoisDe = False
    inputQuadroNotasTravarDepoisDe = navegador.find_element(
        by=By.ID, value="id_grade_item_locktime_enabled"
    )
    if navegador.find_element(
        by=By.ID, value="id_grade_item_locktime_enabled"
    ).is_selected():  # PADRÃO É DESMARCADO
        inputQuadroNotasTravarDepoisDe.click()
        input_QuadroNotasTravarDepoisDe = True
        contQuadroNotas += 1
        # sleep(1)

    """ todasOpcoes = inputNotaCategoriaNotas.find_elements(By.TAG_NAME,"option")
    for opcao in todasOpcoes:
        #print("Valores são: %s" % opcao.get_attribute("value"))
        #print(opcao.text)
        if opcao.text != "Não categorizado": #O É PADRÃO(NÃO CATEGORIZADO)
            #print("O valor é: %s" % opcao.get_attribute("value"))
            opcao.click()
            input_NotaCategoriaNotas = True
            contQuestionario+=1
            sleep(1)
 """
    # SALVAR LIVRO DE NOTAS
    navegador.find_element(by=By.ID, value="id_submitbutton").click()
    sleep(1)

    # CHECA SE A SOMA DAS ATIVIDADES AVALIATIVAS É MAIOR OU MENOR QUE 100 PONTOS. POR PADRÃO, A SOMA DEVE SER IGUAL A 100
    checagemTotal += 1
    # somaDasNotas = navegador.find_element(By.XPATH, "//td[@class='cell column-range level1 levelodd cell c2' and @text='' and @style='']").text
    input_TotalNotas = False
    if (
        navegador.find_element(
            By.XPATH,
            "//td[@class='cell column-range level1 levelodd cell c2' and @text='' and @style='']",
        ).text
        != "100,00"
    ):
        totalNota = navegador.find_element(
            By.XPATH,
            "//td[@class='cell column-range level1 levelodd cell c2' and @text='' and @style='']",
        ).text
        contQuadroNotas += 1
        input_TotalNotas = True

    # print(somaDasNotas)
    sleep(1)

    print("Total de verificações: %i " % checagemTotal)
    if contQuadroNotas > 0:
        if contQuadroNotas < 2:
            print("Total de modificação: %i" % contQuadroNotas)
        else:
            print("Total de modificações: %i" % contQuadroNotas)

        if input_QuadroNotasNomeCompleto != False:
            print("'Nome completo' foi alterado para o valor padrão. Padrão ('Vazio').")

        if input_QuadroNotasAgregacaoNotas != False:
            print(
                "'Forma de agregação das notas' foi alterado para o padrão. Padrão (Soma das notas - Natural)."
            )

        if input_QuadroNotasDesconsiderarNotasVazias != False:
            print(
                "'Desconsiderar notas vazias' foi alterado para o padrão. Padrão (DESMARCADO)."
            )

        # if input_QuadroNotasResultadoAgregacao != False:
        #    print("Quadro de Notas: Resultado Agregação" )

        if input_QuadroNotasNomeTotalCategoria != False:
            print(
                "'Nome para o total da categoria' foi alterado para o padrão. Padrão ('Vazio')."
            )
        if input_QuadroNotasInformacaoItem != False:
            print("'Informação do Item' foi alterado para o padrão. Padrão ('Vazio').")
        if input_QuadroNotasNumIdentificacaoModulo != False:
            print(
                "'Número de Identificação do módulo' foi alterado para o padrão. Padrão ('Vazio')."
            )
        if input_QuadroNotasNotaAprovacao != False:
            print("'Nota para aprovação' foi alterado para o padrão. Padrão ('0,00').")
        if input_QuadroNotasTipoApresentacaoNota != False:
            print(
                "'Nota para aprovação' foi alterado para o padrão. Padrão (Padrão - Real)."
            )
        if input_QuadroNotasPontosDecimaisGeral != False:
            print(
                "'Pontos decimais geral' foi alterado para o padrão. Padrão (Padrão - 2)."
            )
        if input_QuadroNotasPontosDecimaisGeralOculto != False:
            print("'Oculto' foi alterado para o padrão. Padrão (DESMARCADO).")
        if input_QuadroNotasOcultoAte != False:
            print("'Oculto até' foi alterado para o padrão. Padrão (DESMARCADO).")
        if input_QuadroNotasTravado != False:
            print("'Travado' foi alterado para o padrão. Padrão (DESMARCADO).")
        if inputQuadroNotasTravarDepoisDe != False:
            print("'Travar depois de' foi alterado para o padrão. Padrão (DESMARCADO).")

        if input_TotalNotas != False:
            print(
                "ATENÇÃO: A soma das atividades é diferente de 100,00 pontos. Atualmente está em %s"
                % totalNota
            )

    else:
        print("Análise do Quadro de Notas foi concluída sem observações!")

    return contQuadroNotas
